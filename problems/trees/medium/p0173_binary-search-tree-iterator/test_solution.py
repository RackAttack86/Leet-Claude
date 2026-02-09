"""
Tests for LeetCode Problem #173: Binary Search Tree Iterator
"""

import pytest
from solution import BSTIterator, PROBLEM_METADATA
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


class TestBinarySearchTreeIterator:
    """Test cases for Binary Search Tree Iterator problem"""

    def test_example_1(self):
        """Example 1 from problem description"""
        root = array_to_tree([7, 3, 15, None, None, 9, 20])
        iterator = BSTIterator(root)

        assert iterator.next() == 3
        assert iterator.next() == 7
        assert iterator.hasNext() == True
        assert iterator.next() == 9
        assert iterator.hasNext() == True
        assert iterator.next() == 15
        assert iterator.hasNext() == True
        assert iterator.next() == 20
        assert iterator.hasNext() == False


    def test_single_node(self):
        """Test with single node tree"""
        root = array_to_tree([5])
        iterator = BSTIterator(root)

        assert iterator.hasNext() == True
        assert iterator.next() == 5
        assert iterator.hasNext() == False


    def test_left_skewed_tree(self):
        """Test with left-skewed tree"""
        root = TreeNode(3)
        root.left = TreeNode(2)
        root.left.left = TreeNode(1)

        iterator = BSTIterator(root)

        assert iterator.next() == 1
        assert iterator.next() == 2
        assert iterator.next() == 3
        assert iterator.hasNext() == False


    def test_right_skewed_tree(self):
        """Test with right-skewed tree"""
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)

        iterator = BSTIterator(root)

        assert iterator.next() == 1
        assert iterator.next() == 2
        assert iterator.next() == 3
        assert iterator.hasNext() == False

    def test_empty_tree(self):
        """Test with empty tree"""
        iterator = BSTIterator(None)
        assert iterator.hasNext() == False

    def test_large_tree(self):
        """Test with larger tree"""
        root = array_to_tree([7, 3, 15, 1, 5, 9, 20])
        iterator = BSTIterator(root)

        # Inorder: 1, 3, 5, 7, 9, 15, 20
        assert iterator.hasNext() == True
        assert iterator.next() == 1
        assert iterator.next() == 3
        assert iterator.next() == 5
        assert iterator.next() == 7
        assert iterator.next() == 9
        assert iterator.next() == 15
        assert iterator.next() == 20
        assert iterator.hasNext() == False

    def test_interleaved_operations(self):
        """Test with interleaved hasNext and next calls"""
        root = array_to_tree([2, 1, 3])
        iterator = BSTIterator(root)

        # Inorder: 1, 2, 3
        assert iterator.hasNext() == True
        assert iterator.hasNext() == True  # Multiple hasNext calls should be idempotent
        assert iterator.next() == 1
        assert iterator.hasNext() == True
        assert iterator.next() == 2
        assert iterator.hasNext() == True
        assert iterator.next() == 3
        assert iterator.hasNext() == False
        assert iterator.hasNext() == False  # Multiple hasNext calls at end

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
