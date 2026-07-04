#!/usr/bin/env python3


"""
Directory: ex3/
Files to Submit: ft_vault_security.py
Authorized: open(), read(), write(), print()
"""


def secure_archive(name: str, mode: str, content: str
                   ) -> tuple[bool, str]:
    try:
        with open(name, mode) as file:
            if mode == "r":
                return (True, file.read())
            else:
                file.write(content)
                return (True, "Content successfully written to file")
    except Exception as e:
        return (False, str(e))


def ft_vault_security() -> None:
    print("=== Cyber Archives Security ===")
    n: int = 4
    i: int = 0
    content: tuple[bool, str]
    while i < n:
        if i == 0:
            print("\nUsing 'secure_archive' to read from a nonexistent file:")
            print(secure_archive("/not/existing/file", "r", ""))
        elif i == 1:
            print("\nUsing 'secure_archive'to read from an inaccessible file:")
            print(secure_archive("/etc/master.passwd", "r", ""))
        elif i == 2:
            print("\nUsing 'secure_archive' to read from a regular file:")
            content = secure_archive("ancient_fragment.txt", "r", "")
            print(content)
        elif i == 3:
            print(
                "\nUsing 'secure_archive' to "
                "write previous content to a new file:"
            )
            print(secure_archive("new_fragments.txt", "w", content[1]))
        i += 1


def main() -> None:
    ft_vault_security()
    return


if __name__ == "__main__":
    main()
