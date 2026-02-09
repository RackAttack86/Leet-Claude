"""
Tests for LeetCode Problem #226: Invert Binary Tree
"""

import pytest
from solution import Solution, TreeNode, PROBLEM_METADATA


def tree_to_list(root):
    """Convert tree to level-order list for comparison"""
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
    while result and result[-1] is None:
        result.pop()
    return result


class TestInvertBinaryTree:
    """Test cases for Invert Binary Tree problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1: [4,2,7,1,3,6,9] -> [4,7,2,9,6,3,1]"""
        root = TreeNode(4)
        root.left = TreeNode(2, TreeNode(1), TreeNode(3))
        root.right = TreeNode(7, TreeNode(6), TreeNode(9))
        result = solution.invertTree(root)
        assert tree_to_list(result) == [4, 7, 2, 9, 6, 3, 1]

    def test_example_2(self, solution):
        """Example 2: [2,1,3] -> [2,3,1]"""
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        result = solution.invertTree(root)
        assert tree_to_list(result) == [2, 3, 1]

    def test_empty_tree(self, solution):
        """Empty tree returns None"""
        assert solution.invertTree(None) is None

    def test_single_node(self, solution):
        """Single node stays the same"""
        root = TreeNode(1)
        result = solution.invertTree(root)
        assert result.val == 1
        assert result.left is None
        assert result.right is None

    # Edge case tests
    def test_left_skewed(self, solution):
        """Left-skewed tree becomes right-skewed"""
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        result = solution.invertTree(root)
        assert result.val == 1
        assert result.left is None
        assert result.right.val == 2
        assert result.right.left is None
        assert result.right.right.val == 3

    def test_right_skewed(self, solution):
        """Right-skewed tree becomes left-skewed"""
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        result = solution.invertTree(root)
        assert result.val == 1
        assert result.right is None
        assert result.left.val == 2
        assert result.left.right is None
        assert result.left.left.val == 3

    def test_complete_binary_tree(self, solution):
        """Complete binary tree inversion"""
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(4), TreeNode(5))
        root.right = TreeNode(3, TreeNode(6))
        result = solution.invertTree(root)
        assert tree_to_list(result) == [1, 3, 2, None, 6, 5, 4]

    def test_perfect_binary_tree(self, solution):
        """Perfect binary tree inversion"""
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
        result = solution.invertTree(root)
        assert tree_to_list(result) == [1, 3, 2, 7, 6, 5, 4]

    def test_negative_values(self, solution):
        """Tree with negative values"""
        root = TreeNode(-1, TreeNode(-2), TreeNode(-3))
        result = solution.invertTree(root)
        assert result.val == -1
        assert result.left.val == -3
        assert result.right.val == -2

    def test_mixed_values(self, solution):
        """Tree with mixed positive and negative values"""
        root = TreeNode(0, TreeNode(-5), TreeNode(5))
        result = solution.invertTree(root)
        assert result.val == 0
        assert result.left.val == 5
        assert result.right.val == -5

    def test_deep_tree(self, solution):
        """Deep tree inversion"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        root.left.left.left.left = TreeNode(5)
        result = solution.invertTree(root)
        # Deep left becomes deep right
        assert result.right.right.right.right.val == 5

    def test_invert_twice_is_original(self, solution):
        """Inverting twice returns to original structure"""
        root = TreeNode(4)
        root.left = TreeNode(2, TreeNode(1), TreeNode(3))
        root.right = TreeNode(7, TreeNode(6), TreeNode(9))
        original = tree_to_list(root)

        # Invert once
        result = solution.invertTree(root)
        # Invert again
        result = solution.invertTree(result)

        assert tree_to_list(result) == original

    def test_symmetric_tree(self, solution):
        """Symmetric tree stays symmetric after inversion"""
        root = TreeNode(1, TreeNode(2), TreeNode(2))
        result = solution.invertTree(root)
        assert result.left.val == result.right.val == 2

    def test_boundary_values(self, solution):
        """Tree with boundary values"""
        root = TreeNode(100, TreeNode(-100))
        result = solution.invertTree(root)
        assert result.left is None
        assert result.right.val == -100

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
