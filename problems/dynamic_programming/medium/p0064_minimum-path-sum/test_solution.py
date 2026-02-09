"""
Tests for LeetCode Problem #64: Minimum Path Sum
"""

import pytest
from solution import Solution, PROBLEM_METADATA




class TestMinimumPathSum:
    """Test cases for Minimum Path Sum problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        grid = [[1,3,1],[1,5,1],[4,2,1]]
        expected = 7
        result = solution.minPathSum(grid)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        grid = [[1,2,3],[4,5,6]]
        expected = 12
        result = solution.minPathSum(grid)
        assert result == expected


    # Edge cases
    def test_single_cell(self, solution):
        """Single cell grid"""
        assert solution.minPathSum([[5]]) == 5

    def test_single_cell_zero(self, solution):
        """Single cell with zero"""
        assert solution.minPathSum([[0]]) == 0

    def test_single_row(self, solution):
        """Single row grid - must go all right"""
        assert solution.minPathSum([[1,2,3,4]]) == 10

    def test_single_column(self, solution):
        """Single column grid - must go all down"""
        assert solution.minPathSum([[1],[2],[3],[4]]) == 10

    def test_2x2_grid(self, solution):
        """2x2 grid"""
        assert solution.minPathSum([[1,2],[3,4]]) == 7  # 1->2->4

    def test_all_zeros(self, solution):
        """Grid with all zeros"""
        assert solution.minPathSum([[0,0,0],[0,0,0],[0,0,0]]) == 0

    def test_all_same_values(self, solution):
        """Grid with all same values"""
        assert solution.minPathSum([[1,1,1],[1,1,1],[1,1,1]]) == 5

    def test_large_values(self, solution):
        """Grid with large values"""
        assert solution.minPathSum([[100,200],[300,400]]) == 700

    def test_optimal_path_not_obvious(self, solution):
        """Optimal path is not the most direct"""
        grid = [[1,100,1],[1,1,1],[100,100,1]]
        assert solution.minPathSum(grid) == 5

    def test_rectangular_wide(self, solution):
        """Wide rectangular grid"""
        grid = [[1,2,3,4,5]]
        assert solution.minPathSum(grid) == 15

    def test_rectangular_tall(self, solution):
        """Tall rectangular grid"""
        grid = [[1],[2],[3],[4],[5]]
        assert solution.minPathSum(grid) == 15

    def test_increasing_values(self, solution):
        """Grid with increasing values"""
        grid = [[1,2,3],[4,5,6],[7,8,9]]
        assert solution.minPathSum(grid) == 21  # 1->2->3->6->9

    def test_decreasing_path_values(self, solution):
        """Path with decreasing values is optimal"""
        grid = [[9,9,9],[1,1,9],[1,1,1]]
        assert solution.minPathSum(grid) == 13  # 9->1->1->1->1


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
