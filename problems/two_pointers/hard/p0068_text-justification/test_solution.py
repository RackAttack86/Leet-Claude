"""
Tests for LeetCode Problem #68: Text Justification
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA




class TestTextJustification:
    """Test cases for Text Justification problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        words = ["This", "is", "an", "example", "of", "text", "justification."]
        maxWidth = 16
        expected = [
            "This    is    an",
            "example  of text",
            "justification.  "
        ]
        result = solution.fullJustify(words, maxWidth)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        words = ["What","must","be","acknowledgment","shall","be"]
        maxWidth = 16
        expected = [
            "What   must   be",
            "acknowledgment  ",
            "shall be        "
        ]
        result = solution.fullJustify(words, maxWidth)
        assert result == expected


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
        maxWidth = 20
        expected = [
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  "
        ]
        result = solution.fullJustify(words, maxWidth)
        assert result == expected


    def test_edge_case_single_word(self, solution):
        """Test with single word"""
        words = ["Hello"]
        maxWidth = 10
        expected = ["Hello     "]
        result = solution.fullJustify(words, maxWidth)
        assert result == expected

    def test_edge_case_word_equals_maxwidth(self, solution):
        """Test with word exactly equal to maxWidth"""
        words = ["Hello"]
        maxWidth = 5
        expected = ["Hello"]
        result = solution.fullJustify(words, maxWidth)
        assert result == expected


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
