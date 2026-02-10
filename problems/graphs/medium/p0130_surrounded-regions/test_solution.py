"""
Tests for LeetCode Problem #130: Surrounded Regions
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA




class TestSurroundedRegions:
    """Test cases for Surrounded Regions problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
        solution.solve(board)
        expected = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
        assert board == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        board = [["X"]]
        solution.solve(board)
        expected = [["X"]]
        assert board == expected


    def test_all_o_border(self, solution):
        """Test with O's on all borders - none should be captured"""
        board = [["O","O","O"],["O","O","O"],["O","O","O"]]
        solution.solve(board)
        expected = [["O","O","O"],["O","O","O"],["O","O","O"]]
        assert board == expected


    def test_surrounded_o(self, solution):
        """Test with single surrounded O"""
        board = [["X","X","X"],["X","O","X"],["X","X","X"]]
        solution.solve(board)
        expected = [["X","X","X"],["X","X","X"],["X","X","X"]]
        assert board == expected


    # Edge cases
    def test_single_cell_x(self, solution):
        """Single cell with X - no change needed"""
        board = [["X"]]
        solution.solve(board)
        assert board == [["X"]]

    def test_single_cell_o(self, solution):
        """Single cell with O - on border so not captured"""
        board = [["O"]]
        solution.solve(board)
        assert board == [["O"]]

    def test_all_x(self, solution):
        """Board with all X - no change"""
        board = [["X","X","X"],["X","X","X"],["X","X","X"]]
        solution.solve(board)
        assert board == [["X","X","X"],["X","X","X"],["X","X","X"]]

    def test_single_row(self, solution):
        """Single row - all on border, nothing captured"""
        board = [["X","O","O","X","O"]]
        solution.solve(board)
        assert board == [["X","O","O","X","O"]]

    def test_single_column(self, solution):
        """Single column - all on border, nothing captured"""
        board = [["X"],["O"],["O"],["X"],["O"]]
        solution.solve(board)
        assert board == [["X"],["O"],["O"],["X"],["O"]]

    def test_two_by_two_all_o(self, solution):
        """2x2 board with all O - all on border, not captured"""
        board = [["O","O"],["O","O"]]
        solution.solve(board)
        assert board == [["O","O"],["O","O"]]

    def test_two_by_two_all_x(self, solution):
        """2x2 board with all X - no change"""
        board = [["X","X"],["X","X"]]
        solution.solve(board)
        assert board == [["X","X"],["X","X"]]

    def test_o_connected_to_corner(self, solution):
        """O's connected to corner should not be captured"""
        board = [["O","X","X"],["O","O","X"],["X","X","X"]]
        solution.solve(board)
        expected = [["O","X","X"],["O","O","X"],["X","X","X"]]
        assert board == expected

    def test_multiple_surrounded_regions(self, solution):
        """Multiple separate surrounded regions"""
        board = [
            ["X","X","X","X","X"],
            ["X","O","X","O","X"],
            ["X","X","X","X","X"]
        ]
        solution.solve(board)
        expected = [
            ["X","X","X","X","X"],
            ["X","X","X","X","X"],
            ["X","X","X","X","X"]
        ]
        assert board == expected

    def test_large_surrounded_region(self, solution):
        """Large connected region that is surrounded"""
        board = [
            ["X","X","X","X","X"],
            ["X","O","O","O","X"],
            ["X","O","O","O","X"],
            ["X","O","O","O","X"],
            ["X","X","X","X","X"]
        ]
        solution.solve(board)
        expected = [
            ["X","X","X","X","X"],
            ["X","X","X","X","X"],
            ["X","X","X","X","X"],
            ["X","X","X","X","X"],
            ["X","X","X","X","X"]
        ]
        assert board == expected

    def test_empty_board(self, solution):
        """Empty board - should not crash"""
        board = []
        solution.solve(board)
        assert board == []

    def test_complex_pattern(self, solution):
        """Complex pattern with mix of captured and safe O's"""
        board = [
            ["X","O","X","X"],
            ["O","X","O","X"],
            ["X","O","X","O"],
            ["X","X","O","X"]
        ]
        solution.solve(board)
        # O's on border and connected to border stay O, others become X
        expected = [
            ["X","O","X","X"],
            ["O","X","X","X"],
            ["X","X","X","O"],
            ["X","X","O","X"]
        ]
        assert board == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
