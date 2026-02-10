"""
Tests for LeetCode Problem #153: Find Minimum in Rotated Sorted Array
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestFindMinimumInRotatedSortedArray:
    """Test cases for Find Minimum in Rotated Sorted Array problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums = [3, 4, 5, 1, 2]
        assert solution.findMin(nums) == 1

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        nums = [4, 5, 6, 7, 0, 1, 2]
        assert solution.findMin(nums) == 0

    # Edge cases
    def test_not_rotated(self, solution):
        """Array is not rotated (sorted in ascending order)"""
        nums = [1, 2, 3, 4, 5]
        assert solution.findMin(nums) == 1

    def test_not_rotated_larger(self, solution):
        """Larger array not rotated"""
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        assert solution.findMin(nums) == 1

    def test_single_element(self, solution):
        """Single element array"""
        nums = [5]
        assert solution.findMin(nums) == 5

    def test_two_elements_rotated(self, solution):
        """Two elements - rotated"""
        nums = [2, 1]
        assert solution.findMin(nums) == 1

    def test_two_elements_not_rotated(self, solution):
        """Two elements - not rotated"""
        nums = [1, 2]
        assert solution.findMin(nums) == 1

    def test_rotated_by_1(self, solution):
        """Array rotated by 1 position"""
        nums = [5, 1, 2, 3, 4]
        assert solution.findMin(nums) == 1

    def test_rotated_by_n_minus_1(self, solution):
        """Array rotated by n-1 positions (minimum at position 1)"""
        nums = [2, 3, 4, 5, 1]
        assert solution.findMin(nums) == 1

    def test_minimum_at_middle(self, solution):
        """Minimum at approximately middle position"""
        nums = [5, 6, 7, 1, 2, 3, 4]
        assert solution.findMin(nums) == 1

    def test_negative_numbers(self, solution):
        """Array with negative numbers"""
        nums = [2, 3, 4, 5, -5, -4, -3, -2, -1, 0, 1]
        assert solution.findMin(nums) == -5

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
