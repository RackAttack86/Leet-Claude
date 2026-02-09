"""
Tests for LeetCode Problem #74: Search a 2D Matrix
"""

import pytest
from solution import Solution, PROBLEM_METADATA




class TestSearchA2dMatrix:
    """Test cases for Search a 2D Matrix problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        target = 3
        expected = True
        result = solution.searchMatrix(matrix, target)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        target = 13
        expected = False
        result = solution.searchMatrix(matrix, target)
        assert result == expected


    def test_edge_case_empty_matrix(self, solution):
        """Test with empty matrix"""
        matrix = []
        target = 1
        expected = False
        result = solution.searchMatrix(matrix, target)
        assert result == expected

    def test_edge_case_single_element_found(self, solution):
        """Test with single element matrix, target found"""
        matrix = [[5]]
        target = 5
        expected = True
        result = solution.searchMatrix(matrix, target)
        assert result == expected

    def test_edge_case_single_element_not_found(self, solution):
        """Test with single element matrix, target not found"""
        matrix = [[5]]
        target = 3
        expected = False
        result = solution.searchMatrix(matrix, target)
        assert result == expected


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
