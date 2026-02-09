"""
Tests for LeetCode Problem #112: Path Sum
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


class TestPathSum:
    """Test cases for Path Sum problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        root = array_to_tree([5,4,8,11,None,13,4,7,2,None,None,None,1])
        targetSum = 22
        expected = True
        result = solution.hasPathSum(root, targetSum)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        root = array_to_tree([1,2,3])
        targetSum = 5
        expected = False
        result = solution.hasPathSum(root, targetSum)
        assert result == expected


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        root = array_to_tree([])
        targetSum = 0
        expected = False
        result = solution.hasPathSum(root, targetSum)
        assert result == expected


    def test_single_node_match(self, solution):
        """Single node with matching sum"""
        root = TreeNode(5)
        assert solution.hasPathSum(root, 5) == True

    def test_single_node_no_match(self, solution):
        """Single node with non-matching sum"""
        root = TreeNode(5)
        assert solution.hasPathSum(root, 10) == False

    def test_negative_target(self, solution):
        """Negative target sum"""
        root = TreeNode(-2, TreeNode(-3))
        assert solution.hasPathSum(root, -5) == True

    def test_negative_values_positive_sum(self, solution):
        """Negative values with positive target"""
        root = TreeNode(1, TreeNode(-2), TreeNode(3))
        assert solution.hasPathSum(root, -1) == True

    def test_left_skewed_tree(self, solution):
        """Left-skewed tree with path sum"""
        root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
        assert solution.hasPathSum(root, 10) == True  # 1+2+3+4 = 10

    def test_right_skewed_tree(self, solution):
        """Right-skewed tree with path sum"""
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        assert solution.hasPathSum(root, 6) == True  # 1+2+3 = 6

    def test_sum_at_internal_node(self, solution):
        """Sum reached at internal node (not leaf) - should be False"""
        root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))))
        # Path 5->4 = 9, but 4 is not a leaf
        assert solution.hasPathSum(root, 9) == False

    def test_multiple_valid_paths(self, solution):
        """Tree with multiple valid paths"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        assert solution.hasPathSum(root, 3) == True

    def test_perfect_binary_tree(self, solution):
        """Perfect binary tree"""
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
        assert solution.hasPathSum(root, 7) == True  # 1+2+4 = 7
        assert solution.hasPathSum(root, 8) == True  # 1+2+5 = 8
        assert solution.hasPathSum(root, 10) == True  # 1+3+6 = 10
        assert solution.hasPathSum(root, 15) == False

    def test_complete_binary_tree(self, solution):
        """Complete binary tree"""
        root = array_to_tree([1, 2, 3, 4, 5, 6])
        assert solution.hasPathSum(root, 7) == True  # 1+2+4 = 7

    def test_zero_sum(self, solution):
        """Target sum is zero"""
        root = TreeNode(0)
        assert solution.hasPathSum(root, 0) == True

    def test_zero_values_in_tree(self, solution):
        """Tree with zero values"""
        root = TreeNode(1, TreeNode(0), TreeNode(2))
        assert solution.hasPathSum(root, 1) == True
        assert solution.hasPathSum(root, 3) == True

    def test_large_values(self, solution):
        """Tree with large values"""
        root = TreeNode(1000, TreeNode(-1000))
        assert solution.hasPathSum(root, 0) == True

    def test_deep_path(self, solution):
        """Deep path with many nodes"""
        root = TreeNode(1)
        curr = root
        total = 1
        for i in range(2, 8):
            curr.left = TreeNode(i)
            curr = curr.left
            total += i
        assert solution.hasPathSum(root, total) == True

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
