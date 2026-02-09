"""
Tests for LeetCode Problem #994: Rotting Oranges
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestRottingOranges:
    """Test cases for Rotting Oranges problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
        assert solution.orangesRotting(grid) == 4

    def test_example_2(self, solution):
        """Example 2 from problem description - impossible case"""
        grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
        assert solution.orangesRotting(grid) == -1

    # Edge cases
    def test_no_fresh_oranges(self, solution):
        """No fresh oranges - already done"""
        grid = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
        assert solution.orangesRotting(grid) == 0

    def test_no_rotten_oranges(self, solution):
        """No rotten oranges - fresh can never rot"""
        grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        assert solution.orangesRotting(grid) == -1

    def test_already_all_rotten(self, solution):
        """All oranges already rotten"""
        grid = [[2, 2], [2, 2]]
        assert solution.orangesRotting(grid) == 0

    def test_no_oranges(self, solution):
        """No oranges at all - empty grid"""
        grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        assert solution.orangesRotting(grid) == 0

    def test_single_fresh(self, solution):
        """Single fresh orange"""
        grid = [[1]]
        assert solution.orangesRotting(grid) == -1

    def test_single_rotten(self, solution):
        """Single rotten orange"""
        grid = [[2]]
        assert solution.orangesRotting(grid) == 0

    def test_fresh_adjacent_to_rotten(self, solution):
        """Fresh orange next to rotten - 1 minute"""
        grid = [[2, 1]]
        assert solution.orangesRotting(grid) == 1

    def test_linear_spread(self, solution):
        """Linear spread of rot"""
        grid = [[2, 1, 1, 1, 1]]
        assert solution.orangesRotting(grid) == 4

    def test_isolated_fresh_orange(self, solution):
        """Fresh orange isolated by empty cells"""
        grid = [
            [2, 0, 1],
            [0, 0, 0],
            [1, 0, 2]
        ]
        assert solution.orangesRotting(grid) == -1

    def test_multiple_rotten_sources(self, solution):
        """Multiple rotten oranges spreading simultaneously"""
        grid = [
            [2, 1, 1, 1, 2],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]
        ]
        # Center bottom row is furthest from any rotten source
        assert solution.orangesRotting(grid) == 4

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
