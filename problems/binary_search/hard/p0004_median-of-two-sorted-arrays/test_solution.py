"""
Tests for LeetCode Problem #4: Median of Two Sorted Arrays
"""

import pytest
from .solution import Solution, PROBLEM_METADATA




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


    def test_edge_case_empty(self, solution):
        """Test with empty/minimal input"""
        # TODO: Implement edge case test
        pass


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
