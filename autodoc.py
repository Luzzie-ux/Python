#!/usr/bin/env python3
# Copyright (c) 2026 Luz

"""AutoDoc or AutoDocumenting.

The purpose of this Script is to understand the way python handles
file descriptors, file operations and ruff/ty rule checking
for python files, mostly to also save myself from having to
manually correct every single thing ruff is saying it's wrong
"""

import ast
import json
import shutil
import subprocess  # noqa: S404 - used deliberately, only to invoke ruff itself
import sys
from pathlib import Path

# Resolved once so subprocess calls use a full path instead of a bare
# "ruff", which avoids S607 (partial executable path / PATH hijacking).
RUFF_BIN = shutil.which("ruff") or "ruff"

MAX_ARGS: int = 2
COPYRIGHT_LINE = "# Copyright (c) 2026 Luz\n"
SHEBANG_LINE = "#!/usr/bin/env python3\n"
INIT_FILENAME = "__init__.py"

# Ruff codes for "missing docstring" (the D1xx family).
# D100 = missing docstring in a regular module; ruff instead reports D104
# for missing docstring in a package (i.e. __init__.py specifically).
MISSING_MODULE_DOCSTRING_CODES = {"D100", "D104"}
MISSING_CLASS_DOCSTRING_CODES = {"D101", "D106"}
MISSING_FUNCTION_DOCSTRING_CODES = {"D102", "D103", "D105", "D107"}
# Everything above, used to check what our own logic is responsible for.
MISSING_DOCSTRING_CODES = (
    MISSING_MODULE_DOCSTRING_CODES
    | MISSING_CLASS_DOCSTRING_CODES
    | MISSING_FUNCTION_DOCSTRING_CODES
)

# Summary + blank line + description, closing quotes on their own line.
# Every generated docstring (module or function) follows this shape.
# (Used only as a fallback - in practice regular files already carry
# their own real docstring, so this rarely gets inserted.)
MODULE_DOCSTRING_LINES = [
    '"""TODO: describe this module.\n',
    "\n",
    "TODO: add description.\n",
    '"""\n',
]

# __init__.py files get a fixed, minimal docstring instead of a TODO stub,
# since package-level docstrings rarely need real content.
INIT_DOCSTRING_LINES = [
    '"""Function Package.\n',
    "\n",
    "This docstring is to appease Ruff.\n",
    '"""\n',
]


