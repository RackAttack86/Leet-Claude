"""
Tests for LeetCode Problem #542: 01 Matrix
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class Test01Matrix:
    """Test cases for 01 Matrix problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        expected = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        assert solution.updateMatrix(mat) == expected

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
        expected = [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
        assert solution.updateMatrix(mat) == expected

    # Edge cases
    def test_all_zeros(self, solution):
        """Matrix with all zeros"""
        mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expected = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        assert solution.updateMatrix(mat) == expected

    def test_single_one(self, solution):
        """Matrix with single 1 in center"""
        mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        expected = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        assert solution.updateMatrix(mat) == expected

    def test_single_one_corner(self, solution):
        """Single 1 in corner"""
        mat = [[1, 0], [0, 0]]
        expected = [[1, 0], [0, 0]]
        assert solution.updateMatrix(mat) == expected

    def test_single_cell_zero(self, solution):
        """Single cell with 0"""
        mat = [[0]]
        expected = [[0]]
        assert solution.updateMatrix(mat) == expected

    def test_one_surrounded_by_ones(self, solution):
        """1 surrounded by 1s but with 0 at corner"""
        mat = [
            [0, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        expected = [
            [0, 1, 2],
            [1, 2, 3],
            [2, 3, 4]
        ]
        assert solution.updateMatrix(mat) == expected

    def test_single_row(self, solution):
        """Single row matrix"""
        mat = [[0, 1, 1, 0, 1]]
        expected = [[0, 1, 1, 0, 1]]
        assert solution.updateMatrix(mat) == expected

    def test_single_column(self, solution):
        """Single column matrix"""
        mat = [[0], [1], [1], [0], [1]]
        expected = [[0], [1], [1], [0], [1]]
        assert solution.updateMatrix(mat) == expected

    def test_checkerboard(self, solution):
        """Checkerboard pattern"""
        mat = [
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0]
        ]
        expected = [
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0]
        ]
        assert solution.updateMatrix(mat) == expected

    def test_ones_row_at_bottom(self, solution):
        """Row of 1s at bottom"""
        mat = [
            [0, 0, 0],
            [0, 0, 0],
            [1, 1, 1]
        ]
        expected = [
            [0, 0, 0],
            [0, 0, 0],
            [1, 1, 1]
        ]
        assert solution.updateMatrix(mat) == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
