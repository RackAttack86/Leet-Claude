"""
Tests for LeetCode Problem #1197: Minimum Knight Moves
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestMinimumKnightMoves:
    """Test cases for Minimum Knight Moves problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        assert solution.minKnightMoves(2, 1) == 1

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        assert solution.minKnightMoves(5, 5) == 4

    # Edge cases
    def test_already_at_target(self, solution):
        """Already at target (0, 0)"""
        assert solution.minKnightMoves(0, 0) == 0

    def test_one_move_away_2_1(self, solution):
        """One move away - position (2, 1)"""
        assert solution.minKnightMoves(2, 1) == 1

    def test_one_move_away_1_2(self, solution):
        """One move away - position (1, 2)"""
        assert solution.minKnightMoves(1, 2) == 1

    def test_negative_coordinates(self, solution):
        """Negative coordinates - uses symmetry"""
        assert solution.minKnightMoves(-2, -1) == 1
        assert solution.minKnightMoves(-1, -2) == 1

    def test_mixed_coordinates(self, solution):
        """Mixed positive/negative coordinates"""
        assert solution.minKnightMoves(-2, 1) == 1
        assert solution.minKnightMoves(2, -1) == 1

    def test_position_1_1(self, solution):
        """Position (1, 1) - requires 2 moves"""
        assert solution.minKnightMoves(1, 1) == 2

    def test_position_1_0(self, solution):
        """Position (1, 0) - requires 3 moves"""
        assert solution.minKnightMoves(1, 0) == 3

    def test_position_0_1(self, solution):
        """Position (0, 1) - requires 3 moves"""
        assert solution.minKnightMoves(0, 1) == 3

    def test_on_x_axis(self, solution):
        """Target on x-axis"""
        assert solution.minKnightMoves(4, 0) == 2

    def test_on_y_axis(self, solution):
        """Target on y-axis"""
        assert solution.minKnightMoves(0, 4) == 2

    def test_diagonal_position(self, solution):
        """Diagonal position"""
        assert solution.minKnightMoves(2, 2) == 4

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
