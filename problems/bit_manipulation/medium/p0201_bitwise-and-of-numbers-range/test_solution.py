"""
Tests for LeetCode Problem #201: Bitwise AND of Numbers Range
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestBitwiseAndOfNumbersRange:
    """Test cases for Bitwise AND of Numbers Range problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        assert solution.rangeBitwiseAnd(5, 7) == 4

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        assert solution.rangeBitwiseAnd(0, 0) == 0

    def test_example_3(self, solution):
        """Example 3 from problem description"""
        assert solution.rangeBitwiseAnd(1, 2147483647) == 0

    # Edge cases
    def test_same_number(self, solution):
        """left equals right - AND with itself"""
        assert solution.rangeBitwiseAnd(5, 5) == 5
        assert solution.rangeBitwiseAnd(100, 100) == 100
        assert solution.rangeBitwiseAnd(0, 0) == 0

    def test_consecutive_numbers(self, solution):
        """Two consecutive numbers"""
        assert solution.rangeBitwiseAnd(4, 5) == 4
        assert solution.rangeBitwiseAnd(6, 7) == 6
        assert solution.rangeBitwiseAnd(8, 9) == 8

    def test_power_of_two_range(self, solution):
        """Range crossing power of 2 boundary"""
        assert solution.rangeBitwiseAnd(7, 8) == 0
        assert solution.rangeBitwiseAnd(15, 16) == 0

    def test_same_prefix_range(self, solution):
        """Numbers with same prefix bits"""
        assert solution.rangeBitwiseAnd(12, 15) == 12

    def test_zero_to_n(self, solution):
        """Range starting from 0"""
        assert solution.rangeBitwiseAnd(0, 1) == 0
        assert solution.rangeBitwiseAnd(0, 100) == 0

    def test_large_same_number(self, solution):
        """Large number AND with itself"""
        assert solution.rangeBitwiseAnd(1000000, 1000000) == 1000000

    def test_small_range_same_high_bits(self, solution):
        """Small range with same high bits"""
        assert solution.rangeBitwiseAnd(26, 30) == 24

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
