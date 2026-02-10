"""
Tests for LeetCode Problem #704: Binary Search
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestBinarySearch:
    """Test cases for Binary Search problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1: target exists"""
        assert solution.search([-1, 0, 3, 5, 9, 12], 9) == 4

    def test_example_2(self, solution):
        """Example 2: target not found"""
        assert solution.search([-1, 0, 3, 5, 9, 12], 2) == -1

    def test_first_element(self, solution):
        """Target is first element"""
        assert solution.search([1, 2, 3, 4, 5], 1) == 0

    def test_last_element(self, solution):
        """Target is last element"""
        assert solution.search([1, 2, 3, 4, 5], 5) == 4

    # Additional edge case tests
    def test_single_element_found(self, solution):
        """Single element array, target found"""
        assert solution.search([5], 5) == 0

    def test_single_element_not_found(self, solution):
        """Single element array, target not found"""
        assert solution.search([5], 3) == -1

    def test_two_element_found_first(self, solution):
        """Two element array, target at first position"""
        assert solution.search([1, 3], 1) == 0

    def test_two_element_found_second(self, solution):
        """Two element array, target at second position"""
        assert solution.search([1, 3], 3) == 1

    def test_two_element_not_found_smaller(self, solution):
        """Two element array, target smaller than all"""
        assert solution.search([1, 3], 0) == -1

    def test_two_element_not_found_between(self, solution):
        """Two element array, target between elements"""
        assert solution.search([1, 3], 2) == -1

    def test_two_element_not_found_larger(self, solution):
        """Two element array, target larger than all"""
        assert solution.search([1, 3], 4) == -1

    def test_target_smaller_than_all(self, solution):
        """Target smaller than all elements"""
        assert solution.search([2, 4, 6, 8, 10], 1) == -1

    def test_target_larger_than_all(self, solution):
        """Target larger than all elements"""
        assert solution.search([2, 4, 6, 8, 10], 12) == -1

    def test_target_between_elements(self, solution):
        """Target between elements (not in array)"""
        assert solution.search([1, 3, 5, 7, 9], 4) == -1
        assert solution.search([1, 3, 5, 7, 9], 6) == -1
        assert solution.search([1, 3, 5, 7, 9], 8) == -1

    def test_negative_numbers(self, solution):
        """Array with negative numbers"""
        assert solution.search([-10, -5, 0, 5, 10], -5) == 1
        assert solution.search([-10, -5, 0, 5, 10], 0) == 2
        assert solution.search([-10, -5, 0, 5, 10], -7) == -1

    def test_all_negative_numbers(self, solution):
        """Array with all negative numbers"""
        assert solution.search([-100, -50, -25, -10, -1], -25) == 2
        assert solution.search([-100, -50, -25, -10, -1], -30) == -1
        assert solution.search([-100, -50, -25, -10, -1], 0) == -1

    def test_target_at_middle(self, solution):
        """Target at middle position"""
        assert solution.search([1, 2, 3, 4, 5], 3) == 2
        assert solution.search([1, 2, 3, 4, 5, 6, 7], 4) == 3

    def test_large_array(self, solution):
        """Large array with many elements"""
        nums = list(range(0, 10000))
        assert solution.search(nums, 5000) == 5000
        assert solution.search(nums, 0) == 0
        assert solution.search(nums, 9999) == 9999
        assert solution.search(nums, -1) == -1
        assert solution.search(nums, 10000) == -1

    def test_large_array_target_not_found(self, solution):
        """Large array, target not in array"""
        nums = list(range(0, 10000, 2))  # Even numbers only
        assert solution.search(nums, 5001) == -1  # Odd number not in array

    def test_consecutive_elements(self, solution):
        """Array with consecutive elements"""
        nums = list(range(1, 11))
        for i, num in enumerate(nums):
            assert solution.search(nums, num) == i

    def test_sparse_array(self, solution):
        """Array with sparse elements (large gaps)"""
        assert solution.search([1, 100, 1000, 10000], 100) == 1
        assert solution.search([1, 100, 1000, 10000], 500) == -1

    def test_boundary_values(self, solution):
        """Test with boundary constraint values"""
        # Near constraint boundaries: -10^4 < nums[i], target < 10^4
        assert solution.search([-9999, -5000, 0, 5000, 9999], -9999) == 0
        assert solution.search([-9999, -5000, 0, 5000, 9999], 9999) == 4
        assert solution.search([-9999, -5000, 0, 5000, 9999], 0) == 2

    def test_odd_length_array(self, solution):
        """Odd length array"""
        assert solution.search([1, 3, 5, 7, 9], 5) == 2
        assert solution.search([1, 3, 5, 7, 9], 1) == 0
        assert solution.search([1, 3, 5, 7, 9], 9) == 4

    def test_even_length_array(self, solution):
        """Even length array"""
        assert solution.search([1, 3, 5, 7], 5) == 2
        assert solution.search([1, 3, 5, 7], 1) == 0
        assert solution.search([1, 3, 5, 7], 7) == 3

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
