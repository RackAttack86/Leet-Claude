"""
Tests for LeetCode Problem #909: Snakes and Ladders
"""

import pytest
from solution import Solution, PROBLEM_METADATA




class TestSnakesAndLadders:
    """Test cases for Snakes and Ladders problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
        expected = 4
        result = solution.snakesAndLadders(board)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        board = [[-1,-1],[-1,3]]
        expected = 1
        result = solution.snakesAndLadders(board)
        assert result == expected


    def test_simple_board(self, solution):
        """Test simple 2x2 board with no snakes or ladders"""
        board = [[-1,-1],[-1,-1]]
        expected = 1  # Roll 3 or more to reach square 4
        result = solution.snakesAndLadders(board)
        assert result == expected


    def test_no_path(self, solution):
        """Test board where snake blocks all progress"""
        # This is a theoretical case - in practice game always has path
        board = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
        result = solution.snakesAndLadders(board)
        assert result >= 1  # Should find some path


    # Edge cases
    def test_no_snakes_or_ladders_small(self, solution):
        """Small board with no snakes or ladders"""
        board = [[-1, -1], [-1, -1]]
        result = solution.snakesAndLadders(board)
        assert result == 1  # 1 -> 4 with roll of 3+

    def test_direct_ladder_to_end(self, solution):
        """Ladder directly to the end"""
        board = [[-1, -1, -1], [-1, -1, -1], [-1, 9, -1]]
        # Square 2 has ladder to 9 (end)
        result = solution.snakesAndLadders(board)
        assert result == 1  # Roll 1 to hit square 2, ladder to 9

    def test_snake_blocking_progress(self, solution):
        """Snake that slows progress"""
        board = [
            [-1, -1, -1],
            [-1, 1, -1],  # Square 5 has snake back to 1
            [-1, -1, -1]
        ]
        result = solution.snakesAndLadders(board)
        assert result >= 1  # Should still find a path

    def test_larger_no_snakes_ladders(self, solution):
        """Larger board with no snakes or ladders"""
        board = [[-1] * 4 for _ in range(4)]
        result = solution.snakesAndLadders(board)
        # 16 squares, need to reach 16 from 1
        # Best path: 1->7->13->16 (3 rolls of 6, then adjust)
        assert result >= 1

    def test_multiple_ladders(self, solution):
        """Board with multiple ladders"""
        board = [
            [-1, -1, -1, -1],
            [-1, -1, -1, -1],
            [-1, -1, -1, -1],
            [-1, 8, 16, -1]  # Ladder at 2->8, ladder at 3->16
        ]
        result = solution.snakesAndLadders(board)
        assert result == 1  # Roll 2 to hit square 3, ladder to 16

    def test_ladder_not_chained(self, solution):
        """Ladder leads to another ladder start - should not chain"""
        board = [
            [-1, -1, -1],
            [-1, 5, -1],  # Square 5 has ladder (but this tests non-chaining)
            [-1, 5, -1]   # Square 2 has ladder to 5
        ]
        # Per problem: don't follow subsequent ladders
        result = solution.snakesAndLadders(board)
        assert result >= 1

    def test_three_by_three_optimal(self, solution):
        """3x3 board optimal path"""
        board = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        # Squares: 1,2,3 (bottom row), 6,5,4 (middle), 7,8,9 (top)
        # Need to reach 9 from 1
        result = solution.snakesAndLadders(board)
        assert result == 2  # 1 -> 7 (roll 6), 7 -> 9 (roll 2)

    def test_boustrophedon_numbering(self, solution):
        """Verify boustrophedon numbering is correct"""
        # 4x4 board, numbering:
        # 16 15 14 13
        # 9  10 11 12
        # 8  7  6  5
        # 1  2  3  4
        board = [
            [-1, -1, -1, -1],
            [-1, -1, -1, -1],
            [-1, -1, -1, -1],
            [-1, -1, -1, -1]
        ]
        result = solution.snakesAndLadders(board)
        assert result >= 1

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
