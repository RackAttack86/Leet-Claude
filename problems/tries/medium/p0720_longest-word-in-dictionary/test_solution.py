"""
Tests for LeetCode Problem #720: Longest Word in Dictionary
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestLongestWordInDictionary:
    """Test cases for Longest Word in Dictionary problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        words = ["w", "wo", "wor", "worl", "world"]
        assert solution.longestWord(words) == "world"

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
        assert solution.longestWord(words) == "apple"

    def test_edge_case_1(self, solution):
        """Test with single character words only"""
        words = ["a", "b", "c"]
        assert solution.longestWord(words) == "a"

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
