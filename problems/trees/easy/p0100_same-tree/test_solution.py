"""
Tests for LeetCode Problem #100: Same Tree
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA, TreeNode


class TestSameTree:
    """Test cases for Same Tree problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1: Both trees [1,2,3] are the same"""
        p = TreeNode(1, TreeNode(2), TreeNode(3))
        q = TreeNode(1, TreeNode(2), TreeNode(3))
        assert solution.isSameTree(p, q) == True

    def test_example_2(self, solution):
        """Example 2: [1,2] vs [1,null,2] - different structure"""
        p = TreeNode(1, TreeNode(2))
        q = TreeNode(1, None, TreeNode(2))
        assert solution.isSameTree(p, q) == False

    def test_example_3(self, solution):
        """Example 3: [1,2,1] vs [1,1,2] - different values"""
        p = TreeNode(1, TreeNode(2), TreeNode(1))
        q = TreeNode(1, TreeNode(1), TreeNode(2))
        assert solution.isSameTree(p, q) == False

    def test_both_empty(self, solution):
        """Both trees are empty"""
        assert solution.isSameTree(None, None) == True

    def test_one_empty(self, solution):
        """One tree is empty, other is not"""
        p = TreeNode(1)
        assert solution.isSameTree(p, None) == False
        assert solution.isSameTree(None, p) == False

    def test_single_node_same(self, solution):
        """Single node trees with same value"""
        p = TreeNode(5)
        q = TreeNode(5)
        assert solution.isSameTree(p, q) == True

    def test_single_node_different(self, solution):
        """Single node trees with different values"""
        p = TreeNode(5)
        q = TreeNode(10)
        assert solution.isSameTree(p, q) == False

    # Edge case tests
    def test_left_skewed_same(self, solution):
        """Left-skewed trees (only left children) - same"""
        p = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
        q = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
        assert solution.isSameTree(p, q) == True

    def test_right_skewed_same(self, solution):
        """Right-skewed trees (only right children) - same"""
        p = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
        q = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
        assert solution.isSameTree(p, q) == True

    def test_left_skewed_vs_right_skewed(self, solution):
        """Left-skewed vs right-skewed trees - different structure"""
        p = TreeNode(1, TreeNode(2, TreeNode(3)))
        q = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        assert solution.isSameTree(p, q) == False

    def test_complete_binary_tree_same(self, solution):
        """Complete binary tree - same"""
        p = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
        q = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
        assert solution.isSameTree(p, q) == True

    def test_perfect_binary_tree_same(self, solution):
        """Perfect binary tree - same"""
        p = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
        q = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
        assert solution.isSameTree(p, q) == True

    def test_negative_values(self, solution):
        """Trees with negative values"""
        p = TreeNode(-1, TreeNode(-2), TreeNode(-3))
        q = TreeNode(-1, TreeNode(-2), TreeNode(-3))
        assert solution.isSameTree(p, q) == True

    def test_mixed_positive_negative(self, solution):
        """Trees with mixed positive and negative values"""
        p = TreeNode(0, TreeNode(-5), TreeNode(5))
        q = TreeNode(0, TreeNode(-5), TreeNode(5))
        assert solution.isSameTree(p, q) == True

    def test_deep_tree_difference_at_bottom(self, solution):
        """Deep trees that differ only at the bottom"""
        p = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5)))))
        q = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(6)))))
        assert solution.isSameTree(p, q) == False

    def test_wide_tree_same(self, solution):
        """Wide tree (many nodes per level) - same"""
        p = TreeNode(1, TreeNode(2), TreeNode(3))
        p.left.left = TreeNode(4)
        p.left.right = TreeNode(5)
        p.right.left = TreeNode(6)
        p.right.right = TreeNode(7)

        q = TreeNode(1, TreeNode(2), TreeNode(3))
        q.left.left = TreeNode(4)
        q.left.right = TreeNode(5)
        q.right.left = TreeNode(6)
        q.right.right = TreeNode(7)

        assert solution.isSameTree(p, q) == True

    def test_different_subtree_structure(self, solution):
        """Trees with same values but different subtree structure"""
        p = TreeNode(1, TreeNode(2, TreeNode(3)), None)
        q = TreeNode(1, TreeNode(2, None, TreeNode(3)), None)
        assert solution.isSameTree(p, q) == False

    def test_boundary_values(self, solution):
        """Trees with boundary values (-10^4 and 10^4)"""
        p = TreeNode(10000, TreeNode(-10000))
        q = TreeNode(10000, TreeNode(-10000))
        assert solution.isSameTree(p, q) == True

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
