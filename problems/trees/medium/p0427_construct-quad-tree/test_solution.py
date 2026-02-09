"""
Tests for LeetCode Problem #427: Construct Quad Tree
"""

import pytest
from solution import Solution, PROBLEM_METADATA
from solution import Node
from collections import deque



class TestConstructQuadTree:
    """Test cases for Construct Quad Tree problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def serialize_quad_tree(self, root):
        """Serialize quad tree to list format [[isLeaf, val], ...]"""
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node is None:
                result.append(None)
            else:
                result.append([1 if node.isLeaf else 0, 1 if node.val else 0])
                if not node.isLeaf:
                    queue.append(node.topLeft)
                    queue.append(node.topRight)
                    queue.append(node.bottomLeft)
                    queue.append(node.bottomRight)

        # Remove trailing nulls
        while result and result[-1] is None:
            result.pop()

        return result


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        grid = [[0,1],[1,0]]
        expected = [[0,1],[1,0],[1,1],[1,1],[1,0]]
        result = solution.construct(grid)
        assert self.serialize_quad_tree(result) == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
        # Expected output without leaf node children (matching our serialization format)
        expected = [[0, 1], [1, 1], [0, 1], [1, 1], [1, 0], [1, 0], [1, 0], [1, 1], [1, 1]]
        result = solution.construct(grid)
        assert self.serialize_quad_tree(result) == expected


    def test_edge_case_single_cell_one(self, solution):
        """Test with single cell grid containing 1"""
        grid = [[1]]
        result = solution.construct(grid)
        assert result.isLeaf == True
        assert result.val == True


    def test_edge_case_single_cell_zero(self, solution):
        """Test with single cell grid containing 0"""
        grid = [[0]]
        result = solution.construct(grid)
        assert result.isLeaf == True
        assert result.val == False


    def test_uniform_grid(self, solution):
        """Test with uniform grid of all 1s"""
        grid = [[1,1],[1,1]]
        result = solution.construct(grid)
        assert result.isLeaf == True
        assert result.val == True


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
