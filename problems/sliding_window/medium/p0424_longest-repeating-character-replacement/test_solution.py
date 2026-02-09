"""
Tests for LeetCode Problem #424: Longest Repeating Character Replacement
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestLongestRepeatingCharacterReplacement:
    """Test cases for Longest Repeating Character Replacement problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        s = "ABAB"
        k = 2
        assert solution.characterReplacement(s, k) == 4

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        s = "AABABBA"
        k = 1
        assert solution.characterReplacement(s, k) == 4

    # Edge cases
    def test_edge_case_1(self, solution):
        """Test with single character string"""
        s = "A"
        k = 0
        assert solution.characterReplacement(s, k) == 1

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
