"""
Tests for LeetCode Problem #33: Search in Rotated Sorted Array
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestSearchInRotatedSortedArray:
    """Test cases for Search in Rotated Sorted Array problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        assert solution.search(nums, target) == 4

    def test_example_2(self, solution):
        """Example 2 from problem description - target not found"""
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        assert solution.search(nums, target) == -1

    # Edge cases
    def test_not_rotated(self, solution):
        """Array is not rotated (sorted in ascending order)"""
        nums = [1, 2, 3, 4, 5, 6, 7]
        assert solution.search(nums, 3) == 2
        assert solution.search(nums, 1) == 0
        assert solution.search(nums, 7) == 6

    def test_rotated_by_1(self, solution):
        """Array rotated by 1 position"""
        nums = [7, 1, 2, 3, 4, 5, 6]
        assert solution.search(nums, 7) == 0
        assert solution.search(nums, 1) == 1
        assert solution.search(nums, 6) == 6

    def test_target_at_pivot(self, solution):
        """Target is at the pivot point (minimum element)"""
        nums = [4, 5, 6, 7, 0, 1, 2]
        assert solution.search(nums, 0) == 4  # 0 is the pivot

    def test_target_at_pivot_2(self, solution):
        """Target is at the pivot point - different array"""
        nums = [6, 7, 1, 2, 3, 4, 5]
        assert solution.search(nums, 1) == 2  # 1 is the pivot

    def test_single_element_found(self, solution):
        """Single element array - target found"""
        nums = [5]
        assert solution.search(nums, 5) == 0

    def test_single_element_not_found(self, solution):
        """Single element array - target not found"""
        nums = [5]
        assert solution.search(nums, 3) == -1

    def test_two_elements(self, solution):
        """Two element array"""
        nums = [2, 1]  # Rotated
        assert solution.search(nums, 1) == 1
        assert solution.search(nums, 2) == 0
        assert solution.search(nums, 3) == -1

    def test_target_at_start(self, solution):
        """Target at start of rotated array"""
        nums = [4, 5, 6, 7, 0, 1, 2]
        assert solution.search(nums, 4) == 0

    def test_target_at_end(self, solution):
        """Target at end of rotated array"""
        nums = [4, 5, 6, 7, 0, 1, 2]
        assert solution.search(nums, 2) == 6

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
