"""
Tests for LeetCode Problem #14: Longest Common Prefix
"""

import pytest
from .solution import Solution, PROBLEM_METADATA




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
