"""
Tests for LeetCode Problem #648: Replace Words
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestReplaceWords:
    """Test cases for Replace Words problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        dictionary = ["cat", "bat", "rat"]
        sentence = "the cattle was rattled by the battery"
        assert solution.replaceWords(dictionary, sentence) == "the cat was rat by the bat"

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        dictionary = ["a", "b", "c"]
        sentence = "aadsfasf absbs bbab cadsfafs"
        assert solution.replaceWords(dictionary, sentence) == "a a b c"

    def test_edge_case_1(self, solution):
        """Test with no matching roots"""
        dictionary = ["xyz"]
        sentence = "hello world"
        assert solution.replaceWords(dictionary, sentence) == "hello world"

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
