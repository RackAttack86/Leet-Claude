"""
Script to run all tests for a specific pattern
Usage: python scripts/run_pattern.py two_pointers
"""

import argparse
import subprocess
import sys
from pathlib import Path


def run_pattern_tests(pattern: str, verbose: bool = False):
    """Run all tests for a specific pattern"""

    pattern_dir = Path(f"problems/{pattern}")

    if not pattern_dir.exists():
        print(f"Error: Pattern directory not found: {pattern_dir}")
        print("\nAvailable patterns:")
        problems_dir = Path("problems")
        if problems_dir.exists():
            for p in sorted(problems_dir.iterdir()):
                if p.is_dir() and not p.name.startswith("__"):
                    print(f"  - {p.name}")
        sys.exit(1)

    # Build pytest command
    cmd = ["pytest", str(pattern_dir)]
    if verbose:
        cmd.append("-vv")
    cmd.extend(["-m", pattern])

    print(f"Running tests for pattern: {pattern}")
    print(f"Command: {' '.join(cmd)}\n")

    # Run tests
    result = subprocess.run(cmd)
    sys.exit(result.returncode)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run tests for a specific pattern")
    parser.add_argument("pattern", type=str, help="Pattern name (e.g., two_pointers)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")

    args = parser.parse_args()
    run_pattern_tests(args.pattern, args.verbose)
