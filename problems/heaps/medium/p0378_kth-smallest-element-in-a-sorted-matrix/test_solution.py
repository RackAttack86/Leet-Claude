"""
Tests for LeetCode Problem #378: Kth Smallest Element in a Sorted Matrix
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestKthSmallestElementInASortedMatrix:
    """Test cases for Kth Smallest Element in a Sorted Matrix problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
        k = 8
        assert solution.kthSmallest(matrix, k) == 13

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        matrix = [[-5]]
        k = 1
        assert solution.kthSmallest(matrix, k) == -5

    # Edge cases
    def test_single_element(self, solution):
        """1x1 matrix"""
        matrix = [[1]]
        k = 1
        assert solution.kthSmallest(matrix, k) == 1

    def test_first_element(self, solution):
        """k = 1 (smallest element)"""
        matrix = [[1, 2], [3, 4]]
        k = 1
        assert solution.kthSmallest(matrix, k) == 1

    def test_last_element(self, solution):
        """k = n^2 (largest element)"""
        matrix = [[1, 2], [3, 4]]
        k = 4
        assert solution.kthSmallest(matrix, k) == 4

    def test_duplicates(self, solution):
        """Matrix with duplicate values"""
        matrix = [[1, 2, 2], [2, 3, 3], [3, 3, 4]]
        k = 5
        # Sorted: 1, 2, 2, 2, 3, 3, 3, 3, 4 -> 5th is 3
        assert solution.kthSmallest(matrix, k) == 3

    def test_negative_numbers(self, solution):
        """Matrix with negative numbers"""
        matrix = [[-5, -4], [-3, -2]]
        k = 3
        assert solution.kthSmallest(matrix, k) == -3

    def test_larger_matrix(self, solution):
        """Larger 4x4 matrix"""
        matrix = [
            [1, 5, 9, 13],
            [2, 6, 10, 14],
            [3, 7, 11, 15],
            [4, 8, 12, 16]
        ]
        k = 10
        # Sorted: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16
        assert solution.kthSmallest(matrix, k) == 10

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
