"""
Tests for LeetCode Problem #155: Min Stack
"""

import pytest
from solution import MinStack, PROBLEM_METADATA


class TestMinStack:
    """Test cases for Min Stack problem"""

    def test_example_1(self):
        """Example 1 from problem description"""
        min_stack = MinStack()
        min_stack.push(-2)
        min_stack.push(0)
        min_stack.push(-3)
        assert min_stack.getMin() == -3
        min_stack.pop()
        assert min_stack.top() == 0
        assert min_stack.getMin() == -2

    def test_example_2(self):
        """Test with multiple push and pop operations"""
        min_stack = MinStack()
        min_stack.push(1)
        min_stack.push(2)
        assert min_stack.top() == 2
        assert min_stack.getMin() == 1
        min_stack.pop()
        assert min_stack.top() == 1
        assert min_stack.getMin() == 1

    # Edge cases
    def test_edge_case_single_element(self):
        """Single element in stack"""
        min_stack = MinStack()
        min_stack.push(42)
        assert min_stack.top() == 42
        assert min_stack.getMin() == 42

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
