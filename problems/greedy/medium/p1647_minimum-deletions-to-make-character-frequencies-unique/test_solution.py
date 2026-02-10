"""
Tests for LeetCode Problem #1647: Minimum Deletions to Make Character Frequencies Unique
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestMinimumDeletionsToMakeCharacterFrequenciesUnique:
    """Test cases for Minimum Deletions to Make Character Frequencies Unique problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description - already good"""
        s = "aab"
        assert solution.minDeletions(s) == 0

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        s = "aaabbbcc"
        assert solution.minDeletions(s) == 2

    def test_example_3(self, solution):
        """Example 3 from problem description"""
        s = "ceabaacb"
        assert solution.minDeletions(s) == 2

    # Edge cases
    def test_single_char(self, solution):
        """Single character - no deletions needed"""
        s = "a"
        assert solution.minDeletions(s) == 0

    def test_all_same_frequency(self, solution):
        """All characters have same frequency - need deletions"""
        s = "aabbcc"
        assert solution.minDeletions(s) == 3

    def test_no_deletions_needed_unique_freqs(self, solution):
        """Already unique frequencies"""
        s = "aabbc"
        assert solution.minDeletions(s) == 0

    def test_all_same_char(self, solution):
        """All same character - no deletions needed"""
        s = "aaaaaaa"
        assert solution.minDeletions(s) == 0

    def test_two_same_frequency(self, solution):
        """Two characters with same frequency"""
        s = "aabb"
        assert solution.minDeletions(s) == 1

    def test_cascade_deletions(self, solution):
        """Need cascade of deletions"""
        s = "aabbccdd"
        assert solution.minDeletions(s) == 6

    def test_many_same_frequency(self, solution):
        """Many characters with same frequency"""
        s = "abcdefg"
        assert solution.minDeletions(s) == 6

    def test_all_different_frequencies(self, solution):
        """Already all different frequencies"""
        s = "abbccc"
        assert solution.minDeletions(s) == 0

    def test_long_string_same_char(self, solution):
        """Long string of same character"""
        s = "bbbbbbbb"
        assert solution.minDeletions(s) == 0

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
