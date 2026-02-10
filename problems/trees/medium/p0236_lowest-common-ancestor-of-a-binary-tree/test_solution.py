"""
Tests for LeetCode Problem #236: Lowest Common Ancestor of a Binary Tree
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA
from solution import TreeNode


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


class TestLowestCommonAncestorOfABinaryTree:
    """Test cases for Lowest Common Ancestor of a Binary Tree problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        root = array_to_tree([3,5,1,6,2,0,8,None,None,7,4])
        p = find_node(root, 5)
        q = find_node(root, 1)
        result = solution.lowestCommonAncestor(root, p, q)
        assert result.val == 3


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        root = array_to_tree([3,5,1,6,2,0,8,None,None,7,4])
        p = find_node(root, 5)
        q = find_node(root, 4)
        result = solution.lowestCommonAncestor(root, p, q)
        assert result.val == 5


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        root = array_to_tree([1,2])
        p = find_node(root, 1)
        q = find_node(root, 2)
        result = solution.lowestCommonAncestor(root, p, q)
        assert result.val == 1


    def test_edge_case_deep_nodes(self, solution):
        """Test with nodes deep in the tree"""
        root = array_to_tree([3,5,1,6,2,0,8,None,None,7,4])
        p = find_node(root, 7)
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
