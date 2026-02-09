"""
Tests for LeetCode Problem #496: Next Greater Element I
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestNextGreaterElementI:
    """Test cases for Next Greater Element I problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1: nums1=[4,1,2], nums2=[1,3,4,2]"""
        assert solution.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]

    def test_example_2(self, solution):
        """Example 2: nums1=[2,4], nums2=[1,2,3,4]"""
        assert solution.nextGreaterElement([2, 4], [1, 2, 3, 4]) == [3, -1]

    def test_single_element(self, solution):
        """Single element"""
        assert solution.nextGreaterElement([1], [1]) == [-1]

    def test_all_have_greater(self, solution):
        """All elements have next greater"""
        assert solution.nextGreaterElement([1, 2], [1, 2, 3, 4]) == [2, 3]

    def test_none_have_greater(self, solution):
        """No elements have next greater"""
        assert solution.nextGreaterElement([3, 4], [4, 3, 2, 1]) == [-1, -1]

    def test_larger_input(self, solution):
        """Larger input"""
        assert solution.nextGreaterElement([1, 3, 5], [1, 2, 3, 4, 5, 6]) == [2, 4, 6]

    # Additional edge case tests
    def test_all_same_values(self, solution):
        """All same values in nums2 - no greater element possible"""
        # Note: According to constraints, all integers are unique, so this test
        # should use unique values but test when no greater exists
        assert solution.nextGreaterElement([5], [5]) == [-1]

    def test_descending_order(self, solution):
        """Descending order - no element has a greater element to its right"""
        assert solution.nextGreaterElement([5, 4, 3], [5, 4, 3, 2, 1]) == [-1, -1, -1]
        assert solution.nextGreaterElement([4, 3, 2, 1], [4, 3, 2, 1]) == [-1, -1, -1, -1]

    def test_ascending_order(self, solution):
        """Ascending order - every element except last has a greater element"""
        assert solution.nextGreaterElement([1, 2, 3], [1, 2, 3, 4, 5]) == [2, 3, 4]
        assert solution.nextGreaterElement([1, 2, 3, 4], [1, 2, 3, 4, 5]) == [2, 3, 4, 5]

    def test_last_element_in_nums2(self, solution):
        """Query for last element in nums2 - no greater element"""
        assert solution.nextGreaterElement([5], [1, 2, 3, 4, 5]) == [-1]

    def test_first_element_in_nums2(self, solution):
        """Query for first element in nums2"""
        assert solution.nextGreaterElement([1], [1, 2, 3, 4, 5]) == [2]

    def test_mixed_results(self, solution):
        """Mix of elements with and without greater elements"""
        assert solution.nextGreaterElement([2, 6, 1, 8], [1, 2, 3, 6, 4, 8, 5]) == [3, 8, 2, -1]

    def test_nums1_equals_nums2(self, solution):
        """nums1 is same as nums2"""
        assert solution.nextGreaterElement([1, 2, 3, 4], [1, 2, 3, 4]) == [2, 3, 4, -1]

    def test_peak_in_middle(self, solution):
        """Peak value in the middle of nums2"""
        assert solution.nextGreaterElement([1, 5, 3], [1, 2, 5, 3, 4]) == [2, -1, 4]

    def test_two_elements(self, solution):
        """Two element arrays"""
        assert solution.nextGreaterElement([1, 2], [1, 2]) == [2, -1]
        assert solution.nextGreaterElement([2, 1], [2, 1]) == [-1, -1]
        assert solution.nextGreaterElement([1], [1, 2]) == [2]
        assert solution.nextGreaterElement([2], [1, 2]) == [-1]

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
