"""
Tests for LeetCode Problem #98: Validate Binary Search Tree
"""

import pytest
from collections import deque
try:
    from user_solution import Solution
except ImportError:
    from solution import Solution, TreeNode, PROBLEM_METADATA


def array_to_tree(arr):
    """Convert level-order array to binary tree"""
    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])  # Use deque for O(1) popleft
    i = 1

    while queue and i < len(arr):
        node = queue.popleft()  # O(1) instead of O(n) pop(0)
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1

    return root


class TestValidateBinarySearchTree:
    """Test cases for Validate Binary Search Tree problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1: Valid BST [2,1,3]"""
        root = array_to_tree([2, 1, 3])
        assert solution.isValidBST(root) == True

    def test_example_2(self, solution):
        """Example 2: Invalid BST [5,1,4,null,null,3,6]"""
        root = array_to_tree([5, 1, 4, None, None, 3, 6])
        assert solution.isValidBST(root) == False

    # Edge cases
    def test_single_node(self, solution):
        """Single node tree is always a valid BST"""
        root = TreeNode(1)
        assert solution.isValidBST(root) == True

    def test_all_left_children(self, solution):
        """Tree with all left children forming valid BST"""
        root = TreeNode(3)
        root.left = TreeNode(2)
        root.left.left = TreeNode(1)
        assert solution.isValidBST(root) == True

    def test_all_right_children(self, solution):
        """Tree with all right children forming valid BST"""
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        assert solution.isValidBST(root) == True

    def test_int_min_value(self, solution):
        """Test with minimum integer value"""
        root = TreeNode(-2147483648)
        assert solution.isValidBST(root) == True

    def test_int_max_value(self, solution):
        """Test with maximum integer value"""
        root = TreeNode(2147483647)
        assert solution.isValidBST(root) == True

    def test_int_min_max_range(self, solution):
        """Test with INT_MIN and INT_MAX values in tree"""
        root = TreeNode(0)
        root.left = TreeNode(-2147483648)
        root.right = TreeNode(2147483647)
        assert solution.isValidBST(root) == True

    def test_equal_values_invalid(self, solution):
        """Tree with equal values is not a valid BST"""
        root = TreeNode(1)
        root.left = TreeNode(1)
        assert solution.isValidBST(root) == False

    def test_invalid_right_subtree_violation(self, solution):
        """Right subtree contains value less than root"""
        # Tree: 10 -> left: 5, right: 15 -> left: 6, right: 20
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(20)
        assert solution.isValidBST(root) == False

    def test_invalid_left_subtree_violation(self, solution):
        """Left subtree contains value greater than root"""
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.left.right = TreeNode(12)
        assert solution.isValidBST(root) == False

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
