"""
Update test files to import from user_solution.py first, falling back to solution.py.
"""

import re
from pathlib import Path


def update_test_file(test_path: Path) -> bool:
    """Update a test file's import statement."""
    content = test_path.read_text(encoding='utf-8')

    # Check if already updated
    if 'user_solution' in content:
        return False

    # Find and replace the import statement
    old_import = 'from solution import Solution, PROBLEM_METADATA'
    new_import = '''try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA'''

    if old_import not in content:
        # Try alternative pattern
        old_import = 'from solution import Solution'
        new_import = '''try:
    from user_solution import Solution
except ImportError:
    from solution import Solution'''

        if old_import not in content:
            print(f"  Skipped: {test_path.name} - no matching import found")
            return False

    new_content = content.replace(old_import, new_import)
    test_path.write_text(new_content, encoding='utf-8')
    return True


def main():
    problems_dir = Path(__file__).parent.parent / 'problems'

    if not problems_dir.exists():
        print(f"Problems directory not found: {problems_dir}")
        return

    updated = 0
    skipped = 0

    for test_path in problems_dir.rglob('test_solution.py'):
        print(f"Processing: {test_path.parent.name}")

        if update_test_file(test_path):
            updated += 1
        else:
            skipped += 1

    print(f"\nUpdated {updated} test files, skipped {skipped}")


if __name__ == '__main__':
    main()
