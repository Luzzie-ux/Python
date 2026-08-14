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
import subprocess
import sys
from pathlib import Path

MAX_ARGS: int = 2
COPYRIGHT_LINE = "# Copyright (c) 2026 Luz\n"
SHEBANG_LINE = "#!/usr/bin/env python3\n"

# Ruff codes for "missing docstring" (the D1xx family)
MISSING_MODULE_DOCSTRING = "D100"
MISSING_FUNCTION_DOCSTRING_CODES = {"D102", "D103", "D105", "D106", "D107"}


def run_ruff(filepath: Path) -> list[dict]:
    """Run ruff against a file and return CPY/D/DOC violations.

    Parameters
    ----------
    filepath : Path
        path to the given file

    Returns
    -------
    list[dict]
        JSON diagnostics ruff reported for this file

    """
    result = subprocess.run(
        [
            "ruff",
            "check",
            "--select",
            "CPY,D,DOC",
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


def build_stub_docstring(
    node: ast.FunctionDef | ast.AsyncFunctionDef,
    indent: str,
) -> list[str]:
    """Build a numpy-style TODO docstring for a function/method.

    Parameters
    ----------
    node : ast.FunctionDef | ast.AsyncFunctionDef
        the function node missing a docstring
    indent : str
        the indentation string to prefix each generated line with

    Returns
    -------
    list[str]
        lines (including newlines) to insert as the function's docstring

    """
    params = [a.arg for a in node.args.args if a.arg != "self"]
    has_return = node.returns is not None

    lines = [f'{indent}"""TODO: describe {node.name}.\n']
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
    lines.append(f'{indent}\n{indent}"""\n')
    return lines


def find_function_node(
    tree: ast.Module,
    lineno: int,
) -> ast.FunctionDef | ast.AsyncFunctionDef | None:
    """Find the function/method node whose def line matches lineno.

    Parameters
    ----------
    tree : ast.Module
        parsed module to search
    lineno : int
        1-indexed line number ruff reported for the violation

    Returns
    -------
    ast.FunctionDef | ast.AsyncFunctionDef | None
        the matching node, or None if not found

    """
    for node in ast.walk(tree):
        if (
            isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            and node.lineno == lineno
        ):
            return node
    return None


def insert_function_docstrings(
    lines: list[str],
    tree: ast.Module,
    violations: list[dict],
) -> list[str]:
    """Insert TODO docstrings for every function/method missing one.

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
    targets = []
    for v in violations:
        if v["code"] in MISSING_FUNCTION_DOCSTRING_CODES:
            node = find_function_node(tree, v["location"]["row"])
            if node is not None:
                targets.append(node)

    # Insert bottom-up so earlier line numbers stay valid as we mutate.
    targets.sort(key=lambda n: n.lineno, reverse=True)

    for node in targets:
        # Body starts after the (possibly multi-line) def signature.
        insert_at = node.body[0].lineno - 1
        indent = " " * (node.col_offset + 4)
        stub = build_stub_docstring(node, indent)
        lines[insert_at:insert_at] = stub

    return lines


def open_file(filepath: Path) -> bool:
    """Alters the file given to it.

    Parameters
    ----------
    filepath : Path
        path to the given file

    Returns
    -------
    bool
        True if the file was modified, False otherwise

    """
    violations = run_ruff(filepath)
    codes = {v["code"] for v in violations}

    with filepath.open("r", encoding="utf-8") as f:
        source = f.read()
    lines = source.splitlines(keepends=True)

    try:
        tree = ast.parse(source, filename=str(filepath))
    except SyntaxError as e:
        print(f"Skipping {filepath}: {e}", file=sys.stderr)
        return False

    changed = False

    # Function/method-level docstrings first (uses original line numbers).
    if violations:
        new_lines = insert_function_docstrings(lines, tree, violations)
        if new_lines != lines:
            lines = new_lines
            changed = True

    # Header-level fixes (shebang / copyright / module docstring).
    prepend: list[str] = []
    body_start = 0

    if lines and lines[0].startswith("#!"):
        body_start = 1
    else:
        prepend.append(SHEBANG_LINE)

    if "CPY001" in codes:
        prepend.append(COPYRIGHT_LINE)

    if MISSING_MODULE_DOCSTRING in codes:
        prepend.append('"""TODO: describe this module."""\n')

    if prepend:
        lines = lines[:body_start] + prepend + lines[body_start:]
        changed = True

    if changed:
        with filepath.open("w", encoding="utf-8") as f:
            f.writelines(lines)

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
        modified = open_file(py_file)
        status = "updated" if modified else "unchanged"
        print(f"{status}: {py_file}")


if __name__ == "__main__":
    main()
