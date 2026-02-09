"""
Tests for LeetCode Problem #684: Redundant Connection
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestRedundantConnection:
    """Test cases for Redundant Connection problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description - triangle"""
        assert solution.findRedundantConnection([[1, 2], [1, 3], [2, 3]]) == [2, 3]

    def test_example_2(self, solution):
        """Example 2 from problem description - larger graph"""
        assert solution.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]

    # Edge cases
    def test_minimum_edges(self, solution):
        """Minimum case: 3 nodes with triangle (3 edges, 1 redundant)"""
        result = solution.findRedundantConnection([[1, 2], [2, 3], [1, 3]])
        assert result == [1, 3]  # Last edge that creates cycle

    def test_linear_then_cycle(self, solution):
        """Linear graph then edge creates cycle"""
        edges = [[1, 2], [2, 3], [3, 4], [4, 1]]
        result = solution.findRedundantConnection(edges)
        assert result == [4, 1]  # Last edge creates cycle

    def test_redundant_early_in_list(self, solution):
        """When redundant edge appears early but later one exists"""
        edges = [[1, 2], [1, 3], [2, 3], [3, 4]]
        result = solution.findRedundantConnection(edges)
        assert result == [2, 3]  # Creates cycle when added

    def test_star_with_extra_edge(self, solution):
        """Star topology with one extra edge between leaves"""
        edges = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3]]
        result = solution.findRedundantConnection(edges)
        assert result == [2, 3]

    def test_two_triangles_sharing_edge(self, solution):
        """Two triangles sharing one edge"""
        edges = [[1, 2], [2, 3], [3, 1], [3, 4], [4, 5], [5, 3]]
        result = solution.findRedundantConnection(edges)
        # [3, 1] creates the first cycle (1-2-3-1)
        assert result == [3, 1]

    def test_cycle_at_end_of_chain(self, solution):
        """Long chain with cycle at the end"""
        edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [4, 6]]
        result = solution.findRedundantConnection(edges)
        assert result == [4, 6]

    def test_four_node_square(self, solution):
        """Four nodes in a square with diagonal"""
        edges = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3]]
        # [4, 1] creates the first cycle (1-2-3-4-1)
        result = solution.findRedundantConnection(edges)
        assert result == [4, 1]

    def test_multiple_possible_answers(self, solution):
        """Multiple edges could be removed, return last one"""
        # 1-2-3 triangle plus 1-4-3
        edges = [[1, 2], [2, 3], [1, 3], [1, 4], [4, 3]]
        result = solution.findRedundantConnection(edges)
        # [1, 3] creates the first cycle (1-2-3-1)
        assert result == [1, 3]

    def test_large_cycle(self, solution):
        """Large cycle"""
        edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1]]
        result = solution.findRedundantConnection(edges)
        assert result == [7, 1]

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
