"""
Tests for LeetCode Problem #231: Power of Two
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestPowerOfTwo:
    """Test cases for Power of Two problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """1 is power of 2 (2^0)"""
        assert solution.isPowerOfTwo(1) == True

    def test_example_2(self, solution):
        """16 is power of 2 (2^4)"""
        assert solution.isPowerOfTwo(16) == True

    def test_example_3(self, solution):
        """3 is not power of 2"""
        assert solution.isPowerOfTwo(3) == False

    def test_zero(self, solution):
        """0 is not power of 2"""
        assert solution.isPowerOfTwo(0) == False

    def test_negative(self, solution):
        """Negative numbers are not powers of 2"""
        assert solution.isPowerOfTwo(-16) == False

    def test_large_power(self, solution):
        """Large power of 2"""
        assert solution.isPowerOfTwo(1024) == True

    def test_not_power_7(self, solution):
        """7 is not power of 2"""
        assert solution.isPowerOfTwo(7) == False

    def test_all_powers_of_two(self, solution):
        """All powers of 2 up to 2^30"""
        for i in range(31):
            assert solution.isPowerOfTwo(2 ** i) == True

    def test_max_power_of_two(self, solution):
        """Largest power of 2 in 32-bit signed range"""
        assert solution.isPowerOfTwo(2 ** 30) == True  # 1073741824

    def test_two_bits_set(self, solution):
        """Numbers with exactly two bits set are not powers of 2"""
        assert solution.isPowerOfTwo(3) == False  # 11
        assert solution.isPowerOfTwo(5) == False  # 101
        assert solution.isPowerOfTwo(6) == False  # 110

    def test_one_less_than_power_of_two(self, solution):
        """n-1 for powers of 2 are not powers"""
        assert solution.isPowerOfTwo(15) == False  # 2^4 - 1
        assert solution.isPowerOfTwo(31) == False  # 2^5 - 1
        assert solution.isPowerOfTwo(63) == False  # 2^6 - 1

    def test_one_more_than_power_of_two(self, solution):
        """n+1 for powers of 2 are not powers"""
        assert solution.isPowerOfTwo(17) == False  # 2^4 + 1
        assert solution.isPowerOfTwo(33) == False  # 2^5 + 1

    def test_negative_powers_of_two_pattern(self, solution):
        """Negative numbers with power of 2 absolute value"""
        assert solution.isPowerOfTwo(-1) == False
        assert solution.isPowerOfTwo(-2) == False
        assert solution.isPowerOfTwo(-4) == False
        assert solution.isPowerOfTwo(-1073741824) == False

    def test_min_32bit_int(self, solution):
        """Min 32-bit signed integer is not power of 2"""
        assert solution.isPowerOfTwo(-2147483648) == False

    def test_max_32bit_int(self, solution):
        """Max 32-bit signed integer is not power of 2"""
        assert solution.isPowerOfTwo(2147483647) == False

    def test_all_bits_set(self, solution):
        """All bits set is not power of 2"""
        assert solution.isPowerOfTwo(0xFFFFFFFF) == False

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
