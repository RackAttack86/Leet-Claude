"""
Tests for LeetCode Problem #61: Rotate List
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


class TestRotateList:
    """Test cases for Rotate List problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        head = list_to_linked([1,2,3,4,5])
        k = 2
        expected = [4,5,1,2,3]
        result = solution.rotateRight(head, k)
        assert linked_to_list(result) == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        head = list_to_linked([0,1,2])
        k = 4
        expected = [2,0,1]
        result = solution.rotateRight(head, k)
        assert linked_to_list(result) == expected


    def test_k_equals_zero(self, solution):
        """Test rotation with k=0 (no rotation)"""
        head = list_to_linked([1, 2, 3, 4, 5])
        result = solution.rotateRight(head, 0)
        assert linked_to_list(result) == [1, 2, 3, 4, 5]

    def test_k_equals_length(self, solution):
        """Test k equals list length (full rotation, same as original)"""
        head = list_to_linked([1, 2, 3, 4, 5])
        result = solution.rotateRight(head, 5)
        assert linked_to_list(result) == [1, 2, 3, 4, 5]

    def test_k_greater_than_length(self, solution):
        """Test k greater than list length"""
        head = list_to_linked([1, 2, 3])
        result = solution.rotateRight(head, 7)  # 7 % 3 = 1
        assert linked_to_list(result) == [3, 1, 2]

    def test_empty_list(self, solution):
        """Test empty list"""
        result = solution.rotateRight(None, 5)
        assert result is None

    def test_single_node(self, solution):
        """Test single node list"""
        head = list_to_linked([1])
        result = solution.rotateRight(head, 10)
        assert linked_to_list(result) == [1]

    def test_two_nodes_rotate_one(self, solution):
        """Test two node list rotated by 1"""
        head = list_to_linked([1, 2])
        result = solution.rotateRight(head, 1)
        assert linked_to_list(result) == [2, 1]

    def test_k_multiple_of_length(self, solution):
        """Test k is multiple of list length"""
        head = list_to_linked([1, 2, 3])
        result = solution.rotateRight(head, 6)  # 6 % 3 = 0
        assert linked_to_list(result) == [1, 2, 3]


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
