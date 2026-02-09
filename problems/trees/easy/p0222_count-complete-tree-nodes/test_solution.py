"""
Tests for LeetCode Problem #222: Count Complete Tree Nodes
"""

import pytest
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


class TestCountCompleteTreeNodes:
    """Test cases for Count Complete Tree Nodes problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        root = array_to_tree([1,2,3,4,5,6])
        expected = 6
        result = solution.countNodes(root)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        root = array_to_tree([])
        expected = 0
        result = solution.countNodes(root)
        assert result == expected


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        root = array_to_tree([1])
        expected = 1
        result = solution.countNodes(root)
        assert result == expected


    def test_two_nodes(self, solution):
        """Complete tree with 2 nodes"""
        root = array_to_tree([1, 2])
        assert solution.countNodes(root) == 2

    def test_three_nodes(self, solution):
        """Complete tree with 3 nodes (perfect)"""
        root = array_to_tree([1, 2, 3])
        assert solution.countNodes(root) == 3

    def test_four_nodes(self, solution):
        """Complete tree with 4 nodes"""
        root = array_to_tree([1, 2, 3, 4])
        assert solution.countNodes(root) == 4

    def test_five_nodes(self, solution):
        """Complete tree with 5 nodes"""
        root = array_to_tree([1, 2, 3, 4, 5])
        assert solution.countNodes(root) == 5

    def test_perfect_tree_7_nodes(self, solution):
        """Perfect binary tree with 7 nodes (2^3 - 1)"""
        root = array_to_tree([1, 2, 3, 4, 5, 6, 7])
        assert solution.countNodes(root) == 7

    def test_perfect_tree_15_nodes(self, solution):
        """Perfect binary tree with 15 nodes (2^4 - 1)"""
        root = array_to_tree(list(range(1, 16)))
        assert solution.countNodes(root) == 15

    def test_last_level_half_full(self, solution):
        """Complete tree with last level half full"""
        root = array_to_tree([1, 2, 3, 4, 5])
        assert solution.countNodes(root) == 5

    def test_last_level_one_node(self, solution):
        """Complete tree with just one node in last level"""
        root = array_to_tree([1, 2, 3, 4])
        assert solution.countNodes(root) == 4

    def test_negative_values(self, solution):
        """Complete tree with negative values (count should work same)"""
        root = array_to_tree([-1, -2, -3, -4, -5, -6])
        assert solution.countNodes(root) == 6

    def test_larger_complete_tree(self, solution):
        """Larger complete tree"""
        root = array_to_tree(list(range(1, 11)))  # 10 nodes
        assert solution.countNodes(root) == 10

    def test_almost_perfect_missing_one(self, solution):
        """Perfect tree with one node missing"""
        root = array_to_tree([1, 2, 3, 4, 5, 6])
        assert solution.countNodes(root) == 6

    def test_height_one(self, solution):
        """Tree with height 1 (just root)"""
        root = array_to_tree([1])
        assert solution.countNodes(root) == 1

    def test_height_two_complete(self, solution):
        """Complete tree with height 2"""
        root = array_to_tree([1, 2, 3])
        assert solution.countNodes(root) == 3

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
