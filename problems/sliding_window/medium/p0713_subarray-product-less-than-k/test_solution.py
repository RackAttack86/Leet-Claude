"""
Tests for LeetCode Problem #713: Subarray Product Less Than K
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestSubarrayProductLessThanK:
    """Test cases for Subarray Product Less Than K problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums = [10, 5, 2, 6]
        k = 100
        assert solution.numSubarrayProductLessThanK(nums, k) == 8

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        nums = [1, 2, 3]
        k = 0
        assert solution.numSubarrayProductLessThanK(nums, k) == 0

    # Edge cases
    def test_edge_case_1(self, solution):
        """Test with k = 1 (no valid subarrays since all elements >= 1)"""
        nums = [1, 1, 1]
        k = 1
        assert solution.numSubarrayProductLessThanK(nums, k) == 0

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
