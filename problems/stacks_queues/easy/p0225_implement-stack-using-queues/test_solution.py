"""
Tests for LeetCode Problem #225: Implement Stack using Queues
"""

import pytest
from solution import MyStack, PROBLEM_METADATA


class TestImplementStackUsingQueues:
    """Test cases for Implement Stack using Queues problem"""

    def test_example_1(self):
        """Example from problem description"""
        stack = MyStack()
        stack.push(1)
        stack.push(2)
        assert stack.top() == 2
        assert stack.pop() == 2
        assert stack.empty() == False

    def test_push_and_pop(self):
        """Test push and pop operations"""
        stack = MyStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1

    def test_top_multiple(self):
        """Top should return same value without modifying stack"""
        stack = MyStack()
        stack.push(5)
        assert stack.top() == 5
        assert stack.top() == 5
        assert stack.empty() == False

    def test_empty(self):
        """Test empty on new and emptied stack"""
        stack = MyStack()
        assert stack.empty() == True
        stack.push(1)
        assert stack.empty() == False
        stack.pop()
        assert stack.empty() == True

    def test_single_element(self):
        """Single element operations"""
        stack = MyStack()
        stack.push(42)
        assert stack.top() == 42
        assert stack.pop() == 42
        assert stack.empty() == True

    # Additional edge case tests
    def test_empty_stack_is_empty(self):
        """Empty stack should return True for empty()"""
        stack = MyStack()
        assert stack.empty() == True

    def test_push_pop_sequence(self):
        """Test alternating push/pop operations"""
        stack = MyStack()
        stack.push(1)
        assert stack.pop() == 1
        stack.push(2)
        stack.push(3)
        assert stack.pop() == 3
        stack.push(4)
        assert stack.pop() == 4
        assert stack.pop() == 2
        assert stack.empty() == True

    def test_peek_after_pop(self):
        """Peek should return new top after pop"""
        stack = MyStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.top() == 3
        stack.pop()
        assert stack.top() == 2
        stack.pop()
        assert stack.top() == 1

    def test_peek_does_not_modify(self):
        """Multiple peeks should not modify the stack"""
        stack = MyStack()
        stack.push(5)
        stack.push(10)
        for _ in range(5):
            assert stack.top() == 10
        assert stack.pop() == 10
        assert stack.pop() == 5

    def test_lifo_order_large(self):
        """Test LIFO order with more elements"""
        stack = MyStack()
        for i in range(1, 10):
            stack.push(i)
        for i in range(9, 0, -1):
            assert stack.pop() == i
        assert stack.empty() == True

    def test_push_after_empty(self):
        """Push after emptying the stack"""
        stack = MyStack()
        stack.push(1)
        stack.pop()
        assert stack.empty() == True
        stack.push(2)
        assert stack.empty() == False
        assert stack.top() == 2

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
