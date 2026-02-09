"""
Tests for LeetCode Problem #297: Serialize and Deserialize Binary Tree
"""

import pytest
from solution import Solution, PROBLEM_METADATA, Codec, TreeNode


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


class TestSerializeAndDeserializeBinaryTree:
    """Test cases for Serialize and Deserialize Binary Tree problem"""

    @pytest.fixture
    def codec(self):
        """Create a Codec instance for each test"""
        return Codec()

    def test_example_1(self, codec):
        """Example 1 from problem description: root = [1,2,3,null,null,4,5]"""
        root = array_to_tree([1, 2, 3, None, None, 4, 5])
        serialized = codec.serialize(root)
        deserialized = codec.deserialize(serialized)
        assert tree_to_array(deserialized) == [1, 2, 3, None, None, 4, 5]

    def test_example_2(self, codec):
        """Example 2 from problem description: root = []"""
        root = array_to_tree([])
        serialized = codec.serialize(root)
        deserialized = codec.deserialize(serialized)
        assert tree_to_array(deserialized) == []

    def test_edge_case_single_node(self, codec):
        """Test with single node tree"""
        root = array_to_tree([1])
        serialized = codec.serialize(root)
        deserialized = codec.deserialize(serialized)
        assert tree_to_array(deserialized) == [1]

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
