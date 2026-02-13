"""
Tests for LeetCode Problem #230: Kth Smallest Element in a BST
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


class TestKthSmallestElementInABst:
    """Test cases for Kth Smallest Element in a BST problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        root = array_to_tree([3,1,4,None,2])
        k = 1
        expected = 1
        result = solution.kthSmallest(root, k)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        root = array_to_tree([5,3,6,2,4,None,None,1])
        k = 3
        expected = 3
        result = solution.kthSmallest(root, k)
        assert result == expected


    def test_edge_case_single_node(self, solution):
        """Test with single node"""
        root = array_to_tree([1])
        k = 1
        expected = 1
        result = solution.kthSmallest(root, k)
        assert result == expected

    def test_k_equals_1(self, solution):
        """Test with k=1 (smallest element)"""
        root = array_to_tree([5, 3, 6, 2, 4, None, None, 1])
        k = 1
        expected = 1
        result = solution.kthSmallest(root, k)
        assert result == expected

    def test_k_equals_n(self, solution):
        """Test with k=n (largest element)"""
        root = array_to_tree([3, 1, 4, None, 2])
        k = 4  # n = 4 nodes
        expected = 4
        result = solution.kthSmallest(root, k)
        assert result == expected

    def test_left_skewed_tree(self, solution):
        """Test with left-skewed tree"""
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.left.left = TreeNode(1)
        # Inorder: 1, 3, 5
        assert solution.kthSmallest(root, 1) == 1
        assert solution.kthSmallest(root, 2) == 3
        assert solution.kthSmallest(root, 3) == 5

    def test_right_skewed_tree(self, solution):
        """Test with right-skewed tree"""
        root = TreeNode(1)
        root.right = TreeNode(3)
        root.right.right = TreeNode(5)
        # Inorder: 1, 3, 5
        assert solution.kthSmallest(root, 1) == 1
        assert solution.kthSmallest(root, 2) == 3
        assert solution.kthSmallest(root, 3) == 5

    def test_k_middle(self, solution):
        """Test with k in the middle"""
        root = array_to_tree([5, 3, 6, 2, 4, None, None, 1])
        # Inorder: 1, 2, 3, 4, 5, 6
        assert solution.kthSmallest(root, 3) == 3
        assert solution.kthSmallest(root, 4) == 4

    def test_negative_values(self, solution):
        """Test with negative values"""
        root = TreeNode(0)
        root.left = TreeNode(-2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(-3)
        root.left.right = TreeNode(-1)
        # Inorder: -3, -2, -1, 0, 2
        assert solution.kthSmallest(root, 1) == -3
        assert solution.kthSmallest(root, 3) == -1
        assert solution.kthSmallest(root, 5) == 2

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
