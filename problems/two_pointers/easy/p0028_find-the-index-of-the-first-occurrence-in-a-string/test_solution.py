"""
Tests for LeetCode Problem #28: Find the Index of the First Occurrence in a String
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA




class TestFindTheIndexOfTheFirstOccurrenceInAString:
    """Test cases for Find the Index of the First Occurrence in a String problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        haystack = "sadbutsad"
        needle = "sad"
        expected = 0
        result = solution.strStr(haystack, needle)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        haystack = "leetcode"
        needle = "leeto"
        expected = -1
        result = solution.strStr(haystack, needle)
        assert result == expected


    # Edge cases
    def test_needle_at_start(self, solution):
        """Test with needle at the start of haystack"""
        assert solution.strStr("hello", "hel") == 0

    def test_needle_at_end(self, solution):
        """Test with needle at the end of haystack"""
        assert solution.strStr("hello", "llo") == 2

    def test_needle_in_middle(self, solution):
        """Test with needle in the middle"""
        assert solution.strStr("abcdef", "cde") == 2

    def test_needle_equals_haystack(self, solution):
        """Test with needle equal to haystack"""
        assert solution.strStr("abc", "abc") == 0

    def test_single_character_needle(self, solution):
        """Test with single character needle"""
        assert solution.strStr("hello", "e") == 1
        assert solution.strStr("hello", "x") == -1

    def test_single_character_haystack(self, solution):
        """Test with single character haystack"""
        assert solution.strStr("a", "a") == 0
        assert solution.strStr("a", "b") == -1

    def test_needle_longer_than_haystack(self, solution):
        """Test with needle longer than haystack"""
        assert solution.strStr("abc", "abcdef") == -1

    def test_multiple_occurrences(self, solution):
        """Test with multiple occurrences (should return first)"""
        assert solution.strStr("abcabc", "abc") == 0
        assert solution.strStr("aaa", "aa") == 0

    def test_repeated_characters(self, solution):
        """Test with repeated characters"""
        assert solution.strStr("aaaa", "aa") == 0
        assert solution.strStr("aaab", "aab") == 1

    def test_partial_match_then_full(self, solution):
        """Test where partial match exists before full match"""
        assert solution.strStr("mississippi", "issip") == 4
        assert solution.strStr("aabaaabaaac", "aabaaac") == 4

    def test_no_match(self, solution):
        """Test with no match at all"""
        assert solution.strStr("hello", "world") == -1
        assert solution.strStr("abc", "xyz") == -1

    def test_empty_needle(self, solution):
        """Test with empty needle"""
        assert solution.strStr("hello", "") == 0

    # Parametrized tests
    @pytest.mark.parametrize("haystack,needle,expected", [
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),
        ("hello", "ll", 2),
        ("a", "a", 0),
        ("abc", "c", 2),
        ("aaa", "aaaa", -1),
        ("mississippi", "pi", 9),
    ])
    def test_parametrized(self, solution, haystack, needle, expected):
        """Parametrized test for various inputs"""
        assert solution.strStr(haystack, needle) == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
