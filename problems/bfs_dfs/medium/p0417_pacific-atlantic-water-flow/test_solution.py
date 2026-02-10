"""
Tests for LeetCode Problem #417: Pacific Atlantic Water Flow
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestPacificAtlanticWaterFlow:
    """Test cases for Pacific Atlantic Water Flow problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        heights = [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4]
        ]
        result = solution.pacificAtlantic(heights)
        expected = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        # Sort for comparison since order doesn't matter
        assert sorted(result) == sorted(expected)

    def test_example_2(self, solution):
        """Example 2 from problem description - single cell"""
        heights = [[1]]
        result = solution.pacificAtlantic(heights)
        assert result == [[0, 0]]

    # Edge cases
    def test_single_cell(self, solution):
        """Single cell touches both oceans"""
        heights = [[5]]
        result = solution.pacificAtlantic(heights)
        assert result == [[0, 0]]

    def test_flat_terrain(self, solution):
        """Flat terrain - all same heights"""
        heights = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        result = solution.pacificAtlantic(heights)
        # All cells should reach both oceans
        expected = [[i, j] for i in range(3) for j in range(3)]
        assert sorted(result) == sorted(expected)

    def test_single_row(self, solution):
        """Single row - all cells touch both oceans"""
        heights = [[1, 2, 3, 4, 5]]
        result = solution.pacificAtlantic(heights)
        expected = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]]
        assert sorted(result) == sorted(expected)

    def test_single_column(self, solution):
        """Single column - all cells touch both oceans"""
        heights = [[1], [2], [3], [4], [5]]
        result = solution.pacificAtlantic(heights)
        expected = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]
        assert sorted(result) == sorted(expected)

    def test_descending_to_atlantic(self, solution):
        """Heights descend toward Atlantic (bottom-right)"""
        heights = [
            [5, 4, 3],
            [4, 3, 2],
            [3, 2, 1]
        ]
        result = solution.pacificAtlantic(heights)
        # Top-left corner can flow to both
        assert [0, 0] in result

    def test_ascending_to_atlantic(self, solution):
        """Heights ascend toward Atlantic"""
        heights = [
            [1, 2, 3],
            [2, 3, 4],
            [3, 4, 5]
        ]
        result = solution.pacificAtlantic(heights)
        # Bottom-right corner can flow to both
        assert [2, 2] in result

    def test_two_by_two(self, solution):
        """2x2 grid"""
        heights = [
            [1, 2],
            [4, 3]
        ]
        result = solution.pacificAtlantic(heights)
        # [0,0] with height 1 cannot flow to Atlantic (blocked by higher cells)
        expected = [[0, 1], [1, 0], [1, 1]]
        assert sorted(result) == sorted(expected)

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
