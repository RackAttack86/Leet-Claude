"""
Tests for LeetCode Problem #83: Remove Duplicates from Sorted List
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA, ListNode


def list_to_linked(vals):
    """Helper to convert list to linked list"""
    if not vals:
        return None
    head = ListNode(vals[0])
    current = head
    for val in vals[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_to_list(head):
    """Helper to convert linked list to list"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


class TestRemoveDuplicatesFromSortedList:
    """Test cases for Remove Duplicates from Sorted List problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1: [1,1,2] -> [1,2]"""
        head = list_to_linked([1, 1, 2])
        result = solution.deleteDuplicates(head)
        assert linked_to_list(result) == [1, 2]

    def test_example_2(self, solution):
        """Example 2: [1,1,2,3,3] -> [1,2,3]"""
        head = list_to_linked([1, 1, 2, 3, 3])
        result = solution.deleteDuplicates(head)
        assert linked_to_list(result) == [1, 2, 3]

    def test_empty_list(self, solution):
        """Empty list"""
        result = solution.deleteDuplicates(None)
        assert result is None

    def test_single_element(self, solution):
        """Single element list"""
        head = list_to_linked([1])
        result = solution.deleteDuplicates(head)
        assert linked_to_list(result) == [1]

    def test_no_duplicates(self, solution):
        """No duplicates in list"""
        head = list_to_linked([1, 2, 3])
        result = solution.deleteDuplicates(head)
        assert linked_to_list(result) == [1, 2, 3]

    def test_all_duplicates(self, solution):
        """All elements are the same"""
        head = list_to_linked([1, 1, 1, 1])
        result = solution.deleteDuplicates(head)
        assert linked_to_list(result) == [1]

    # Edge case tests
    def test_two_nodes_same(self, solution):
        """Two nodes with same value"""
        head = list_to_linked([1, 1])
        result = solution.deleteDuplicates(head)
        assert linked_to_list(result) == [1]

    def test_two_nodes_different(self, solution):
        """Two nodes with different values"""
        head = list_to_linked([1, 2])
        result = solution.deleteDuplicates(head)
        assert linked_to_list(result) == [1, 2]

    def test_consecutive_duplicates_at_start(self, solution):
        """Multiple duplicates at start"""
        head = list_to_linked([1, 1, 1, 2, 3])
        result = solution.deleteDuplicates(head)
        assert linked_to_list(result) == [1, 2, 3]

    def test_consecutive_duplicates_at_end(self, solution):
        """Multiple duplicates at end"""
        head = list_to_linked([1, 2, 3, 3, 3])
        result = solution.deleteDuplicates(head)
        assert linked_to_list(result) == [1, 2, 3]

    def test_consecutive_duplicates_in_middle(self, solution):
        """Multiple duplicates in middle"""
        head = list_to_linked([1, 2, 2, 2, 3])
        result = solution.deleteDuplicates(head)
        assert linked_to_list(result) == [1, 2, 3]

    def test_multiple_groups_of_duplicates(self, solution):
        """Multiple groups of duplicates"""
        head = list_to_linked([1, 1, 2, 2, 3, 3])
        result = solution.deleteDuplicates(head)
        assert linked_to_list(result) == [1, 2, 3]

    def test_negative_values(self, solution):
        """List with negative values"""
        head = list_to_linked([-3, -3, -1, -1, 0, 0, 1])
        result = solution.deleteDuplicates(head)
        assert linked_to_list(result) == [-3, -1, 0, 1]

    def test_long_list_all_same(self, solution):
        """Long list with all same values"""
        head = list_to_linked([5] * 20)
        result = solution.deleteDuplicates(head)
        assert linked_to_list(result) == [5]

    def test_long_list_no_duplicates(self, solution):
        """Long list with no duplicates"""
        vals = list(range(-10, 11))
        head = list_to_linked(vals)
        result = solution.deleteDuplicates(head)
        assert linked_to_list(result) == vals

    def test_alternating_duplicates(self, solution):
        """Every element has one duplicate"""
        head = list_to_linked([1, 1, 2, 2, 3, 3, 4, 4, 5, 5])
        result = solution.deleteDuplicates(head)
        assert linked_to_list(result) == [1, 2, 3, 4, 5]

    def test_boundary_values(self, solution):
        """Boundary values from constraints"""
        head = list_to_linked([-100, -100, 0, 100, 100])
        result = solution.deleteDuplicates(head)
        assert linked_to_list(result) == [-100, 0, 100]

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
