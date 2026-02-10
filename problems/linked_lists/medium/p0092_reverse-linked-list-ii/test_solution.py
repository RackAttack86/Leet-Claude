"""
Tests for LeetCode Problem #92: Reverse Linked List II
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA, ListNode


def list_to_linked(arr):
    """Convert array to linked list"""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_to_list(head):
    """Convert linked list to array"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


class TestReverseLinkedListIi:
    """Test cases for Reverse Linked List II problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        head = list_to_linked([1, 2, 3, 4, 5])
        result = solution.reverseBetween(head, 2, 4)
        assert linked_to_list(result) == [1, 4, 3, 2, 5]

    def test_example_2(self, solution):
        """Example 2 from problem description: single node"""
        head = list_to_linked([5])
        result = solution.reverseBetween(head, 1, 1)
        assert linked_to_list(result) == [5]

    def test_reverse_entire_list(self, solution):
        """Test reversing the entire list"""
        head = list_to_linked([1, 2, 3, 4, 5])
        result = solution.reverseBetween(head, 1, 5)
        assert linked_to_list(result) == [5, 4, 3, 2, 1]

    def test_reverse_single_node(self, solution):
        """Test reversing a single node (left == right)"""
        head = list_to_linked([1, 2, 3, 4, 5])
        result = solution.reverseBetween(head, 3, 3)
        assert linked_to_list(result) == [1, 2, 3, 4, 5]

    def test_reverse_from_start(self, solution):
        """Test reversing from the start of list"""
        head = list_to_linked([1, 2, 3, 4, 5])
        result = solution.reverseBetween(head, 1, 3)
        assert linked_to_list(result) == [3, 2, 1, 4, 5]

    def test_reverse_to_end(self, solution):
        """Test reversing to the end of list"""
        head = list_to_linked([1, 2, 3, 4, 5])
        result = solution.reverseBetween(head, 3, 5)
        assert linked_to_list(result) == [1, 2, 5, 4, 3]

    def test_two_nodes_reverse_both(self, solution):
        """Test two node list, reverse both"""
        head = list_to_linked([1, 2])
        result = solution.reverseBetween(head, 1, 2)
        assert linked_to_list(result) == [2, 1]

    def test_reverse_two_adjacent(self, solution):
        """Test reversing two adjacent nodes in middle"""
        head = list_to_linked([1, 2, 3, 4, 5])
        result = solution.reverseBetween(head, 2, 3)
        assert linked_to_list(result) == [1, 3, 2, 4, 5]

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
