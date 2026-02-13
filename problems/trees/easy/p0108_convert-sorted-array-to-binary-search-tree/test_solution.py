"""
Tests for LeetCode Problem #108: Convert Sorted Array to Binary Search Tree
"""

import pytest
from collections import deque
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


def tree_to_array(root):
    """Convert binary tree to level-order array"""
    if not root:
        return []

    result = []
    queue = deque([root])  # Use deque for O(1) popleft

    while queue:
        node = queue.popleft()  # O(1) instead of O(n) pop(0)
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


class TestConvertSortedArrayToBinarySearchTree:
    """Test cases for Convert Sorted Array to Binary Search Tree problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums = [-10,-3,0,5,9]
        # Multiple valid BST structures are acceptable
        result = solution.sortedArrayToBST(nums)
        result_array = tree_to_array(result)
        # Verify it's a valid height-balanced BST with the correct elements
        assert sorted([x for x in result_array if x is not None]) == sorted(nums)


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        nums = [1,3]
        # Multiple valid BST structures are acceptable
        result = solution.sortedArrayToBST(nums)
        result_array = tree_to_array(result)
        # Verify it's a valid height-balanced BST with the correct elements
        assert sorted([x for x in result_array if x is not None]) == sorted(nums)


    def test_single_element(self, solution):
        """Single element array"""
        nums = [0]
        result = solution.sortedArrayToBST(nums)
        assert result is not None
        assert result.val == 0
        assert result.left is None
        assert result.right is None

    def test_two_elements(self, solution):
        """Two element array"""
        nums = [1, 3]
        result = solution.sortedArrayToBST(nums)
        result_array = tree_to_array(result)
        assert sorted([x for x in result_array if x is not None]) == sorted(nums)

    def test_three_elements(self, solution):
        """Three element array - should create balanced tree"""
        nums = [1, 2, 3]
        result = solution.sortedArrayToBST(nums)
        result_array = tree_to_array(result)
        assert sorted([x for x in result_array if x is not None]) == sorted(nums)
        # Root should be middle element
        assert result.val == 2

    def test_negative_values(self, solution):
        """Array with negative values"""
        nums = [-10, -5, 0, 5, 10]
        result = solution.sortedArrayToBST(nums)
        result_array = tree_to_array(result)
        assert sorted([x for x in result_array if x is not None]) == sorted(nums)

    def test_all_negative(self, solution):
        """Array with all negative values"""
        nums = [-100, -50, -25, -10, -1]
        result = solution.sortedArrayToBST(nums)
        result_array = tree_to_array(result)
        assert sorted([x for x in result_array if x is not None]) == sorted(nums)

    def test_large_array(self, solution):
        """Larger array to test balance"""
        nums = list(range(1, 16))  # 15 elements
        result = solution.sortedArrayToBST(nums)
        result_array = tree_to_array(result)
        assert sorted([x for x in result_array if x is not None]) == sorted(nums)

    def test_power_of_two_minus_one(self, solution):
        """Array with 2^n - 1 elements (perfect binary tree)"""
        nums = list(range(1, 8))  # 7 elements
        result = solution.sortedArrayToBST(nums)
        result_array = tree_to_array(result)
        assert sorted([x for x in result_array if x is not None]) == sorted(nums)

    def test_height_balanced(self, solution):
        """Verify result is height-balanced"""
        nums = [-10, -3, 0, 5, 9]
        result = solution.sortedArrayToBST(nums)

        def get_height(node):
            if not node:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))

        def is_balanced(node):
            if not node:
                return True
            left_h = get_height(node.left)
            right_h = get_height(node.right)
            if abs(left_h - right_h) > 1:
                return False
            return is_balanced(node.left) and is_balanced(node.right)

        assert is_balanced(result) == True

    def test_bst_property(self, solution):
        """Verify result maintains BST property"""
        nums = [-10, -3, 0, 5, 9]
        result = solution.sortedArrayToBST(nums)

        def is_valid_bst(node, min_val=float('-inf'), max_val=float('inf')):
            if not node:
                return True
            if node.val <= min_val or node.val >= max_val:
                return False
            return (is_valid_bst(node.left, min_val, node.val) and
                    is_valid_bst(node.right, node.val, max_val))

        assert is_valid_bst(result) == True

    def test_boundary_values(self, solution):
        """Array with boundary values"""
        nums = [-10000, 0, 10000]
        result = solution.sortedArrayToBST(nums)
        result_array = tree_to_array(result)
        assert sorted([x for x in result_array if x is not None]) == sorted(nums)

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
