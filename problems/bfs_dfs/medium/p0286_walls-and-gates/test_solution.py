"""
Tests for LeetCode Problem #286: Walls and Gates
"""

import pytest
from solution import Solution, PROBLEM_METADATA

INF = 2147483647


class TestWallsAndGates:
    """Test cases for Walls and Gates problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        rooms = [
            [INF, -1, 0, INF],
            [INF, INF, INF, -1],
            [INF, -1, INF, -1],
            [0, -1, INF, INF]
        ]
        expected = [
            [3, -1, 0, 1],
            [2, 2, 1, -1],
            [1, -1, 2, -1],
            [0, -1, 3, 4]
        ]
        solution.wallsAndGates(rooms)
        assert rooms == expected

    def test_example_2(self, solution):
        """Example 2 from problem description - single wall"""
        rooms = [[-1]]
        expected = [[-1]]
        solution.wallsAndGates(rooms)
        assert rooms == expected

    # Edge cases
    def test_no_gates(self, solution):
        """No gates in the grid - rooms stay INF"""
        rooms = [
            [INF, -1, INF],
            [INF, INF, INF],
            [INF, -1, INF]
        ]
        expected = [
            [INF, -1, INF],
            [INF, INF, INF],
            [INF, -1, INF]
        ]
        solution.wallsAndGates(rooms)
        assert rooms == expected

    def test_no_empty_rooms(self, solution):
        """No empty rooms - only gates and walls"""
        rooms = [
            [0, -1, 0],
            [-1, 0, -1],
            [0, -1, 0]
        ]
        expected = [
            [0, -1, 0],
            [-1, 0, -1],
            [0, -1, 0]
        ]
        solution.wallsAndGates(rooms)
        assert rooms == expected

    def test_all_gates(self, solution):
        """All cells are gates"""
        rooms = [
            [0, 0],
            [0, 0]
        ]
        expected = [
            [0, 0],
            [0, 0]
        ]
        solution.wallsAndGates(rooms)
        assert rooms == expected

    def test_all_walls(self, solution):
        """All cells are walls"""
        rooms = [
            [-1, -1],
            [-1, -1]
        ]
        expected = [
            [-1, -1],
            [-1, -1]
        ]
        solution.wallsAndGates(rooms)
        assert rooms == expected

    def test_single_gate(self, solution):
        """Single gate"""
        rooms = [[0]]
        expected = [[0]]
        solution.wallsAndGates(rooms)
        assert rooms == expected

    def test_single_empty_room(self, solution):
        """Single empty room"""
        rooms = [[INF]]
        expected = [[INF]]
        solution.wallsAndGates(rooms)
        assert rooms == expected

    def test_room_unreachable(self, solution):
        """Empty room completely surrounded by walls"""
        rooms = [
            [0, -1, INF],
            [-1, -1, -1],
            [INF, -1, 0]
        ]
        expected = [
            [0, -1, INF],  # top-right room unreachable
            [-1, -1, -1],
            [INF, -1, 0]   # bottom-left room unreachable
        ]
        solution.wallsAndGates(rooms)
        assert rooms == expected

    def test_multiple_gates(self, solution):
        """Multiple gates - rooms get closest distance"""
        rooms = [
            [0, INF, INF, 0],
            [INF, INF, INF, INF],
            [INF, INF, INF, INF]
        ]
        expected = [
            [0, 1, 1, 0],
            [1, 2, 2, 1],
            [2, 3, 3, 2]
        ]
        solution.wallsAndGates(rooms)
        assert rooms == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
