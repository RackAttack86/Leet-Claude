"""
Tests for LeetCode Problem #5: Longest Palindromic Substring
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestLongestPalindromicSubstring:
    """Test cases for Longest Palindromic Substring problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        result = solution.longestPalindrome("babad")
        assert result in ["bab", "aba"]

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        assert solution.longestPalindrome("cbbd") == "bb"

    # Edge cases
    def test_single_character(self, solution):
        """Single character is a palindrome"""
        assert solution.longestPalindrome("a") == "a"

    def test_all_same_characters(self, solution):
        """All same characters form one large palindrome"""
        assert solution.longestPalindrome("aaaa") == "aaaa"

    def test_no_palindrome_longer_than_one(self, solution):
        """No palindrome longer than 1, return first char"""
        result = solution.longestPalindrome("abcd")
        assert len(result) == 1
        assert result in "abcd"

    def test_two_same_characters(self, solution):
        """Two same characters form a palindrome"""
        assert solution.longestPalindrome("aa") == "aa"

    def test_two_different_characters(self, solution):
        """Two different characters - return first"""
        result = solution.longestPalindrome("ab")
        assert len(result) == 1

    def test_entire_string_palindrome(self, solution):
        """Entire string is a palindrome"""
        assert solution.longestPalindrome("racecar") == "racecar"

    def test_palindrome_at_start(self, solution):
        """Palindrome at the start of string"""
        result = solution.longestPalindrome("abaxy")
        assert result == "aba"

    def test_palindrome_at_end(self, solution):
        """Palindrome at the end of string"""
        result = solution.longestPalindrome("xyaba")
        assert result == "aba"

    def test_even_length_palindrome(self, solution):
        """Even length palindrome"""
        result = solution.longestPalindrome("abccba")
        assert result == "abccba"

    def test_odd_length_palindrome(self, solution):
        """Odd length palindrome"""
        result = solution.longestPalindrome("abcba")
        assert result == "abcba"

    def test_mixed_case_palindrome(self, solution):
        """Mixed alphanumeric characters"""
        result = solution.longestPalindrome("a1b2b1a")
        assert result == "a1b2b1a"

    def test_long_string_with_small_palindrome(self, solution):
        """Long string with small palindrome"""
        result = solution.longestPalindrome("abcdefghijklmnopponmlkjihgfedcba")
        assert result == "abcdefghijklmnopponmlkjihgfedcba"

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
