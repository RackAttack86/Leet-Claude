"""
Tests for LeetCode Problem #21: Merge Two Sorted Lists
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


class TestMergeTwoSortedLists:
    """Test cases for Merge Two Sorted Lists problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1: [1,2,4] + [1,3,4] = [1,1,2,3,4,4]"""
        list1 = list_to_linked([1, 2, 4])
        list2 = list_to_linked([1, 3, 4])
        result = solution.mergeTwoLists(list1, list2)
        assert linked_to_list(result) == [1, 1, 2, 3, 4, 4]

    def test_example_2(self, solution):
        """Example 2: Both empty lists"""
        result = solution.mergeTwoLists(None, None)
        assert result is None

    def test_example_3(self, solution):
        """Example 3: One empty list"""
        list2 = list_to_linked([0])
        result = solution.mergeTwoLists(None, list2)
        assert linked_to_list(result) == [0]

    def test_first_empty(self, solution):
        """First list is empty"""
        list2 = list_to_linked([1, 2, 3])
        result = solution.mergeTwoLists(None, list2)
        assert linked_to_list(result) == [1, 2, 3]

    def test_second_empty(self, solution):
        """Second list is empty"""
        list1 = list_to_linked([1, 2, 3])
        result = solution.mergeTwoLists(list1, None)
        assert linked_to_list(result) == [1, 2, 3]

    def test_single_elements(self, solution):
        """Both lists have single element"""
        list1 = list_to_linked([1])
        list2 = list_to_linked([2])
        result = solution.mergeTwoLists(list1, list2)
        assert linked_to_list(result) == [1, 2]

    # Edge case tests
    def test_two_nodes_interleaved(self, solution):
        """Two nodes each, values interleaved"""
        list1 = list_to_linked([1, 3])
        list2 = list_to_linked([2, 4])
        result = solution.mergeTwoLists(list1, list2)
        assert linked_to_list(result) == [1, 2, 3, 4]

    def test_all_same_values(self, solution):
        """Both lists have all same values"""
        list1 = list_to_linked([2, 2, 2])
        list2 = list_to_linked([2, 2])
        result = solution.mergeTwoLists(list1, list2)
        assert linked_to_list(result) == [2, 2, 2, 2, 2]

    def test_first_list_all_smaller(self, solution):
        """All elements of first list smaller than second"""
        list1 = list_to_linked([1, 2, 3])
        list2 = list_to_linked([4, 5, 6])
        result = solution.mergeTwoLists(list1, list2)
        assert linked_to_list(result) == [1, 2, 3, 4, 5, 6]

    def test_first_list_all_larger(self, solution):
        """All elements of first list larger than second"""
        list1 = list_to_linked([4, 5, 6])
        list2 = list_to_linked([1, 2, 3])
        result = solution.mergeTwoLists(list1, list2)
        assert linked_to_list(result) == [1, 2, 3, 4, 5, 6]

    def test_negative_values(self, solution):
        """Lists with negative values"""
        list1 = list_to_linked([-5, -3, 0])
        list2 = list_to_linked([-4, -2, 1])
        result = solution.mergeTwoLists(list1, list2)
        assert linked_to_list(result) == [-5, -4, -3, -2, 0, 1]

    def test_long_lists(self, solution):
        """Longer lists"""
        list1 = list_to_linked(list(range(0, 20, 2)))  # [0, 2, 4, ..., 18]
        list2 = list_to_linked(list(range(1, 20, 2)))  # [1, 3, 5, ..., 19]
        result = solution.mergeTwoLists(list1, list2)
        assert linked_to_list(result) == list(range(20))

    def test_unequal_lengths(self, solution):
        """Lists with very different lengths"""
        list1 = list_to_linked([1])
        list2 = list_to_linked([2, 3, 4, 5, 6, 7, 8, 9, 10])
        result = solution.mergeTwoLists(list1, list2)
        assert linked_to_list(result) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_duplicates_across_lists(self, solution):
        """Same values appearing in both lists"""
        list1 = list_to_linked([1, 3, 5])
        list2 = list_to_linked([1, 3, 5])
        result = solution.mergeTwoLists(list1, list2)
        assert linked_to_list(result) == [1, 1, 3, 3, 5, 5]

    def test_boundary_values(self, solution):
        """Boundary values from constraints (-100 to 100)"""
        list1 = list_to_linked([-100, 0, 100])
        list2 = list_to_linked([-50, 50])
        result = solution.mergeTwoLists(list1, list2)
        assert linked_to_list(result) == [-100, -50, 0, 50, 100]

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
