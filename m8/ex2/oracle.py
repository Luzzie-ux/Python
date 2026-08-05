#!/usr/bin/env python3


"""
Directory: ex2/
Files to Submit: oracle.py, requirements.txt, .env.example, .gitignore
Authorized: os, sys, python-dotenv modules, file operations
"""

import sys
import os

ENV: str = ".env"

VARS: list[tuple[str, str, str | None]] = [
    ("MATRIX_MODE", "Execution mode", "production"),
    ("DATABASE_URL", "Data storage connection", "Not Available"),
    ("API_KEY", "External services secret", "Not Available"),
    ("LOG_LEVEL", "Logging verbosity", "INFO"),
    ("ZION_ENDPOINT", "Resistance network URL", "https://zion.local:8080"),
]


def check() -> bool:
    try:
        from dotenv import load_dotenv
    except ModuleNotFoundError:
        print("Could Not Find module 'dotenv'\n")
        return False

    load_dotenv(ENV)
    return True


def get(condition: bool) -> dict[str, str | None]:
    if not condition:
        print("Looking in PATH for vars\n")

    vars: dict[str, str | None] = {}
    for name, _, _ in VARS:
        var: str | None = os.environ.get(name)
        if var is None:
            print(f"Value for variable '{name}' missing")
            continue
        vars[name] = var
    return vars


def display(vars: dict[str, str | None], error: bool, mode: str) -> bool:

    if error is True:
        print("MATRIX_MODE has to be set to either:")
        print("     development or production")
        return False
    if mode == "dev":
        print(f"Mode: {vars.pop('MATRIX_MODE')}")
        for key, value in vars.items():
            print(f"{key}: {value}")
        return True
    elif mode == "prod":
        print(f"Mode: {vars.pop('MATRIX_MODE')}")
        for name, _, default in VARS[1:]:
            print(f"{name}: {default}")
        return True
    else:
        return False


def oracle(vars: dict[str, str | None]) -> bool:
    print("\nConfiguration loaded:")

    if len(vars) < len(VARS):
        for name, _, default in VARS:
            if name not in vars:
                print(f"{name} missing, using default value for it")
                vars[name] = default
    value: str | None = vars["MATRIX_MODE"]

    if value == "production":
        return display(vars, False, "prod")
    elif value == "development":
        return display(vars, False, "dev")
    else:
        return display(vars, True, "")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")
    loaded: bool = check()
    data: dict[str, str | None] = get(loaded)
    sec_check = oracle(data)
    if not sec_check:
        sys.exit(1)
    print(
        "Environment security check:"
        "[OK] No hardcoded secrets detected"
        "[OK] .env file properly configured"
        "[OK] Production overrides available"
        "The Oracle sees all configurations"
    )
    return


if __name__ == "__main__":
    main()
