"""
Tests for LeetCode Problem #26: Remove Duplicates from Sorted Array
"""

import pytest
from solution import Solution, PROBLEM_METADATA




class TestRemoveDuplicatesFromSortedArray:
    """Test cases for Remove Duplicates from Sorted Array problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums = [1, 1, 2]
        k = solution.removeDuplicates(nums)
        assert k == 2
        assert nums[:k] == [1, 2]

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        k = solution.removeDuplicates(nums)
        assert k == 5
        assert nums[:k] == [0, 1, 2, 3, 4]

    def test_edge_case_single_element(self, solution):
        """Test with single element array"""
        nums = [1]
        k = solution.removeDuplicates(nums)
        assert k == 1
        assert nums[:k] == [1]

    def test_edge_case_all_same(self, solution):
        """Test with all same elements"""
        nums = [5, 5, 5, 5]
        k = solution.removeDuplicates(nums)
        assert k == 1
        assert nums[:k] == [5]

    def test_no_duplicates(self, solution):
        """Test with no duplicates"""
        nums = [1, 2, 3, 4, 5]
        k = solution.removeDuplicates(nums)
        assert k == 5
        assert nums[:k] == [1, 2, 3, 4, 5]


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
