"""
Tests for LeetCode Problem #91: Decode Ways
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestDecodeWays:
    """Test cases for Decode Ways problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        assert solution.numDecodings("12") == 2

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        assert solution.numDecodings("226") == 3

    # Edge cases
    def test_starts_with_zero(self, solution):
        """Starts with 0 - invalid"""
        assert solution.numDecodings("0") == 0

    def test_leading_zero(self, solution):
        """Leading zero in multi-digit - invalid"""
        assert solution.numDecodings("06") == 0

    def test_double_zero(self, solution):
        """Double zero - invalid"""
        assert solution.numDecodings("00") == 0

    def test_all_ones(self, solution):
        """All 1s - maximum ways (Fibonacci-like)"""
        assert solution.numDecodings("111") == 3

    def test_all_twos(self, solution):
        """All 2s - maximum ways"""
        assert solution.numDecodings("222") == 3

    def test_single_digit_valid(self, solution):
        """Single valid digit"""
        assert solution.numDecodings("1") == 1
        assert solution.numDecodings("9") == 1

    def test_ten(self, solution):
        """10 - only one way to decode"""
        assert solution.numDecodings("10") == 1

    def test_twenty(self, solution):
        """20 - only one way to decode"""
        assert solution.numDecodings("20") == 1

    def test_zero_in_middle(self, solution):
        """Zero in middle that can be part of 10 or 20"""
        assert solution.numDecodings("101") == 1
        assert solution.numDecodings("201") == 1

    def test_invalid_zero_position(self, solution):
        """Zero that cannot form valid number"""
        assert solution.numDecodings("30") == 0
        assert solution.numDecodings("40") == 0

    def test_27_and_above(self, solution):
        """Numbers 27 and above - cannot be decoded as two digits"""
        assert solution.numDecodings("27") == 1
        assert solution.numDecodings("99") == 1

    def test_11_to_19(self, solution):
        """11-19 range - two ways each"""
        assert solution.numDecodings("11") == 2
        assert solution.numDecodings("19") == 2

    def test_21_to_26(self, solution):
        """21-26 range - two ways each"""
        assert solution.numDecodings("21") == 2
        assert solution.numDecodings("26") == 2

    def test_long_string_all_ones(self, solution):
        """Long string of 1s"""
        assert solution.numDecodings("1111") == 5  # Fibonacci(5)

    def test_mixed_valid_string(self, solution):
        """Mixed valid string"""
        assert solution.numDecodings("1234") == 3

    def test_ends_with_zero(self, solution):
        """Ends with valid zero combination"""
        assert solution.numDecodings("1210") == 2

    def test_multiple_zeros(self, solution):
        """Multiple zeros in valid positions"""
        assert solution.numDecodings("10101") == 1


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
