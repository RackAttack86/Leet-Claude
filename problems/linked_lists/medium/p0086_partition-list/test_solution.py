"""
Tests for LeetCode Problem #86: Partition List
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


class TestPartitionList:
    """Test cases for Partition List problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        head = list_to_linked([1, 4, 3, 2, 5, 2])
        result = solution.partition(head, 3)
        assert linked_to_list(result) == [1, 2, 2, 4, 3, 5]

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        head = list_to_linked([2, 1])
        result = solution.partition(head, 2)
        assert linked_to_list(result) == [1, 2]

    def test_all_less_than_x(self, solution):
        """Test when all elements are less than x"""
        head = list_to_linked([1, 2, 3, 4, 5])
        result = solution.partition(head, 10)
        assert linked_to_list(result) == [1, 2, 3, 4, 5]

    def test_all_greater_than_or_equal_x(self, solution):
        """Test when all elements are >= x"""
        head = list_to_linked([5, 6, 7, 8, 9])
        result = solution.partition(head, 1)
        assert linked_to_list(result) == [5, 6, 7, 8, 9]

    def test_empty_list(self, solution):
        """Test empty list"""
        result = solution.partition(None, 3)
        assert result is None

    def test_single_node_less(self, solution):
        """Test single node less than x"""
        head = list_to_linked([1])
        result = solution.partition(head, 3)
        assert linked_to_list(result) == [1]

    def test_single_node_greater(self, solution):
        """Test single node greater than x"""
        head = list_to_linked([5])
        result = solution.partition(head, 3)
        assert linked_to_list(result) == [5]

    def test_all_equal_to_x(self, solution):
        """Test when all elements equal x"""
        head = list_to_linked([3, 3, 3])
        result = solution.partition(head, 3)
        assert linked_to_list(result) == [3, 3, 3]

    def test_alternating_less_greater(self, solution):
        """Test alternating less and greater values"""
        head = list_to_linked([1, 5, 2, 6, 3, 7])
        result = solution.partition(head, 4)
        assert linked_to_list(result) == [1, 2, 3, 5, 6, 7]

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
