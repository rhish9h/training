"""
Script to check mypy compliance with strict settings.

This script runs mypy with strict settings on the utils.py file
and reports the results.
"""

import subprocess
import sys


def run_mypy_check():
    """Run mypy with strict settings and report results."""
    print("Running mypy check with strict settings...")
    result = subprocess.run(
        ["mypy", "--strict", "utils.py"],
        capture_output=True,
        text=True,
    )
    
    # Print output
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    
    # Check for errors
    if result.returncode == 0:
        print("✅ Success! All types are valid.")
        return True
    else:
        print(f"❌ MyPy found type errors. Return code: {result.returncode}")
        return False


if __name__ == "__main__":
    success = run_mypy_check()
    sys.exit(0 if success else 1)
