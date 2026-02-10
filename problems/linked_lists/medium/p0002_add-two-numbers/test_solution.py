"""
Tests for LeetCode Problem #2: Add Two Numbers
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
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


class TestAddTwoNumbers:
    """Test cases for Add Two Numbers problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        l1 = list_to_linked([2,4,3])
        l2 = list_to_linked([5,6,4])
        expected = [7,0,8]
        result = solution.addTwoNumbers(l1, l2)
        assert linked_to_list(result) == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        l1 = list_to_linked([0])
        l2 = list_to_linked([0])
        expected = [0]
        result = solution.addTwoNumbers(l1, l2)
        assert linked_to_list(result) == expected


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        l1 = list_to_linked([9,9,9,9,9,9,9])
        l2 = list_to_linked([9,9,9,9])
        expected = [8,9,9,9,0,0,0,1]
        result = solution.addTwoNumbers(l1, l2)
        assert linked_to_list(result) == expected


    def test_carry_propagation(self, solution):
        """Test carry propagation through multiple digits"""
        # 99 + 1 = 100
        l1 = list_to_linked([9, 9])
        l2 = list_to_linked([1])
        expected = [0, 0, 1]
        result = solution.addTwoNumbers(l1, l2)
        assert linked_to_list(result) == expected

    def test_different_lengths(self, solution):
        """Test lists with different lengths"""
        # 123 + 4567 = 4690
        l1 = list_to_linked([3, 2, 1])
        l2 = list_to_linked([7, 6, 5, 4])
        expected = [0, 9, 6, 4]
        result = solution.addTwoNumbers(l1, l2)
        assert linked_to_list(result) == expected

    def test_result_longer_than_inputs(self, solution):
        """Test where result has more digits than either input"""
        # 999 + 999 = 1998
        l1 = list_to_linked([9, 9, 9])
        l2 = list_to_linked([9, 9, 9])
        expected = [8, 9, 9, 1]
        result = solution.addTwoNumbers(l1, l2)
        assert linked_to_list(result) == expected

    def test_single_digit_no_carry(self, solution):
        """Test single digit addition without carry"""
        l1 = list_to_linked([3])
        l2 = list_to_linked([4])
        expected = [7]
        result = solution.addTwoNumbers(l1, l2)
        assert linked_to_list(result) == expected

    def test_single_digit_with_carry(self, solution):
        """Test single digit addition with carry"""
        l1 = list_to_linked([7])
        l2 = list_to_linked([8])
        expected = [5, 1]
        result = solution.addTwoNumbers(l1, l2)
        assert linked_to_list(result) == expected


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
