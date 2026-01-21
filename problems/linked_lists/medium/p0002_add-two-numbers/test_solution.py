"""
Tests for LeetCode Problem #2: Add Two Numbers
"""

import pytest
from .solution import Solution, PROBLEM_METADATA
from .solution import ListNode
from .solution import Node


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


class TestAddTwoNumbers:
    """Test cases for Add Two Numbers problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        l1 = [2,4,3]
        l2 = [5,6,4]
        expected = [7,0,8]
        result = solution.addTwoNumbers(l1, l2)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        l1 = [0]
        l2 = [0]
        expected = [0]
        result = solution.addTwoNumbers(l1, l2)
        assert result == expected


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        l1 = [9,9,9,9,9,9,9]
        l2 = [9,9,9,9]
        expected = [8,9,9,9,0,0,0,1]
        result = solution.addTwoNumbers(l1, l2)
        assert result == expected


    def test_edge_case_empty(self, solution):
        """Test with empty/minimal input"""
        # TODO: Implement edge case test
        pass


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
