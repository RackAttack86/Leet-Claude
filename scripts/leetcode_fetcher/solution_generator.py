"""
Solution Generator

Generates solution.py files with correct function signatures and metadata.
"""

from typing import Dict, Any, List, Optional
from .problem_parser import get_required_imports, needs_helper_class


SOLUTION_TEMPLATE = '''"""
LeetCode Problem #{number}: {title}
Difficulty: {difficulty}
Pattern: {pattern_display}
Link: https://leetcode.com/problems/{slug}/

Problem:
--------
{description}

Constraints:
-----------
{constraints}

Examples:
---------
{examples}
"""

{imports}
{helper_classes}

class Solution:
    """
    Solution to LeetCode Problem #{number}: {title}

    Approach: [TODO: Describe approach]
    Time Complexity: O(?)
    Space Complexity: O(?)

    Key Insights:
    [TODO: Add key insights]
    """

    {method_signature}


# Metadata for tracking
PROBLEM_METADATA = {{
    "number": {number},
    "name": "{title}",
    "difficulty": "{difficulty}",
    "pattern": "{pattern_display}",
    "topics": {topics},
    "url": "https://leetcode.com/problems/{slug}/",
    "companies": [],
    "time_complexity": "O(?)",
    "space_complexity": "O(?)",
}}
'''

# Helper class definitions
HELPER_CLASSES = {
    "ListNode": '''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
''',
    "TreeNode": '''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
''',
    "Node": '''
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
''',
}


class SolutionGenerator:
    """Generates solution.py files for LeetCode problems."""

    def generate(self, problem_data: Dict[str, Any]) -> str:
        """
        Generate complete solution.py content.

        Args:
            problem_data: Parsed problem data from ProblemParser

        Returns:
            Complete solution.py file content as string
        """
        signature = problem_data.get("signature")

        # Generate imports
        imports = self._generate_imports(signature, problem_data)

        # Generate helper classes if needed
        helper_classes = self._generate_helper_classes(signature)

        # Format method signature
        method_sig = self._format_method_signature(signature)

        # Format constraints
        constraints = self._format_constraints(problem_data.get("constraints", []))

        # Format examples
        examples = self._format_examples(problem_data.get("examples", []))

        # Get pattern display name
        pattern_display = problem_data.get("pattern", "").replace("_", " ").title()

        return SOLUTION_TEMPLATE.format(
            number=problem_data.get("number", 0),
            title=problem_data.get("title", "Unknown"),
            difficulty=problem_data.get("difficulty", "Medium"),
            pattern_display=pattern_display,
            slug=problem_data.get("slug", "unknown"),
            description=problem_data.get("description", "[Problem description]"),
            constraints=constraints,
            examples=examples,
            imports=imports,
            helper_classes=helper_classes,
            method_signature=method_sig,
            topics=problem_data.get("topics", []),
        )

    def _generate_imports(
        self,
        signature: Optional[Dict[str, Any]],
        problem_data: Dict[str, Any]
    ) -> str:
        """Generate import statements."""
        lines = []

        # Typing imports
        typing_imports = get_required_imports(signature)
        if typing_imports:
            lines.append(f"from typing import {', '.join(typing_imports)}")

        # Pattern-specific imports
        pattern = problem_data.get("pattern", "")

        if pattern == "heaps":
            lines.append("import heapq")

        # Check if Counter might be useful (based on topics or description)
        topics_str = " ".join(problem_data.get("topics", [])).lower()
        desc = problem_data.get("description", "").lower()

        if "frequency" in desc or "count" in desc or "hash table" in topics_str:
            lines.append("from collections import Counter, defaultdict")
        elif "hash" in topics_str:
            lines.append("from collections import defaultdict")

        if "deque" in desc.lower() or pattern == "bfs_dfs":
            if "from collections import" in "\n".join(lines):
                # Modify existing import
                for i, line in enumerate(lines):
                    if "from collections import" in line:
                        if "deque" not in line:
                            lines[i] = line.rstrip() + ", deque"
            else:
                lines.append("from collections import deque")

        return "\n".join(lines)

    def _generate_helper_classes(
        self,
        signature: Optional[Dict[str, Any]]
    ) -> str:
        """Generate helper class definitions if needed."""
        classes = []

        for class_name, class_def in HELPER_CLASSES.items():
            if needs_helper_class(signature, class_name):
                classes.append(class_def)

        return "\n".join(classes)

    def _format_method_signature(
        self,
        signature: Optional[Dict[str, Any]]
    ) -> str:
        """Format the method signature(s)."""
        if not signature:
            return "def solve(self):"

        # Check if this is a design problem with multiple methods
        all_methods = signature.get("all_methods", [])
        is_design = signature.get("is_design_problem", False)

        if is_design and len(all_methods) > 1:
            # Generate all methods for design problems
            method_strs = []
            for method in all_methods:
                method_str = self._format_single_method(method)
                method_strs.append(method_str)
            return "\n\n    ".join(method_strs)
        else:
            # Single method
            return self._format_single_method(signature)

    def _format_single_method(self, method: Dict[str, Any]) -> str:
        """Format a single method signature."""
        method_name = method.get("method_name", "solve")
        params = method.get("params", [])
        return_type = method.get("return_type", "")

        # Build parameter string
        param_strs = ["self"]
        for name, type_hint in params:
            param_strs.append(f"{name}: {type_hint}")

        params_str = ", ".join(param_strs)

        if return_type:
            sig = f"def {method_name}({params_str}) -> {return_type}:"
        else:
            sig = f"def {method_name}({params_str}):"

        # Add docstring and pass
        return f'''{sig}
        """
        [TODO: Implement]
        """
        pass'''

    def _format_constraints(self, constraints: List[str]) -> str:
        """Format constraints as bullet list."""
        if not constraints:
            return "[See LeetCode for constraints]"

        return "\n".join(f"- {c}" for c in constraints)

    def _format_examples(self, examples: List[str]) -> str:
        """Format examples."""
        if not examples:
            return "[See LeetCode for examples]"

        return "\n\n".join(examples)


README_TEMPLATE = '''# Problem {number}: {title}

**Difficulty:** {difficulty}
**Pattern:** {pattern_display}
**Link:** [LeetCode](https://leetcode.com/problems/{slug}/)

## Problem Description

{description}

## Constraints

{constraints}

## Examples

{examples}

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
'''


class ReadmeGenerator:
    """Generates README.md files for problems."""

    def generate(self, problem_data: Dict[str, Any]) -> str:
        """
        Generate README.md content.

        Args:
            problem_data: Parsed problem data

        Returns:
            README.md content as string
        """
        pattern_display = problem_data.get("pattern", "").replace("_", " ").title()

        constraints = problem_data.get("constraints", [])
        constraints_str = "\n".join(f"- {c}" for c in constraints) if constraints else "[See LeetCode]"

        examples = problem_data.get("examples", [])
        examples_str = "\n\n".join(examples) if examples else "[See LeetCode]"

        return README_TEMPLATE.format(
            number=problem_data.get("number", 0),
            title=problem_data.get("title", "Unknown"),
            difficulty=problem_data.get("difficulty", "Medium"),
            pattern_display=pattern_display,
            slug=problem_data.get("slug", "unknown"),
            description=problem_data.get("description", "[Problem description]"),
            constraints=constraints_str,
            examples=examples_str,
        )
