"""
Tests for LeetCode Problem #1004: Max Consecutive Ones III
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestMaxConsecutiveOnesIii:
    """Test cases for Max Consecutive Ones III problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
        k = 2
        assert solution.longestOnes(nums, k) == 6

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
        k = 3
        assert solution.longestOnes(nums, k) == 10

    # Edge cases
    def test_edge_case_1(self, solution):
        """Test with all ones and k=0"""
        nums = [1, 1, 1, 1]
        k = 0
        assert solution.longestOnes(nums, k) == 4

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
