"""
Tests for LeetCode Problem #19: Remove Nth Node From End of List
"""

import pytest
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


class TestRemoveNthNodeFromEndOfList:
    """Test cases for Remove Nth Node From End of List problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description: [1,2,3,4,5], n=2 -> [1,2,3,5]"""
        head = list_to_linked([1, 2, 3, 4, 5])
        result = solution.removeNthFromEnd(head, 2)
        assert linked_to_list(result) == [1, 2, 3, 5]

    def test_example_2(self, solution):
        """Example 2 from problem description: [1], n=1 -> []"""
        head = list_to_linked([1])
        result = solution.removeNthFromEnd(head, 1)
        assert linked_to_list(result) == []

    def test_example_3(self, solution):
        """Example 3: [1,2], n=1 -> [1]"""
        head = list_to_linked([1, 2])
        result = solution.removeNthFromEnd(head, 1)
        assert linked_to_list(result) == [1]

    def test_remove_head(self, solution):
        """Test removing the head node (nth from end equals list length)"""
        head = list_to_linked([1, 2, 3, 4, 5])
        result = solution.removeNthFromEnd(head, 5)
        assert linked_to_list(result) == [2, 3, 4, 5]

    def test_remove_tail(self, solution):
        """Test removing the tail node (n=1)"""
        head = list_to_linked([1, 2, 3, 4, 5])
        result = solution.removeNthFromEnd(head, 1)
        assert linked_to_list(result) == [1, 2, 3, 4]

    def test_single_node_remove(self, solution):
        """Test removing from single node list"""
        head = list_to_linked([42])
        result = solution.removeNthFromEnd(head, 1)
        assert linked_to_list(result) == []

    def test_two_nodes_remove_first(self, solution):
        """Test two node list, remove head"""
        head = list_to_linked([1, 2])
        result = solution.removeNthFromEnd(head, 2)
        assert linked_to_list(result) == [2]

    def test_two_nodes_remove_second(self, solution):
        """Test two node list, remove tail"""
        head = list_to_linked([1, 2])
        result = solution.removeNthFromEnd(head, 1)
        assert linked_to_list(result) == [1]

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
