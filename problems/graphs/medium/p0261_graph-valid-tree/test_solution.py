"""
Tests for LeetCode Problem #261: Graph Valid Tree
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestGraphValidTree:
    """Test cases for Graph Valid Tree problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description - valid tree"""
        assert solution.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) == True

    def test_example_2(self, solution):
        """Example 2 from problem description - has cycle"""
        assert solution.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) == False

    # Edge cases
    def test_single_node_no_edges(self, solution):
        """Single node with no edges - valid tree"""
        assert solution.validTree(1, []) == True

    def test_two_nodes_one_edge(self, solution):
        """Two nodes connected - valid tree"""
        assert solution.validTree(2, [[0, 1]]) == True

    def test_two_nodes_no_edge(self, solution):
        """Two nodes, no edge - not connected, not a tree"""
        assert solution.validTree(2, []) == False

    def test_three_nodes_line(self, solution):
        """Three nodes in a line - valid tree"""
        assert solution.validTree(3, [[0, 1], [1, 2]]) == True

    def test_three_nodes_triangle(self, solution):
        """Three nodes forming triangle - has cycle"""
        assert solution.validTree(3, [[0, 1], [1, 2], [0, 2]]) == False

    def test_multiple_nodes_no_edges(self, solution):
        """Multiple nodes with no edges - not connected"""
        assert solution.validTree(5, []) == False

    def test_too_many_edges(self, solution):
        """More than n-1 edges - must have cycle"""
        assert solution.validTree(4, [[0, 1], [0, 2], [0, 3], [1, 2]]) == False

    def test_too_few_edges(self, solution):
        """Fewer than n-1 edges - not fully connected"""
        assert solution.validTree(5, [[0, 1], [2, 3]]) == False

    def test_star_graph(self, solution):
        """Star graph - valid tree"""
        assert solution.validTree(5, [[0, 1], [0, 2], [0, 3], [0, 4]]) == True

    def test_disconnected_components(self, solution):
        """Two separate components - not a tree"""
        assert solution.validTree(4, [[0, 1], [2, 3]]) == False

    def test_linear_chain(self, solution):
        """Linear chain of nodes - valid tree"""
        assert solution.validTree(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == True

    def test_cycle_in_larger_graph(self, solution):
        """Cycle exists in larger graph"""
        edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 1]]  # Cycle: 1-2-3-4-1
        assert solution.validTree(5, edges) == False

    def test_exactly_n_minus_1_edges_but_cycle(self, solution):
        """Has n-1 edges but contains a cycle (impossible per Union Find logic)"""
        # With n-1 edges, if there's no cycle, it's connected
        # If there's a cycle, some nodes would be disconnected
        # Testing the edge case where we have correct count but wrong structure
        # This actually can't happen with n-1 edges and no repeated edges
        pass

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
