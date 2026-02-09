"""
Tests for LeetCode Problem #438: Find All Anagrams in a String
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestFindAllAnagramsInAString:
    """Test cases for Find All Anagrams in a String problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        s = "cbaebabacd"
        p = "abc"
        assert solution.findAnagrams(s, p) == [0, 6]

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        s = "abab"
        p = "ab"
        assert solution.findAnagrams(s, p) == [0, 1, 2]

    # Edge cases
    def test_edge_case_1(self, solution):
        """Test when pattern is longer than string"""
        s = "a"
        p = "abc"
        assert solution.findAnagrams(s, p) == []

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
