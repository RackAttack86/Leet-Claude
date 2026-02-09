"""
Tests for LeetCode Problem #120: Triangle
"""

import pytest
from solution import Solution, PROBLEM_METADATA




class TestTriangle:
    """Test cases for Triangle problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
        expected = 11
        result = solution.minimumTotal(triangle)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        triangle = [[-10]]
        expected = -10
        result = solution.minimumTotal(triangle)
        assert result == expected


    # Edge cases
    def test_single_row(self, solution):
        """Single row triangle"""
        assert solution.minimumTotal([[5]]) == 5

    def test_single_row_negative(self, solution):
        """Single row with negative value"""
        assert solution.minimumTotal([[-5]]) == -5

    def test_two_rows(self, solution):
        """Two rows triangle"""
        assert solution.minimumTotal([[1],[2,3]]) == 3  # 1 + 2

    def test_two_rows_pick_right(self, solution):
        """Two rows, optimal path goes right"""
        assert solution.minimumTotal([[1],[5,2]]) == 3  # 1 + 2

    def test_all_zeros(self, solution):
        """Triangle with all zeros"""
        assert solution.minimumTotal([[0],[0,0],[0,0,0]]) == 0

    def test_all_same_values(self, solution):
        """Triangle with all same values"""
        assert solution.minimumTotal([[1],[1,1],[1,1,1]]) == 3

    def test_all_negative(self, solution):
        """Triangle with all negative values"""
        triangle = [[-1],[-2,-3],[-4,-5,-6]]
        assert solution.minimumTotal(triangle) == -10  # -1 + -3 + -6

    def test_large_values(self, solution):
        """Triangle with large values"""
        triangle = [[1000],[1000,1000],[1000,1000,1000]]
        assert solution.minimumTotal(triangle) == 3000

    def test_increasing_rows(self, solution):
        """Values increase in each row"""
        triangle = [[1],[2,3],[4,5,6],[7,8,9,10]]
        # Optimal: 1 + 2 + 4 + 7 = 14
        assert solution.minimumTotal(triangle) == 14

    def test_optimal_path_not_leftmost(self, solution):
        """Optimal path is not always leftmost"""
        triangle = [[10],[1,100],[100,1,100]]
        # Optimal: 10 + 1 + 1 = 12
        assert solution.minimumTotal(triangle) == 12

    def test_optimal_path_not_rightmost(self, solution):
        """Optimal path is not always rightmost"""
        triangle = [[10],[100,1],[100,1,100]]
        # Optimal: 10 + 1 + 1 = 12
        assert solution.minimumTotal(triangle) == 12

    def test_mixed_positive_negative(self, solution):
        """Mixed positive and negative values"""
        triangle = [[1],[-2,3],[4,-5,6]]
        # Optimal: 1 + -2 + -5 = -6
        assert solution.minimumTotal(triangle) == -6

    def test_three_rows(self, solution):
        """Three row triangle"""
        triangle = [[2],[3,4],[6,5,7]]
        # Optimal: 2 + 3 + 5 = 10
        assert solution.minimumTotal(triangle) == 10


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
