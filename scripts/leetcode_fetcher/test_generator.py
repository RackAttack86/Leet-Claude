"""
Test Generator

Generates test_solution.py files with example-based tests.
"""

import re
from typing import Dict, Any, List, Optional
from .problem_parser import needs_helper_class


TEST_TEMPLATE = '''"""
Tests for LeetCode Problem #{number}: {title}
"""

import pytest
from .solution import Solution, PROBLEM_METADATA
{helper_imports}

{helper_functions}

class Test{class_name}:
    """Test cases for {title} problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

{test_methods}

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
'''


# Helper functions for common data structures
HELPER_FUNCTIONS = {
    "ListNode": '''
def list_to_linked(arr):
    """Convert array to linked list"""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_to_list(head):
    """Convert linked list to array"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result
''',
    "TreeNode": '''
def array_to_tree(arr):
    """Convert level-order array to binary tree"""
    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    queue = [root]
    i = 1

    while queue and i < len(arr):
        node = queue.pop(0)
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1

    return root


def tree_to_array(root):
    """Convert binary tree to level-order array"""
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing Nones
    while result and result[-1] is None:
        result.pop()

    return result
''',
}


class TestGenerator:
    """Generates test_solution.py files for LeetCode problems."""

    def generate(self, problem_data: Dict[str, Any]) -> str:
        """
        Generate test_solution.py content.

        Args:
            problem_data: Parsed problem data

        Returns:
            Complete test file content as string
        """
        signature = problem_data.get("signature")

        # Generate class name
        class_name = self._to_class_name(problem_data.get("title", "Unknown"))

        # Generate helper imports
        helper_imports = self._generate_helper_imports(signature)

        # Generate helper functions
        helper_functions = self._generate_helper_functions(signature)

        # Generate test methods
        test_methods = self._generate_test_methods(problem_data)

        return TEST_TEMPLATE.format(
            number=problem_data.get("number", 0),
            title=problem_data.get("title", "Unknown"),
            class_name=class_name,
            helper_imports=helper_imports,
            helper_functions=helper_functions,
            test_methods=test_methods,
        )

    def _to_class_name(self, title: str) -> str:
        """Convert title to PascalCase class name."""
        # Remove special characters and numbers at the start
        clean = re.sub(r'[^a-zA-Z0-9\s]', '', title)
        words = clean.split()
        return ''.join(word.capitalize() for word in words)

    def _generate_helper_imports(
        self,
        signature: Optional[Dict[str, Any]]
    ) -> str:
        """Generate imports for helper classes."""
        imports = []

        if needs_helper_class(signature, "ListNode"):
            imports.append("from .solution import ListNode")

        if needs_helper_class(signature, "TreeNode"):
            imports.append("from .solution import TreeNode")

        if needs_helper_class(signature, "Node"):
            imports.append("from .solution import Node")

        return "\n".join(imports)

    def _generate_helper_functions(
        self,
        signature: Optional[Dict[str, Any]]
    ) -> str:
        """Generate helper functions based on types used."""
        functions = []

        for class_name, func_code in HELPER_FUNCTIONS.items():
            if needs_helper_class(signature, class_name):
                functions.append(func_code)

        return "\n".join(functions)

    def _generate_test_methods(self, problem_data: Dict[str, Any]) -> str:
        """Generate test methods from examples."""
        examples = problem_data.get("examples", [])
        signature = problem_data.get("signature", {})
        method_name = signature.get("method_name", "solve") if signature else "solve"

        test_methods = []

        for i, example in enumerate(examples, 1):
            test_method = self._generate_single_test(example, i, method_name, signature)
            test_methods.append(test_method)

        # Add edge case placeholders
        test_methods.append('''
    def test_edge_case_empty(self, solution):
        """Test with empty/minimal input"""
        # TODO: Implement edge case test
        pass
''')

        return "\n".join(test_methods)

    def _generate_single_test(
        self,
        example: str,
        index: int,
        method_name: str,
        signature: Optional[Dict[str, Any]]
    ) -> str:
        """Generate a single test method from an example."""
        # Clean markdown from example
        example_clean = re.sub(r'\*\*', '', example)

        # Try to parse the example
        input_match = re.search(
            r'Input:\s*(.+?)(?=Output:|$)',
            example_clean,
            re.DOTALL | re.IGNORECASE
        )
        output_match = re.search(
            r'Output:\s*(.+?)(?=Explanation:|Example|$)',
            example_clean,
            re.DOTALL | re.IGNORECASE
        )

        if input_match and output_match:
            input_str = input_match.group(1).strip()
            output_str = output_match.group(1).strip()

            # Try to extract variable assignments
            params = self._parse_input_vars(input_str, signature)

            # Clean and extract expected value
            expected = output_str.split('\n')[0].strip()
            expected = re.sub(r'\*\*', '', expected)  # Remove markdown
            expected = re.sub(r'`', '', expected)      # Remove code markers

            # Generate test body
            if params:
                param_assignments = "\n        ".join(
                    f"{name} = {value}" for name, value in params.items()
                )
                param_call = ", ".join(params.keys())

                return f'''
    def test_example_{index}(self, solution):
        """Example {index} from problem description"""
        {param_assignments}
        expected = {expected}
        result = solution.{method_name}({param_call})
        assert result == expected
'''

        # Fallback: generate placeholder test
        return f'''
    def test_example_{index}(self, solution):
        """Example {index} from problem description"""
        # TODO: Parse and implement test for this example
        pass
'''

    def _parse_input_vars(
        self,
        input_str: str,
        signature: Optional[Dict[str, Any]]
    ) -> Dict[str, str]:
        """Parse input string to extract variable assignments."""
        params = {}

        # Get expected parameter names from signature
        expected_params = []
        if signature and signature.get("params"):
            expected_params = [p[0] for p in signature["params"]]

        # Clean up input string - remove markdown formatting
        input_str = re.sub(r'\*\*', '', input_str)
        input_str = re.sub(r'`', '', input_str)

        # Try to parse "name = value" or "name: value" patterns
        # Common patterns: nums = [1,2,3], target = 9
        patterns = [
            r'(\w+)\s*=\s*(\[.*?\]|\{.*?\}|"[^"]*"|\'[^\']*\'|-?\d+|true|false|null)',
        ]

        for pattern in patterns:
            matches = re.findall(pattern, input_str, re.IGNORECASE | re.DOTALL)
            for name, value in matches:
                # Convert JavaScript-style values to Python
                value = value.replace('true', 'True')
                value = value.replace('false', 'False')
                value = value.replace('null', 'None')
                # Clean up any remaining formatting
                value = re.sub(r'\*\*', '', value).strip()
                params[name] = value

        # If we found params, filter to only expected ones (if we know them)
        if expected_params and params:
            filtered = {}
            for name in expected_params:
                if name in params:
                    filtered[name] = params[name]
            if filtered:
                return filtered

        return params
