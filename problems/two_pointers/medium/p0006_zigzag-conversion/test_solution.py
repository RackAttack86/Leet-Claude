"""
Tests for LeetCode Problem #6: Zigzag Conversion
"""

import pytest
from solution import Solution, PROBLEM_METADATA




class TestZigzagConversion:
    """Test cases for Zigzag Conversion problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        s = "PAYPALISHIRING"
        numRows = 3
        expected = "PAHNAPLSIIGYIR"
        result = solution.convert(s, numRows)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        s = "PAYPALISHIRING"
        numRows = 4
        expected = "PINALSIGYAHRPI"
        result = solution.convert(s, numRows)
        assert result == expected


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        s = "A"
        numRows = 1
        expected = "A"
        result = solution.convert(s, numRows)
        assert result == expected


    def test_edge_case_numrows_equals_length(self, solution):
        """Test when numRows equals string length"""
        s = "ABC"
        numRows = 3
        expected = "ABC"
        result = solution.convert(s, numRows)
        assert result == expected

    def test_edge_case_numrows_greater_than_length(self, solution):
        """Test when numRows is greater than string length"""
        s = "AB"
        numRows = 5
        expected = "AB"
        result = solution.convert(s, numRows)
        assert result == expected


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
