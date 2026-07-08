#!/usr/bin/env python3


"""
Directory: ex3/
Files to Submit: ft_vault_security.py
Authorized: open(), read(), write(), print()
"""


def secure_archive(
    filename: str, mode: str, content: str | None = None
) -> tuple[bool, str]:
    try:
        with open(filename, mode) as f:
            if mode == "r":
                return (True, f.read())
            else:
                f.write(content)
                return (True, "Content successfully written to file")
    except (FileNotFoundError, PermissionError) as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")
    test: dict[str, str] = {
        "/not/existing/file": "r",
        "/etc/master.passwd": "r",
        "ancient_fragment.txt": "r",
        "new_fragments.txt": "w",
    }
    content: tuple[bool, str]
    for file, mode in test.items():
        if file == "/not/existing/file":
            print("\nUsing 'secure_archive'to read from a nonexistent file:")
            print(secure_archive(file, mode))
        elif file == "/etc/master.passwd":
            print("\nUsing 'secure_archive'to read from an inaccessible file:")
            print(secure_archive(file, mode))
        elif file == "ancient_fragment.txt":
            print("\nUsing 'secure_archive'to read from a regular file:")
            content = secure_archive(file, mode)
            print(content)
        elif file == "new_fragments.txt":
            print(
                "\nUsing 'secure_archive'to write"
                "previous content to a new file:"
            )
            print(secure_archive(file, mode, content[1]))
        else:
            return
    return


if __name__ == "__main__":
    main()
