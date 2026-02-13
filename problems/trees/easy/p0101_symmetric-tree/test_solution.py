"""
Tests for LeetCode Problem #101: Symmetric Tree
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


class TestSymmetricTree:
    """Test cases for Symmetric Tree problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        root = array_to_tree([1,2,2,3,4,4,3])
        expected = True
        result = solution.isSymmetric(root)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        root = array_to_tree([1,2,2,None,3,None,3])
        expected = False
        result = solution.isSymmetric(root)
        assert result == expected


    def test_empty_tree(self, solution):
        """Empty tree is symmetric"""
        assert solution.isSymmetric(None) == True

    def test_single_node(self, solution):
        """Single node tree is symmetric"""
        root = TreeNode(1)
        assert solution.isSymmetric(root) == True

    def test_two_nodes_symmetric(self, solution):
        """Two-level symmetric tree"""
        root = TreeNode(1, TreeNode(2), TreeNode(2))
        assert solution.isSymmetric(root) == True

    def test_two_nodes_asymmetric(self, solution):
        """Two-level asymmetric tree (different values)"""
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        assert solution.isSymmetric(root) == False

    def test_left_only(self, solution):
        """Tree with only left child is not symmetric"""
        root = TreeNode(1, TreeNode(2))
        assert solution.isSymmetric(root) == False

    def test_right_only(self, solution):
        """Tree with only right child is not symmetric"""
        root = TreeNode(1, None, TreeNode(2))
        assert solution.isSymmetric(root) == False

    def test_deep_symmetric(self, solution):
        """Deep symmetric tree"""
        root = array_to_tree([1, 2, 2, 3, 4, 4, 3, 5, 6, 7, 8, 8, 7, 6, 5])
        assert solution.isSymmetric(root) == True

    def test_asymmetric_at_depth(self, solution):
        """Tree symmetric at top but asymmetric at depth"""
        root = array_to_tree([1, 2, 2, 3, 4, 4, 5])
        assert solution.isSymmetric(root) == False

    def test_negative_values_symmetric(self, solution):
        """Symmetric tree with negative values"""
        root = TreeNode(-1, TreeNode(-2), TreeNode(-2))
        assert solution.isSymmetric(root) == True

    def test_mixed_values_symmetric(self, solution):
        """Symmetric tree with mixed positive/negative values"""
        root = TreeNode(0, TreeNode(-5, TreeNode(10)), TreeNode(-5, None, TreeNode(10)))
        assert solution.isSymmetric(root) == True

    def test_same_values_asymmetric_structure(self, solution):
        """Tree with same values but asymmetric structure"""
        root = TreeNode(1, TreeNode(2, TreeNode(2)), TreeNode(2, TreeNode(2)))
        assert solution.isSymmetric(root) == False

    def test_wide_symmetric(self, solution):
        """Wide symmetric tree"""
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(4), TreeNode(5))
        root.right = TreeNode(2, TreeNode(5), TreeNode(4))
        assert solution.isSymmetric(root) == True

    def test_boundary_values(self, solution):
        """Symmetric tree with boundary values"""
        root = TreeNode(0, TreeNode(-100), TreeNode(-100))
        assert solution.isSymmetric(root) == True

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
