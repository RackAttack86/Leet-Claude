"""
Tests for LeetCode Problem #73: Set Matrix Zeroes
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA




class TestSetMatrixZeroes:
    """Test cases for Set Matrix Zeroes problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        matrix = [[1,1,1],[1,0,1],[1,1,1]]
        expected = [[1,0,1],[0,0,0],[1,0,1]]
        solution.setZeroes(matrix)
        assert matrix == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
        expected = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
        solution.setZeroes(matrix)
        assert matrix == expected


    def test_edge_case_no_zeros(self, solution):
        """Test with matrix containing no zeros"""
        matrix = [[1, 2], [3, 4]]
        expected = [[1, 2], [3, 4]]  # No change when no zeros present
        solution.setZeroes(matrix)
        assert matrix == expected


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
