"""
Tests for LeetCode Problem #28: Find the Index of the First Occurrence in a String
"""

import pytest
from .solution import Solution, PROBLEM_METADATA




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


    def test_edge_case_empty(self, solution):
        """Test with empty/minimal input"""
        # TODO: Implement edge case test
        pass


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
