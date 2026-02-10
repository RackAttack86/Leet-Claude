"""
Tests for LeetCode Problem #137: Single Number II
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA




class TestSingleNumberIi:
    """Test cases for Single Number II problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums = [2,2,3,2]
        expected = 3
        result = solution.singleNumber(nums)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        nums = [0,1,0,1,0,1,99]
        expected = 99
        result = solution.singleNumber(nums)
        assert result == expected


    def test_single_element(self, solution):
        """Test with single element array"""
        nums = [42]
        assert solution.singleNumber(nums) == 42

    def test_minimum_value(self, solution):
        """Test with minimum 32-bit integer value"""
        nums = [-2147483648, -2147483648, -2147483648, 5]
        assert solution.singleNumber(nums) == 5

    def test_maximum_value(self, solution):
        """Test with maximum 32-bit integer value"""
        nums = [2147483647, 2147483647, 2147483647, 7]
        assert solution.singleNumber(nums) == 7

    def test_single_is_negative(self, solution):
        """Test when single number is negative"""
        nums = [1, 1, 1, -5]
        assert solution.singleNumber(nums) == -5

    def test_all_negative(self, solution):
        """Test with all negative numbers"""
        nums = [-1, -1, -1, -2, -2, -2, -3]
        assert solution.singleNumber(nums) == -3

    def test_single_is_zero(self, solution):
        """Test when single number is zero"""
        nums = [1, 1, 1, 0]
        assert solution.singleNumber(nums) == 0

    def test_mixed_positive_negative(self, solution):
        """Test with mixed positive and negative numbers"""
        nums = [-3, -3, -3, 5, 5, 5, 10]
        assert solution.singleNumber(nums) == 10

    def test_large_array(self, solution):
        """Test with larger array"""
        nums = [7, 7, 7, 3, 3, 3, 1, 1, 1, 42]
        assert solution.singleNumber(nums) == 42

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
