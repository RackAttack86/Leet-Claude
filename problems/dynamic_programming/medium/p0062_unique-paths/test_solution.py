"""
Tests for LeetCode Problem #62: Unique Paths
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestUniquePaths:
    """Test cases for Unique Paths problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        assert solution.uniquePaths(3, 7) == 28

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        assert solution.uniquePaths(3, 2) == 3

    # Edge cases
    def test_1x1_grid(self, solution):
        """1x1 grid - only one path (stay in place)"""
        assert solution.uniquePaths(1, 1) == 1

    def test_1xn_grid(self, solution):
        """1xn grid - only one path (all right)"""
        assert solution.uniquePaths(1, 5) == 1

    def test_nx1_grid(self, solution):
        """nx1 grid - only one path (all down)"""
        assert solution.uniquePaths(5, 1) == 1

    def test_2x2_grid(self, solution):
        """2x2 grid - two paths"""
        assert solution.uniquePaths(2, 2) == 2

    def test_2x3_grid(self, solution):
        """2x3 grid"""
        assert solution.uniquePaths(2, 3) == 3

    def test_3x3_grid(self, solution):
        """3x3 grid"""
        assert solution.uniquePaths(3, 3) == 6

    def test_symmetric_grid(self, solution):
        """Symmetric grid should give same result"""
        assert solution.uniquePaths(3, 7) == solution.uniquePaths(7, 3)

    def test_larger_grid(self, solution):
        """Larger grid with known result"""
        assert solution.uniquePaths(7, 3) == 28

    def test_10x10_grid(self, solution):
        """10x10 grid"""
        assert solution.uniquePaths(10, 10) == 48620

    def test_maximum_constraint(self, solution):
        """Near maximum constraint - 100x100"""
        # C(198, 99) is a very large number
        result = solution.uniquePaths(100, 100)
        assert result > 0  # Just verify it doesn't crash

    def test_rectangular_grid_wide(self, solution):
        """Wide rectangular grid"""
        assert solution.uniquePaths(2, 10) == 10

    def test_rectangular_grid_tall(self, solution):
        """Tall rectangular grid"""
        assert solution.uniquePaths(10, 2) == 10

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
