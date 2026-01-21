"""
Tests for LeetCode Problem #26: Remove Duplicates from Sorted Array
"""

import pytest
from .solution import Solution, PROBLEM_METADATA




class TestRemoveDuplicatesFromSortedArray:
    """Test cases for Remove Duplicates from Sorted Array problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums = [1,1,2]
        expected = 2, nums = [1,2,_]
        result = solution.removeDuplicates(nums)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        nums = [0,0,1,1,1,2,2,3,3,4]
        expected = 5, nums = [0,1,2,3,4,_,_,_,_,_]
        result = solution.removeDuplicates(nums)
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
