"""
Tests for LeetCode Problem #30: Substring with Concatenation of All Words
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA




class TestSubstringWithConcatenationOfAllWords:
    """Test cases for Substring with Concatenation of All Words problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        s = "barfoothefoobarman"
        words = ["foo","bar"]
        expected = [0,9]
        result = solution.findSubstring(s, words)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        s = "wordgoodgoodgoodbestword"
        words = ["word","good","best","word"]
        expected = []
        result = solution.findSubstring(s, words)
        assert result == expected


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        s = "barfoofoobarthefoobarman"
        words = ["bar","foo","the"]
        expected = [6,9,12]
        result = solution.findSubstring(s, words)
        assert result == expected


    def test_edge_case_empty(self, solution):
        """Test with empty string"""
        s = ""
        words = ["foo", "bar"]
        assert solution.findSubstring(s, words) == []


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
