"""
Tests for LeetCode Problem #48: Rotate Image
"""

import pytest
from .solution import Solution, PROBLEM_METADATA




class TestRotateImage:
    """Test cases for Rotate Image problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        matrix = [[1,2,3]
        expected = [[7,4,1],[8,5,2],[9,6,3]]
        result = solution.rotate(matrix)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        matrix = [[5,1,9,11]
        expected = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
        result = solution.rotate(matrix)
        assert result == expected


    def test_edge_case_empty(self, solution):
        """Test with empty/minimal input"""
        # TODO: Implement edge case test
        pass


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
