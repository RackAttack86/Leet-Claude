"""
Tests for LeetCode Problem #104: Maximum Depth of Binary Tree
"""

import pytest
from solution import Solution, TreeNode, PROBLEM_METADATA


class TestMaximumDepthOfBinaryTree:
    """Test cases for Maximum Depth of Binary Tree problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1: [3,9,20,null,null,15,7] -> 3"""
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        assert solution.maxDepth(root) == 3

    def test_example_2(self, solution):
        """Example 2: [1,null,2] -> 2"""
        root = TreeNode(1)
        root.right = TreeNode(2)
        assert solution.maxDepth(root) == 2

    def test_empty_tree(self, solution):
        """Empty tree has depth 0"""
        assert solution.maxDepth(None) == 0

    def test_single_node(self, solution):
        """Single node has depth 1"""
        assert solution.maxDepth(TreeNode(1)) == 1

    # Edge case tests
    def test_left_skewed(self, solution):
        """Left-skewed tree (only left children)"""
        root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5)))))
        assert solution.maxDepth(root) == 5

    def test_right_skewed(self, solution):
        """Right-skewed tree (only right children)"""
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        assert solution.maxDepth(root) == 4

    def test_complete_binary_tree(self, solution):
        """Complete binary tree"""
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(4), TreeNode(5))
        root.right = TreeNode(3, TreeNode(6))
        assert solution.maxDepth(root) == 3

    def test_perfect_binary_tree(self, solution):
        """Perfect binary tree (all levels full)"""
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(4), TreeNode(5))
        root.right = TreeNode(3, TreeNode(6), TreeNode(7))
        assert solution.maxDepth(root) == 3

    def test_negative_values(self, solution):
        """Tree with negative values (depth should still work)"""
        root = TreeNode(-1, TreeNode(-2, TreeNode(-3)), TreeNode(-4))
        assert solution.maxDepth(root) == 3

    def test_unbalanced_left_heavy(self, solution):
        """Unbalanced tree - left subtree much deeper"""
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(3, TreeNode(4)))
        root.right = TreeNode(5)
        assert solution.maxDepth(root) == 4

    def test_unbalanced_right_heavy(self, solution):
        """Unbalanced tree - right subtree much deeper"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3, None, TreeNode(4, None, TreeNode(5)))
        assert solution.maxDepth(root) == 4

    def test_wide_shallow_tree(self, solution):
        """Wide but shallow tree"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        assert solution.maxDepth(root) == 3

    def test_zigzag_path(self, solution):
        """Tree with zigzag path (alternating left/right)"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(3)
        root.left.right.left = TreeNode(4)
        root.left.right.left.right = TreeNode(5)
        assert solution.maxDepth(root) == 5

    def test_boundary_value_nodes(self, solution):
        """Tree with boundary values (-100, 100)"""
        root = TreeNode(100, TreeNode(-100), None)
        assert solution.maxDepth(root) == 2

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
