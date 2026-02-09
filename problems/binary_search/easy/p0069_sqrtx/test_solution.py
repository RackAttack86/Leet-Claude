"""
Tests for LeetCode Problem #69: Sqrt(x)
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestSqrtX:
    """Test cases for Sqrt(x) problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        x = 4
        expected = 2
        result = solution.mySqrt(x)
        assert result == expected

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        x = 8
        expected = 2
        result = solution.mySqrt(x)
        assert result == expected

    def test_zero(self, solution):
        """Test with zero"""
        x = 0
        expected = 0
        result = solution.mySqrt(x)
        assert result == expected

    def test_one(self, solution):
        """Test with one"""
        x = 1
        expected = 1
        result = solution.mySqrt(x)
        assert result == expected

    # Additional edge case tests
    def test_perfect_squares(self, solution):
        """Test with perfect squares"""
        assert solution.mySqrt(9) == 3
        assert solution.mySqrt(16) == 4
        assert solution.mySqrt(25) == 5
        assert solution.mySqrt(36) == 6
        assert solution.mySqrt(49) == 7
        assert solution.mySqrt(64) == 8
        assert solution.mySqrt(81) == 9
        assert solution.mySqrt(100) == 10

    def test_non_perfect_squares(self, solution):
        """Test with non-perfect squares (floor result)"""
        assert solution.mySqrt(2) == 1
        assert solution.mySqrt(3) == 1
        assert solution.mySqrt(5) == 2
        assert solution.mySqrt(6) == 2
        assert solution.mySqrt(7) == 2
        assert solution.mySqrt(10) == 3
        assert solution.mySqrt(15) == 3
        assert solution.mySqrt(17) == 4

    def test_small_values(self, solution):
        """Test small values near boundaries"""
        assert solution.mySqrt(0) == 0
        assert solution.mySqrt(1) == 1
        assert solution.mySqrt(2) == 1
        assert solution.mySqrt(3) == 1
        assert solution.mySqrt(4) == 2

    def test_large_perfect_square(self, solution):
        """Test with large perfect squares"""
        assert solution.mySqrt(10000) == 100
        assert solution.mySqrt(1000000) == 1000
        assert solution.mySqrt(100000000) == 10000

    def test_large_non_perfect_square(self, solution):
        """Test with large non-perfect squares"""
        assert solution.mySqrt(99999) == 316  # sqrt(99999) = 316.226...
        assert solution.mySqrt(999999) == 999  # sqrt(999999) = 999.999...
        assert solution.mySqrt(1000001) == 1000  # sqrt(1000001) = 1000.0004...

    def test_maximum_constraint(self, solution):
        """Test near maximum constraint (2^31 - 1)"""
        # sqrt(2^31 - 1) = sqrt(2147483647) = 46340.95...
        assert solution.mySqrt(2147483647) == 46340

    def test_values_just_below_perfect_squares(self, solution):
        """Test values just below perfect squares"""
        assert solution.mySqrt(8) == 2  # just below 9
        assert solution.mySqrt(15) == 3  # just below 16
        assert solution.mySqrt(24) == 4  # just below 25
        assert solution.mySqrt(35) == 5  # just below 36

    def test_values_just_above_perfect_squares(self, solution):
        """Test values just above perfect squares"""
        assert solution.mySqrt(10) == 3  # just above 9
        assert solution.mySqrt(17) == 4  # just above 16
        assert solution.mySqrt(26) == 5  # just above 25
        assert solution.mySqrt(37) == 6  # just above 36

    def test_power_of_two(self, solution):
        """Test powers of 2"""
        assert solution.mySqrt(2) == 1
        assert solution.mySqrt(4) == 2
        assert solution.mySqrt(8) == 2
        assert solution.mySqrt(16) == 4
        assert solution.mySqrt(32) == 5
        assert solution.mySqrt(64) == 8
        assert solution.mySqrt(128) == 11
        assert solution.mySqrt(256) == 16

    def test_medium_values(self, solution):
        """Test medium range values"""
        assert solution.mySqrt(500) == 22
        assert solution.mySqrt(1000) == 31
        assert solution.mySqrt(5000) == 70
        assert solution.mySqrt(10000) == 100

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
