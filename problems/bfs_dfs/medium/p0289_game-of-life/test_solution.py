"""
Tests for LeetCode Problem #289: Game of Life
"""

import pytest
from .solution import Solution, PROBLEM_METADATA




class TestGameOfLife:
    """Test cases for Game of Life problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        board = [[0,1,0]
        expected = [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
        result = solution.gameOfLife(board)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        board = [[1,1]
        expected = [[1,1],[1,1]]
        result = solution.gameOfLife(board)
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
