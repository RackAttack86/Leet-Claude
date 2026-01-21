"""
Tests for LeetCode Problem #80: Remove Duplicates from Sorted Array II
"""

import pytest
from solution import Solution, PROBLEM_METADATA




class TestRemoveDuplicatesFromSortedArrayIi:
    """Test cases for Remove Duplicates from Sorted Array II problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums = [1, 1, 1, 2, 2, 3]
        k = solution.removeDuplicates(nums)
        assert k == 5
        assert nums[:k] == [1, 1, 2, 2, 3]

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        k = solution.removeDuplicates(nums)
        assert k == 7
        assert nums[:k] == [0, 0, 1, 1, 2, 3, 3]

    def test_edge_case_single_element(self, solution):
        """Test with single element array"""
        nums = [1]
        k = solution.removeDuplicates(nums)
        assert k == 1
        assert nums[:k] == [1]

    def test_edge_case_two_same(self, solution):
        """Test with two same elements"""
        nums = [1, 1]
        k = solution.removeDuplicates(nums)
        assert k == 2
        assert nums[:k] == [1, 1]

    def test_edge_case_three_same(self, solution):
        """Test with three same elements - should keep only two"""
        nums = [1, 1, 1]
        k = solution.removeDuplicates(nums)
        assert k == 2
        assert nums[:k] == [1, 1]

    def test_no_duplicates(self, solution):
        """Test with no duplicates"""
        nums = [1, 2, 3, 4, 5]
        k = solution.removeDuplicates(nums)
        assert k == 5
        assert nums[:k] == [1, 2, 3, 4, 5]

    def test_all_duplicates_twice(self, solution):
        """Test where all elements appear exactly twice"""
        nums = [1, 1, 2, 2, 3, 3]
        k = solution.removeDuplicates(nums)
        assert k == 6
        assert nums[:k] == [1, 1, 2, 2, 3, 3]


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
