"""
Tests for LeetCode Problem #129: Sum Root to Leaf Numbers
"""

import pytest
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


class TestSumRootToLeafNumbers:
    """Test cases for Sum Root to Leaf Numbers problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        root = array_to_tree([1,2,3])
        expected = 25
        result = solution.sumNumbers(root)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        root = array_to_tree([4,9,0,5,1])
        expected = 1026
        result = solution.sumNumbers(root)
        assert result == expected


    def test_edge_case_single_node(self, solution):
        """Test with single node"""
        root = array_to_tree([5])
        expected = 5
        result = solution.sumNumbers(root)
        assert result == expected

    def test_single_path_left(self, solution):
        """Test with single path going left"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        # Path: 1 -> 2 -> 3 = 123
        expected = 123
        result = solution.sumNumbers(root)
        assert result == expected

    def test_single_path_right(self, solution):
        """Test with single path going right"""
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        # Path: 1 -> 2 -> 3 = 123
        expected = 123
        result = solution.sumNumbers(root)
        assert result == expected

    def test_zero_root(self, solution):
        """Test with zero as root"""
        root = array_to_tree([0, 1, 2])
        # Paths: 0->1 = 01 = 1, 0->2 = 02 = 2, sum = 3
        expected = 3
        result = solution.sumNumbers(root)
        assert result == expected

    def test_all_zeros(self, solution):
        """Test with all zeros"""
        root = array_to_tree([0, 0, 0])
        # Paths: 0->0 = 0, 0->0 = 0, sum = 0
        expected = 0
        result = solution.sumNumbers(root)
        assert result == expected

    def test_large_numbers(self, solution):
        """Test with values 0-9 forming larger numbers"""
        root = array_to_tree([9, 9, 9])
        # Paths: 9->9 = 99, 9->9 = 99, sum = 198
        expected = 198
        result = solution.sumNumbers(root)
        assert result == expected

    def test_complete_tree_three_levels(self, solution):
        """Test with complete tree of three levels"""
        root = array_to_tree([1, 2, 3, 4, 5, 6, 7])
        # Paths: 1->2->4 = 124, 1->2->5 = 125, 1->3->6 = 136, 1->3->7 = 137
        expected = 124 + 125 + 136 + 137
        result = solution.sumNumbers(root)
        assert result == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
