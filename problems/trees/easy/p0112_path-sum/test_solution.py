"""
Tests for LeetCode Problem #112: Path Sum
"""

import pytest
from .solution import Solution, PROBLEM_METADATA
from .solution import TreeNode
from .solution import Node


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


class TestPathSum:
    """Test cases for Path Sum problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        root = [5,4,8,11,None,13,4,7,2,None,None,None,1]
        targetSum = 22
        expected = true
        result = solution.hasPathSum(root, targetSum)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        root = [1,2,3]
        targetSum = 5
        expected = false
        result = solution.hasPathSum(root, targetSum)
        assert result == expected


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        root = []
        targetSum = 0
        expected = false
        result = solution.hasPathSum(root, targetSum)
        assert result == expected


    def test_edge_case_empty(self, solution):
        """Test with empty/minimal input"""
        # TODO: Implement edge case test
        pass


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
