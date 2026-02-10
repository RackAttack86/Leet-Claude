"""
Tests for LeetCode Problem #530: Minimum Absolute Difference in BST
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


class TestMinimumAbsoluteDifferenceInBst:
    """Test cases for Minimum Absolute Difference in BST problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        root = array_to_tree([4,2,6,1,3])
        expected = 1
        result = solution.getMinimumDifference(root)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        root = array_to_tree([1,0,48,None,None,12,49])
        expected = 1
        result = solution.getMinimumDifference(root)
        assert result == expected


    def test_two_nodes(self, solution):
        """BST with only two nodes"""
        root = TreeNode(1, None, TreeNode(3))
        assert solution.getMinimumDifference(root) == 2

    def test_two_nodes_adjacent(self, solution):
        """BST with two adjacent values"""
        root = TreeNode(1, None, TreeNode(2))
        assert solution.getMinimumDifference(root) == 1

    def test_left_skewed_bst(self, solution):
        """Left-skewed BST"""
        root = TreeNode(4, TreeNode(2, TreeNode(1)))
        assert solution.getMinimumDifference(root) == 1

    def test_right_skewed_bst(self, solution):
        """Right-skewed BST"""
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(4)))
        assert solution.getMinimumDifference(root) == 1

    def test_balanced_bst(self, solution):
        """Balanced BST"""
        root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7)))
        assert solution.getMinimumDifference(root) == 1

    def test_large_differences(self, solution):
        """BST with large differences between nodes"""
        root = TreeNode(100, TreeNode(50), TreeNode(200))
        assert solution.getMinimumDifference(root) == 50

    def test_minimum_at_leaves(self, solution):
        """Minimum difference is between leaf and parent"""
        root = array_to_tree([8, 4, 12, 2, 6])
        assert solution.getMinimumDifference(root) == 2

    def test_minimum_at_different_levels(self, solution):
        """Minimum difference between nodes at different levels"""
        root = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15))
        assert solution.getMinimumDifference(root) == 2

    def test_consecutive_values(self, solution):
        """BST with consecutive values"""
        root = array_to_tree([3, 2, 4, 1])
        assert solution.getMinimumDifference(root) == 1

    def test_perfect_bst(self, solution):
        """Perfect BST"""
        root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7)))
        assert solution.getMinimumDifference(root) == 1

    def test_large_bst(self, solution):
        """Larger BST"""
        # Create a BST with values 1, 2, 4, 8, 16, 32
        root = TreeNode(8, TreeNode(2, TreeNode(1), TreeNode(4)), TreeNode(16, None, TreeNode(32)))
        assert solution.getMinimumDifference(root) == 1

    def test_minimum_not_adjacent_in_tree(self, solution):
        """Minimum is between nodes not adjacent in tree structure"""
        root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(7))
        # In sorted order: 2, 3, 4, 5, 7 - min diff is 1 (between 2-3, 3-4, or 4-5)
        assert solution.getMinimumDifference(root) == 1

    def test_zero_values(self, solution):
        """BST containing zero"""
        root = TreeNode(0, None, TreeNode(1))
        assert solution.getMinimumDifference(root) == 1

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
