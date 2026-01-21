"""
Tests for LeetCode Problem #34: Find First and Last Position of Element in Sorted Array
"""

import pytest
from .solution import Solution, PROBLEM_METADATA




class TestFindFirstAndLastPositionOfElementInSortedArray:
    """Test cases for Find First and Last Position of Element in Sorted Array problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums = [5,7,7,8,8,10]
        target = 8
        expected = [3,4]
        result = solution.searchRange(nums, target)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        nums = [5,7,7,8,8,10]
        target = 6
        expected = [-1,-1]
        result = solution.searchRange(nums, target)
        assert result == expected


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        nums = []
        target = 0
        expected = [-1,-1]
        result = solution.searchRange(nums, target)
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
