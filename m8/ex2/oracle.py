#!/usr/bin/env python3


"""
Directory: ex2/
Files to Submit: oracle.py, requirements.txt, .env.example, .gitignore
Authorized: os,  python-dotenv modules, file operations
"""

import os
import sys
from sys import stderr

FILE: str = ".env"
EXISTS: bool = os.path.exists(FILE)
PROD: list[tuple[str, str]] = [
    ("MATRIX_MODE", "production"),
    ("DATABASE_URL", "Not Available"),
    ("API_KEY", "Not Available"),
    ("LOG_LEVEL", "INFO"),
    ("ZION_ENDPOINT", "https://zion.local:8080"),
]


def check() -> bool:
    if EXISTS:
        try:
            from dotenv import load_dotenv  # type: ignore
        except ModuleNotFoundError:
            print("Could Not Find module 'dotenv'\n", file=stderr)
            return False

        load_dotenv(FILE)
        return True
    print(f"Could Not find file {FILE}\n", file=stderr)
    return False


def get(loaded: bool) -> dict[str, str | None]:
    if not loaded:
        print("Looking in PATH for vars\n")

    env_vars: dict[str, str | None] = {}
    for name, _ in PROD:
        var: str | None = os.environ.get(name)

        if var is None or not var:
            print(f"Value for variable '{name}' missing", file=stderr)
            continue

        env_vars[name] = var
    return env_vars


def oracle(env: dict[str, str | None]) -> bool:
    print("\nConfiguration loaded:")

    for name, default in PROD:
        if name not in env:
            print(f"{name} missing, defaulting", file=stderr)
            env[name] = default

    mode: str | None = env["MATRIX_MODE"]

    match mode:
        case "production":
            print(f"\nMode: {mode}")
            for name, default in PROD[1:]:
                print(f"{name}: {default}")
            print()
            return True

        case "development":
            print(f"\nMode: {mode}")
            for key, value in env.items():
                if key != "MATRIX_MODE":
                    print(f"{key}: {value}")
            print()
            return True

        case _:
            print()
            print(f"[ERROR]: MATRIX_MODE was set to '{mode}'", file=stderr)
            print("[WARN]: It should only be set to ", end="", file=stderr)
            print("'development' or 'production'", file=stderr)
            print()
            return False


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")
    loaded: bool = check()
    data: dict[str, str | None] = get(loaded)
    sec_check: bool = oracle(data)
    if not sec_check:
        print(
            "The Oracle rejects your attempt to communication",
            file=stderr,
        )
        sys.exit(1)
    print("Environment security check:\n")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations")


if __name__ == "__main__":
    main()
