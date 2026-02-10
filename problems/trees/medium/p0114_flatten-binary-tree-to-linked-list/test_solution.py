"""
Tests for LeetCode Problem #114: Flatten Binary Tree to Linked List
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


def flattened_tree_to_list(root):
    """Convert flattened tree (linked list via right pointers) to list"""
    result = []
    current = root
    while current:
        result.append(current.val)
        # After flattening, left should be None and right points to next
        assert current.left is None, "Left child should be None after flattening"
        current = current.right
    return result


class TestFlattenBinaryTreeToLinkedList:
    """Test cases for Flatten Binary Tree to Linked List problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        root = array_to_tree([1,2,5,3,4,None,6])
        # Expected flattened order (preorder): 1, 2, 3, 4, 5, 6
        expected = [1, 2, 3, 4, 5, 6]
        solution.flatten(root)
        result = flattened_tree_to_list(root)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        root = array_to_tree([])
        expected = []
        solution.flatten(root)
        result = flattened_tree_to_list(root)
        assert result == expected


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        root = array_to_tree([0])
        expected = [0]
        solution.flatten(root)
        result = flattened_tree_to_list(root)
        assert result == expected


    def test_edge_case_empty(self, solution):
        """Test with empty/minimal input"""
        root = None
        solution.flatten(root)
        assert root is None

    def test_single_node(self, solution):
        """Test with single node"""
        root = TreeNode(1)
        solution.flatten(root)
        result = flattened_tree_to_list(root)
        assert result == [1]

    def test_only_right_children(self, solution):
        """Test with tree already having only right children"""
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        expected = [1, 2, 3]
        solution.flatten(root)
        result = flattened_tree_to_list(root)
        assert result == expected

    def test_only_left_children(self, solution):
        """Test with tree having only left children"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        expected = [1, 2, 3]  # Preorder: 1, 2, 3
        solution.flatten(root)
        result = flattened_tree_to_list(root)
        assert result == expected

    def test_two_nodes_left(self, solution):
        """Test with two nodes, left child"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        expected = [1, 2]
        solution.flatten(root)
        result = flattened_tree_to_list(root)
        assert result == expected

    def test_two_nodes_right(self, solution):
        """Test with two nodes, right child"""
        root = TreeNode(1)
        root.right = TreeNode(2)
        expected = [1, 2]
        solution.flatten(root)
        result = flattened_tree_to_list(root)
        assert result == expected

    def test_complete_tree(self, solution):
        """Test with complete binary tree"""
        root = array_to_tree([1, 2, 3, 4, 5, 6, 7])
        # Preorder: 1, 2, 4, 5, 3, 6, 7
        expected = [1, 2, 4, 5, 3, 6, 7]
        solution.flatten(root)
        result = flattened_tree_to_list(root)
        assert result == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
