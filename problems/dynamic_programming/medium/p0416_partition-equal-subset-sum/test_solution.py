"""
Tests for LeetCode Problem #416: Partition Equal Subset Sum
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestPartitionEqualSubsetSum:
    """Test cases for Partition Equal Subset Sum problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums = [1, 5, 11, 5]
        assert solution.canPartition(nums) == True

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        nums = [1, 2, 3, 5]
        assert solution.canPartition(nums) == False

    # Edge cases
    def test_edge_case_1(self, solution):
        """Test with single element (cannot partition)"""
        nums = [1]
        assert solution.canPartition(nums) == False

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
