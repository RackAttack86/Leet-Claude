"""
Tests for LeetCode Problem #133: Clone Graph
"""

import pytest
from solution import Solution, PROBLEM_METADATA
from solution import Node



class TestCloneGraph:
    """Test cases for Clone Graph problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def build_graph(self, adj_list):
        """Build graph from adjacency list"""
        if not adj_list:
            return None

        nodes = [Node(i + 1) for i in range(len(adj_list))]
        for i, neighbors in enumerate(adj_list):
            nodes[i].neighbors = [nodes[j - 1] for j in neighbors]
        return nodes[0] if nodes else None

    def graph_to_adj_list(self, node):
        """Convert graph back to adjacency list"""
        if not node:
            return []

        visited = {}
        adj_list = []

        def dfs(n):
            if n.val in visited:
                return
            visited[n.val] = n
            while len(adj_list) < n.val:
                adj_list.append([])
            adj_list[n.val - 1] = sorted([neighbor.val for neighbor in n.neighbors])
            for neighbor in n.neighbors:
                dfs(neighbor)

        dfs(node)
        return adj_list

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        adj_list = [[2,4],[1,3],[2,4],[1,3]]
        original = self.build_graph(adj_list)
        cloned = solution.cloneGraph(original)

        # Verify it's a deep copy (different objects)
        assert cloned is not original

        # Verify structure is the same
        result = self.graph_to_adj_list(cloned)
        assert result == adj_list


    def test_example_2(self, solution):
        """Example 2 from problem description - single node"""
        adj_list = [[]]
        original = self.build_graph(adj_list)
        cloned = solution.cloneGraph(original)

        assert cloned is not original
        assert cloned.val == 1
        assert cloned.neighbors == []


    def test_example_3(self, solution):
        """Example 3 from problem description - empty graph"""
        result = solution.cloneGraph(None)
        assert result is None


    def test_two_nodes(self, solution):
        """Test with two connected nodes"""
        adj_list = [[2],[1]]
        original = self.build_graph(adj_list)
        cloned = solution.cloneGraph(original)

        assert cloned is not original
        result = self.graph_to_adj_list(cloned)
        assert result == adj_list


    # Edge cases
    def test_null_input(self, solution):
        """Null input should return null"""
        assert solution.cloneGraph(None) is None

    def test_single_node_no_neighbors(self, solution):
        """Single node with no neighbors"""
        node = Node(1)
        cloned = solution.cloneGraph(node)

        assert cloned is not node
        assert cloned.val == 1
        assert cloned.neighbors == []

    def test_three_nodes_linear(self, solution):
        """Linear graph: 1 - 2 - 3"""
        adj_list = [[2], [1, 3], [2]]
        original = self.build_graph(adj_list)
        cloned = solution.cloneGraph(original)

        assert cloned is not original
        result = self.graph_to_adj_list(cloned)
        assert result == adj_list

    def test_complete_graph_four_nodes(self, solution):
        """Fully connected graph with 4 nodes"""
        adj_list = [[2, 3, 4], [1, 3, 4], [1, 2, 4], [1, 2, 3]]
        original = self.build_graph(adj_list)
        cloned = solution.cloneGraph(original)

        assert cloned is not original
        result = self.graph_to_adj_list(cloned)
        assert result == adj_list

    def test_star_graph(self, solution):
        """Star graph: node 1 connected to all others"""
        adj_list = [[2, 3, 4, 5], [1], [1], [1], [1]]
        original = self.build_graph(adj_list)
        cloned = solution.cloneGraph(original)

        assert cloned is not original
        result = self.graph_to_adj_list(cloned)
        assert result == adj_list

    def test_cycle_graph(self, solution):
        """Cycle graph: 1 - 2 - 3 - 4 - 1"""
        adj_list = [[2, 4], [1, 3], [2, 4], [1, 3]]
        original = self.build_graph(adj_list)
        cloned = solution.cloneGraph(original)

        assert cloned is not original
        result = self.graph_to_adj_list(cloned)
        assert result == adj_list

    def test_deep_copy_independence(self, solution):
        """Verify cloned graph is truly independent from original"""
        adj_list = [[2], [1]]
        original = self.build_graph(adj_list)
        cloned = solution.cloneGraph(original)

        # Modify original
        original.val = 100

        # Clone should be unaffected
        assert cloned.val == 1

    def test_five_nodes_complex(self, solution):
        """Complex graph with 5 nodes"""
        adj_list = [[2, 4], [1, 3], [2, 4, 5], [1, 3, 5], [3, 4]]
        original = self.build_graph(adj_list)
        cloned = solution.cloneGraph(original)

        assert cloned is not original
        result = self.graph_to_adj_list(cloned)
        assert result == adj_list

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
