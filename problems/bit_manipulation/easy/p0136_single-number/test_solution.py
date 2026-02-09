"""
Tests for LeetCode Problem #136: Single Number
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestSingleNumber:
    """Test cases for Single Number problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1: [2,2,1] -> 1"""
        assert solution.singleNumber([2, 2, 1]) == 1

    def test_example_2(self, solution):
        """Example 2: [4,1,2,1,2] -> 4"""
        assert solution.singleNumber([4, 1, 2, 1, 2]) == 4

    def test_single_element(self, solution):
        """Single element array"""
        assert solution.singleNumber([1]) == 1

    def test_negative_numbers(self, solution):
        """Array with negative numbers"""
        assert solution.singleNumber([-1, -1, -2]) == -2

    def test_zero_is_single(self, solution):
        """Zero as the single number"""
        assert solution.singleNumber([1, 0, 1]) == 0

    def test_zero_in_pairs(self, solution):
        """Zero appears in pairs"""
        assert solution.singleNumber([0, 1, 0]) == 1

    def test_large_array(self, solution):
        """Larger array with many pairs"""
        assert solution.singleNumber([1, 2, 3, 4, 5, 4, 3, 2, 1]) == 5

    def test_mixed_positive_negative(self, solution):
        """Mixed positive and negative numbers"""
        assert solution.singleNumber([-1, 1, -1, 2, 2]) == 1

    def test_powers_of_two(self, solution):
        """Powers of 2 testing XOR properties"""
        assert solution.singleNumber([1, 2, 4, 2, 1]) == 4
        assert solution.singleNumber([8, 16, 8]) == 16

    def test_single_large_number(self, solution):
        """Large number as single"""
        assert solution.singleNumber([30000, 30000, 29999]) == 29999

    def test_alternating_bit_patterns(self, solution):
        """Numbers with alternating bits"""
        # 0xAAAA = 43690 (10101010...)
        # 0x5555 = 21845 (01010101...)
        assert solution.singleNumber([43690, 21845, 43690]) == 21845

    def test_consecutive_pairs(self, solution):
        """Pairs appear consecutively"""
        assert solution.singleNumber([3, 3, 4, 4, 5]) == 5

    def test_single_at_start(self, solution):
        """Single number at start of array"""
        assert solution.singleNumber([7, 1, 1, 2, 2]) == 7

    def test_single_at_end(self, solution):
        """Single number at end of array"""
        assert solution.singleNumber([1, 1, 2, 2, 7]) == 7

    def test_all_same_except_one(self, solution):
        """Many of same pair values"""
        assert solution.singleNumber([5, 5, 5, 5, 3]) == 3

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
