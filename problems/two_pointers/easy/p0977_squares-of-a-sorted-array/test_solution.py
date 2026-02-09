"""
Tests for LeetCode Problem #977: Squares of a Sorted Array
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestSquaresOfASortedArray:
    """Test cases for Squares of a Sorted Array problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums = [-4, -1, 0, 3, 10]
        expected = [0, 1, 9, 16, 100]
        result = solution.sortedSquares(nums)
        assert result == expected

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        nums = [-7, -3, 2, 3, 11]
        expected = [4, 9, 9, 49, 121]
        result = solution.sortedSquares(nums)
        assert result == expected

    def test_edge_case_single_element(self, solution):
        """Test with single element array"""
        nums = [5]
        expected = [25]
        result = solution.sortedSquares(nums)
        assert result == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
