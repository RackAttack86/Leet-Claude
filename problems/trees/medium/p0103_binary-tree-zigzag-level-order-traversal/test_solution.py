"""
Tests for LeetCode Problem #103: Binary Tree Zigzag Level Order Traversal
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


class TestBinaryTreeZigzagLevelOrderTraversal:
    """Test cases for Binary Tree Zigzag Level Order Traversal problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        root = array_to_tree([3,9,20,None,None,15,7])
        expected = [[3],[20,9],[15,7]]
        result = solution.zigzagLevelOrder(root)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        root = array_to_tree([1])
        expected = [[1]]
        result = solution.zigzagLevelOrder(root)
        assert result == expected


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        root = array_to_tree([])
        expected = []
        result = solution.zigzagLevelOrder(root)
        assert result == expected


    def test_single_level(self, solution):
        """Test with single level (just root)"""
        root = array_to_tree([5])
        expected = [[5]]
        result = solution.zigzagLevelOrder(root)
        assert result == expected

    def test_two_levels(self, solution):
        """Test with two levels"""
        root = array_to_tree([1, 2, 3])
        # Level 0: left to right -> [1]
        # Level 1: right to left -> [3, 2]
        expected = [[1], [3, 2]]
        result = solution.zigzagLevelOrder(root)
        assert result == expected

    def test_three_levels_complete(self, solution):
        """Test with three levels complete tree"""
        root = array_to_tree([1, 2, 3, 4, 5, 6, 7])
        # Level 0: left to right -> [1]
        # Level 1: right to left -> [3, 2]
        # Level 2: left to right -> [4, 5, 6, 7]
        expected = [[1], [3, 2], [4, 5, 6, 7]]
        result = solution.zigzagLevelOrder(root)
        assert result == expected

    def test_left_skewed(self, solution):
        """Test with left-skewed tree"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        expected = [[1], [2], [3]]
        result = solution.zigzagLevelOrder(root)
        assert result == expected

    def test_right_skewed(self, solution):
        """Test with right-skewed tree"""
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        expected = [[1], [2], [3]]
        result = solution.zigzagLevelOrder(root)
        assert result == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
