"""
Tests for LeetCode Problem #106: Construct Binary Tree from Inorder and Postorder Traversal
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


class TestConstructBinaryTreeFromInorderAndPostorderTraversal:
    """Test cases for Construct Binary Tree from Inorder and Postorder Traversal problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        inorder = [9,3,15,20,7]
        postorder = [9,15,7,20,3]
        expected = [3,9,20,None,None,15,7]
        result = solution.buildTree(inorder, postorder)
        assert tree_to_array(result) == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        inorder = [-1]
        postorder = [-1]
        expected = [-1]
        result = solution.buildTree(inorder, postorder)
        assert tree_to_array(result) == expected


    def test_single_node(self, solution):
        """Test with single node"""
        inorder = [5]
        postorder = [5]
        expected = [5]
        result = solution.buildTree(inorder, postorder)
        assert tree_to_array(result) == expected

    def test_all_right_children(self, solution):
        """Test with tree having all right children"""
        # Tree: 1 -> 2 -> 3 (all right)
        inorder = [1, 2, 3]
        postorder = [3, 2, 1]
        result = solution.buildTree(inorder, postorder)
        arr = tree_to_array(result)
        assert arr == [1, None, 2, None, 3]

    def test_all_left_children(self, solution):
        """Test with tree having all left children"""
        # Tree: 3 -> 2 -> 1 (all left)
        inorder = [1, 2, 3]
        postorder = [1, 2, 3]
        result = solution.buildTree(inorder, postorder)
        arr = tree_to_array(result)
        assert arr == [3, 2, None, 1]

    def test_two_nodes_left(self, solution):
        """Test with two nodes, left child"""
        inorder = [1, 2]
        postorder = [1, 2]
        result = solution.buildTree(inorder, postorder)
        arr = tree_to_array(result)
        assert arr == [2, 1]

    def test_two_nodes_right(self, solution):
        """Test with two nodes, right child"""
        inorder = [1, 2]
        postorder = [2, 1]
        result = solution.buildTree(inorder, postorder)
        arr = tree_to_array(result)
        assert arr == [1, None, 2]

    def test_complete_tree(self, solution):
        """Test with complete binary tree"""
        inorder = [4, 2, 5, 1, 6, 3, 7]
        postorder = [4, 5, 2, 6, 7, 3, 1]
        result = solution.buildTree(inorder, postorder)
        arr = tree_to_array(result)
        assert arr == [1, 2, 3, 4, 5, 6, 7]

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
