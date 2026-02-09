"""
Tests for LeetCode Problem #213: House Robber II
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestHouseRobberIi:
    """Test cases for House Robber II problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums = [2, 3, 2]
        assert solution.rob(nums) == 3

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        nums = [1, 2, 3, 1]
        assert solution.rob(nums) == 4

    # Edge cases
    def test_edge_case_1(self, solution):
        """Test with single house"""
        nums = [5]
        assert solution.rob(nums) == 5

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
