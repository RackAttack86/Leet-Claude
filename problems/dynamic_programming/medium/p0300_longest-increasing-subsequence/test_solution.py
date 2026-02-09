"""
Tests for LeetCode Problem #300: Longest Increasing Subsequence
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestLongestIncreasingSubsequence:
    """Test cases for Longest Increasing Subsequence problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        assert solution.lengthOfLIS(nums) == 4

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        nums = [0, 1, 0, 3, 2, 3]
        assert solution.lengthOfLIS(nums) == 4

    # Edge cases
    def test_edge_case_1(self, solution):
        """Test with single element array"""
        nums = [5]
        assert solution.lengthOfLIS(nums) == 1

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
