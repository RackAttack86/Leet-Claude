"""
Tests for LeetCode Problem #378: Kth Smallest Element in a Sorted Matrix
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
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

    def test_k_equals_one_smallest(self, solution):
        """k=1 returns the smallest element"""
        matrix = [[5, 10, 15], [20, 25, 30], [35, 40, 45]]
        k = 1
        assert solution.kthSmallest(matrix, k) == 5

    def test_k_equals_n_squared_largest(self, solution):
        """k=n*n returns the largest element"""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        k = 9
        assert solution.kthSmallest(matrix, k) == 9

    def test_all_same_values(self, solution):
        """Matrix with all identical values"""
        matrix = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
        k = 5
        assert solution.kthSmallest(matrix, k) == 5

    def test_2x2_matrix_all_k(self, solution):
        """2x2 matrix with all k values"""
        matrix = [[1, 2], [3, 4]]
        assert solution.kthSmallest(matrix, 1) == 1
        assert solution.kthSmallest(matrix, 2) == 2
        assert solution.kthSmallest(matrix, 3) == 3
        assert solution.kthSmallest(matrix, 4) == 4

    def test_matrix_with_zeros(self, solution):
        """Matrix including zero values"""
        matrix = [[0, 0, 1], [0, 1, 2], [1, 2, 3]]
        k = 4
        # Sorted: 0, 0, 0, 1, 1, 1, 2, 2, 3 -> 4th is 1
        assert solution.kthSmallest(matrix, k) == 1

    def test_large_single_row(self, solution):
        """1xn matrix (single row)"""
        matrix = [[1, 3, 5, 7, 9]]
        k = 3
        assert solution.kthSmallest(matrix, k) == 5

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
