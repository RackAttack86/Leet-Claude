"""
Tests for LeetCode Problem #190: Reverse Bits
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestReverseBits:
    """Test cases for Reverse Bits problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        # 43261596 = 00000010100101000001111010011100
        # Reversed = 00111001011110000010100101000000 = 964176192
        assert solution.reverseBits(43261596) == 964176192

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        # 4294967293 = 11111111111111111111111111111101
        # Reversed = 10111111111111111111111111111111 = 3221225471
        assert solution.reverseBits(4294967293) == 3221225471

    def test_zero(self, solution):
        """0 reversed is 0"""
        assert solution.reverseBits(0) == 0

    def test_one(self, solution):
        """1 reversed"""
        # 1 = 00...01, reversed = 10...00 = 2^31
        assert solution.reverseBits(1) == 2147483648

    def test_max_value(self, solution):
        """All 1s stays all 1s"""
        # All 32 bits set stays the same
        assert solution.reverseBits(4294967295) == 4294967295

    def test_power_of_two(self, solution):
        """Powers of 2"""
        # 2 = 00...010, reversed = 01...00 = 2^30
        assert solution.reverseBits(2) == 1073741824
        # 4 = 00...100, reversed = 001...0 = 2^29
        assert solution.reverseBits(4) == 536870912
        # 8 = 00...1000, reversed = 0001...0 = 2^28
        assert solution.reverseBits(8) == 268435456

    def test_single_bit_high(self, solution):
        """Single high bit"""
        # 2^31 reversed is 1
        assert solution.reverseBits(2147483648) == 1

    def test_alternating_bits_aaaa(self, solution):
        """Alternating bits pattern 0xAAAAAAAA"""
        # 10101010... reversed is 01010101... = 0x55555555
        assert solution.reverseBits(0xAAAAAAAA) == 0x55555555

    def test_alternating_bits_5555(self, solution):
        """Alternating bits pattern 0x55555555"""
        # 01010101... reversed is 10101010... = 0xAAAAAAAA
        assert solution.reverseBits(0x55555555) == 0xAAAAAAAA

    def test_low_nibble_set(self, solution):
        """Low 4 bits set (15)"""
        # 00...01111 reversed = 11110...0
        assert solution.reverseBits(15) == 4026531840

    def test_high_nibble_set(self, solution):
        """High 4 bits set"""
        # 11110...0 reversed = 00...01111
        assert solution.reverseBits(4026531840) == 15

    def test_palindrome_pattern(self, solution):
        """Palindrome bit patterns stay same"""
        # Pattern that reads same forwards and backwards in 32 bits
        # 0x81818181 = 10000001100000011000000110000001
        # Its reverse should be calculated
        assert solution.reverseBits(0x81818181) == 0x81818181

    def test_byte_boundary(self, solution):
        """Test at byte boundaries"""
        # 255 = 0xFF in low byte
        assert solution.reverseBits(255) == 4278190080
        # 256 = bit 8 set
        assert solution.reverseBits(256) == 8388608

    def test_16bit_value(self, solution):
        """16-bit value (fits in lower half)"""
        # 65535 = 0xFFFF (16 ones in low bits)
        assert solution.reverseBits(65535) == 4294901760

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
