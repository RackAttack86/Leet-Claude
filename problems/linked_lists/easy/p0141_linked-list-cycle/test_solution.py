"""
Tests for LeetCode Problem #141: Linked List Cycle
"""

import pytest
from solution import Solution, PROBLEM_METADATA, ListNode


def create_cycle_list(vals, pos):
    """Helper to create linked list with cycle at position pos (-1 for no cycle)"""
    if not vals:
        return None
    head = ListNode(vals[0])
    current = head
    cycle_node = head if pos == 0 else None

    for i, val in enumerate(vals[1:], 1):
        current.next = ListNode(val)
        current = current.next
        if i == pos:
            cycle_node = current

    if pos >= 0 and cycle_node:
        current.next = cycle_node

    return head


class TestLinkedListCycle:
    """Test cases for Linked List Cycle problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1: [3,2,0,-4] with cycle at pos 1"""
        head = create_cycle_list([3, 2, 0, -4], 1)
        assert solution.hasCycle(head) == True

    def test_example_2(self, solution):
        """Example 2: [1,2] with cycle at pos 0"""
        head = create_cycle_list([1, 2], 0)
        assert solution.hasCycle(head) == True

    def test_example_3(self, solution):
        """Example 3: [1] with no cycle"""
        head = create_cycle_list([1], -1)
        assert solution.hasCycle(head) == False

    def test_empty_list(self, solution):
        """Empty list"""
        assert solution.hasCycle(None) == False

    def test_no_cycle(self, solution):
        """List without cycle"""
        head = create_cycle_list([1, 2, 3, 4, 5], -1)
        assert solution.hasCycle(head) == False

    def test_single_node_cycle(self, solution):
        """Single node pointing to itself"""
        head = ListNode(1)
        head.next = head
        assert solution.hasCycle(head) == True

    # Edge case tests
    def test_two_nodes_no_cycle(self, solution):
        """Two nodes without cycle"""
        head = create_cycle_list([1, 2], -1)
        assert solution.hasCycle(head) == False

    def test_two_nodes_with_cycle(self, solution):
        """Two nodes with cycle back to head"""
        head = create_cycle_list([1, 2], 0)
        assert solution.hasCycle(head) == True

    def test_cycle_at_tail(self, solution):
        """Cycle connecting tail to last node before tail"""
        head = create_cycle_list([1, 2, 3, 4, 5], 3)
        assert solution.hasCycle(head) == True

    def test_cycle_at_middle(self, solution):
        """Cycle connecting tail to middle node"""
        head = create_cycle_list([1, 2, 3, 4, 5, 6], 2)
        assert solution.hasCycle(head) == True

    def test_long_list_no_cycle(self, solution):
        """Long list without cycle"""
        head = create_cycle_list(list(range(100)), -1)
        assert solution.hasCycle(head) == False

    def test_long_list_with_cycle(self, solution):
        """Long list with cycle"""
        head = create_cycle_list(list(range(100)), 50)
        assert solution.hasCycle(head) == True

    def test_negative_values(self, solution):
        """List with negative values and cycle"""
        head = create_cycle_list([-5, -4, -3, -2, -1], 2)
        assert solution.hasCycle(head) == True

    def test_all_same_values_no_cycle(self, solution):
        """All same values without cycle"""
        head = create_cycle_list([1, 1, 1, 1], -1)
        assert solution.hasCycle(head) == False

    def test_all_same_values_with_cycle(self, solution):
        """All same values with cycle"""
        head = create_cycle_list([1, 1, 1, 1], 1)
        assert solution.hasCycle(head) == True

    def test_three_nodes_cycle_to_head(self, solution):
        """Three nodes cycle back to head"""
        head = create_cycle_list([1, 2, 3], 0)
        assert solution.hasCycle(head) == True

    def test_three_nodes_cycle_to_middle(self, solution):
        """Three nodes cycle back to middle"""
        head = create_cycle_list([1, 2, 3], 1)
        assert solution.hasCycle(head) == True

    def test_boundary_values(self, solution):
        """Boundary values from constraints"""
        head = create_cycle_list([-100000, 0, 100000], 0)
        assert solution.hasCycle(head) == True

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
