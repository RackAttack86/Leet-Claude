"""
Tests for LeetCode Problem #215: Kth Largest Element in an Array
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestKthLargestElementInAnArray:
    """Test cases for Kth Largest Element in an Array problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        assert solution.findKthLargest(nums, k) == 5

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k = 4
        assert solution.findKthLargest(nums, k) == 4

    # Edge cases
    def test_single_element(self, solution):
        """Array with single element"""
        assert solution.findKthLargest([1], 1) == 1

    def test_k_equals_length(self, solution):
        """k equals array length (find minimum)"""
        assert solution.findKthLargest([3, 1, 2], 3) == 1

    def test_duplicates(self, solution):
        """Array with duplicate values"""
        assert solution.findKthLargest([2, 2, 2, 2], 2) == 2

    def test_negative_numbers(self, solution):
        """Array with negative numbers"""
        assert solution.findKthLargest([-1, -2, -3, -4], 2) == -2

    def test_k_equals_one_largest(self, solution):
        """k=1 returns the largest element"""
        assert solution.findKthLargest([3, 2, 1, 5, 6, 4], 1) == 6

    def test_k_equals_n_smallest(self, solution):
        """k=n returns the smallest element"""
        assert solution.findKthLargest([3, 2, 1, 5, 6, 4], 6) == 1

    def test_all_same_elements(self, solution):
        """Array with all identical elements"""
        assert solution.findKthLargest([7, 7, 7, 7, 7], 1) == 7
        assert solution.findKthLargest([7, 7, 7, 7, 7], 3) == 7
        assert solution.findKthLargest([7, 7, 7, 7, 7], 5) == 7

    def test_two_elements(self, solution):
        """Array with exactly two elements"""
        assert solution.findKthLargest([1, 2], 1) == 2
        assert solution.findKthLargest([1, 2], 2) == 1

    def test_mixed_positive_negative(self, solution):
        """Array with mixed positive and negative numbers"""
        assert solution.findKthLargest([-5, 0, 5, -10, 10], 1) == 10
        assert solution.findKthLargest([-5, 0, 5, -10, 10], 5) == -10

    def test_large_k(self, solution):
        """k close to array length"""
        nums = list(range(1, 101))  # 1 to 100
        assert solution.findKthLargest(nums, 100) == 1
        assert solution.findKthLargest(nums, 1) == 100

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
