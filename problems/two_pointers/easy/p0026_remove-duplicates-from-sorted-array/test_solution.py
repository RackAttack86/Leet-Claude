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

    def test_two_elements_same(self, solution):
        """Test with two same elements"""
        nums = [2, 2]
        k = solution.removeDuplicates(nums)
        assert k == 1
        assert nums[:k] == [2]

    def test_two_elements_different(self, solution):
        """Test with two different elements"""
        nums = [1, 2]
        k = solution.removeDuplicates(nums)
        assert k == 2
        assert nums[:k] == [1, 2]

    def test_negative_numbers(self, solution):
        """Test with negative numbers"""
        nums = [-5, -5, -3, -1, -1, 0, 0, 2]
        k = solution.removeDuplicates(nums)
        assert k == 5
        assert nums[:k] == [-5, -3, -1, 0, 2]

    def test_duplicates_at_start(self, solution):
        """Test with duplicates at the start"""
        nums = [1, 1, 1, 2, 3, 4]
        k = solution.removeDuplicates(nums)
        assert k == 4
        assert nums[:k] == [1, 2, 3, 4]

    def test_duplicates_at_end(self, solution):
        """Test with duplicates at the end"""
        nums = [1, 2, 3, 4, 4, 4]
        k = solution.removeDuplicates(nums)
        assert k == 4
        assert nums[:k] == [1, 2, 3, 4]

    def test_alternating_duplicates(self, solution):
        """Test with alternating duplicates"""
        nums = [1, 1, 2, 2, 3, 3]
        k = solution.removeDuplicates(nums)
        assert k == 3
        assert nums[:k] == [1, 2, 3]

    def test_large_range(self, solution):
        """Test with large range of numbers"""
        nums = [-100, -50, 0, 0, 0, 50, 100]
        k = solution.removeDuplicates(nums)
        assert k == 5
        assert nums[:k] == [-100, -50, 0, 50, 100]

    # Parametrized tests
    @pytest.mark.parametrize("nums,expected_k,expected_result", [
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
        ([1], 1, [1]),
        ([1, 1], 1, [1]),
        ([1, 2], 2, [1, 2]),
        ([-1, 0, 0, 0, 1], 3, [-1, 0, 1]),
    ])
    def test_parametrized(self, solution, nums, expected_k, expected_result):
        """Parametrized test for various inputs"""
        k = solution.removeDuplicates(nums)
        assert k == expected_k
        assert nums[:k] == expected_result

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
