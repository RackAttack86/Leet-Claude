"""
Tests for LeetCode Problem #543: Diameter of Binary Tree
"""

import pytest
from solution import Solution, PROBLEM_METADATA, TreeNode


class TestDiameterOfBinaryTree:
    """Test cases for Diameter of Binary Tree problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1: [1,2,3,4,5] has diameter 3"""
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(4), TreeNode(5))
        root.right = TreeNode(3)
        assert solution.diameterOfBinaryTree(root) == 3

    def test_example_2(self, solution):
        """Example 2: [1,2] has diameter 1"""
        root = TreeNode(1, TreeNode(2))
        assert solution.diameterOfBinaryTree(root) == 1

    def test_single_node(self, solution):
        """Single node has diameter 0"""
        root = TreeNode(1)
        assert solution.diameterOfBinaryTree(root) == 0

    def test_balanced_tree(self, solution):
        """Balanced tree"""
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        assert solution.diameterOfBinaryTree(root) == 2

    def test_left_heavy(self, solution):
        """Left-heavy tree"""
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(3, TreeNode(4)))
        assert solution.diameterOfBinaryTree(root) == 3

    def test_path_not_through_root(self, solution):
        """Diameter path doesn't go through root"""
        # Tree: 1 - 2 - 4 - 6
        #           |   ` 7
        #           ` 5
        # Longest path: 6->4->2->5 or 7->4->2->5 = 3 edges
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(4, TreeNode(6), TreeNode(7)), TreeNode(5))
        assert solution.diameterOfBinaryTree(root) == 3

    # Additional edge case tests
    def test_left_skewed(self, solution):
        """Left-skewed tree"""
        root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5)))))
        assert solution.diameterOfBinaryTree(root) == 4

    def test_right_skewed(self, solution):
        """Right-skewed tree"""
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        assert solution.diameterOfBinaryTree(root) == 3

    def test_complete_binary_tree(self, solution):
        """Complete binary tree"""
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(4), TreeNode(5))
        root.right = TreeNode(3, TreeNode(6))
        assert solution.diameterOfBinaryTree(root) == 4

    def test_perfect_binary_tree(self, solution):
        """Perfect binary tree"""
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
        assert solution.diameterOfBinaryTree(root) == 4

    def test_negative_values(self, solution):
        """Tree with negative values (values don't affect diameter)"""
        root = TreeNode(-1, TreeNode(-2), TreeNode(-3))
        assert solution.diameterOfBinaryTree(root) == 2

    def test_diameter_in_subtree(self, solution):
        """Diameter entirely within a subtree, not touching root"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3, TreeNode(5), TreeNode(6))
        root.left.right = TreeNode(4, TreeNode(7), TreeNode(8))
        # Longest path: 5->3->2->4->7 or similar = 4
        assert solution.diameterOfBinaryTree(root) == 4

    def test_symmetric_tree(self, solution):
        """Symmetric tree"""
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(2, TreeNode(5), TreeNode(4)))
        assert solution.diameterOfBinaryTree(root) == 4

    def test_only_left_child_chain(self, solution):
        """Root with only left children forming a chain"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        assert solution.diameterOfBinaryTree(root) == 2

    def test_only_right_child_chain(self, solution):
        """Root with only right children forming a chain"""
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        assert solution.diameterOfBinaryTree(root) == 2

    def test_v_shaped_tree(self, solution):
        """V-shaped tree (left chain + right chain)"""
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(3))
        root.right = TreeNode(4, None, TreeNode(5))
        assert solution.diameterOfBinaryTree(root) == 4

    def test_two_nodes(self, solution):
        """Tree with just two nodes"""
        root = TreeNode(1, TreeNode(2))
        assert solution.diameterOfBinaryTree(root) == 1

    def test_boundary_values(self, solution):
        """Tree with boundary values"""
        root = TreeNode(100, TreeNode(-100))
        assert solution.diameterOfBinaryTree(root) == 1

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
