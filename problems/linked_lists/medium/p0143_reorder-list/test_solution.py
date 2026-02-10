"""
Tests for LeetCode Problem #143: Reorder List
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA, ListNode


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


class TestReorderList:
    """Test cases for Reorder List problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description: [1,2,3,4] -> [1,4,2,3]"""
        head = list_to_linked([1, 2, 3, 4])
        solution.reorderList(head)
        assert linked_to_list(head) == [1, 4, 2, 3]

    def test_example_2(self, solution):
        """Example 2 from problem description: [1,2,3,4,5] -> [1,5,2,4,3]"""
        head = list_to_linked([1, 2, 3, 4, 5])
        solution.reorderList(head)
        assert linked_to_list(head) == [1, 5, 2, 4, 3]

    def test_single_node(self, solution):
        """Test single node list"""
        head = list_to_linked([1])
        solution.reorderList(head)
        assert linked_to_list(head) == [1]

    def test_two_nodes(self, solution):
        """Test two node list"""
        head = list_to_linked([1, 2])
        solution.reorderList(head)
        assert linked_to_list(head) == [1, 2]

    def test_three_nodes(self, solution):
        """Test three node list"""
        head = list_to_linked([1, 2, 3])
        solution.reorderList(head)
        assert linked_to_list(head) == [1, 3, 2]

    def test_six_nodes(self, solution):
        """Test six node list"""
        head = list_to_linked([1, 2, 3, 4, 5, 6])
        solution.reorderList(head)
        assert linked_to_list(head) == [1, 6, 2, 5, 3, 4]

    def test_empty_list(self, solution):
        """Test empty list (should not crash)"""
        head = None
        solution.reorderList(head)
        assert head is None

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
