"""
Tests for LeetCode Problem #138: Copy List with Random Pointer
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA
from solution import Node



class TestCopyListWithRandomPointer:
    """Test cases for Copy List with Random Pointer problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def build_list(self, data):
        """Helper to build a linked list from [[val, random_index], ...] format"""
        if not data:
            return None

        # Create all nodes
        nodes = [Node(val) for val, _ in data]

        # Set next pointers
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

        # Set random pointers
        for i, (_, random_idx) in enumerate(data):
            if random_idx is not None:
                nodes[i].random = nodes[random_idx]

        return nodes[0]

    def list_to_array(self, head):
        """Convert linked list to [[val, random_index], ...] format for comparison"""
        if not head:
            return []

        # First pass: collect all nodes and create index mapping
        nodes = []
        node_to_idx = {}
        current = head
        idx = 0
        while current:
            nodes.append(current)
            node_to_idx[current] = idx
            current = current.next
            idx += 1

        # Second pass: build result array
        result = []
        for node in nodes:
            random_idx = node_to_idx[node.random] if node.random else None
            result.append([node.val, random_idx])

        return result

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        head = self.build_list([[7,None],[13,0],[11,4],[10,2],[1,0]])
        expected = [[7,None],[13,0],[11,4],[10,2],[1,0]]
        result = solution.copyRandomList(head)
        assert self.list_to_array(result) == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        head = self.build_list([[1,1],[2,1]])
        expected = [[1,1],[2,1]]
        result = solution.copyRandomList(head)
        assert self.list_to_array(result) == expected


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        head = self.build_list([[3,None],[3,0],[3,None]])
        expected = [[3,None],[3,0],[3,None]]
        result = solution.copyRandomList(head)
        assert self.list_to_array(result) == expected


    def test_edge_case_empty(self, solution):
        """Test with empty list"""
        result = solution.copyRandomList(None)
        assert result is None

    def test_no_random_pointers(self, solution):
        """Test list where all random pointers are None"""
        head = self.build_list([[1, None], [2, None], [3, None]])
        expected = [[1, None], [2, None], [3, None]]
        result = solution.copyRandomList(head)
        assert self.list_to_array(result) == expected

    def test_all_random_point_to_same(self, solution):
        """Test all random pointers point to the same node"""
        head = self.build_list([[1, 0], [2, 0], [3, 0]])
        expected = [[1, 0], [2, 0], [3, 0]]
        result = solution.copyRandomList(head)
        assert self.list_to_array(result) == expected

    def test_single_node_no_random(self, solution):
        """Test single node with no random pointer"""
        head = self.build_list([[1, None]])
        expected = [[1, None]]
        result = solution.copyRandomList(head)
        assert self.list_to_array(result) == expected

    def test_single_node_random_to_self(self, solution):
        """Test single node with random pointing to itself"""
        head = self.build_list([[1, 0]])
        expected = [[1, 0]]
        result = solution.copyRandomList(head)
        assert self.list_to_array(result) == expected

    def test_two_nodes_cross_random(self, solution):
        """Test two nodes with cross random pointers"""
        head = self.build_list([[1, 1], [2, 0]])
        expected = [[1, 1], [2, 0]]
        result = solution.copyRandomList(head)
        assert self.list_to_array(result) == expected

    def test_random_points_to_last(self, solution):
        """Test random pointers pointing to last node"""
        head = self.build_list([[1, 2], [2, 2], [3, None]])
        expected = [[1, 2], [2, 2], [3, None]]
        result = solution.copyRandomList(head)
        assert self.list_to_array(result) == expected

    def test_is_deep_copy(self, solution):
        """Test that the result is a deep copy, not sharing nodes"""
        head = self.build_list([[1, None], [2, None]])
        result = solution.copyRandomList(head)
        # Verify result structure is correct
        assert self.list_to_array(result) == [[1, None], [2, None]]
        # Verify nodes are different objects
        assert result is not head
        assert result.next is not head.next


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
