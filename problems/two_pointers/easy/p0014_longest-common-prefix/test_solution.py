"""
Tests for LeetCode Problem #14: Longest Common Prefix
"""

import pytest
from solution import Solution, PROBLEM_METADATA




class TestLongestCommonPrefix:
    """Test cases for Longest Common Prefix problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        strs = ["flower","flow","flight"]
        expected = "fl"
        result = solution.longestCommonPrefix(strs)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        strs = ["dog","racecar","car"]
        expected = ""
        result = solution.longestCommonPrefix(strs)
        assert result == expected


    # Edge cases
    def test_empty_array(self, solution):
        """Test with empty array"""
        assert solution.longestCommonPrefix([]) == ""

    def test_single_string(self, solution):
        """Test with single string in array"""
        assert solution.longestCommonPrefix(["alone"]) == "alone"

    def test_single_character_strings(self, solution):
        """Test with single character strings"""
        assert solution.longestCommonPrefix(["a", "a", "a"]) == "a"
        assert solution.longestCommonPrefix(["a", "b", "c"]) == ""

    def test_empty_string_in_array(self, solution):
        """Test with empty string in array"""
        assert solution.longestCommonPrefix(["", "abc", "abd"]) == ""
        assert solution.longestCommonPrefix(["abc", "", "abd"]) == ""

    def test_all_same_strings(self, solution):
        """Test with all identical strings"""
        assert solution.longestCommonPrefix(["test", "test", "test"]) == "test"

    def test_first_string_is_prefix(self, solution):
        """Test where first string is the common prefix"""
        assert solution.longestCommonPrefix(["ab", "abc", "abcd"]) == "ab"

    def test_no_common_prefix(self, solution):
        """Test with no common prefix at all"""
        assert solution.longestCommonPrefix(["xyz", "abc", "def"]) == ""

    def test_two_strings(self, solution):
        """Test with exactly two strings"""
        assert solution.longestCommonPrefix(["flower", "flow"]) == "flow"
        assert solution.longestCommonPrefix(["abc", "xyz"]) == ""

    def test_common_prefix_is_single_char(self, solution):
        """Test where common prefix is just one character"""
        assert solution.longestCommonPrefix(["apple", "ape", "april"]) == "ap"
        assert solution.longestCommonPrefix(["abc", "axy", "azz"]) == "a"

    def test_long_strings(self, solution):
        """Test with longer strings"""
        assert solution.longestCommonPrefix(["interview", "internet", "internal"]) == "inter"

    def test_one_string_is_prefix_of_others(self, solution):
        """Test where one string is prefix of all others"""
        assert solution.longestCommonPrefix(["a", "ab", "abc"]) == "a"

    # Parametrized tests
    @pytest.mark.parametrize("strs,expected", [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        ([""], ""),
        (["a"], "a"),
        (["aa", "aa"], "aa"),
        (["cir", "car"], "c"),
        (["prefix", "prefix", "prefix"], "prefix"),
    ])
    def test_parametrized(self, solution, strs, expected):
        """Parametrized test for various inputs"""
        assert solution.longestCommonPrefix(strs) == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
