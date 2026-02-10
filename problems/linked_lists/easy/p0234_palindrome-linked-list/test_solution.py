"""
Tests for LeetCode Problem #234: Palindrome Linked List
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


class TestPalindromeLinkedList:
    """Test cases for Palindrome Linked List problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1: [1,2,2,1] is palindrome"""
        head = list_to_linked([1, 2, 2, 1])
        assert solution.isPalindrome(head) == True

    def test_example_2(self, solution):
        """Example 2: [1,2] is not palindrome"""
        head = list_to_linked([1, 2])
        assert solution.isPalindrome(head) == False

    def test_single_element(self, solution):
        """Single element is palindrome"""
        head = list_to_linked([1])
        assert solution.isPalindrome(head) == True

    def test_two_same_elements(self, solution):
        """Two same elements is palindrome"""
        head = list_to_linked([1, 1])
        assert solution.isPalindrome(head) == True

    def test_odd_length_palindrome(self, solution):
        """Odd length palindrome"""
        head = list_to_linked([1, 2, 3, 2, 1])
        assert solution.isPalindrome(head) == True

    def test_odd_length_not_palindrome(self, solution):
        """Odd length not palindrome"""
        head = list_to_linked([1, 2, 3, 4, 5])
        assert solution.isPalindrome(head) == False

    def test_empty_list(self, solution):
        """Empty list is palindrome"""
        assert solution.isPalindrome(None) == True

    # Edge case tests
    def test_three_elements_palindrome(self, solution):
        """Three element palindrome"""
        head = list_to_linked([1, 2, 1])
        assert solution.isPalindrome(head) == True

    def test_three_elements_not_palindrome(self, solution):
        """Three elements not palindrome"""
        head = list_to_linked([1, 2, 3])
        assert solution.isPalindrome(head) == False

    def test_four_elements_palindrome(self, solution):
        """Four element palindrome"""
        head = list_to_linked([1, 2, 2, 1])
        assert solution.isPalindrome(head) == True

    def test_four_elements_not_palindrome(self, solution):
        """Four elements not palindrome"""
        head = list_to_linked([1, 2, 3, 4])
        assert solution.isPalindrome(head) == False

    def test_all_same_values(self, solution):
        """All same values is palindrome"""
        head = list_to_linked([5, 5, 5, 5, 5])
        assert solution.isPalindrome(head) == True

    def test_two_different_elements(self, solution):
        """Two different elements not palindrome"""
        head = list_to_linked([1, 2])
        assert solution.isPalindrome(head) == False

    def test_long_palindrome_even(self, solution):
        """Long even length palindrome"""
        vals = list(range(10)) + list(range(9, -1, -1))
        head = list_to_linked(vals)
        assert solution.isPalindrome(head) == True

    def test_long_palindrome_odd(self, solution):
        """Long odd length palindrome"""
        vals = list(range(10)) + [10] + list(range(9, -1, -1))
        head = list_to_linked(vals)
        assert solution.isPalindrome(head) == True

    def test_long_not_palindrome(self, solution):
        """Long list not palindrome"""
        head = list_to_linked(list(range(20)))
        assert solution.isPalindrome(head) == False

    def test_almost_palindrome_off_by_one(self, solution):
        """Almost palindrome but differs in middle"""
        head = list_to_linked([1, 2, 3, 4, 2, 1])
        assert solution.isPalindrome(head) == False

    def test_almost_palindrome_off_at_end(self, solution):
        """Almost palindrome but differs at end"""
        head = list_to_linked([1, 2, 3, 3, 2, 2])
        assert solution.isPalindrome(head) == False

    def test_single_digit_values(self, solution):
        """Values within 0-9 range (constraint)"""
        head = list_to_linked([0, 1, 2, 3, 3, 2, 1, 0])
        assert solution.isPalindrome(head) == True

    def test_boundary_values(self, solution):
        """Boundary values 0 and 9"""
        head = list_to_linked([0, 9, 9, 0])
        assert solution.isPalindrome(head) == True

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
