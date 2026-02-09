"""
Tests for LeetCode Problem #461: Hamming Distance
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestHammingDistance:
    """Test cases for Hamming Distance problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """x=1, y=4: hamming distance is 2"""
        # 1 = 0001, 4 = 0100 -> 2 bits differ
        assert solution.hammingDistance(1, 4) == 2

    def test_example_2(self, solution):
        """x=3, y=1: hamming distance is 1"""
        # 3 = 11, 1 = 01 -> 1 bit differs
        assert solution.hammingDistance(3, 1) == 1

    def test_same_numbers(self, solution):
        """Same numbers have 0 hamming distance"""
        assert solution.hammingDistance(5, 5) == 0

    def test_zero_and_zero(self, solution):
        """0 and 0"""
        assert solution.hammingDistance(0, 0) == 0

    def test_all_bits_different(self, solution):
        """All bits different (7 vs 0)"""
        # 7 = 111, 0 = 000 -> 3 bits differ
        assert solution.hammingDistance(7, 0) == 3

    def test_large_numbers(self, solution):
        """Larger numbers"""
        # 93 = 01011101, 73 = 01001001
        assert solution.hammingDistance(93, 73) == 2

    def test_zero_and_one(self, solution):
        """0 and 1 differ in 1 bit"""
        assert solution.hammingDistance(0, 1) == 1

    def test_zero_and_max(self, solution):
        """0 and max 32-bit differ in 31 bits"""
        assert solution.hammingDistance(0, 2147483647) == 31

    def test_powers_of_two(self, solution):
        """Two different powers of 2"""
        assert solution.hammingDistance(1, 2) == 2  # 01 vs 10
        assert solution.hammingDistance(2, 4) == 2  # 010 vs 100
        assert solution.hammingDistance(1, 4) == 2  # 001 vs 100

    def test_adjacent_numbers(self, solution):
        """Adjacent numbers"""
        assert solution.hammingDistance(0, 1) == 1
        assert solution.hammingDistance(1, 2) == 2
        assert solution.hammingDistance(2, 3) == 1
        assert solution.hammingDistance(7, 8) == 4

    def test_alternating_patterns(self, solution):
        """Alternating bit patterns are maximally different"""
        # 0xAAAAAAAA vs 0x55555555 - all 32 bits differ
        assert solution.hammingDistance(0xAAAAAAAA, 0x55555555) == 32

    def test_same_pattern_different_values(self, solution):
        """Same pattern count, different values"""
        assert solution.hammingDistance(3, 5) == 2  # 011 vs 101
        assert solution.hammingDistance(3, 6) == 2  # 011 vs 110

    def test_one_bit_difference(self, solution):
        """Numbers differing in exactly one bit"""
        assert solution.hammingDistance(0, 1) == 1
        assert solution.hammingDistance(4, 5) == 1
        assert solution.hammingDistance(8, 9) == 1
        assert solution.hammingDistance(16, 17) == 1

    def test_max_unsigned_values(self, solution):
        """Near max unsigned 32-bit values"""
        # 4294967295 = all 1s, 4294967294 = all 1s except last
        assert solution.hammingDistance(4294967295, 4294967294) == 1

    def test_symmetric(self, solution):
        """Hamming distance is symmetric"""
        assert solution.hammingDistance(10, 20) == solution.hammingDistance(20, 10)
        assert solution.hammingDistance(0, 100) == solution.hammingDistance(100, 0)

    def test_byte_boundary(self, solution):
        """Values at byte boundaries"""
        assert solution.hammingDistance(255, 256) == 9  # 11111111 vs 100000000

    def test_all_ones_vs_single_bit(self, solution):
        """All 1s vs single bit"""
        assert solution.hammingDistance(255, 1) == 7  # 11111111 vs 00000001

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
