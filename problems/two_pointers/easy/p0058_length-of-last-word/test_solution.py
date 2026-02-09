"""
Tests for LeetCode Problem #58: Length of Last Word
"""

import pytest
from solution import Solution, PROBLEM_METADATA




class TestLengthOfLastWord:
    """Test cases for Length of Last Word problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        s = "Hello World"
        expected = 5
        result = solution.lengthOfLastWord(s)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        s = "   fly me   to   the moon  "
        expected = 4
        result = solution.lengthOfLastWord(s)
        assert result == expected


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        s = "luffy is still joyboy"
        expected = 6
        result = solution.lengthOfLastWord(s)
        assert result == expected


    def test_edge_case_single_word(self, solution):
        """Test with single word"""
        s = "Hello"
        expected = 5
        result = solution.lengthOfLastWord(s)
        assert result == expected


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
