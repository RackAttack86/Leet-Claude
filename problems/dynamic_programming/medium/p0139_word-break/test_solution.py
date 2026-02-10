"""
Tests for LeetCode Problem #139: Word Break
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestWordBreak:
    """Test cases for Word Break problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        s = "leetcode"
        wordDict = ["leet", "code"]
        assert solution.wordBreak(s, wordDict) == True

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        s = "applepenapple"
        wordDict = ["apple", "pen"]
        assert solution.wordBreak(s, wordDict) == True

    # Edge cases
    def test_edge_case_1(self, solution):
        """Test with word that cannot be segmented"""
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        assert solution.wordBreak(s, wordDict) == False

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
