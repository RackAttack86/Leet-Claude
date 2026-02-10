"""
Tests for LeetCode Problem #127: Word Ladder
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA




class TestWordLadder:
    """Test cases for Word Ladder problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log","cog"]
        expected = 5
        result = solution.ladderLength(beginWord, endWord, wordList)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log"]
        expected = 0
        result = solution.ladderLength(beginWord, endWord, wordList)
        assert result == expected


    def test_direct_transform(self, solution):
        """Test direct one-step transformation"""
        beginWord = "hot"
        endWord = "dot"
        wordList = ["dot"]
        expected = 2
        result = solution.ladderLength(beginWord, endWord, wordList)
        assert result == expected


    def test_no_path(self, solution):
        """Test when no transformation path exists"""
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot"]
        expected = 0
        result = solution.ladderLength(beginWord, endWord, wordList)
        assert result == expected


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
