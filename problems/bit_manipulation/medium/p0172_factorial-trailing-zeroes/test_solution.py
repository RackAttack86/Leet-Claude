"""
Tests for LeetCode Problem #172: Factorial Trailing Zeroes
"""

import pytest
from solution import Solution, PROBLEM_METADATA




class TestFactorialTrailingZeroes:
    """Test cases for Factorial Trailing Zeroes problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        n = 3
        expected = 0
        result = solution.trailingZeroes(n)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        n = 5
        expected = 1
        result = solution.trailingZeroes(n)
        assert result == expected


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        n = 0
        expected = 0
        result = solution.trailingZeroes(n)
        assert result == expected


    def test_n_equals_zero(self, solution):
        """n=0 should return 0 (0! = 1, no trailing zeros)"""
        assert solution.trailingZeroes(0) == 0

    def test_n_equals_five(self, solution):
        """n=5 should return 1 (5! = 120, one trailing zero)"""
        assert solution.trailingZeroes(5) == 1

    def test_power_of_five_25(self, solution):
        """n=25 (5^2) should return 6"""
        # 25! has 25/5 + 25/25 = 5 + 1 = 6 trailing zeros
        assert solution.trailingZeroes(25) == 6

    def test_power_of_five_125(self, solution):
        """n=125 (5^3) should return 31"""
        # 125/5 + 125/25 + 125/125 = 25 + 5 + 1 = 31
        assert solution.trailingZeroes(125) == 31

    def test_power_of_five_625(self, solution):
        """n=625 (5^4) should return 156"""
        # 625/5 + 625/25 + 625/125 + 625/625 = 125 + 25 + 5 + 1 = 156
        assert solution.trailingZeroes(625) == 156

    def test_n_just_below_five(self, solution):
        """n=4 should return 0"""
        assert solution.trailingZeroes(4) == 0

    def test_n_just_above_five(self, solution):
        """n=6 should return 1"""
        assert solution.trailingZeroes(6) == 1

    def test_n_ten(self, solution):
        """n=10 should return 2"""
        assert solution.trailingZeroes(10) == 2

    def test_large_n(self, solution):
        """Test with large n"""
        # 1000/5 + 1000/25 + 1000/125 + 1000/625 = 200 + 40 + 8 + 1 = 249
        assert solution.trailingZeroes(1000) == 249

    def test_n_one(self, solution):
        """n=1 should return 0"""
        assert solution.trailingZeroes(1) == 0

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
