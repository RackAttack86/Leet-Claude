"""
Tests for LeetCode Problem #13: Roman to Integer
"""

import pytest
from .solution import Solution, PROBLEM_METADATA




class TestRomanToInteger:
    """Test cases for Roman to Integer problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        s = "III"
        expected = 3
        result = solution.romanToInt(s)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        s = "LVIII"
        expected = 58
        result = solution.romanToInt(s)
        assert result == expected


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        s = "MCMXCIV"
        expected = 1994
        result = solution.romanToInt(s)
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
