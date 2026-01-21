"""
Tests for LeetCode Problem #61: Rotate List
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


class TestRotateList:
    """Test cases for Rotate List problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        head = [1,2,3,4,5]
        k = 2
        expected = [4,5,1,2,3]
        result = solution.rotateRight(head, k)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        head = [0,1,2]
        k = 4
        expected = [2,0,1]
        result = solution.rotateRight(head, k)
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
