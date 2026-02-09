"""
Tests for LeetCode Problem #63: Unique Paths II
"""

import pytest
from solution import Solution, PROBLEM_METADATA




class TestUniquePathsIi:
    """Test cases for Unique Paths II problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
        expected = 2
        result = solution.uniquePathsWithObstacles(obstacleGrid)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        obstacleGrid = [[0,1],[0,0]]
        expected = 1
        result = solution.uniquePathsWithObstacles(obstacleGrid)
        assert result == expected


    # Edge cases
    def test_obstacle_at_start(self, solution):
        """Obstacle at starting position - no path possible"""
        assert solution.uniquePathsWithObstacles([[1,0],[0,0]]) == 0

    def test_obstacle_at_end(self, solution):
        """Obstacle at ending position - no path possible"""
        assert solution.uniquePathsWithObstacles([[0,0],[0,1]]) == 0

    def test_single_cell_no_obstacle(self, solution):
        """Single cell without obstacle"""
        assert solution.uniquePathsWithObstacles([[0]]) == 1

    def test_single_cell_with_obstacle(self, solution):
        """Single cell with obstacle"""
        assert solution.uniquePathsWithObstacles([[1]]) == 0

    def test_no_obstacles(self, solution):
        """Grid without any obstacles"""
        assert solution.uniquePathsWithObstacles([[0,0,0],[0,0,0],[0,0,0]]) == 6

    def test_all_obstacles_except_path(self, solution):
        """Only one valid path exists"""
        grid = [[0,1,1],[0,1,1],[0,0,0]]
        assert solution.uniquePathsWithObstacles(grid) == 1

    def test_1xn_grid_no_obstacles(self, solution):
        """1xn grid without obstacles"""
        assert solution.uniquePathsWithObstacles([[0,0,0,0]]) == 1

    def test_1xn_grid_with_obstacle(self, solution):
        """1xn grid with obstacle blocking path"""
        assert solution.uniquePathsWithObstacles([[0,1,0,0]]) == 0

    def test_nx1_grid_no_obstacles(self, solution):
        """nx1 grid without obstacles"""
        assert solution.uniquePathsWithObstacles([[0],[0],[0],[0]]) == 1

    def test_nx1_grid_with_obstacle(self, solution):
        """nx1 grid with obstacle blocking path"""
        assert solution.uniquePathsWithObstacles([[0],[1],[0],[0]]) == 0

    def test_obstacle_blocks_all_paths(self, solution):
        """Obstacles block all possible paths"""
        grid = [[0,0,0],[1,1,1],[0,0,0]]
        assert solution.uniquePathsWithObstacles(grid) == 0

    def test_obstacles_at_corners(self, solution):
        """Obstacles at corners (not start/end)"""
        grid = [[0,0,0],[0,0,0],[0,0,0]]
        assert solution.uniquePathsWithObstacles(grid) == 6

    def test_2x2_no_obstacles(self, solution):
        """2x2 grid without obstacles"""
        assert solution.uniquePathsWithObstacles([[0,0],[0,0]]) == 2

    def test_multiple_obstacles(self, solution):
        """Multiple obstacles in grid"""
        grid = [[0,0,0,0],[0,1,0,1],[0,0,0,0]]
        assert solution.uniquePathsWithObstacles(grid) == 2


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
