"""
Tests for LeetCode Problem #643: Maximum Average Subarray I
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestMaximumAverageSubarrayI:
    """Test cases for Maximum Average Subarray I problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1: nums=[1,12,-5,-6,50,3], k=4"""
        result = solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4)
        assert abs(result - 12.75) < 1e-5

    def test_example_2(self, solution):
        """Example 2: single element"""
        result = solution.findMaxAverage([5], 1)
        assert abs(result - 5.0) < 1e-5

    def test_entire_array(self, solution):
        """k equals array length"""
        result = solution.findMaxAverage([1, 2, 3, 4], 4)
        assert abs(result - 2.5) < 1e-5

    def test_negative_numbers(self, solution):
        """Array with negative numbers"""
        result = solution.findMaxAverage([-1, -2, -3, -4], 2)
        assert abs(result - (-1.5)) < 1e-5

    def test_k_equals_1(self, solution):
        """k equals 1, should find max element"""
        result = solution.findMaxAverage([1, 5, 3, 2, 8], 1)
        assert abs(result - 8.0) < 1e-5

    # Additional edge case tests
    def test_all_same_values(self, solution):
        """All same values"""
        result = solution.findMaxAverage([5, 5, 5, 5, 5], 3)
        assert abs(result - 5.0) < 1e-5

    def test_k_equals_array_length(self, solution):
        """k equals array length - use entire array"""
        result = solution.findMaxAverage([1, 2, 3, 4, 5], 5)
        assert abs(result - 3.0) < 1e-5

    def test_all_negative_values(self, solution):
        """All negative values"""
        result = solution.findMaxAverage([-5, -10, -3, -8, -2], 2)
        assert abs(result - (-2.5)) < 1e-5

    def test_mixed_positive_negative(self, solution):
        """Mixed positive and negative values"""
        result = solution.findMaxAverage([-1, 5, -3, 10, -2, 8], 2)
        assert abs(result - 4.0) < 1e-5  # max is (10 + -2) / 2 = 4 or (-2 + 8) / 2 = 3

    def test_single_element_array(self, solution):
        """Single element array with k=1"""
        result = solution.findMaxAverage([7], 1)
        assert abs(result - 7.0) < 1e-5

    def test_two_elements_k_2(self, solution):
        """Two elements with k=2"""
        result = solution.findMaxAverage([3, 7], 2)
        assert abs(result - 5.0) < 1e-5

    def test_maximum_at_start(self, solution):
        """Maximum average subarray at start"""
        result = solution.findMaxAverage([10, 10, 1, 1, 1], 2)
        assert abs(result - 10.0) < 1e-5

    def test_maximum_at_end(self, solution):
        """Maximum average subarray at end"""
        result = solution.findMaxAverage([1, 1, 1, 10, 10], 2)
        assert abs(result - 10.0) < 1e-5

    def test_maximum_in_middle(self, solution):
        """Maximum average subarray in middle"""
        result = solution.findMaxAverage([1, 1, 10, 10, 1, 1], 2)
        assert abs(result - 10.0) < 1e-5

    def test_large_values(self, solution):
        """Large values"""
        result = solution.findMaxAverage([10000, 10000, 10000], 2)
        assert abs(result - 10000.0) < 1e-5

    def test_decimal_average(self, solution):
        """Average results in decimal"""
        result = solution.findMaxAverage([1, 2, 3], 2)
        assert abs(result - 2.5) < 1e-5

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
