"""
Tests for LeetCode Problem #235: Lowest Common Ancestor of a Binary Search Tree
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


def find_node(root, val):
    """Find a node with the given value in the tree"""
    if not root:
        return None
    if root.val == val:
        return root
    left = find_node(root.left, val)
    if left:
        return left
    return find_node(root.right, val)


class TestLowestCommonAncestorOfABinarySearchTree:
    """Test cases for Lowest Common Ancestor of a Binary Search Tree problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1: LCA of 2 and 8 is 6"""
        root = array_to_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = find_node(root, 2)
        q = find_node(root, 8)
        result = solution.lowestCommonAncestor(root, p, q)
        assert result.val == 6

    def test_example_2(self, solution):
        """Example 2: LCA of 2 and 4 is 2"""
        root = array_to_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = find_node(root, 2)
        q = find_node(root, 4)
        result = solution.lowestCommonAncestor(root, p, q)
        assert result.val == 2

    # Edge cases
    def test_same_node(self, solution):
        """Test where p and q are the same node"""
        root = array_to_tree([6, 2, 8, 0, 4, 7, 9])
        p = find_node(root, 4)
        q = find_node(root, 4)
        result = solution.lowestCommonAncestor(root, p, q)
        assert result.val == 4

    def test_root_is_lca(self, solution):
        """Test where root is the LCA"""
        root = array_to_tree([6, 2, 8, 0, 4, 7, 9])
        p = find_node(root, 0)  # Leftmost
        q = find_node(root, 9)  # Rightmost
        result = solution.lowestCommonAncestor(root, p, q)
        assert result.val == 6

    def test_two_nodes(self, solution):
        """Test with only two nodes"""
        root = TreeNode(2)
        root.left = TreeNode(1)
        p = root
        q = root.left
        result = solution.lowestCommonAncestor(root, p, q)
        assert result.val == 2

    def test_p_is_ancestor_of_q(self, solution):
        """Test where p is an ancestor of q"""
        root = array_to_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = find_node(root, 2)
        q = find_node(root, 5)
        result = solution.lowestCommonAncestor(root, p, q)
        assert result.val == 2

    def test_both_in_right_subtree(self, solution):
        """Test where both nodes are in the right subtree"""
        root = array_to_tree([6, 2, 8, 0, 4, 7, 9])
        p = find_node(root, 7)
        q = find_node(root, 9)
        result = solution.lowestCommonAncestor(root, p, q)
        assert result.val == 8

    def test_both_in_left_subtree(self, solution):
        """Test where both nodes are in the left subtree"""
        root = array_to_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = find_node(root, 3)
        q = find_node(root, 5)
        result = solution.lowestCommonAncestor(root, p, q)
        assert result.val == 4

    def test_leaf_nodes(self, solution):
        """Test with two leaf nodes"""
        root = array_to_tree([6, 2, 8, 0, 4, 7, 9])
        p = find_node(root, 0)
        q = find_node(root, 4)
        result = solution.lowestCommonAncestor(root, p, q)
        assert result.val == 2

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
