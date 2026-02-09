"""
Tests for LeetCode Problem #15: 3Sum
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class Test3sum:
    """Test cases for 3Sum problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, -1, 2], [-1, 0, 1]]
        result = solution.threeSum(nums)
        assert sorted(result) == sorted(expected)

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        nums = [0, 1, 1]
        expected = []
        result = solution.threeSum(nums)
        assert result == expected

    # Edge cases
    def test_all_zeros(self, solution):
        """All elements are zero"""
        nums = [0, 0, 0]
        expected = [[0, 0, 0]]
        result = solution.threeSum(nums)
        assert result == expected

    def test_no_triplets(self, solution):
        """No valid triplets exist"""
        nums = [1, 2, 3]
        expected = []
        result = solution.threeSum(nums)
        assert result == expected

    def test_multiple_duplicates(self, solution):
        """Array with many duplicate values"""
        nums = [-2, 0, 0, 2, 2]
        expected = [[-2, 0, 2]]
        result = solution.threeSum(nums)
        assert result == expected

    def test_minimum_length(self, solution):
        """Array with exactly 3 elements"""
        nums = [-1, 0, 1]
        expected = [[-1, 0, 1]]
        result = solution.threeSum(nums)
        assert result == expected

    def test_all_negative(self, solution):
        """All negative numbers"""
        nums = [-5, -4, -3, -2, -1]
        expected = []
        result = solution.threeSum(nums)
        assert result == expected

    def test_all_positive(self, solution):
        """All positive numbers"""
        nums = [1, 2, 3, 4, 5]
        expected = []
        result = solution.threeSum(nums)
        assert result == expected

    def test_large_duplicates(self, solution):
        """Multiple zeros with duplicates"""
        nums = [0, 0, 0, 0]
        expected = [[0, 0, 0]]
        result = solution.threeSum(nums)
        assert result == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
