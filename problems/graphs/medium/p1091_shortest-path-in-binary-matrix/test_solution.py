"""
Tests for LeetCode Problem #1091: Shortest Path in Binary Matrix
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestShortestPathInBinaryMatrix:
    """Test cases for Shortest Path in Binary Matrix problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        grid = [[0, 1], [1, 0]]
        assert solution.shortestPathBinaryMatrix(grid) == 2

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
        assert solution.shortestPathBinaryMatrix(grid) == 4

    def test_example_3(self, solution):
        """Example 3 - blocked start"""
        grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
        assert solution.shortestPathBinaryMatrix(grid) == -1

    # Edge cases
    def test_single_cell_open(self, solution):
        """Single cell that is open"""
        grid = [[0]]
        assert solution.shortestPathBinaryMatrix(grid) == 1

    def test_single_cell_blocked(self, solution):
        """Single cell that is blocked"""
        grid = [[1]]
        assert solution.shortestPathBinaryMatrix(grid) == -1

    def test_start_blocked(self, solution):
        """Start cell is blocked"""
        grid = [[1, 0], [0, 0]]
        assert solution.shortestPathBinaryMatrix(grid) == -1

    def test_end_blocked(self, solution):
        """End cell is blocked"""
        grid = [[0, 0], [0, 1]]
        assert solution.shortestPathBinaryMatrix(grid) == -1

    def test_both_corners_blocked(self, solution):
        """Both start and end blocked"""
        grid = [[1, 0], [0, 1]]
        assert solution.shortestPathBinaryMatrix(grid) == -1

    def test_diagonal_path(self, solution):
        """Diagonal path is shortest"""
        grid = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
        assert solution.shortestPathBinaryMatrix(grid) == 3

    def test_all_zeros(self, solution):
        """All cells are open - diagonal is shortest"""
        grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        assert solution.shortestPathBinaryMatrix(grid) == 3

    def test_no_path_blocked_middle(self, solution):
        """No path exists due to blocked middle"""
        grid = [
            [0, 0, 0],
            [1, 1, 1],
            [0, 0, 0]
        ]
        assert solution.shortestPathBinaryMatrix(grid) == -1

    def test_winding_path(self, solution):
        """Path requires winding around obstacles"""
        grid = [
            [0, 0, 1],
            [1, 0, 1],
            [1, 0, 0]
        ]
        assert solution.shortestPathBinaryMatrix(grid) == 4

    def test_two_by_two_all_open(self, solution):
        """2x2 grid all open"""
        grid = [[0, 0], [0, 0]]
        assert solution.shortestPathBinaryMatrix(grid) == 2

    def test_large_open_grid(self, solution):
        """Larger grid all open - test diagonal path"""
        n = 5
        grid = [[0] * n for _ in range(n)]
        assert solution.shortestPathBinaryMatrix(grid) == n

    def test_corridor_path(self, solution):
        """Single corridor path available"""
        grid = [
            [0, 1, 1, 1],
            [0, 0, 0, 1],
            [1, 1, 0, 1],
            [1, 1, 0, 0]
        ]
        result = solution.shortestPathBinaryMatrix(grid)
        assert result == 6

    def test_multiple_paths_same_length(self, solution):
        """Multiple paths of same length exist"""
        grid = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        assert solution.shortestPathBinaryMatrix(grid) == 3

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
