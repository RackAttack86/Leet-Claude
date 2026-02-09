"""
Tests for LeetCode Problem #392: Is Subsequence
"""

import pytest
from solution import Solution, PROBLEM_METADATA




class TestIsSubsequence:
    """Test cases for Is Subsequence problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        s = "abc"
        t = "ahbgdc"
        expected = True
        result = solution.isSubsequence(s, t)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        s = "axc"
        t = "ahbgdc"
        expected = False
        result = solution.isSubsequence(s, t)
        assert result == expected


    def test_edge_case_empty_s(self, solution):
        """Test with empty s (always a subsequence)"""
        s = ""
        t = "ahbgdc"
        expected = True
        result = solution.isSubsequence(s, t)
        assert result == expected


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
