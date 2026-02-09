"""
Tests for LeetCode Problem #105: Construct Binary Tree from Preorder and Inorder Traversal
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


class TestConstructBinaryTreeFromPreorderAndInorderTraversal:
    """Test cases for Construct Binary Tree from Preorder and Inorder Traversal problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        expected = [3,9,20,None,None,15,7]
        result = solution.buildTree(preorder, inorder)
        assert tree_to_array(result) == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        preorder = [-1]
        inorder = [-1]
        expected = [-1]
        result = solution.buildTree(preorder, inorder)
        assert tree_to_array(result) == expected


    def test_single_node(self, solution):
        """Test with single node"""
        preorder = [5]
        inorder = [5]
        expected = [5]
        result = solution.buildTree(preorder, inorder)
        assert tree_to_array(result) == expected

    def test_all_left_children(self, solution):
        """Test with tree having all left children"""
        # Tree: 3 -> 2 -> 1 (all left)
        preorder = [3, 2, 1]
        inorder = [1, 2, 3]
        result = solution.buildTree(preorder, inorder)
        arr = tree_to_array(result)
        assert arr == [3, 2, None, 1]

    def test_all_right_children(self, solution):
        """Test with tree having all right children"""
        # Tree: 1 -> 2 -> 3 (all right)
        preorder = [1, 2, 3]
        inorder = [1, 2, 3]
        result = solution.buildTree(preorder, inorder)
        arr = tree_to_array(result)
        assert arr == [1, None, 2, None, 3]

    def test_two_nodes_left(self, solution):
        """Test with two nodes, left child"""
        preorder = [2, 1]
        inorder = [1, 2]
        result = solution.buildTree(preorder, inorder)
        arr = tree_to_array(result)
        assert arr == [2, 1]

    def test_two_nodes_right(self, solution):
        """Test with two nodes, right child"""
        preorder = [1, 2]
        inorder = [1, 2]
        result = solution.buildTree(preorder, inorder)
        arr = tree_to_array(result)
        assert arr == [1, None, 2]

    def test_complete_tree(self, solution):
        """Test with complete binary tree"""
        preorder = [1, 2, 4, 5, 3, 6, 7]
        inorder = [4, 2, 5, 1, 6, 3, 7]
        result = solution.buildTree(preorder, inorder)
        arr = tree_to_array(result)
        assert arr == [1, 2, 3, 4, 5, 6, 7]

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
