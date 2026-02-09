"""
Tests for LeetCode Problem #232: Implement Queue using Stacks
"""

import pytest
from solution import MyQueue, PROBLEM_METADATA


class TestImplementQueueUsingStacks:
    """Test cases for Implement Queue using Stacks problem"""

    def test_example_1(self):
        """Example from problem description"""
        queue = MyQueue()
        queue.push(1)
        queue.push(2)
        assert queue.peek() == 1
        assert queue.pop() == 1
        assert queue.empty() == False

    def test_fifo_order(self):
        """Test FIFO order"""
        queue = MyQueue()
        queue.push(1)
        queue.push(2)
        queue.push(3)
        assert queue.pop() == 1
        assert queue.pop() == 2
        assert queue.pop() == 3

    def test_peek_multiple(self):
        """Peek should return same value without modifying queue"""
        queue = MyQueue()
        queue.push(5)
        assert queue.peek() == 5
        assert queue.peek() == 5
        assert queue.empty() == False

    def test_empty(self):
        """Test empty on new and emptied queue"""
        queue = MyQueue()
        assert queue.empty() == True
        queue.push(1)
        assert queue.empty() == False
        queue.pop()
        assert queue.empty() == True

    def test_interleaved_operations(self):
        """Test interleaved push and pop"""
        queue = MyQueue()
        queue.push(1)
        queue.push(2)
        assert queue.pop() == 1
        queue.push(3)
        assert queue.pop() == 2
        assert queue.pop() == 3

    # Additional edge case tests
    def test_empty_queue_is_empty(self):
        """Empty queue should return True for empty()"""
        queue = MyQueue()
        assert queue.empty() == True

    def test_alternating_push_pop(self):
        """Alternating push and pop operations"""
        queue = MyQueue()
        queue.push(1)
        assert queue.pop() == 1
        queue.push(2)
        assert queue.pop() == 2
        queue.push(3)
        assert queue.pop() == 3
        assert queue.empty() == True

    def test_peek_after_pop(self):
        """Peek should return new front after pop"""
        queue = MyQueue()
        queue.push(1)
        queue.push(2)
        queue.push(3)
        assert queue.peek() == 1
        queue.pop()
        assert queue.peek() == 2
        queue.pop()
        assert queue.peek() == 3

    def test_peek_does_not_modify(self):
        """Multiple peeks should not modify the queue"""
        queue = MyQueue()
        queue.push(5)
        queue.push(10)
        for _ in range(5):
            assert queue.peek() == 5
        assert queue.pop() == 5
        assert queue.pop() == 10

    def test_fifo_order_large(self):
        """Test FIFO order with more elements"""
        queue = MyQueue()
        for i in range(1, 10):
            queue.push(i)
        for i in range(1, 10):
            assert queue.pop() == i
        assert queue.empty() == True

    def test_push_after_empty(self):
        """Push after emptying the queue"""
        queue = MyQueue()
        queue.push(1)
        queue.pop()
        assert queue.empty() == True
        queue.push(2)
        assert queue.empty() == False
        assert queue.peek() == 2

    def test_batch_push_then_pop(self):
        """Push multiple, then pop all"""
        queue = MyQueue()
        queue.push(1)
        queue.push(2)
        queue.push(3)
        queue.push(4)
        queue.push(5)
        assert queue.pop() == 1
        assert queue.pop() == 2
        assert queue.pop() == 3
        assert queue.pop() == 4
        assert queue.pop() == 5
        assert queue.empty() == True

    def test_single_element_queue(self):
        """Single element operations"""
        queue = MyQueue()
        queue.push(42)
        assert queue.peek() == 42
        assert queue.pop() == 42
        assert queue.empty() == True

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
