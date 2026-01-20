"""
Tests for LeetCode Problem #767: Reorganize String
"""

import pytest
from solution import Solution, PROBLEM_METADATA


def is_valid_reorganization(s, result):
    """Check if result is a valid reorganization of s"""
    if result == "":
        return True  # Empty means impossible
    # Check same characters
    if sorted(s) != sorted(result):
        return False
    # Check no adjacent same characters
    for i in range(1, len(result)):
        if result[i] == result[i - 1]:
            return False
    return True


class TestReorganizeString:
    """Test cases for Reorganize String problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        s = "aab"
        result = solution.reorganizeString(s)
        assert is_valid_reorganization(s, result)
        assert result != ""  # Should be possible

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        s = "aaab"
        result = solution.reorganizeString(s)
        assert result == ""  # Impossible

    # Edge cases
    def test_single_character(self, solution):
        """Single character string"""
        s = "a"
        result = solution.reorganizeString(s)
        assert result == "a"

    def test_two_same_characters(self, solution):
        """Two same characters - impossible"""
        s = "aa"
        result = solution.reorganizeString(s)
        assert result == ""

    def test_two_different_characters(self, solution):
        """Two different characters"""
        s = "ab"
        result = solution.reorganizeString(s)
        assert is_valid_reorganization(s, result)

    def test_all_different(self, solution):
        """All different characters"""
        s = "abcdef"
        result = solution.reorganizeString(s)
        assert is_valid_reorganization(s, result)

    def test_alternating_possible(self, solution):
        """Exactly alternating distribution"""
        s = "aabb"
        result = solution.reorganizeString(s)
        assert is_valid_reorganization(s, result)

    def test_odd_length_valid(self, solution):
        """Odd length with valid distribution"""
        s = "aaabb"
        result = solution.reorganizeString(s)
        assert is_valid_reorganization(s, result)

    def test_many_characters(self, solution):
        """Many different characters"""
        s = "vvvlo"
        result = solution.reorganizeString(s)
        assert is_valid_reorganization(s, result)

    def test_impossible_majority(self, solution):
        """Impossible - one char has majority"""
        s = "aaaab"
        result = solution.reorganizeString(s)
        assert result == ""

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
