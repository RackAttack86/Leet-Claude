"""
Tests for LeetCode Problem #34: Find First and Last Position of Element in Sorted Array
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestFindFirstAndLastPositionOfElementInSortedArray:
    """Test cases for Find First and Last Position of Element in Sorted Array problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums = [5, 7, 7, 8, 8, 10]
        target = 8
        expected = [3, 4]
        result = solution.searchRange(nums, target)
        assert result == expected

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        nums = [5, 7, 7, 8, 8, 10]
        target = 6
        expected = [-1, -1]
        result = solution.searchRange(nums, target)
        assert result == expected

    def test_example_3(self, solution):
        """Example 3 from problem description - empty array"""
        nums = []
        target = 0
        expected = [-1, -1]
        result = solution.searchRange(nums, target)
        assert result == expected

    # Edge cases
    def test_all_same_elements(self, solution):
        """Array with all same elements"""
        nums = [8, 8, 8, 8, 8]
        target = 8
        expected = [0, 4]
        assert solution.searchRange(nums, target) == expected

    def test_all_same_elements_long(self, solution):
        """Longer array with all same elements"""
        nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        target = 5
        expected = [0, 9]
        assert solution.searchRange(nums, target) == expected

    def test_element_not_found_smaller(self, solution):
        """Target smaller than all elements"""
        nums = [5, 7, 8, 10, 12]
        target = 3
        expected = [-1, -1]
        assert solution.searchRange(nums, target) == expected

    def test_element_not_found_larger(self, solution):
        """Target larger than all elements"""
        nums = [5, 7, 8, 10, 12]
        target = 15
        expected = [-1, -1]
        assert solution.searchRange(nums, target) == expected

    def test_element_not_found_in_middle(self, solution):
        """Target falls between existing elements"""
        nums = [1, 3, 5, 7, 9]
        target = 4
        expected = [-1, -1]
        assert solution.searchRange(nums, target) == expected

    def test_single_element_found(self, solution):
        """Single element array - target found"""
        nums = [5]
        target = 5
        expected = [0, 0]
        assert solution.searchRange(nums, target) == expected

    def test_single_element_not_found(self, solution):
        """Single element array - target not found"""
        nums = [5]
        target = 3
        expected = [-1, -1]
        assert solution.searchRange(nums, target) == expected

    def test_target_only_at_start(self, solution):
        """Target appears only at start"""
        nums = [1, 2, 3, 4, 5]
        target = 1
        expected = [0, 0]
        assert solution.searchRange(nums, target) == expected

    def test_target_only_at_end(self, solution):
        """Target appears only at end"""
        nums = [1, 2, 3, 4, 5]
        target = 5
        expected = [4, 4]
        assert solution.searchRange(nums, target) == expected

    def test_target_range_at_start(self, solution):
        """Target range at beginning of array"""
        nums = [1, 1, 1, 2, 3, 4, 5]
        target = 1
        expected = [0, 2]
        assert solution.searchRange(nums, target) == expected

    def test_target_range_at_end(self, solution):
        """Target range at end of array"""
        nums = [1, 2, 3, 4, 5, 5, 5]
        target = 5
        expected = [4, 6]
        assert solution.searchRange(nums, target) == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
