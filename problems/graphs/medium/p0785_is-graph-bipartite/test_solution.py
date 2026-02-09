"""
Tests for LeetCode Problem #785: Is Graph Bipartite
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestIsGraphBipartite:
    """Test cases for Is Graph Bipartite problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description - not bipartite"""
        graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
        assert solution.isBipartite(graph) == False

    def test_example_2(self, solution):
        """Example 2 from problem description - bipartite"""
        graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
        assert solution.isBipartite(graph) == True

    # Edge cases
    def test_single_node(self, solution):
        """Single node with no edges - trivially bipartite"""
        graph = [[]]
        assert solution.isBipartite(graph) == True

    def test_two_nodes_connected(self, solution):
        """Two connected nodes - bipartite"""
        graph = [[1], [0]]
        assert solution.isBipartite(graph) == True

    def test_two_nodes_disconnected(self, solution):
        """Two disconnected nodes - bipartite"""
        graph = [[], []]
        assert solution.isBipartite(graph) == True

    def test_triangle_not_bipartite(self, solution):
        """Triangle (odd cycle) - not bipartite"""
        graph = [[1, 2], [0, 2], [0, 1]]
        assert solution.isBipartite(graph) == False

    def test_square_bipartite(self, solution):
        """Square (even cycle) - bipartite"""
        graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
        assert solution.isBipartite(graph) == True

    def test_pentagon_not_bipartite(self, solution):
        """Pentagon (5-cycle, odd) - not bipartite"""
        graph = [[1, 4], [0, 2], [1, 3], [2, 4], [0, 3]]
        assert solution.isBipartite(graph) == False

    def test_hexagon_bipartite(self, solution):
        """Hexagon (6-cycle, even) - bipartite"""
        graph = [[1, 5], [0, 2], [1, 3], [2, 4], [3, 5], [0, 4]]
        assert solution.isBipartite(graph) == True

    def test_star_graph(self, solution):
        """Star graph - bipartite (center vs leaves)"""
        graph = [[1, 2, 3, 4], [0], [0], [0], [0]]
        assert solution.isBipartite(graph) == True

    def test_disconnected_bipartite_components(self, solution):
        """Two disconnected bipartite components"""
        graph = [[1], [0], [3], [2]]  # Two separate edges
        assert solution.isBipartite(graph) == True

    def test_disconnected_with_odd_cycle(self, solution):
        """Disconnected components, one has odd cycle"""
        graph = [[1], [0], [3, 4], [2, 4], [2, 3]]  # Edge + triangle
        assert solution.isBipartite(graph) == False

    def test_complete_bipartite(self, solution):
        """Complete bipartite graph K(2,2)"""
        graph = [[2, 3], [2, 3], [0, 1], [0, 1]]
        assert solution.isBipartite(graph) == True

    def test_all_isolated_nodes(self, solution):
        """All nodes isolated - bipartite"""
        graph = [[], [], [], []]
        assert solution.isBipartite(graph) == True

    def test_linear_chain(self, solution):
        """Linear chain - bipartite"""
        graph = [[1], [0, 2], [1, 3], [2, 4], [3]]
        assert solution.isBipartite(graph) == True

    def test_tree_bipartite(self, solution):
        """Tree structure - always bipartite"""
        graph = [[1, 2], [0, 3, 4], [0], [1], [1]]
        assert solution.isBipartite(graph) == True

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
