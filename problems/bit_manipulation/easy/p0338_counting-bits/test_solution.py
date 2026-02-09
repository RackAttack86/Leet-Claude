"""
Tests for LeetCode Problem #338: Counting Bits
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestCountingBits:
    """Test cases for Counting Bits problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """n=2: [0,1,1]"""
        assert solution.countBits(2) == [0, 1, 1]

    def test_example_2(self, solution):
        """n=5: [0,1,1,2,1,2]"""
        assert solution.countBits(5) == [0, 1, 1, 2, 1, 2]

    def test_zero(self, solution):
        """n=0: [0]"""
        assert solution.countBits(0) == [0]

    def test_one(self, solution):
        """n=1: [0,1]"""
        assert solution.countBits(1) == [0, 1]

    def test_power_of_two(self, solution):
        """n=8 - includes several powers of 2"""
        result = solution.countBits(8)
        # 0=0, 1=1, 2=1, 3=2, 4=1, 5=2, 6=2, 7=3, 8=1
        assert result == [0, 1, 1, 2, 1, 2, 2, 3, 1]

    def test_n_15(self, solution):
        """n=15 covers all 4-bit numbers"""
        result = solution.countBits(15)
        expected = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]
        assert result == expected

    def test_powers_of_two_all_have_one_bit(self, solution):
        """All powers of 2 have exactly 1 bit"""
        result = solution.countBits(32)
        assert result[1] == 1   # 2^0
        assert result[2] == 1   # 2^1
        assert result[4] == 1   # 2^2
        assert result[8] == 1   # 2^3
        assert result[16] == 1  # 2^4
        assert result[32] == 1  # 2^5

    def test_one_less_than_power_of_two(self, solution):
        """Numbers 2^k - 1 have k bits set"""
        result = solution.countBits(63)
        assert result[1] == 1   # 2^1 - 1 = 1, has 1 bit
        assert result[3] == 2   # 2^2 - 1 = 3, has 2 bits
        assert result[7] == 3   # 2^3 - 1 = 7, has 3 bits
        assert result[15] == 4  # 2^4 - 1 = 15, has 4 bits
        assert result[31] == 5  # 2^5 - 1 = 31, has 5 bits
        assert result[63] == 6  # 2^6 - 1 = 63, has 6 bits

    def test_consecutive_numbers(self, solution):
        """Check pattern between consecutive numbers"""
        result = solution.countBits(10)
        # Verify each result is correct using bin count
        for i in range(11):
            assert result[i] == bin(i).count('1')

    def test_larger_n(self, solution):
        """Larger n value"""
        result = solution.countBits(100)
        assert len(result) == 101
        assert result[100] == 3  # 100 = 1100100, 3 bits set

    def test_n_255(self, solution):
        """n=255 (all 8-bit numbers)"""
        result = solution.countBits(255)
        assert result[255] == 8  # 11111111
        assert result[128] == 1  # 10000000

    def test_alternating_bits(self, solution):
        """Numbers with alternating bits"""
        result = solution.countBits(170)
        assert result[170] == 4  # 10101010
        assert result[85] == 4   # 01010101

    def test_first_element_is_zero(self, solution):
        """First element is always 0"""
        for n in range(10):
            result = solution.countBits(n)
            assert result[0] == 0

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
