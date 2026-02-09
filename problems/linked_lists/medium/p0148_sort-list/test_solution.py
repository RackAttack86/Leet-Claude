"""
Tests for LeetCode Problem #148: Sort List
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


class TestSortList:
    """Test cases for Sort List problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        head = list_to_linked([4,2,1,3])
        expected = [1,2,3,4]
        result = solution.sortList(head)
        assert linked_to_list(result) == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        head = list_to_linked([-1,5,3,4,0])
        expected = [-1,0,3,4,5]
        result = solution.sortList(head)
        assert linked_to_list(result) == expected


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        head = list_to_linked([])
        expected = []
        result = solution.sortList(head)
        assert linked_to_list(result) == expected


    def test_edge_case_single_element(self, solution):
        """Test with single element list"""
        head = list_to_linked([1])
        expected = [1]
        result = solution.sortList(head)
        assert linked_to_list(result) == expected


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
