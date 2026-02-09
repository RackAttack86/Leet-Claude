"""
Tests for LeetCode Problem #151: Reverse Words in a String
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestReverseWordsInAString:
    """Test cases for Reverse Words in a String problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        s = "the sky is blue"
        expected = "blue is sky the"
        result = solution.reverseWords(s)
        assert result == expected

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        s = "  hello world  "
        expected = "world hello"
        result = solution.reverseWords(s)
        assert result == expected

    def test_example_3(self, solution):
        """Example 3 from problem description"""
        s = "a good   example"
        expected = "example good a"
        result = solution.reverseWords(s)
        assert result == expected

    def test_single_word(self, solution):
        """Test with single word"""
        s = "hello"
        expected = "hello"
        result = solution.reverseWords(s)
        assert result == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
