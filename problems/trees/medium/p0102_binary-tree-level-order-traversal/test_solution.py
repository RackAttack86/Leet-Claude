"""
Tests for LeetCode Problem #102: Binary Tree Level Order Traversal
"""

import pytest
try:
    from user_solution import Solution
except ImportError:
    from solution import Solution, TreeNode, PROBLEM_METADATA


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


class TestBinaryTreeLevelOrderTraversal:
    """Test cases for Binary Tree Level Order Traversal problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1: [3,9,20,null,null,15,7]"""
        root = array_to_tree([3, 9, 20, None, None, 15, 7])
        expected = [[3], [9, 20], [15, 7]]
        assert solution.levelOrder(root) == expected

    def test_example_2(self, solution):
        """Example 2: Single node [1]"""
        root = array_to_tree([1])
        expected = [[1]]
        assert solution.levelOrder(root) == expected

    def test_example_3(self, solution):
        """Example 3: Empty tree"""
        root = None
        expected = []
        assert solution.levelOrder(root) == expected

    # Edge cases
    def test_empty_tree(self, solution):
        """Empty tree returns empty list"""
        assert solution.levelOrder(None) == []

    def test_single_node(self, solution):
        """Single node tree"""
        root = TreeNode(5)
        assert solution.levelOrder(root) == [[5]]

    def test_left_skewed_tree(self, solution):
        """Left-skewed tree (all left children)"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        expected = [[1], [2], [3], [4]]
        assert solution.levelOrder(root) == expected

    def test_right_skewed_tree(self, solution):
        """Right-skewed tree (all right children)"""
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        expected = [[1], [2], [3]]
        assert solution.levelOrder(root) == expected

    def test_complete_binary_tree(self, solution):
        """Complete binary tree"""
        root = array_to_tree([1, 2, 3, 4, 5, 6, 7])
        expected = [[1], [2, 3], [4, 5, 6, 7]]
        assert solution.levelOrder(root) == expected

    def test_negative_values(self, solution):
        """Tree with negative values"""
        root = array_to_tree([-10, 9, 20, None, None, -15, 7])
        expected = [[-10], [9, 20], [-15, 7]]
        assert solution.levelOrder(root) == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
