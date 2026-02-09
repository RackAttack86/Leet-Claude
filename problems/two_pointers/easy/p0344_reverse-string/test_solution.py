"""
Tests for LeetCode Problem #344: Reverse String
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestReverseString:
    """Test cases for Reverse String problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        s = ["h", "e", "l", "l", "o"]
        expected = ["o", "l", "l", "e", "h"]
        solution.reverseString(s)
        assert s == expected

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        s = ["H", "a", "n", "n", "a", "h"]
        expected = ["h", "a", "n", "n", "a", "H"]
        solution.reverseString(s)
        assert s == expected

    def test_edge_case_single_char(self, solution):
        """Test with single character array"""
        s = ["a"]
        expected = ["a"]
        solution.reverseString(s)
        assert s == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
