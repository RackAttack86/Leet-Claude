"""
Tests for LeetCode Problem #209: Minimum Size Subarray Sum
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestMinimumSizeSubarraySum:
    """Test cases for Minimum Size Subarray Sum problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        target = 7
        nums = [2, 3, 1, 2, 4, 3]
        assert solution.minSubArrayLen(target, nums) == 2

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        target = 4
        nums = [1, 4, 4]
        assert solution.minSubArrayLen(target, nums) == 1

    # Edge cases
    def test_edge_case_1(self, solution):
        """Test when no subarray sum meets target"""
        target = 100
        nums = [1, 2, 3]
        assert solution.minSubArrayLen(target, nums) == 0

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
