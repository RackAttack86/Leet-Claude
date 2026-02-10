"""
Tests for LeetCode Problem #3: Longest Substring Without Repeating Characters
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestLongestSubstringWithoutRepeatingCharacters:
    """Test cases for Longest Substring Without Repeating Characters problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        s = "abcabcbb"
        assert solution.lengthOfLongestSubstring(s) == 3

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        s = "bbbbb"
        assert solution.lengthOfLongestSubstring(s) == 1

    # Edge cases
    def test_edge_case_1(self, solution):
        """Test with empty string"""
        s = ""
        assert solution.lengthOfLongestSubstring(s) == 0

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
