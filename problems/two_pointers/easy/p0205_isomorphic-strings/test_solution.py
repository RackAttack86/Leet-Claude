"""
Tests for LeetCode Problem #205: Isomorphic Strings
"""

import pytest
from solution import Solution, PROBLEM_METADATA




class TestIsomorphicStrings:
    """Test cases for Isomorphic Strings problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        s = "egg"
        t = "add"
        expected = True
        result = solution.isIsomorphic(s, t)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        s = "foo"
        t = "bar"
        expected = False
        result = solution.isIsomorphic(s, t)
        assert result == expected


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        s = "paper"
        t = "title"
        expected = True
        result = solution.isIsomorphic(s, t)
        assert result == expected


    def test_edge_case_single_char(self, solution):
        """Test with single character strings"""
        s = "a"
        t = "b"
        expected = True
        result = solution.isIsomorphic(s, t)
        assert result == expected


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
