"""
Tests for LeetCode Problem #200: Number of Islands
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestNumberOfIslands:
    """Test cases for Number of Islands problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        assert solution.numIslands(grid) == 1

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        assert solution.numIslands(grid) == 3

    # Edge cases
    def test_all_water(self, solution):
        """Grid with all water - no islands"""
        grid = [
            ["0", "0", "0"],
            ["0", "0", "0"],
            ["0", "0", "0"]
        ]
        assert solution.numIslands(grid) == 0

    def test_all_land(self, solution):
        """Grid with all land - one island"""
        grid = [
            ["1", "1", "1"],
            ["1", "1", "1"],
            ["1", "1", "1"]
        ]
        assert solution.numIslands(grid) == 1

    def test_single_cell_land(self, solution):
        """Single cell grid with land"""
        grid = [["1"]]
        assert solution.numIslands(grid) == 1

    def test_single_cell_water(self, solution):
        """Single cell grid with water"""
        grid = [["0"]]
        assert solution.numIslands(grid) == 0

    def test_diagonal_islands(self, solution):
        """Diagonal cells are separate islands"""
        grid = [
            ["1", "0", "1"],
            ["0", "1", "0"],
            ["1", "0", "1"]
        ]
        assert solution.numIslands(grid) == 5

    def test_single_row(self, solution):
        """Single row with multiple islands"""
        grid = [["1", "0", "1", "0", "1"]]
        assert solution.numIslands(grid) == 3

    def test_single_column(self, solution):
        """Single column with multiple islands"""
        grid = [["1"], ["0"], ["1"], ["0"], ["1"]]
        assert solution.numIslands(grid) == 3

    def test_l_shaped_island(self, solution):
        """L-shaped island"""
        grid = [
            ["1", "0", "0"],
            ["1", "0", "0"],
            ["1", "1", "1"]
        ]
        assert solution.numIslands(grid) == 1

    def test_surrounded_water(self, solution):
        """Water surrounded by land"""
        grid = [
            ["1", "1", "1"],
            ["1", "0", "1"],
            ["1", "1", "1"]
        ]
        assert solution.numIslands(grid) == 1

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
