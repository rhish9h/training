"""
Script to check mypy compliance with strict settings.

This script runs mypy with strict settings on the benchmark.py file
and reports the results.
"""

import subprocess
import sys


def run_mypy_check():
    """Run mypy with strict settings and report results."""
    print("Running mypy check with strict settings...")
    result = subprocess.run(
        ["mypy", "--strict", "benchmark.py"],
        capture_output=True,
        text=True,
    )
    
    # Print output
    if result.stdout:
        print("\nOutput:")
        print(result.stdout)
    
    if result.stderr:
        print("\nErrors:")
        print(result.stderr)
    
    # Check if successful
    if result.returncode == 0:
        print("\n✅ Success! No type errors found.")
        return True
    else:
        print(f"\n❌ Failed with return code {result.returncode}")
        print("Please fix the type errors above.")
        return False


if __name__ == "__main__":
    success = run_mypy_check()
    sys.exit(0 if success else 1)
