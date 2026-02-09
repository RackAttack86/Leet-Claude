"""
Tests for LeetCode Problem #347: Top K Frequent Elements
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestTopKFrequentElements:
    """Test cases for Top K Frequent Elements problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        result = solution.topKFrequent(nums, k)
        assert sorted(result) == [1, 2]

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        nums = [1]
        k = 1
        assert solution.topKFrequent(nums, k) == [1]

    # Edge cases
    def test_all_same_frequency(self, solution):
        """All elements have same frequency"""
        nums = [1, 2, 3, 4]
        k = 2
        result = solution.topKFrequent(nums, k)
        assert len(result) == 2
        assert all(x in [1, 2, 3, 4] for x in result)

    def test_k_equals_unique_elements(self, solution):
        """k equals number of unique elements"""
        nums = [1, 1, 2, 2, 3, 3]
        k = 3
        assert sorted(solution.topKFrequent(nums, k)) == [1, 2, 3]

    def test_negative_numbers(self, solution):
        """Array with negative numbers"""
        nums = [-1, -1, -2, -2, -2, -3]
        k = 2
        result = solution.topKFrequent(nums, k)
        assert sorted(result) == [-2, -1]

    def test_large_frequency_difference(self, solution):
        """Large difference in frequencies"""
        nums = [1] * 100 + [2] * 10 + [3]
        k = 2
        assert sorted(solution.topKFrequent(nums, k)) == [1, 2]

    def test_all_same_frequency_k_equals_n(self, solution):
        """All elements have same frequency and k equals unique count"""
        nums = [1, 2, 3, 4, 5]
        k = 5
        result = solution.topKFrequent(nums, k)
        assert sorted(result) == [1, 2, 3, 4, 5]

    def test_all_same_frequency_partial(self, solution):
        """All elements have same frequency, k < unique count"""
        nums = [1, 1, 2, 2, 3, 3, 4, 4]
        k = 2
        result = solution.topKFrequent(nums, k)
        assert len(result) == 2
        assert all(x in [1, 2, 3, 4] for x in result)

    def test_single_element_repeated(self, solution):
        """Single element repeated multiple times"""
        nums = [5, 5, 5, 5, 5]
        k = 1
        assert solution.topKFrequent(nums, k) == [5]

    def test_k_equals_one(self, solution):
        """k equals 1 - most frequent only"""
        nums = [1, 1, 1, 2, 2, 3, 3, 3, 3]
        k = 1
        assert solution.topKFrequent(nums, k) == [3]

    def test_two_elements_tied_frequency(self, solution):
        """Two elements with same top frequency"""
        nums = [1, 1, 2, 2]
        k = 2
        result = solution.topKFrequent(nums, k)
        assert sorted(result) == [1, 2]

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
