"""
Tests for LeetCode Problem #35: Search Insert Position
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestSearchInsertPosition:
    """Test cases for Search Insert Position problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Target exists in array"""
        assert solution.searchInsert([1, 3, 5, 6], 5) == 2

    def test_example_2(self, solution):
        """Target would be inserted in middle"""
        assert solution.searchInsert([1, 3, 5, 6], 2) == 1

    def test_example_3(self, solution):
        """Target would be inserted at end"""
        assert solution.searchInsert([1, 3, 5, 6], 7) == 4

    def test_insert_at_beginning(self, solution):
        """Target would be inserted at beginning"""
        assert solution.searchInsert([1, 3, 5, 6], 0) == 0

    def test_single_element_found(self, solution):
        """Single element array, target found"""
        assert solution.searchInsert([5], 5) == 0

    def test_single_element_insert_before(self, solution):
        """Single element array, insert before"""
        assert solution.searchInsert([5], 3) == 0

    def test_single_element_insert_after(self, solution):
        """Single element array, insert after"""
        assert solution.searchInsert([5], 7) == 1

    # Additional edge case tests
    def test_two_element_array_found_first(self, solution):
        """Two element array, target found at first position"""
        assert solution.searchInsert([1, 3], 1) == 0

    def test_two_element_array_found_second(self, solution):
        """Two element array, target found at second position"""
        assert solution.searchInsert([1, 3], 3) == 1

    def test_two_element_array_insert_between(self, solution):
        """Two element array, insert between elements"""
        assert solution.searchInsert([1, 3], 2) == 1

    def test_two_element_array_insert_before(self, solution):
        """Two element array, insert before first"""
        assert solution.searchInsert([1, 3], 0) == 0

    def test_two_element_array_insert_after(self, solution):
        """Two element array, insert after last"""
        assert solution.searchInsert([1, 3], 4) == 2

    def test_target_at_first_position(self, solution):
        """Target exists at first position"""
        assert solution.searchInsert([2, 4, 6, 8, 10], 2) == 0

    def test_target_at_last_position(self, solution):
        """Target exists at last position"""
        assert solution.searchInsert([2, 4, 6, 8, 10], 10) == 4

    def test_target_smaller_than_all(self, solution):
        """Target smaller than all elements"""
        assert solution.searchInsert([10, 20, 30, 40], 5) == 0

    def test_target_larger_than_all(self, solution):
        """Target larger than all elements"""
        assert solution.searchInsert([10, 20, 30, 40], 50) == 4

    def test_target_between_elements(self, solution):
        """Target between elements (not in array)"""
        assert solution.searchInsert([1, 3, 5, 7, 9], 4) == 2
        assert solution.searchInsert([1, 3, 5, 7, 9], 6) == 3
        assert solution.searchInsert([1, 3, 5, 7, 9], 8) == 4

    def test_negative_numbers(self, solution):
        """Array with negative numbers"""
        assert solution.searchInsert([-10, -5, 0, 5, 10], -5) == 1
        assert solution.searchInsert([-10, -5, 0, 5, 10], -7) == 1
        assert solution.searchInsert([-10, -5, 0, 5, 10], -15) == 0
        assert solution.searchInsert([-10, -5, 0, 5, 10], 15) == 5

    def test_all_negative_numbers(self, solution):
        """Array with all negative numbers"""
        assert solution.searchInsert([-100, -50, -25, -10, -1], -25) == 2
        assert solution.searchInsert([-100, -50, -25, -10, -1], -30) == 2
        assert solution.searchInsert([-100, -50, -25, -10, -1], 0) == 5

    def test_large_array(self, solution):
        """Large array with many elements"""
        nums = list(range(0, 10000, 2))  # Even numbers from 0 to 9998
        assert solution.searchInsert(nums, 5000) == 2500
        assert solution.searchInsert(nums, 5001) == 2501  # Insert between 5000 and 5002
        assert solution.searchInsert(nums, -1) == 0
        assert solution.searchInsert(nums, 10000) == 5000

    def test_consecutive_elements(self, solution):
        """Array with consecutive elements"""
        assert solution.searchInsert([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 4
        assert solution.searchInsert([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1) == 0
        assert solution.searchInsert([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10) == 9

    def test_sparse_array(self, solution):
        """Array with sparse elements (large gaps)"""
        assert solution.searchInsert([1, 100, 1000, 10000], 500) == 2
        assert solution.searchInsert([1, 100, 1000, 10000], 1) == 0
        assert solution.searchInsert([1, 100, 1000, 10000], 10000) == 3

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
