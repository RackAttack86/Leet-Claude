"""
Tests for LeetCode Problem #743: Network Delay Time
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestNetworkDelayTime:
    """Test cases for Network Delay Time problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
        assert solution.networkDelayTime(times, 4, 2) == 2

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        times = [[1, 2, 1]]
        assert solution.networkDelayTime(times, 2, 1) == 1

    def test_example_3(self, solution):
        """Example 3 - unreachable node"""
        times = [[1, 2, 1]]
        assert solution.networkDelayTime(times, 2, 2) == -1

    # Edge cases
    def test_single_node(self, solution):
        """Single node - instant delivery"""
        times = []
        assert solution.networkDelayTime(times, 1, 1) == 0

    def test_unreachable_node(self, solution):
        """Some nodes are unreachable"""
        times = [[1, 2, 1], [2, 3, 1]]
        assert solution.networkDelayTime(times, 4, 1) == -1  # Node 4 unreachable

    def test_linear_chain(self, solution):
        """Linear chain of nodes"""
        times = [[1, 2, 1], [2, 3, 2], [3, 4, 3]]
        assert solution.networkDelayTime(times, 4, 1) == 6  # 1+2+3

    def test_all_from_source(self, solution):
        """All nodes directly connected from source"""
        times = [[1, 2, 5], [1, 3, 10], [1, 4, 3]]
        assert solution.networkDelayTime(times, 4, 1) == 10  # Max delay to reach all

    def test_faster_indirect_path(self, solution):
        """Indirect path is faster than direct"""
        times = [[1, 2, 100], [1, 3, 1], [3, 2, 1]]
        # Direct 1->2 = 100, but 1->3->2 = 2
        assert solution.networkDelayTime(times, 3, 1) == 2

    def test_cycle_in_graph(self, solution):
        """Graph contains cycles"""
        times = [[1, 2, 1], [2, 3, 1], [3, 1, 1], [2, 4, 2]]
        assert solution.networkDelayTime(times, 4, 1) == 3

    def test_multiple_paths_to_same_node(self, solution):
        """Multiple paths to same node, take shortest"""
        times = [[1, 2, 1], [1, 3, 4], [2, 3, 2]]
        # Path to 3: direct = 4, via 2 = 1+2 = 3
        assert solution.networkDelayTime(times, 3, 1) == 3

    def test_zero_weight_edge(self, solution):
        """Edge with zero weight"""
        times = [[1, 2, 0], [2, 3, 1]]
        assert solution.networkDelayTime(times, 3, 1) == 1

    def test_two_disconnected_components(self, solution):
        """Two disconnected components - unreachable"""
        times = [[1, 2, 1], [3, 4, 1]]
        assert solution.networkDelayTime(times, 4, 1) == -1

    def test_start_from_middle(self, solution):
        """Start from middle node - cannot reach all nodes"""
        times = [[1, 2, 1], [2, 3, 1], [3, 4, 1]]
        # Edges are directed, so starting from 2 cannot reach node 1
        assert solution.networkDelayTime(times, 4, 2) == -1

    def test_dense_graph(self, solution):
        """Densely connected graph"""
        times = [
            [1, 2, 1], [1, 3, 2], [1, 4, 3],
            [2, 3, 1], [2, 4, 2],
            [3, 4, 1]
        ]
        # Node 2: 1, Node 3: 2, Node 4: min(3, 1+2, 2+1) = 3
        assert solution.networkDelayTime(times, 4, 1) == 3

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
