"""
Tests for LeetCode Problem #342: Power of Four
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestPowerOfFour:
    """Test cases for Power of Four problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """16 is power of 4 (4^2)"""
        assert solution.isPowerOfFour(16) == True

    def test_example_2(self, solution):
        """5 is not power of 4"""
        assert solution.isPowerOfFour(5) == False

    def test_example_3(self, solution):
        """1 is power of 4 (4^0)"""
        assert solution.isPowerOfFour(1) == True

    def test_four(self, solution):
        """4 is power of 4"""
        assert solution.isPowerOfFour(4) == True

    def test_power_of_two_not_four(self, solution):
        """8 is power of 2 but not 4"""
        assert solution.isPowerOfFour(8) == False

    def test_64(self, solution):
        """64 is power of 4 (4^3)"""
        assert solution.isPowerOfFour(64) == True

    def test_zero(self, solution):
        """0 is not power of 4"""
        assert solution.isPowerOfFour(0) == False

    def test_negative(self, solution):
        """Negative numbers are not powers of 4"""
        assert solution.isPowerOfFour(-16) == False

    def test_all_powers_of_four(self, solution):
        """All powers of 4 up to 4^15"""
        powers = [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536,
                  262144, 1048576, 4194304, 16777216, 67108864, 268435456, 1073741824]
        for p in powers:
            assert solution.isPowerOfFour(p) == True

    def test_powers_of_two_not_four(self, solution):
        """Powers of 2 that are not powers of 4"""
        not_powers_of_four = [2, 8, 32, 128, 512, 2048]
        for n in not_powers_of_four:
            assert solution.isPowerOfFour(n) == False

    def test_two(self, solution):
        """2 is not power of 4"""
        assert solution.isPowerOfFour(2) == False

    def test_three(self, solution):
        """3 is not power of 4"""
        assert solution.isPowerOfFour(3) == False

    def test_five(self, solution):
        """5 is not power of 4"""
        assert solution.isPowerOfFour(5) == False

    def test_large_power_of_four(self, solution):
        """Largest power of 4 in 32-bit signed range"""
        assert solution.isPowerOfFour(1073741824) == True  # 4^15 = 2^30

    def test_max_32bit_int(self, solution):
        """Max 32-bit signed integer is not power of 4"""
        assert solution.isPowerOfFour(2147483647) == False

    def test_negative_ones(self, solution):
        """Various negative numbers"""
        assert solution.isPowerOfFour(-1) == False
        assert solution.isPowerOfFour(-4) == False
        assert solution.isPowerOfFour(-64) == False

    def test_one_more_than_power_of_four(self, solution):
        """Numbers just above powers of 4"""
        assert solution.isPowerOfFour(5) == False   # 4 + 1
        assert solution.isPowerOfFour(17) == False  # 16 + 1
        assert solution.isPowerOfFour(65) == False  # 64 + 1

    def test_one_less_than_power_of_four(self, solution):
        """Numbers just below powers of 4"""
        assert solution.isPowerOfFour(3) == False   # 4 - 1
        assert solution.isPowerOfFour(15) == False  # 16 - 1
        assert solution.isPowerOfFour(63) == False  # 64 - 1

    def test_multiple_bits_set(self, solution):
        """Numbers with multiple bits set"""
        assert solution.isPowerOfFour(7) == False
        assert solution.isPowerOfFour(12) == False
        assert solution.isPowerOfFour(20) == False

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
