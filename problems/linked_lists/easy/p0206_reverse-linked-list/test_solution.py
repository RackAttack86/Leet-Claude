"""
Tests for LeetCode Problem #206: Reverse Linked List
"""

import pytest
try:
    from user_solution import Solution
except ImportError:
    from solution import Solution, ListNode, PROBLEM_METADATA


def list_to_array(head):
    """Convert linked list to array for comparison"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def array_to_list(arr):
    """Convert array to linked list"""
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


class TestReverseLinkedList:
    """Test cases for Reverse Linked List problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1: [1,2,3,4,5] -> [5,4,3,2,1]"""
        head = array_to_list([1, 2, 3, 4, 5])
        result = solution.reverseList(head)
        assert list_to_array(result) == [5, 4, 3, 2, 1]

    def test_example_2(self, solution):
        """Example 2: [1,2] -> [2,1]"""
        head = array_to_list([1, 2])
        result = solution.reverseList(head)
        assert list_to_array(result) == [2, 1]

    def test_empty_list(self, solution):
        """Empty list returns None"""
        assert solution.reverseList(None) is None

    def test_single_node(self, solution):
        """Single node stays the same"""
        head = ListNode(1)
        result = solution.reverseList(head)
        assert list_to_array(result) == [1]

    # Edge case tests
    def test_three_nodes(self, solution):
        """Three nodes"""
        head = array_to_list([1, 2, 3])
        result = solution.reverseList(head)
        assert list_to_array(result) == [3, 2, 1]

    def test_all_same_values(self, solution):
        """All nodes have same value"""
        head = array_to_list([5, 5, 5, 5])
        result = solution.reverseList(head)
        assert list_to_array(result) == [5, 5, 5, 5]

    def test_negative_values(self, solution):
        """List with negative values"""
        head = array_to_list([-3, -2, -1, 0, 1])
        result = solution.reverseList(head)
        assert list_to_array(result) == [1, 0, -1, -2, -3]

    def test_long_list(self, solution):
        """Long list"""
        vals = list(range(100))
        head = array_to_list(vals)
        result = solution.reverseList(head)
        assert list_to_array(result) == list(range(99, -1, -1))

    def test_already_reversed_pattern(self, solution):
        """Descending values (reverse of sorted)"""
        head = array_to_list([5, 4, 3, 2, 1])
        result = solution.reverseList(head)
        assert list_to_array(result) == [1, 2, 3, 4, 5]

    def test_alternating_values(self, solution):
        """Alternating high and low values"""
        head = array_to_list([1, 100, 2, 99, 3, 98])
        result = solution.reverseList(head)
        assert list_to_array(result) == [98, 3, 99, 2, 100, 1]

    def test_boundary_values(self, solution):
        """Boundary values from constraints"""
        head = array_to_list([-5000, 0, 5000])
        result = solution.reverseList(head)
        assert list_to_array(result) == [5000, 0, -5000]

    def test_two_nodes_same_value(self, solution):
        """Two nodes with same value"""
        head = array_to_list([7, 7])
        result = solution.reverseList(head)
        assert list_to_array(result) == [7, 7]

    def test_palindrome_values(self, solution):
        """Palindrome values remain palindrome after reverse"""
        head = array_to_list([1, 2, 3, 2, 1])
        result = solution.reverseList(head)
        assert list_to_array(result) == [1, 2, 3, 2, 1]

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
