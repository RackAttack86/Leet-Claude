"""
Tests for LeetCode Problem #1135: Connecting Cities With Minimum Cost
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestConnectingCitiesWithMinimumCost:
    """Test cases for Connecting Cities With Minimum Cost problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        n = 3
        connections = [[1, 2, 5], [1, 3, 6], [2, 3, 1]]
        assert solution.minimumCost(n, connections) == 6

    def test_example_2(self, solution):
        """Example 2 from problem description - impossible"""
        n = 4
        connections = [[1, 2, 3], [3, 4, 4]]
        assert solution.minimumCost(n, connections) == -1

    # Edge cases
    def test_single_city(self, solution):
        """Single city - already connected, cost 0"""
        n = 1
        connections = []
        assert solution.minimumCost(n, connections) == 0

    def test_two_cities_one_edge(self, solution):
        """Two cities with one connection"""
        n = 2
        connections = [[1, 2, 10]]
        assert solution.minimumCost(n, connections) == 10

    def test_two_cities_no_edge(self, solution):
        """Two cities with no connection - impossible"""
        n = 2
        connections = []
        assert solution.minimumCost(n, connections) == -1

    def test_already_mst(self, solution):
        """Connections already form MST"""
        n = 4
        connections = [[1, 2, 1], [2, 3, 2], [3, 4, 3]]
        assert solution.minimumCost(n, connections) == 6

    def test_cycle_choose_minimum(self, solution):
        """Cycle in graph - must choose minimum edges"""
        n = 3
        connections = [[1, 2, 1], [2, 3, 2], [1, 3, 3]]
        # MST uses edges with cost 1 and 2, not 3
        assert solution.minimumCost(n, connections) == 3

    def test_multiple_edges_between_cities(self, solution):
        """Multiple edges between same cities - use cheapest"""
        n = 2
        connections = [[1, 2, 10], [1, 2, 5], [1, 2, 8]]
        assert solution.minimumCost(n, connections) == 5

    def test_star_topology(self, solution):
        """Star topology - all connect to center"""
        n = 5
        connections = [[1, 2, 1], [1, 3, 2], [1, 4, 3], [1, 5, 4]]
        assert solution.minimumCost(n, connections) == 10  # 1+2+3+4

    def test_linear_chain(self, solution):
        """Linear chain of cities"""
        n = 4
        connections = [[1, 2, 1], [2, 3, 2], [3, 4, 3]]
        assert solution.minimumCost(n, connections) == 6

    def test_complete_graph_small(self, solution):
        """Complete graph - must pick n-1 cheapest edges carefully"""
        n = 4
        connections = [
            [1, 2, 1], [1, 3, 2], [1, 4, 3],
            [2, 3, 4], [2, 4, 5],
            [3, 4, 6]
        ]
        # MST: 1-2 (1), 1-3 (2), 1-4 (3) = 6
        assert solution.minimumCost(n, connections) == 6

    def test_disconnected_components(self, solution):
        """Disconnected components - impossible"""
        n = 5
        connections = [[1, 2, 1], [2, 3, 2], [4, 5, 3]]
        assert solution.minimumCost(n, connections) == -1

    def test_zero_cost_edge(self, solution):
        """Edge with zero cost"""
        n = 2
        connections = [[1, 2, 0]]
        assert solution.minimumCost(n, connections) == 0

    def test_large_costs(self, solution):
        """Large edge costs"""
        n = 3
        connections = [[1, 2, 100000], [2, 3, 100000]]
        assert solution.minimumCost(n, connections) == 200000

    def test_many_redundant_edges(self, solution):
        """Many redundant edges, few needed"""
        n = 3
        connections = [
            [1, 2, 1], [1, 2, 10], [1, 2, 100],
            [2, 3, 2], [2, 3, 20], [2, 3, 200],
            [1, 3, 5], [1, 3, 50]
        ]
        # MST: 1-2 (1) + 2-3 (2) = 3
        assert solution.minimumCost(n, connections) == 3

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
