"""
Script to scaffold a new LeetCode problem
Usage: python scripts/create_problem.py --number 1 --name "Two Sum" --pattern two_pointers --difficulty Easy
"""

import argparse
import os
from pathlib import Path


SOLUTION_TEMPLATE = '''"""
LeetCode Problem #{number}: {name}
Difficulty: {difficulty}
Pattern: {pattern_display}
Link: https://leetcode.com/problems/{slug}/

Problem:
--------
[TODO: Add problem description]

Constraints:
-----------
[TODO: Add constraints]

Examples:
---------
[TODO: Add examples]
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #{number}: {name}

    Approach: [TODO: Describe approach]
    Time Complexity: O(?)
    Space Complexity: O(?)

    Key Insights:
    [TODO: Add key insights]
    """

    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {{
    "number": {number},
    "name": "{name}",
    "difficulty": "{difficulty}",
    "pattern": "{pattern_display}",
    "topics": [],  # TODO: Add topics
    "url": "https://leetcode.com/problems/{slug}/",
    "companies": [],  # TODO: Add companies
    "time_complexity": "O(?)",
    "space_complexity": "O(?)",
}}
'''

TEST_TEMPLATE = '''"""
Tests for LeetCode Problem #{number}: {name}
"""

import pytest
from .solution import Solution, PROBLEM_METADATA


class Test{class_name}:
    """Test cases for {name} problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        # TODO: Implement test
        pass

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        # TODO: Implement test
        pass

    # Edge cases
    def test_edge_case_1(self, solution):
        """TODO: Describe edge case"""
        # TODO: Implement test
        pass

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
'''

README_TEMPLATE = '''# Problem {number}: {name}

**Difficulty:** {difficulty}
**Pattern:** {pattern_display}
**Link:** [LeetCode](https://leetcode.com/problems/{slug}/)

## Problem Description

[TODO: Add problem description]

## Approaches

### 1. [Approach Name]

**Time Complexity:** O(?)
**Space Complexity:** O(?)

```python
# TODO: Add code snippet
```

**Why this works:**
[TODO: Explain approach]

## Key Insights

[TODO: Add key insights]

## Common Mistakes

[TODO: Add common mistakes]

## Related Problems

[TODO: Add related problems]

## Tags

[TODO: Add tags]
'''


def slugify(name: str) -> str:
    """Convert problem name to URL slug"""
    return name.lower().replace(" ", "-").replace("'", "")


def create_problem(number: int, name: str, pattern: str, difficulty: str):
    """Create all files for a new problem"""

    # Validate inputs
    valid_difficulties = ["Easy", "Medium", "Hard"]
    if difficulty not in valid_difficulties:
        raise ValueError(f"Difficulty must be one of {valid_difficulties}")

    # Create paths
    slug = slugify(name)
    problem_dir = Path(f"problems/{pattern}/p{number:04d}_{slug}")

    if problem_dir.exists():
        print(f"Error: Problem directory already exists: {problem_dir}")
        return

    # Create directory
    problem_dir.mkdir(parents=True, exist_ok=True)
    print(f"Created directory: {problem_dir}")

    # Create __init__.py
    (problem_dir / "__init__.py").touch()

    # Create solution.py
    class_name = "".join(word.capitalize() for word in name.split())
    pattern_display = pattern.replace("_", " ").title()
    solution_content = SOLUTION_TEMPLATE.format(
        number=number,
        name=name,
        difficulty=difficulty,
        pattern_display=pattern_display,
        slug=slug,
        class_name=class_name
    )
    (problem_dir / "solution.py").write_text(solution_content)
    print(f"Created: {problem_dir / 'solution.py'}")

    # Create test_solution.py
    test_content = TEST_TEMPLATE.format(
        number=number,
        name=name,
        class_name=class_name
    )
    (problem_dir / "test_solution.py").write_text(test_content)
    print(f"Created: {problem_dir / 'test_solution.py'}")

    # Create README.md
    readme_content = README_TEMPLATE.format(
        number=number,
        name=name,
        difficulty=difficulty,
        pattern_display=pattern_display,
        slug=slug
    )
    (problem_dir / "README.md").write_text(readme_content)
    print(f"Created: {problem_dir / 'README.md'}")

    print(f"\nSuccessfully created problem {number}: {name}")
    print(f"Location: {problem_dir}")
    print(f"\nNext steps:")
    print(f"1. Edit {problem_dir / 'solution.py'} to implement the solution")
    print(f"2. Edit {problem_dir / 'test_solution.py'} to add test cases")
    print(f"3. Run tests: pytest {problem_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a new LeetCode problem")
    parser.add_argument("--number", "-n", type=int, required=True, help="Problem number")
    parser.add_argument("--name", type=str, required=True, help="Problem name")
    parser.add_argument("--pattern", "-p", type=str, required=True, help="Pattern directory name")
    parser.add_argument("--difficulty", "-d", type=str, required=True,
                       choices=["Easy", "Medium", "Hard"], help="Problem difficulty")

    args = parser.parse_args()

    create_problem(args.number, args.name, args.pattern, args.difficulty)
