"""
Tests for LeetCode Problem #572: Subtree of Another Tree
"""

import pytest
from solution import Solution, PROBLEM_METADATA, TreeNode


class TestSubtreeOfAnotherTree:
    """Test cases for Subtree of Another Tree problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1: [4,1,2] is subtree of [3,4,5,1,2]"""
        root = TreeNode(3)
        root.left = TreeNode(4, TreeNode(1), TreeNode(2))
        root.right = TreeNode(5)

        subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
        assert solution.isSubtree(root, subRoot) == True

    def test_example_2(self, solution):
        """Example 2: [4,1,2] is NOT subtree of [3,4,5,1,2,null,null,null,null,0]"""
        root = TreeNode(3)
        root.left = TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0)))
        root.right = TreeNode(5)

        subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
        assert solution.isSubtree(root, subRoot) == False

    def test_single_node_match(self, solution):
        """Single node matches"""
        root = TreeNode(1)
        subRoot = TreeNode(1)
        assert solution.isSubtree(root, subRoot) == True

    def test_single_node_no_match(self, solution):
        """Single node doesn't match"""
        root = TreeNode(1)
        subRoot = TreeNode(2)
        assert solution.isSubtree(root, subRoot) == False

    def test_subtree_is_root(self, solution):
        """Subtree is the entire tree"""
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        subRoot = TreeNode(1, TreeNode(2), TreeNode(3))
        assert solution.isSubtree(root, subRoot) == True

    def test_empty_root(self, solution):
        """Empty root can't contain any subtree"""
        subRoot = TreeNode(1)
        assert solution.isSubtree(None, subRoot) == False

    # Additional edge case tests
    def test_left_skewed_subtree(self, solution):
        """Left-skewed tree contains left-skewed subtree"""
        root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
        subRoot = TreeNode(3, TreeNode(4))
        assert solution.isSubtree(root, subRoot) == True

    def test_right_skewed_subtree(self, solution):
        """Right-skewed tree contains right-skewed subtree"""
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
        subRoot = TreeNode(3, None, TreeNode(4))
        assert solution.isSubtree(root, subRoot) == True

    def test_subtree_at_different_depths(self, solution):
        """Subtree appears at multiple depths, but only matches at one"""
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(3), TreeNode(4))
        root.right = TreeNode(2, TreeNode(3))  # Missing TreeNode(4)
        subRoot = TreeNode(2, TreeNode(3), TreeNode(4))
        assert solution.isSubtree(root, subRoot) == True

    def test_subtree_leaf_only(self, solution):
        """Subtree is a single leaf node"""
        root = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4))
        subRoot = TreeNode(3)
        assert solution.isSubtree(root, subRoot) == True

    def test_subtree_with_extra_children(self, solution):
        """Root node has extra children compared to subRoot"""
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(3), TreeNode(4))
        root.right = TreeNode(5)
        subRoot = TreeNode(2, TreeNode(3))  # Missing TreeNode(4)
        assert solution.isSubtree(root, subRoot) == False

    def test_negative_values(self, solution):
        """Trees with negative values"""
        root = TreeNode(-1, TreeNode(-2), TreeNode(-3))
        subRoot = TreeNode(-2)
        assert solution.isSubtree(root, subRoot) == True

    def test_mixed_values(self, solution):
        """Trees with mixed positive and negative values"""
        root = TreeNode(0, TreeNode(-5, TreeNode(10)), TreeNode(5, None, TreeNode(-10)))
        subRoot = TreeNode(-5, TreeNode(10))
        assert solution.isSubtree(root, subRoot) == True

    def test_same_values_different_structure(self, solution):
        """Same values but different tree structure"""
        root = TreeNode(1, TreeNode(1, TreeNode(1)))
        subRoot = TreeNode(1, None, TreeNode(1))
        assert solution.isSubtree(root, subRoot) == False

    def test_complete_tree_subtree(self, solution):
        """Complete tree with complete subtree"""
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(4), TreeNode(5))
        root.right = TreeNode(3, TreeNode(6))
        subRoot = TreeNode(2, TreeNode(4), TreeNode(5))
        assert solution.isSubtree(root, subRoot) == True

    def test_perfect_tree_subtree(self, solution):
        """Perfect tree with perfect subtree"""
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(4), TreeNode(5))
        root.right = TreeNode(3, TreeNode(6), TreeNode(7))
        subRoot = TreeNode(3, TreeNode(6), TreeNode(7))
        assert solution.isSubtree(root, subRoot) == True

    def test_subtree_at_rightmost(self, solution):
        """Subtree is at the rightmost position"""
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        subRoot = TreeNode(3)
        assert solution.isSubtree(root, subRoot) == True

    def test_large_root_small_subtree(self, solution):
        """Large tree with small subtree"""
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(4), TreeNode(5))
        root.right = TreeNode(3, TreeNode(6), TreeNode(7))
        root.left.left.left = TreeNode(8)
        subRoot = TreeNode(4, TreeNode(8))
        assert solution.isSubtree(root, subRoot) == True

    def test_boundary_values(self, solution):
        """Trees with boundary values"""
        root = TreeNode(10000, TreeNode(-10000))
        subRoot = TreeNode(-10000)
        assert solution.isSubtree(root, subRoot) == True

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
