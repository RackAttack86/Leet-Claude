"""
Tests for LeetCode Problem #53: Maximum Subarray
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA




class TestMaximumSubarray:
    """Test cases for Maximum Subarray problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        expected = 6
        result = solution.maxSubArray(nums)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        nums = [1]
        expected = 1
        result = solution.maxSubArray(nums)
        assert result == expected


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        nums = [5,4,-1,7,8]
        expected = 23
        result = solution.maxSubArray(nums)
        assert result == expected


    # Edge cases
    def test_single_element_positive(self, solution):
        """Single positive element"""
        assert solution.maxSubArray([5]) == 5

    def test_single_element_negative(self, solution):
        """Single negative element"""
        assert solution.maxSubArray([-5]) == -5

    def test_single_element_zero(self, solution):
        """Single zero element"""
        assert solution.maxSubArray([0]) == 0

    def test_all_negative(self, solution):
        """All negative numbers - pick least negative"""
        assert solution.maxSubArray([-3, -1, -4, -2]) == -1

    def test_all_positive(self, solution):
        """All positive numbers - sum all"""
        assert solution.maxSubArray([1, 2, 3, 4, 5]) == 15

    def test_all_zeros(self, solution):
        """All zeros"""
        assert solution.maxSubArray([0, 0, 0, 0]) == 0

    def test_alternating_positive_negative(self, solution):
        """Alternating positive and negative"""
        assert solution.maxSubArray([1, -1, 1, -1, 1]) == 1

    def test_large_negative_then_positive(self, solution):
        """Large negative followed by small positive"""
        assert solution.maxSubArray([-100, 1, 2, 3]) == 6

    def test_positive_then_large_negative(self, solution):
        """Positive followed by large negative"""
        assert solution.maxSubArray([1, 2, 3, -100]) == 6

    def test_two_elements_positive(self, solution):
        """Two positive elements"""
        assert solution.maxSubArray([1, 2]) == 3

    def test_two_elements_negative(self, solution):
        """Two negative elements"""
        assert solution.maxSubArray([-1, -2]) == -1

    def test_max_subarray_in_middle(self, solution):
        """Maximum subarray is in the middle"""
        assert solution.maxSubArray([-1, 5, 6, -1]) == 11

    def test_max_subarray_at_end(self, solution):
        """Maximum subarray is at the end"""
        assert solution.maxSubArray([-5, -4, 3, 4, 5]) == 12

    def test_max_subarray_at_start(self, solution):
        """Maximum subarray is at the start"""
        assert solution.maxSubArray([3, 4, 5, -100, 1]) == 12

    def test_large_values(self, solution):
        """Large positive and negative values"""
        assert solution.maxSubArray([10000, -9999, 10000]) == 10001


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