def run_ruff(filepath: Path) -> list[dict]:
    """Run ruff against a file and return CPY/D violations.

    Parameters
    ----------
    filepath : Path
        path to the given file

    Returns
    -------
    list[dict]
        JSON diagnostics ruff reported for this file

    """
    result = subprocess.run(  # noqa: S603 - list args, no shell, trusted binary
        [
            RUFF_BIN,
            "check",
            "--select",
            "CPY,D",
            "--output-format=json",
            str(filepath),
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    if not result.stdout.strip():
        return []
    return json.loads(result.stdout)


def apply_ruff_autofix(filepath: Path) -> bool:
    """Apply ruff's own autofixes for CPY/D violations, if any exist.

    This handles every style-level issue ruff already knows how to fix
    on its own (quote style, whitespace, blank-line placement, missing
    end punctuation, capitalization, and similar) so our own logic only
    has to deal with things ruff can't safely infer, like the actual
    text of a missing docstring. `--unsafe-fixes` is included because
    the only "unsafe" fixes in the D ruleset are things like appending
    a period to a docstring's first line - low risk, worth automating.

    Parameters
    ----------
    filepath : Path
        path to the file to autofix

    Returns
    -------
    bool
        True if ruff changed the file

    """
    before = filepath.read_text(encoding="utf-8")
    subprocess.run(  # noqa: S603 - list args, no shell, trusted binary
        [
            RUFF_BIN,
            "check",
            "--select",
            "CPY,D",
            "--fix-only",
            "--unsafe-fixes",
            "--output-format=json",
            str(filepath),
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    after = filepath.read_text(encoding="utf-8")
    return before != after


def _annotation_is_none(annotation: ast.expr | None) -> bool:
    """Check whether a return annotation is explicitly `None`.

    Parameters
    ----------
    annotation : ast.expr | None
        the `node.returns` annotation of a function, if any

    Returns
    -------
    bool
        True if the annotation is missing or is literally `None`

    """
    if annotation is None:
        return True
    if isinstance(annotation, ast.Constant) and annotation.value is None:
        return True
    return isinstance(annotation, ast.Name) and annotation.id == "None"


def build_stub_docstring(
    node: ast.FunctionDef | ast.AsyncFunctionDef | ast.ClassDef,
    indent: str,
) -> list[str]:
    """Build a numpy-style TODO docstring for a function, method, or class.

    Follows the same shape as the module docstring: a one-line summary,
    a blank line, a short description, then any Parameters/Returns
    sections (functions/methods only), with the closing quotes on their
    own line.

    Parameters
    ----------
    node : ast.FunctionDef | ast.AsyncFunctionDef | ast.ClassDef
        the node missing a docstring
    indent : str
        the indentation string to prefix each generated line with

    Returns
    -------
    list[str]
        lines (including newlines) to insert as the node's docstring

    """
    is_class = isinstance(node, ast.ClassDef)
    params = (
        [] if is_class else [a.arg for a in node.args.args if a.arg != "self"]
    )
    # Only document a Returns section if there's a non-None return
    # annotation. No annotation at all is treated as "unknown/none" too,
    # since we have no real type info to describe.
    has_return = (
        not is_class
        and node.returns is not None
        and not _annotation_is_none(node.returns)
    )

    lines = [
        f'{indent}"""TODO: describe {node.name}.\n',
        f"{indent}\n",
        f"{indent}TODO: add description.\n",
    ]
    if params:
        lines.extend(
            (f"{indent}\n", f"{indent}Parameters\n", f"{indent}----------\n"),
        )
        for p in params:
            lines.extend(
                (f"{indent}{p} : TODO\n", f"{indent}    TODO: describe {p}\n"),
            )
    if has_return:
        lines.extend(
            (
                f"{indent}\n",
                f"{indent}Returns\n",
                f"{indent}-------\n",
                f"{indent}TODO\n",
                f"{indent}    TODO: describe return value\n",
            ),
        )
    # Numpy-style (D413) wants a blank line after the last section, but
    # only when there was a section to begin with.
    if params or has_return:
        lines.append(f"{indent}\n")
    lines.append(f'{indent}"""\n')
    return lines


def find_docstring_node(
    tree: ast.Module,
    lineno: int,
) -> ast.FunctionDef | ast.AsyncFunctionDef | ast.ClassDef | None:
    """Find the function, method, or class node matching a violation's line.

    Parameters
    ----------
    tree : ast.Module
        parsed module to search
    lineno : int
        1-indexed line number ruff reported for the violation

    Returns
    -------
    ast.FunctionDef | ast.AsyncFunctionDef | ast.ClassDef | None
        the matching node, or None if not found

    """
    node_types = (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)
    for node in ast.walk(tree):
        if isinstance(node, node_types) and node.lineno == lineno:
            return node
    return None


def insert_missing_docstrings(
    lines: list[str],
    tree: ast.Module,
    violations: list[dict],
) -> list[str]:
    """Insert TODO docstrings for every function, method, or class missing one.

    Parameters
    ----------
    lines : list[str]
        current file contents, one entry per line (with newlines)
    tree : ast.Module
        parsed AST of the current file contents
    violations : list[dict]
        ruff JSON diagnostics for this file

    Returns
    -------
    list[str]
        updated file contents with stub docstrings inserted

    """
    codes = MISSING_CLASS_DOCSTRING_CODES | MISSING_FUNCTION_DOCSTRING_CODES
    targets = []
    for v in violations:
        if v["code"] in codes:
            node = find_docstring_node(tree, v["location"]["row"])
            if node is not None:
                targets.append(node)

    # Insert bottom-up so earlier line numbers stay valid as we mutate.
    targets.sort(key=lambda n: n.lineno, reverse=True)

    for node in targets:
        # Body starts after the (possibly multi-line) def/class signature.
        insert_at = node.body[0].lineno - 1
        indent = " " * (node.col_offset + 4)
        stub = build_stub_docstring(node, indent)
        lines[insert_at:insert_at] = stub

    return lines


def _relative_path_comment(filepath: Path, root: Path | None) -> str:
    """Build the '# path/to/file.py' comment line used in init headers.

    Parameters
    ----------
    filepath : Path
        the file being processed
    root : Path | None
        the root folder passed on the command line, if known

    Returns
    -------
    str
        a comment line with the file's path relative to root

    """
    if root is not None:
        try:
            rel = filepath.relative_to(root)
        except ValueError:
            rel = filepath
    else:
        rel = filepath
    return f"# {rel.as_posix()}\n"


def build_header_prepend(
    filepath: Path,
    root: Path | None,
    codes: set[str],
    lines: list[str],
) -> tuple[list[str], int]:
    """Work out which header lines (shebang/copyright/docstring) to add.

    __init__.py files get: copyright, a "# relative/path.py" comment,
    then the fixed package docstring directly underneath (no shebang,
    no blank line before the docstring, one blank line after it).

    Every other file gets: shebang, copyright, a blank line, then the
    module docstring - matching what ruff itself expects.

    Parameters
    ----------
    filepath : Path
        the file being processed
    root : Path | None
        the root folder passed on the command line, if known
    codes : set[str]
        ruff violation codes still present for this file
    lines : list[str]
        current file contents, one entry per line

    Returns
    -------
    tuple[list[str], int]
        the lines to insert, and the index to insert them at

    """
    is_init = filepath.name == INIT_FILENAME
    prepend: list[str] = []
    body_start = 0

    if lines and lines[0].startswith("#!"):
        body_start = 1
    elif not is_init:
        # __init__.py files don't get a shebang - they aren't executed
        # directly, just imported.
        prepend.append(SHEBANG_LINE)

    if "CPY001" in codes:
        prepend.append(COPYRIGHT_LINE)
        if is_init:
            prepend.append(_relative_path_comment(filepath, root))

    if codes & MISSING_MODULE_DOCSTRING_CODES:
        if is_init:
            prepend.extend(INIT_DOCSTRING_LINES)
            prepend.append("\n")
        else:
            prepend.append("\n")
            prepend.extend(MODULE_DOCSTRING_LINES)

    return prepend, body_start


def finalize_and_report(filepath: Path) -> bool:
    """Run a second autofix pass, then report anything still unresolved.

    Our inserted stubs can themselves trigger new *fixable* violations
    (e.g. a class docstring needs a blank line after it before D204 is
    happy), so autofix runs again here to mop those up. Whatever's left
    after that is a genuinely unresolved issue needing a human's
    judgment (e.g. D401 imperative mood, D417 argument descriptions
    that don't match reality) - reported, not touched.

    Parameters
    ----------
    filepath : Path
        the file to finalize

    Returns
    -------
    bool
        True if this second pass changed the file

    """
    changed = apply_ruff_autofix(filepath)
    leftover = {v["code"] for v in run_ruff(filepath)}
    if leftover:
        codes_str = ", ".join(sorted(leftover))
        print(
            f"  needs manual review ({codes_str}): {filepath}",
            file=sys.stderr,
        )
    return changed


def open_file(filepath: Path, root: Path | None = None) -> bool:
    """Alters the file given to it.

    Runs ruff's own autofix first (covers every D/CPY violation ruff can
    safely resolve on its own), re-checks what's left, then fills in
    missing docstrings/copyright notices with TODO stubs since ruff has
    no way to invent that content itself. Anything still flagged after
    both passes is left alone and reported for manual review.

    Parameters
    ----------
    filepath : Path
        path to the given file
    root : Path | None
        the root folder this file was discovered under, used to build
        the relative-path comment in __init__.py headers

    Returns
    -------
    bool
        True if the file was modified, False otherwise

    """
    changed = apply_ruff_autofix(filepath)

    violations = run_ruff(filepath)
    codes = {v["code"] for v in violations}

    with filepath.open("r", encoding="utf-8") as f:
        source = f.read()
    lines = source.splitlines(keepends=True)

    try:
        tree = ast.parse(source, filename=str(filepath))
    except SyntaxError as e:
        print(f"Skipping {filepath}: {e}", file=sys.stderr)
        return changed

    # Function/method/class-level docstrings first (uses original line
    # numbers, before the header gets any lines prepended to it).
    if violations:
        new_lines = insert_missing_docstrings(lines, tree, violations)
        if new_lines != lines:
            lines = new_lines
            changed = True

    prepend, body_start = build_header_prepend(filepath, root, codes, lines)
    if prepend:
        lines = lines[:body_start] + prepend + lines[body_start:]
        changed = True

    if changed:
        with filepath.open("w", encoding="utf-8") as f:
            f.writelines(lines)

    if finalize_and_report(filepath):
        changed = True

    return changed


def main() -> None:
    """Entry point of the script."""
    if len(sys.argv) != MAX_ARGS:
        print("Usage: python autodoc.py <folder>", file=sys.stderr)
        sys.exit(0)
    folder: Path = Path(sys.argv[1])
    if not folder.is_dir():
        print(f"{folder} is not a valid dir", file=sys.stderr)
        sys.exit(1)
    for py_file in folder.rglob("*.py"):
        modified = open_file(py_file, root=folder)
        status = "updated" if modified else "unchanged"
        print(f"{status}: {py_file}")


if __name__ == "__main__":
    main()
