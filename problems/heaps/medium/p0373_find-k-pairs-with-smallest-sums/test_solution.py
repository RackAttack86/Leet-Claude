"""
Tests for LeetCode Problem #373: Find K Pairs with Smallest Sums
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestFindKPairsWithSmallestSums:
    """Test cases for Find K Pairs with Smallest Sums problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums1 = [1, 7, 11]
        nums2 = [2, 4, 6]
        k = 3
        result = solution.kSmallestPairs(nums1, nums2, k)
        # Sort each pair and the result for comparison
        result_sorted = sorted([sorted(pair) for pair in result])
        expected_sorted = sorted([[1, 2], [1, 4], [1, 6]])
        assert result_sorted == expected_sorted

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        nums1 = [1, 1, 2]
        nums2 = [1, 2, 3]
        k = 2
        result = solution.kSmallestPairs(nums1, nums2, k)
        # Both pairs should sum to 2 (1+1)
        assert len(result) == 2
        for pair in result:
            assert sum(pair) == 2

    # Edge cases
    def test_single_elements(self, solution):
        """Single element in each array"""
        nums1 = [1]
        nums2 = [2]
        k = 1
        result = solution.kSmallestPairs(nums1, nums2, k)
        assert result == [[1, 2]]

    def test_k_larger_than_possible(self, solution):
        """k larger than possible pairs"""
        nums1 = [1, 2]
        nums2 = [3]
        k = 5
        result = solution.kSmallestPairs(nums1, nums2, k)
        assert len(result) == 2  # Only 2 pairs possible

    def test_same_elements(self, solution):
        """Arrays with same elements"""
        nums1 = [1, 1, 1]
        nums2 = [1, 1, 1]
        k = 3
        result = solution.kSmallestPairs(nums1, nums2, k)
        assert len(result) == 3
        for pair in result:
            assert sum(pair) == 2

    def test_negative_numbers(self, solution):
        """Arrays with negative numbers"""
        nums1 = [-3, -1, 2]
        nums2 = [-2, 0, 4]
        k = 3
        result = solution.kSmallestPairs(nums1, nums2, k)
        # Smallest sums: -3+-2=-5, -3+0=-3, -1+-2=-3
        sums = sorted([sum(pair) for pair in result])
        assert sums == [-5, -3, -3]

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
