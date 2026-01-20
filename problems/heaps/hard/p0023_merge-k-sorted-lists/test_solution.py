"""
Tests for LeetCode Problem #23: Merge k Sorted Lists
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


class TestMergeKSortedLists:
    """Test cases for Merge k Sorted Lists problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        lists = [
            list_to_linked([1, 4, 5]),
            list_to_linked([1, 3, 4]),
            list_to_linked([2, 6])
        ]
        result = solution.mergeKLists(lists)
        assert linked_to_list(result) == [1, 1, 2, 3, 4, 4, 5, 6]

    def test_example_2(self, solution):
        """Example 2: Empty input"""
        result = solution.mergeKLists([])
        assert result is None

    def test_example_3(self, solution):
        """Example 3: List with empty list"""
        result = solution.mergeKLists([None])
        assert result is None

    def test_single_list(self, solution):
        """Single list"""
        lists = [list_to_linked([1, 2, 3])]
        result = solution.mergeKLists(lists)
        assert linked_to_list(result) == [1, 2, 3]

    def test_two_lists(self, solution):
        """Two lists"""
        lists = [
            list_to_linked([1, 3, 5]),
            list_to_linked([2, 4, 6])
        ]
        result = solution.mergeKLists(lists)
        assert linked_to_list(result) == [1, 2, 3, 4, 5, 6]

    def test_lists_with_duplicates(self, solution):
        """Lists with duplicate values"""
        lists = [
            list_to_linked([1, 1, 1]),
            list_to_linked([1, 1, 1])
        ]
        result = solution.mergeKLists(lists)
        assert linked_to_list(result) == [1, 1, 1, 1, 1, 1]

    def test_negative_numbers(self, solution):
        """Lists with negative numbers"""
        lists = [
            list_to_linked([-3, -1, 2]),
            list_to_linked([-2, 0, 3])
        ]
        result = solution.mergeKLists(lists)
        assert linked_to_list(result) == [-3, -2, -1, 0, 2, 3]

    def test_mixed_empty_lists(self, solution):
        """Mix of empty and non-empty lists"""
        lists = [
            None,
            list_to_linked([1, 2]),
            None,
            list_to_linked([3, 4])
        ]
        result = solution.mergeKLists(lists)
        assert linked_to_list(result) == [1, 2, 3, 4]

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
