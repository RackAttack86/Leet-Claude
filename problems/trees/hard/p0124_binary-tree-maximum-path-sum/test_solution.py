"""
Tests for LeetCode Problem #124: Binary Tree Maximum Path Sum
"""

import pytest
from collections import deque
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA
from solution import TreeNode
from solution import Node


def array_to_tree(arr):
    """Convert level-order array to binary tree"""
    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])  # Use deque for O(1) popleft
    i = 1

    while queue and i < len(arr):
        node = queue.popleft()  # O(1) instead of O(n) pop(0)
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
    queue = deque([root])  # Use deque for O(1) popleft

    while queue:
        node = queue.popleft()  # O(1) instead of O(n) pop(0)
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


class TestBinaryTreeMaximumPathSum:
    """Test cases for Binary Tree Maximum Path Sum problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        root = array_to_tree([1,2,3])
        expected = 6
        result = solution.maxPathSum(root)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        root = array_to_tree([-10,9,20,None,None,15,7])
        expected = 42
        result = solution.maxPathSum(root)
        assert result == expected


    def test_edge_case_single_node(self, solution):
        """Test with single node tree"""
        root = array_to_tree([5])
        expected = 5
        result = solution.maxPathSum(root)
        assert result == expected

    def test_edge_case_all_negative(self, solution):
        """Test with all negative values"""
        root = array_to_tree([-3])
        expected = -3
        result = solution.maxPathSum(root)
        assert result == expected


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
