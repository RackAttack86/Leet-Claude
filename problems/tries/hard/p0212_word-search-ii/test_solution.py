"""
Tests for LeetCode Problem #212: Word Search II
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestWordSearchIi:
    """Test cases for Word Search II problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
        words = ["oath","pea","eat","rain"]
        result = solution.findWords(board, words)
        assert sorted(result) == sorted(["eat","oath"])

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        board = [["a","b"],["c","d"]]
        words = ["abcb"]
        assert solution.findWords(board, words) == []

    def test_edge_case_1(self, solution):
        """Test with single cell board"""
        board = [["a"]]
        words = ["a", "b"]
        assert solution.findWords(board, words) == ["a"]

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
