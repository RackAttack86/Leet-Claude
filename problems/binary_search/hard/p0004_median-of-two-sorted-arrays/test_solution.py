"""
Tests for LeetCode Problem #4: Median of Two Sorted Arrays
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA




class TestMedianOfTwoSortedArrays:
    """Test cases for Median of Two Sorted Arrays problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums1 = [1,3]
        nums2 = [2]
        expected = 2.00000
        result = solution.findMedianSortedArrays(nums1, nums2)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        nums1 = [1,2]
        nums2 = [3,4]
        expected = 2.50000
        result = solution.findMedianSortedArrays(nums1, nums2)
        assert result == expected


    def test_one_empty_array(self, solution):
        """Edge case: one array is empty"""
        nums1 = []
        nums2 = [1]
        expected = 1.0
        result = solution.findMedianSortedArrays(nums1, nums2)
        assert result == expected

    def test_other_empty_array(self, solution):
        """Edge case: first array is empty with multiple elements in second"""
        nums1 = []
        nums2 = [1, 2, 3, 4, 5]
        expected = 3.0
        result = solution.findMedianSortedArrays(nums1, nums2)
        assert result == expected

    def test_single_elements(self, solution):
        """Edge case: single element in each array"""
        nums1 = [1]
        nums2 = [2]
        expected = 1.5
        result = solution.findMedianSortedArrays(nums1, nums2)
        assert result == expected

    def test_all_same_values(self, solution):
        """Edge case: all elements have the same value"""
        nums1 = [1, 1, 1]
        nums2 = [1, 1, 1]
        expected = 1.0
        result = solution.findMedianSortedArrays(nums1, nums2)
        assert result == expected

    def test_no_overlap_first_smaller(self, solution):
        """Edge case: arrays don't overlap, first is all smaller"""
        nums1 = [1, 2]
        nums2 = [3, 4, 5, 6]
        expected = 3.5
        result = solution.findMedianSortedArrays(nums1, nums2)
        assert result == expected

    def test_no_overlap_second_smaller(self, solution):
        """Edge case: arrays don't overlap, second is all smaller"""
        nums1 = [5, 6, 7]
        nums2 = [1, 2]
        expected = 5.0
        result = solution.findMedianSortedArrays(nums1, nums2)
        assert result == expected

    def test_negative_numbers(self, solution):
        """Edge case: arrays with negative numbers"""
        nums1 = [-5, -3, -1]
        nums2 = [-2, 0, 2]
        expected = -1.5
        result = solution.findMedianSortedArrays(nums1, nums2)
        assert result == expected

    def test_large_difference_in_sizes(self, solution):
        """Edge case: one array much larger than other"""
        nums1 = [1]
        nums2 = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = 5.5
        result = solution.findMedianSortedArrays(nums1, nums2)
        assert result == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
