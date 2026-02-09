"""
Tests for LeetCode Problem #54: Spiral Matrix
"""

import pytest
from solution import Solution, PROBLEM_METADATA




class TestSpiralMatrix:
    """Test cases for Spiral Matrix problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        expected = [1,2,3,6,9,8,7,4,5]
        result = solution.spiralOrder(matrix)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        expected = [1,2,3,4,8,12,11,10,9,5,6,7]
        result = solution.spiralOrder(matrix)
        assert result == expected


    def test_edge_case_single_element(self, solution):
        """Test with single element matrix"""
        matrix = [[1]]
        expected = [1]
        result = solution.spiralOrder(matrix)
        assert result == expected


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
