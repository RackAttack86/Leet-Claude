"""
Tests for LeetCode Problem #72: Edit Distance
"""

import pytest
from solution import Solution, PROBLEM_METADATA




class TestEditDistance:
    """Test cases for Edit Distance problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        word1 = "horse"
        word2 = "ros"
        expected = 3
        result = solution.minDistance(word1, word2)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        word1 = "intention"
        word2 = "execution"
        expected = 5
        result = solution.minDistance(word1, word2)
        assert result == expected


    # Edge cases
    def test_both_empty(self, solution):
        """Both strings empty"""
        assert solution.minDistance("", "") == 0

    def test_first_empty(self, solution):
        """First string empty - all insertions"""
        assert solution.minDistance("", "abc") == 3

    def test_second_empty(self, solution):
        """Second string empty - all deletions"""
        assert solution.minDistance("abc", "") == 3

    def test_same_strings(self, solution):
        """Both strings are identical"""
        assert solution.minDistance("abc", "abc") == 0

    def test_completely_different(self, solution):
        """Completely different strings of same length"""
        assert solution.minDistance("abc", "xyz") == 3

    def test_single_char_same(self, solution):
        """Single character strings that are same"""
        assert solution.minDistance("a", "a") == 0

    def test_single_char_different(self, solution):
        """Single character strings that are different"""
        assert solution.minDistance("a", "b") == 1

    def test_one_insertion(self, solution):
        """One insertion needed"""
        assert solution.minDistance("ac", "abc") == 1

    def test_one_deletion(self, solution):
        """One deletion needed"""
        assert solution.minDistance("abc", "ac") == 1

    def test_one_replacement(self, solution):
        """One replacement needed"""
        assert solution.minDistance("abc", "adc") == 1

    def test_prefix_match(self, solution):
        """Strings share common prefix"""
        assert solution.minDistance("abc", "abxyz") == 3

    def test_suffix_match(self, solution):
        """Strings share common suffix"""
        # Replace 'x' with 'a', delete 'y', delete 'z' = 3 operations
        assert solution.minDistance("xyzbc", "abc") == 3

    def test_reverse_strings(self, solution):
        """One string is reverse of other"""
        assert solution.minDistance("abc", "cba") == 2

    def test_repeated_characters(self, solution):
        """Strings with repeated characters"""
        assert solution.minDistance("aaa", "aaaa") == 1

    def test_long_strings_same(self, solution):
        """Long identical strings"""
        word = "abcdefghij"
        assert solution.minDistance(word, word) == 0

    def test_case_sensitive(self, solution):
        """Case sensitive comparison"""
        assert solution.minDistance("ABC", "abc") == 3


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
