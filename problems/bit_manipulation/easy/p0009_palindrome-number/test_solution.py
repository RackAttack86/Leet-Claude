"""
Tests for LeetCode Problem #9: Palindrome Number
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA




class TestPalindromeNumber:
    """Test cases for Palindrome Number problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        x = 121
        expected = True
        result = solution.isPalindrome(x)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        x = -121
        expected = False
        result = solution.isPalindrome(x)
        assert result == expected


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        x = 10
        expected = False
        result = solution.isPalindrome(x)
        assert result == expected


    def test_zero(self, solution):
        """Zero is a palindrome"""
        assert solution.isPalindrome(0) == True

    def test_single_digit_palindromes(self, solution):
        """All single digits are palindromes"""
        for i in range(10):
            assert solution.isPalindrome(i) == True

    def test_negative_numbers(self, solution):
        """Negative numbers are never palindromes"""
        assert solution.isPalindrome(-1) == False
        assert solution.isPalindrome(-121) == False
        assert solution.isPalindrome(-2147483648) == False

    def test_numbers_ending_in_zero(self, solution):
        """Numbers ending in 0 (except 0) are not palindromes"""
        assert solution.isPalindrome(10) == False
        assert solution.isPalindrome(100) == False
        assert solution.isPalindrome(1000) == False

    def test_two_digit_palindromes(self, solution):
        """Two-digit palindromes"""
        assert solution.isPalindrome(11) == True
        assert solution.isPalindrome(22) == True
        assert solution.isPalindrome(99) == True

    def test_two_digit_non_palindromes(self, solution):
        """Two-digit non-palindromes"""
        assert solution.isPalindrome(12) == False
        assert solution.isPalindrome(21) == False

    def test_large_palindrome(self, solution):
        """Large palindrome numbers"""
        assert solution.isPalindrome(1234321) == True
        assert solution.isPalindrome(12344321) == True
        assert solution.isPalindrome(123454321) == True

    def test_max_32bit_int(self, solution):
        """Max 32-bit signed integer is not a palindrome"""
        assert solution.isPalindrome(2147483647) == False

    def test_power_of_two_values(self, solution):
        """Powers of 2 (testing various patterns)"""
        assert solution.isPalindrome(1) == True
        assert solution.isPalindrome(2) == True  # Single digit palindrome
        assert solution.isPalindrome(4) == True  # Single digit palindrome
        assert solution.isPalindrome(8) == True  # Single digit palindrome
        assert solution.isPalindrome(16) == False  # 16 is not a palindrome
        assert solution.isPalindrome(32) == False  # 32 is not a palindrome
        assert solution.isPalindrome(64) == False  # 64 is not a palindrome

    def test_odd_length_palindromes(self, solution):
        """Odd-length palindromes"""
        assert solution.isPalindrome(12321) == True
        assert solution.isPalindrome(1001) == True

    def test_even_length_palindromes(self, solution):
        """Even-length palindromes"""
        assert solution.isPalindrome(1221) == True
        assert solution.isPalindrome(123321) == True

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
