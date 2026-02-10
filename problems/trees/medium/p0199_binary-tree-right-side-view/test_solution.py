"""
Tests for LeetCode Problem #199: Binary Tree Right Side View
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


class TestBinaryTreeRightSideView:
    """Test cases for Binary Tree Right Side View problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        root = array_to_tree([1,2,3,None,5,None,4])
        expected = [1,3,4]
        result = solution.rightSideView(root)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        root = array_to_tree([1,2,3,4,None,None,None,5])
        expected = [1,3,4,5]
        result = solution.rightSideView(root)
        assert result == expected


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        root = array_to_tree([1,None,3])
        expected = [1,3]
        result = solution.rightSideView(root)
        assert result == expected


    def test_example_4(self, solution):
        """Example 4 from problem description"""
        root = array_to_tree([])
        expected = []
        result = solution.rightSideView(root)
        assert result == expected


    def test_edge_case_single_node(self, solution):
        """Test with single node"""
        root = array_to_tree([1])
        expected = [1]
        result = solution.rightSideView(root)
        assert result == expected

    def test_empty_tree(self, solution):
        """Test with empty tree"""
        assert solution.rightSideView(None) == []

    def test_left_skewed_tree(self, solution):
        """Test with left-skewed tree (only left children)"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        expected = [1, 2, 3, 4]  # Each level has only one node on the left
        result = solution.rightSideView(root)
        assert result == expected

    def test_right_skewed_tree(self, solution):
        """Test with right-skewed tree (only right children)"""
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        expected = [1, 2, 3]
        result = solution.rightSideView(root)
        assert result == expected

    def test_left_deeper_than_right(self, solution):
        """Test where left subtree is deeper than right"""
        root = array_to_tree([1, 2, 3, 4])
        # Level 0: 1, Level 1: 2, 3, Level 2: 4
        expected = [1, 3, 4]
        result = solution.rightSideView(root)
        assert result == expected

    def test_complete_tree(self, solution):
        """Test with complete binary tree"""
        root = array_to_tree([1, 2, 3, 4, 5, 6, 7])
        expected = [1, 3, 7]
        result = solution.rightSideView(root)
        assert result == expected

    def test_zigzag_tree(self, solution):
        """Test with zigzag pattern tree"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(3)
        root.left.right.left = TreeNode(4)
        expected = [1, 2, 3, 4]
        result = solution.rightSideView(root)
        assert result == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
