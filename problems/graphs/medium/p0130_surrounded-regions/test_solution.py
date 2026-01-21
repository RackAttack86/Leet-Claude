"""
Tests for LeetCode Problem #130: Surrounded Regions
"""

import pytest
from .solution import Solution, PROBLEM_METADATA




class TestSurroundedRegions:
    """Test cases for Surrounded Regions problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        board = [["X","X","X","X"]
        expected = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
        result = solution.solve(board)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        board = [["X"]
        expected = [["X"]]
        result = solution.solve(board)
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
