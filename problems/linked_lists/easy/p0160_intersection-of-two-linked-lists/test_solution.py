"""
Tests for LeetCode Problem #160: Intersection of Two Linked Lists
"""

import pytest
from solution import Solution, PROBLEM_METADATA, ListNode


def create_intersecting_lists(valsA, valsB, skipA, skipB, intersection_vals):
    """Create two lists that intersect at a common node"""
    # Create the intersection part
    if not intersection_vals:
        # No intersection
        headA = None
        if valsA:
            headA = ListNode(valsA[0])
            curr = headA
            for val in valsA[1:]:
                curr.next = ListNode(val)
                curr = curr.next

        headB = None
        if valsB:
            headB = ListNode(valsB[0])
            curr = headB
            for val in valsB[1:]:
                curr.next = ListNode(val)
                curr = curr.next

        return headA, headB, None

    # Create intersection node
    intersect = ListNode(intersection_vals[0])
    curr = intersect
    for val in intersection_vals[1:]:
        curr.next = ListNode(val)
        curr = curr.next

    # Create list A up to intersection
    headA = None
    if valsA:
        headA = ListNode(valsA[0])
        curr = headA
        for i, val in enumerate(valsA[1:], 1):
            if i < skipA:
                curr.next = ListNode(val)
                curr = curr.next
        curr.next = intersect

    # Create list B up to intersection
    headB = None
    if valsB:
        headB = ListNode(valsB[0])
        curr = headB
        for i, val in enumerate(valsB[1:], 1):
            if i < skipB:
                curr.next = ListNode(val)
                curr = curr.next
        curr.next = intersect

    return headA, headB, intersect


class TestIntersectionOfTwoLinkedLists:
    """Test cases for Intersection of Two Linked Lists problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1: Lists intersect at node with value 8"""
        headA, headB, intersect = create_intersecting_lists(
            [4, 1], [5, 6, 1], 2, 3, [8, 4, 5]
        )
        result = solution.getIntersectionNode(headA, headB)
        assert result == intersect

    def test_no_intersection(self, solution):
        """No intersection between lists"""
        headA, headB, _ = create_intersecting_lists(
            [2, 6, 4], [1, 5], 3, 2, []
        )
        result = solution.getIntersectionNode(headA, headB)
        assert result is None

    def test_one_empty(self, solution):
        """One list is empty"""
        headB = ListNode(1)
        headB.next = ListNode(2)
        result = solution.getIntersectionNode(None, headB)
        assert result is None

    def test_both_empty(self, solution):
        """Both lists are empty"""
        result = solution.getIntersectionNode(None, None)
        assert result is None

    def test_same_single_node(self, solution):
        """Both lists are the same single node"""
        node = ListNode(1)
        result = solution.getIntersectionNode(node, node)
        assert result == node

    # Edge case tests
    def test_intersection_at_first_node_of_listA(self, solution):
        """Intersection at first node of listA (listA is part of listB)"""
        # Create listA
        intersect = ListNode(1)
        intersect.next = ListNode(2)
        intersect.next.next = ListNode(3)
        # listB prefix
        headB = ListNode(5)
        headB.next = ListNode(6)
        headB.next.next = intersect
        result = solution.getIntersectionNode(intersect, headB)
        assert result == intersect

    def test_two_single_nodes_no_intersection(self, solution):
        """Two single nodes that don't intersect"""
        headA = ListNode(1)
        headB = ListNode(2)
        result = solution.getIntersectionNode(headA, headB)
        assert result is None

    def test_intersection_at_last_node(self, solution):
        """Intersection only at the last node"""
        intersect = ListNode(10)
        headA = ListNode(1)
        headA.next = ListNode(2)
        headA.next.next = intersect
        headB = ListNode(5)
        headB.next = ListNode(6)
        headB.next.next = ListNode(7)
        headB.next.next.next = intersect
        result = solution.getIntersectionNode(headA, headB)
        assert result == intersect

    def test_different_length_lists_no_intersection(self, solution):
        """Lists of very different lengths with no intersection"""
        headA = ListNode(1)
        curr = headA
        for i in range(2, 20):
            curr.next = ListNode(i)
            curr = curr.next
        headB = ListNode(100)
        headB.next = ListNode(101)
        result = solution.getIntersectionNode(headA, headB)
        assert result is None

    def test_long_intersection(self, solution):
        """Long shared intersection section"""
        # Create long intersection
        intersect = ListNode(10)
        curr = intersect
        for i in range(11, 20):
            curr.next = ListNode(i)
            curr = curr.next
        # Short prefix for A
        headA = ListNode(1)
        headA.next = intersect
        # Short prefix for B
        headB = ListNode(5)
        headB.next = ListNode(6)
        headB.next.next = intersect
        result = solution.getIntersectionNode(headA, headB)
        assert result == intersect

    def test_same_length_lists_no_intersection(self, solution):
        """Same length lists with no intersection"""
        headA = ListNode(1)
        headA.next = ListNode(2)
        headA.next.next = ListNode(3)
        headB = ListNode(4)
        headB.next = ListNode(5)
        headB.next.next = ListNode(6)
        result = solution.getIntersectionNode(headA, headB)
        assert result is None

    def test_same_length_lists_with_intersection(self, solution):
        """Same length lists that intersect in middle"""
        intersect = ListNode(10)
        intersect.next = ListNode(11)
        headA = ListNode(1)
        headA.next = intersect
        headB = ListNode(5)
        headB.next = intersect
        result = solution.getIntersectionNode(headA, headB)
        assert result == intersect

    def test_one_list_is_prefix_of_other(self, solution):
        """One list is entirely contained in another"""
        headB = ListNode(1)
        curr = headB
        for i in range(2, 6):
            curr.next = ListNode(i)
            curr = curr.next
        # headA starts at second node of headB
        headA = headB.next.next
        result = solution.getIntersectionNode(headA, headB)
        assert result == headA

    def test_intersection_with_negative_values(self, solution):
        """Lists with negative values"""
        intersect = ListNode(-5)
        intersect.next = ListNode(-4)
        headA = ListNode(-10)
        headA.next = intersect
        headB = ListNode(-20)
        headB.next = ListNode(-15)
        headB.next.next = intersect
        result = solution.getIntersectionNode(headA, headB)
        assert result == intersect

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
