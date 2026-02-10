"""
Tests for LeetCode Problem #67: Add Binary
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA




class TestAddBinary:
    """Test cases for Add Binary problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        a = "11"
        b = "1"
        expected = "100"
        result = solution.addBinary(a, b)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        a = "1010"
        b = "1011"
        expected = "10101"
        result = solution.addBinary(a, b)
        assert result == expected


    def test_both_zeros(self, solution):
        """0 + 0 = 0"""
        assert solution.addBinary("0", "0") == "0"

    def test_one_zero(self, solution):
        """Adding with zero"""
        assert solution.addBinary("1", "0") == "1"
        assert solution.addBinary("0", "1") == "1"

    def test_both_ones(self, solution):
        """1 + 1 = 10"""
        assert solution.addBinary("1", "1") == "10"

    def test_single_bit_carry_propagation(self, solution):
        """Test carry propagation"""
        assert solution.addBinary("111", "1") == "1000"

    def test_different_lengths(self, solution):
        """Strings of different lengths"""
        assert solution.addBinary("1", "111") == "1000"
        assert solution.addBinary("10", "1111") == "10001"

    def test_long_strings(self, solution):
        """Longer binary strings"""
        assert solution.addBinary("11111111", "1") == "100000000"
        assert solution.addBinary("10101010", "01010101") == "11111111"

    def test_power_of_two_results(self, solution):
        """Results that are powers of 2"""
        assert solution.addBinary("1", "1") == "10"  # 2
        assert solution.addBinary("10", "10") == "100"  # 4
        assert solution.addBinary("100", "100") == "1000"  # 8

    def test_alternating_bits(self, solution):
        """Alternating bit patterns"""
        assert solution.addBinary("10101", "10101") == "101010"
        assert solution.addBinary("1010", "0101") == "1111"

    def test_all_ones(self, solution):
        """Adding numbers where one or both have all 1s"""
        assert solution.addBinary("1111", "1111") == "11110"
        assert solution.addBinary("11111111", "11111111") == "111111110"

    def test_max_carry_chain(self, solution):
        """Long chain of carries"""
        assert solution.addBinary("11111111111111111111", "1") == "100000000000000000000"

    def test_single_chars(self, solution):
        """Single character inputs"""
        assert solution.addBinary("0", "0") == "0"
        assert solution.addBinary("1", "1") == "10"

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
