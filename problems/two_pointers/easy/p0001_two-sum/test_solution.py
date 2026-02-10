"""
Tests for LeetCode Problem #1: Two Sum
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestTwoSum:
    """Test cases for Two Sum problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums = [2, 7, 11, 15]
        target = 9
        result = solution.twoSum(nums, target)
        assert sorted(result) == [0, 1]
        assert nums[result[0]] + nums[result[1]] == target

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        nums = [3, 2, 4]
        target = 6
        result = solution.twoSum(nums, target)
        assert sorted(result) == [1, 2]
        assert nums[result[0]] + nums[result[1]] == target

    def test_example_3(self, solution):
        """Example 3 from problem description"""
        nums = [3, 3]
        target = 6
        result = solution.twoSum(nums, target)
        assert sorted(result) == [0, 1]

    # Edge cases
    def test_minimum_input(self, solution):
        """Test with minimum array size"""
        nums = [1, 2]
        target = 3
        result = solution.twoSum(nums, target)
        assert sorted(result) == [0, 1]

    def test_negative_numbers(self, solution):
        """Test with negative numbers"""
        nums = [-1, -2, -3, -4, -5]
        target = -8
        result = solution.twoSum(nums, target)
        assert nums[result[0]] + nums[result[1]] == target

    def test_with_zero(self, solution):
        """Test with zero in array"""
        nums = [0, 4, 3, 0]
        target = 0
        result = solution.twoSum(nums, target)
        assert nums[result[0]] + nums[result[1]] == target

    def test_large_numbers(self, solution):
        """Test with large numbers"""
        nums = [1000000000, -1000000000, 500000000]
        target = 0
        result = solution.twoSum(nums, target)
        assert len(result) == 2
        assert nums[result[0]] + nums[result[1]] == target

    # Parametrized tests
    @pytest.mark.parametrize("nums,target,expected_sum", [
        ([2, 7, 11, 15], 9, 9),
        ([3, 2, 4], 6, 6),
        ([3, 3], 6, 6),
        ([-1, -2, -3, -4], -6, -6),
        ([0, 1, 2], 2, 2),
    ])
    def test_parametrized(self, solution, nums, target, expected_sum):
        """Parametrized test for multiple cases"""
        result = solution.twoSum(nums, target)
        assert len(result) == 2
        assert nums[result[0]] + nums[result[1]] == expected_sum

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
