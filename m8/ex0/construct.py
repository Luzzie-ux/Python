#!/usr/bin/env python3


"""
Directory: ex0/
Files to Submit: construct.py
Authorized: sys, os, site modules, print()
"""

import sys, os, site


def is_venv() -> bool:
    if sys.prefix != sys.base_exec_prefix:
        return True
    elif os.environ.get("VIRTUAL_ENV"):
        return True
    return False


def env_name() -> str:
    env: str | None = os.environ.get("VIRTUAL_ENV")
    if env:
        return os.path.basename(env)
    return os.path.basename(sys.prefix)


def path() -> str:
    return os.environ.get("VIRTUAL_ENV", sys.prefix)


def get_pkcg() -> str:

    pyv: str = f"python{sys.version_info.major}.{sys.version_info.minor}"
    pgkc: str = os.path.join(sys.prefix, "lib", pyv, "site-packages")
    
    if hasattr(site, "getsitepackages"):
        pack: list[str] = site.getsitepackages()
        return pack[0] if pack else pgkc


def main() -> None:
    print("\nMATRIX STATUS: ", end="")
    if is_venv():
        return print(
            "Welcome to the construct\n\n"
            f"Current Python: {sys.executable}\n"
            f"Virtual Environment: {env_name()} \n"
            f"Environment Path: {path()}\n\n"
            "SUCCESS: You're in an isolated environment!\n"
            "Safe to install packages without affecting\n"
            "the global system.\n\n"
            "Package installation path:\n"
            f"{get_pkcg()}"
        )
    return print(
        "You're still plugged in\n\n"
        f"Current Python: {sys.executable}\n"
        "Virtual Environment: None detected\n\n"
        "WARNING: You're in the global environment!\n"
        "The machines can see everything you install.\n\n"
        "To enter the construct, run:\n"
        "python -m venv matrix_env\n"
        "source matrix_env/bin/activate # On Unix\n"
        "matrix_env\\Scripts\\activate # On Windows\n\n"
        "Then run this program again."
    )


if __name__ == "__main__":
    has_venv_var = os.environ.get("VIRTUAL_ENV") is not None

    has_prefix_diff = sys.prefix != getattr(sys, "base_prefix", sys.prefix)

    has_real_prefix = hasattr(sys, "real_prefix")

    print(has_venv_var or has_prefix_diff or has_real_prefix)
    
    #main()