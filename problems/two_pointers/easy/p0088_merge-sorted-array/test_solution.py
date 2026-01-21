"""
Tests for LeetCode Problem #88: Merge Sorted Array
"""

import pytest
from solution import Solution, PROBLEM_METADATA




class TestMergeSortedArray:
    """Test cases for Merge Sorted Array problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums1 = [1,2,3,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3
        expected = [1,2,2,3,5,6]
        solution.merge(nums1, m, nums2, n)
        assert nums1 == expected

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        expected = [1]
        solution.merge(nums1, m, nums2, n)
        assert nums1 == expected

    def test_example_3(self, solution):
        """Example 3 from problem description"""
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        expected = [1]
        solution.merge(nums1, m, nums2, n)
        assert nums1 == expected


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
