"""
Tests for LeetCode Problem #117: Populating Next Right Pointers in Each Node II
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA
from solution import Node



class TestPopulatingNextRightPointersInEachNodeIi:
    """Test cases for Populating Next Right Pointers in Each Node II problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def build_tree(self, values):
        """Build a tree from a list of values (level order, None for missing nodes)"""
        if not values:
            return None

        root = Node(values[0])
        queue = [root]
        i = 1

        while queue and i < len(values):
            node = queue.pop(0)

            # Left child
            if i < len(values) and values[i] is not None:
                node.left = Node(values[i])
                queue.append(node.left)
            i += 1

            # Right child
            if i < len(values) and values[i] is not None:
                node.right = Node(values[i])
                queue.append(node.right)
            i += 1

        return root

    def serialize_with_next(self, root):
        """Serialize tree with next pointers, using '#' to mark end of each level"""
        if not root:
            return []

        result = []
        leftmost = root

        while leftmost:
            current = leftmost
            leftmost = None
            next_leftmost = None

            while current:
                result.append(current.val)

                # Track leftmost node of next level
                if not next_leftmost:
                    if current.left:
                        next_leftmost = current.left
                    elif current.right:
                        next_leftmost = current.right

                current = current.next

            result.append('#')
            leftmost = next_leftmost

        return result

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        root = self.build_tree([1,2,3,4,5,None,7])
        expected = [1,'#',2,3,'#',4,5,7,'#']
        solution.connect(root)
        assert self.serialize_with_next(root) == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        root = self.build_tree([])
        result = solution.connect(root)
        assert result is None


    def test_edge_case_empty(self, solution):
        """Test with empty/minimal input"""
        result = solution.connect(None)
        assert result is None

    def test_single_node(self, solution):
        """Test with single node"""
        root = Node(1)
        result = solution.connect(root)
        assert result.val == 1
        assert result.next is None

    def test_perfect_tree(self, solution):
        """Test with perfect binary tree"""
        root = self.build_tree([1, 2, 3, 4, 5, 6, 7])
        expected = [1, '#', 2, 3, '#', 4, 5, 6, 7, '#']
        solution.connect(root)
        assert self.serialize_with_next(root) == expected

    def test_incomplete_tree_left_heavy(self, solution):
        """Test with incomplete tree (left heavy)"""
        root = self.build_tree([1, 2, 3, 4, 5, None, None])
        expected = [1, '#', 2, 3, '#', 4, 5, '#']
        solution.connect(root)
        assert self.serialize_with_next(root) == expected

    def test_incomplete_tree_right_heavy(self, solution):
        """Test with incomplete tree (right heavy)"""
        root = self.build_tree([1, 2, 3, None, None, 6, 7])
        expected = [1, '#', 2, 3, '#', 6, 7, '#']
        solution.connect(root)
        assert self.serialize_with_next(root) == expected

    def test_sparse_tree(self, solution):
        """Test with sparse tree (gaps in middle)"""
        root = self.build_tree([1, 2, 3, 4, None, None, 7])
        expected = [1, '#', 2, 3, '#', 4, 7, '#']
        solution.connect(root)
        assert self.serialize_with_next(root) == expected

    def test_left_skewed(self, solution):
        """Test with left-skewed tree"""
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(3)
        expected = [1, '#', 2, '#', 3, '#']
        solution.connect(root)
        assert self.serialize_with_next(root) == expected

    def test_right_skewed(self, solution):
        """Test with right-skewed tree"""
        root = Node(1)
        root.right = Node(2)
        root.right.right = Node(3)
        expected = [1, '#', 2, '#', 3, '#']
        solution.connect(root)
        assert self.serialize_with_next(root) == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
