"""
Tests for LeetCode Problem #12: Integer to Roman
"""

import pytest
from solution import Solution, PROBLEM_METADATA




class TestIntegerToRoman:
    """Test cases for Integer to Roman problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        num = 3749
        expected = "MMMDCCXLIX"
        result = solution.intToRoman(num)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        num = 58
        expected = "LVIII"
        result = solution.intToRoman(num)
        assert result == expected


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        num = 1994
        expected = "MCMXCIV"
        result = solution.intToRoman(num)
        assert result == expected


    def test_edge_case_minimum(self, solution):
        """Test with minimum input value (1)"""
        num = 1
        expected = "I"
        result = solution.intToRoman(num)
        assert result == expected

    def test_edge_case_maximum(self, solution):
        """Test with maximum input value (3999)"""
        num = 3999
        expected = "MMMCMXCIX"
        result = solution.intToRoman(num)
        assert result == expected


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
