"""
Tests for LeetCode Problem #25: Reverse Nodes in k-Group
"""

import pytest
from solution import Solution, PROBLEM_METADATA
from solution import ListNode
from solution import Node


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


class TestReverseNodesInKgroup:
    """Test cases for Reverse Nodes in k-Group problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        head = list_to_linked([1,2,3,4,5])
        k = 2
        expected = [2,1,4,3,5]
        result = solution.reverseKGroup(head, k)
        assert linked_to_list(result) == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        head = list_to_linked([1,2,3,4,5])
        k = 3
        expected = [3,2,1,4,5]
        result = solution.reverseKGroup(head, k)
        assert linked_to_list(result) == expected


    def test_edge_case_k_equals_1(self, solution):
        """Test with k=1, list should remain unchanged"""
        head = list_to_linked([1, 2, 3, 4, 5])
        k = 1
        expected = [1, 2, 3, 4, 5]
        result = solution.reverseKGroup(head, k)
        assert linked_to_list(result) == expected

    def test_edge_case_empty_list(self, solution):
        """Test with empty list"""
        head = list_to_linked([])
        k = 2
        expected = []
        result = solution.reverseKGroup(head, k)
        assert linked_to_list(result) == expected


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
