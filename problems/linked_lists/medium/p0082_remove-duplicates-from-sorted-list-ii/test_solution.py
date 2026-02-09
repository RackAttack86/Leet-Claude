"""
Tests for LeetCode Problem #82: Remove Duplicates from Sorted List II
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


class TestRemoveDuplicatesFromSortedListIi:
    """Test cases for Remove Duplicates from Sorted List II problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        head = list_to_linked([1,2,3,3,4,4,5])
        expected = [1,2,5]
        result = solution.deleteDuplicates(head)
        assert linked_to_list(result) == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        head = list_to_linked([1,1,1,2,3])
        expected = [2,3]
        result = solution.deleteDuplicates(head)
        assert linked_to_list(result) == expected


    def test_all_duplicates(self, solution):
        """Test when all elements are duplicates"""
        head = list_to_linked([1, 1, 1, 1, 1])
        result = solution.deleteDuplicates(head)
        assert linked_to_list(result) == []

    def test_no_duplicates(self, solution):
        """Test when no elements are duplicates"""
        head = list_to_linked([1, 2, 3, 4, 5])
        result = solution.deleteDuplicates(head)
        assert linked_to_list(result) == [1, 2, 3, 4, 5]

    def test_empty_list(self, solution):
        """Test empty list"""
        result = solution.deleteDuplicates(None)
        assert result is None

    def test_single_node(self, solution):
        """Test single node list"""
        head = list_to_linked([1])
        result = solution.deleteDuplicates(head)
        assert linked_to_list(result) == [1]

    def test_two_same_nodes(self, solution):
        """Test two nodes with same value"""
        head = list_to_linked([1, 1])
        result = solution.deleteDuplicates(head)
        assert linked_to_list(result) == []

    def test_two_different_nodes(self, solution):
        """Test two nodes with different values"""
        head = list_to_linked([1, 2])
        result = solution.deleteDuplicates(head)
        assert linked_to_list(result) == [1, 2]

    def test_duplicates_at_start_and_end(self, solution):
        """Test duplicates at both ends"""
        head = list_to_linked([1, 1, 2, 3, 3])
        result = solution.deleteDuplicates(head)
        assert linked_to_list(result) == [2]

    def test_multiple_duplicate_groups(self, solution):
        """Test multiple groups of duplicates"""
        head = list_to_linked([1, 1, 2, 2, 3, 3, 4, 4])
        result = solution.deleteDuplicates(head)
        assert linked_to_list(result) == []


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
