"""
Tests for LeetCode Problem #110: Balanced Binary Tree
"""

import pytest
from solution import Solution, PROBLEM_METADATA, TreeNode


class TestBalancedBinaryTree:
    """Test cases for Balanced Binary Tree problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1: [3,9,20,null,null,15,7] is balanced"""
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20, TreeNode(15), TreeNode(7))
        assert solution.isBalanced(root) == True

    def test_example_2(self, solution):
        """Example 2: [1,2,2,3,3,null,null,4,4] is not balanced"""
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3))
        root.right = TreeNode(2)
        assert solution.isBalanced(root) == False

    def test_empty_tree(self, solution):
        """Empty tree is balanced"""
        assert solution.isBalanced(None) == True

    def test_single_node(self, solution):
        """Single node tree is balanced"""
        root = TreeNode(1)
        assert solution.isBalanced(root) == True

    def test_perfectly_balanced(self, solution):
        """Perfectly balanced tree"""
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        assert solution.isBalanced(root) == True

    def test_left_heavy(self, solution):
        """Left-heavy unbalanced tree"""
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        assert solution.isBalanced(root) == False

    # Additional edge case tests
    def test_right_heavy_unbalanced(self, solution):
        """Right-heavy unbalanced tree"""
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        assert solution.isBalanced(root) == False

    def test_left_skewed_deep(self, solution):
        """Deep left-skewed tree (very unbalanced)"""
        root = TreeNode(1)
        curr = root
        for i in range(2, 6):
            curr.left = TreeNode(i)
            curr = curr.left
        assert solution.isBalanced(root) == False

    def test_right_skewed_deep(self, solution):
        """Deep right-skewed tree (very unbalanced)"""
        root = TreeNode(1)
        curr = root
        for i in range(2, 6):
            curr.right = TreeNode(i)
            curr = curr.right
        assert solution.isBalanced(root) == False

    def test_complete_binary_tree(self, solution):
        """Complete binary tree is balanced"""
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(4), TreeNode(5))
        root.right = TreeNode(3, TreeNode(6))
        assert solution.isBalanced(root) == True

    def test_perfect_binary_tree(self, solution):
        """Perfect binary tree is balanced"""
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(4), TreeNode(5))
        root.right = TreeNode(3, TreeNode(6), TreeNode(7))
        assert solution.isBalanced(root) == True

    def test_unbalanced_deep_in_subtree(self, solution):
        """Tree balanced at root but unbalanced in subtree"""
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(3, TreeNode(4)))
        root.right = TreeNode(5, TreeNode(6))
        assert solution.isBalanced(root) == False

    def test_negative_values(self, solution):
        """Balanced tree with negative values"""
        root = TreeNode(-1, TreeNode(-2), TreeNode(-3))
        assert solution.isBalanced(root) == True

    def test_one_level_difference(self, solution):
        """Tree with exactly 1 level difference (still balanced)"""
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(4))
        root.right = TreeNode(3)
        assert solution.isBalanced(root) == True

    def test_two_level_difference(self, solution):
        """Tree with exactly 2 level difference (unbalanced)"""
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(4, TreeNode(5)))
        root.right = TreeNode(3)
        assert solution.isBalanced(root) == False

    def test_zigzag_balanced(self, solution):
        """Zigzag path but still balanced"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(3)
        root.right = TreeNode(4)
        root.right.left = TreeNode(5)
        assert solution.isBalanced(root) == True

    def test_wide_tree(self, solution):
        """Wide but shallow tree (balanced)"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        assert solution.isBalanced(root) == True

    def test_boundary_values(self, solution):
        """Tree with boundary values"""
        root = TreeNode(10000, TreeNode(-10000))
        assert solution.isBalanced(root) == True

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
