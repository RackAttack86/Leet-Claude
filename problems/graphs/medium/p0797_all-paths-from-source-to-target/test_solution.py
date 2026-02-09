"""
Tests for LeetCode Problem #797: All Paths From Source to Target
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestAllPathsFromSourceToTarget:
    """Test cases for All Paths From Source to Target problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        graph = [[1, 2], [3], [3], []]
        result = solution.allPathsSourceTarget(graph)
        expected = [[0, 1, 3], [0, 2, 3]]
        assert sorted(result) == sorted(expected)

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
        result = solution.allPathsSourceTarget(graph)
        expected = [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
        assert sorted(result) == sorted(expected)

    # Edge cases
    def test_direct_path_only(self, solution):
        """Direct edge from 0 to n-1"""
        graph = [[1], []]
        result = solution.allPathsSourceTarget(graph)
        assert result == [[0, 1]]

    def test_two_nodes_direct(self, solution):
        """Simplest case: two nodes with direct path"""
        graph = [[1], []]
        result = solution.allPathsSourceTarget(graph)
        assert result == [[0, 1]]

    def test_single_path(self, solution):
        """Only one path exists"""
        graph = [[1], [2], [3], []]
        result = solution.allPathsSourceTarget(graph)
        assert result == [[0, 1, 2, 3]]

    def test_multiple_parallel_paths(self, solution):
        """Multiple parallel paths of same length"""
        graph = [[1, 2, 3], [], [], []]  # Wait, this doesn't work - 1,2,3 don't lead to 3
        # Let me fix: 0 connects to 1,2 which both connect to 3
        graph = [[1, 2], [3], [3], []]
        result = solution.allPathsSourceTarget(graph)
        expected = [[0, 1, 3], [0, 2, 3]]
        assert sorted(result) == sorted(expected)

    def test_diamond_dag(self, solution):
        """Diamond DAG: 0 -> 1,2 -> 3"""
        graph = [[1, 2], [3], [3], []]
        result = solution.allPathsSourceTarget(graph)
        expected = [[0, 1, 3], [0, 2, 3]]
        assert sorted(result) == sorted(expected)

    def test_complex_dag(self, solution):
        """Complex DAG with many paths"""
        graph = [[1, 2], [2, 3], [3], []]
        result = solution.allPathsSourceTarget(graph)
        # Paths: 0->1->2->3, 0->1->3, 0->2->3
        expected = [[0, 1, 2, 3], [0, 1, 3], [0, 2, 3]]
        assert sorted(result) == sorted(expected)

    def test_no_edges_from_source(self, solution):
        """Source has no outgoing edges - no paths"""
        graph = [[], []]
        result = solution.allPathsSourceTarget(graph)
        assert result == []

    def test_wide_graph(self, solution):
        """Wide graph with many children at each level"""
        graph = [[1, 2, 3], [4], [4], [4], []]
        result = solution.allPathsSourceTarget(graph)
        expected = [[0, 1, 4], [0, 2, 4], [0, 3, 4]]
        assert sorted(result) == sorted(expected)

    def test_long_path(self, solution):
        """Long single path"""
        graph = [[1], [2], [3], [4], [5], []]
        result = solution.allPathsSourceTarget(graph)
        assert result == [[0, 1, 2, 3, 4, 5]]

    def test_target_only_reachable_via_one_path(self, solution):
        """Multiple branches but only one reaches target"""
        graph = [[1, 2], [3], [], []]  # Only path through 1 reaches 3
        result = solution.allPathsSourceTarget(graph)
        assert result == [[0, 1, 3]]

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
