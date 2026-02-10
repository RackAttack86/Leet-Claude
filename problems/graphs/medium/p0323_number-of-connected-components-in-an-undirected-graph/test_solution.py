"""
Tests for LeetCode Problem #323: Number of Connected Components in an Undirected Graph
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestNumberOfConnectedComponentsInAnUndirectedGraph:
    """Test cases for Number of Connected Components in an Undirected Graph problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description - two components"""
        assert solution.countComponents(5, [[0, 1], [1, 2], [3, 4]]) == 2

    def test_example_2(self, solution):
        """Example 2 from problem description - one component"""
        assert solution.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1

    # Edge cases
    def test_single_node(self, solution):
        """Single node with no edges - one component"""
        assert solution.countComponents(1, []) == 1

    def test_all_disconnected(self, solution):
        """All nodes disconnected - n components"""
        assert solution.countComponents(5, []) == 5

    def test_all_connected_chain(self, solution):
        """All nodes in a chain - one component"""
        edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]
        assert solution.countComponents(6, edges) == 1

    def test_all_connected_star(self, solution):
        """Star topology - all connected to center"""
        edges = [[0, 1], [0, 2], [0, 3], [0, 4]]
        assert solution.countComponents(5, edges) == 1

    def test_two_pairs(self, solution):
        """Two separate pairs"""
        assert solution.countComponents(4, [[0, 1], [2, 3]]) == 2

    def test_triangle_and_single(self, solution):
        """Triangle plus isolated node"""
        edges = [[0, 1], [1, 2], [0, 2]]
        assert solution.countComponents(4, edges) == 2

    def test_fully_connected(self, solution):
        """Fully connected graph - one component"""
        edges = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]
        assert solution.countComponents(4, edges) == 1

    def test_three_separate_components(self, solution):
        """Three separate components of different sizes"""
        edges = [[0, 1], [2, 3], [3, 4]]  # {0,1}, {2,3,4}, {5}
        assert solution.countComponents(6, edges) == 3

    def test_cycle_single_component(self, solution):
        """Cycle forms single component"""
        edges = [[0, 1], [1, 2], [2, 3], [3, 0]]
        assert solution.countComponents(4, edges) == 1

    def test_two_nodes_connected(self, solution):
        """Two nodes, one edge - single component"""
        assert solution.countComponents(2, [[0, 1]]) == 1

    def test_two_nodes_disconnected(self, solution):
        """Two nodes, no edges - two components"""
        assert solution.countComponents(2, []) == 2

    def test_many_isolated_nodes(self, solution):
        """Many isolated nodes"""
        assert solution.countComponents(10, []) == 10

    def test_merge_multiple_components(self, solution):
        """Edges that merge multiple components into one"""
        edges = [[0, 1], [2, 3], [4, 5], [1, 2], [3, 4]]  # Links three pairs
        assert solution.countComponents(6, edges) == 1

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
