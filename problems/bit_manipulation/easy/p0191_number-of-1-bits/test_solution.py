"""
Tests for LeetCode Problem #191: Number of 1 Bits
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestNumberOf1Bits:
    """Test cases for Number of 1 Bits problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """11 in binary is 1011, has 3 ones"""
        assert solution.hammingWeight(11) == 3

    def test_example_2(self, solution):
        """128 in binary is 10000000, has 1 one"""
        assert solution.hammingWeight(128) == 1

    def test_example_3(self, solution):
        """4294967293 has 31 ones"""
        # 11111111111111111111111111111101
        assert solution.hammingWeight(4294967293) == 31

    def test_zero(self, solution):
        """0 has no 1 bits"""
        assert solution.hammingWeight(0) == 0

    def test_one(self, solution):
        """1 has one 1 bit"""
        assert solution.hammingWeight(1) == 1

    def test_seven(self, solution):
        """7 = 111 has 3 ones"""
        assert solution.hammingWeight(7) == 3

    def test_power_of_two(self, solution):
        """Powers of 2 have exactly 1 bit set"""
        assert solution.hammingWeight(16) == 1
        assert solution.hammingWeight(1024) == 1

    def test_all_32_bits_set(self, solution):
        """All 32 bits set"""
        assert solution.hammingWeight(4294967295) == 32

    def test_max_signed_32bit(self, solution):
        """Max signed 32-bit (2^31 - 1) has 31 bits set"""
        assert solution.hammingWeight(2147483647) == 31

    def test_alternating_bits_aaaa(self, solution):
        """Alternating bits 0xAAAAAAAA has 16 bits"""
        assert solution.hammingWeight(0xAAAAAAAA) == 16

    def test_alternating_bits_5555(self, solution):
        """Alternating bits 0x55555555 has 16 bits"""
        assert solution.hammingWeight(0x55555555) == 16

    def test_single_high_bit(self, solution):
        """Highest bit set (2^31)"""
        assert solution.hammingWeight(2147483648) == 1

    def test_two_bits_set(self, solution):
        """Exactly two bits set"""
        assert solution.hammingWeight(3) == 2  # 11
        assert solution.hammingWeight(5) == 2  # 101
        assert solution.hammingWeight(6) == 2  # 110

    def test_consecutive_ones(self, solution):
        """Consecutive 1 bits"""
        assert solution.hammingWeight(15) == 4  # 1111
        assert solution.hammingWeight(31) == 5  # 11111
        assert solution.hammingWeight(63) == 6  # 111111

    def test_sparse_bits(self, solution):
        """Sparsely set bits"""
        assert solution.hammingWeight(0x80000001) == 2  # highest and lowest bits

    def test_byte_values(self, solution):
        """Full byte values"""
        assert solution.hammingWeight(255) == 8  # 11111111

    def test_large_sparse_number(self, solution):
        """Large number with few bits set"""
        assert solution.hammingWeight(0x10001000) == 2

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
