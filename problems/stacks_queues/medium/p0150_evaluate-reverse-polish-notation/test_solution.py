"""
Tests for LeetCode Problem #150: Evaluate Reverse Polish Notation
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestEvaluateReversePolishNotation:
    """Test cases for Evaluate Reverse Polish Notation problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        tokens = ["2", "1", "+", "3", "*"]
        expected = 9
        assert solution.evalRPN(tokens) == expected

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        tokens = ["4", "13", "5", "/", "+"]
        expected = 6
        assert solution.evalRPN(tokens) == expected

    # Edge cases
    def test_edge_case_single_number(self, solution):
        """Single number as input"""
        tokens = ["42"]
        expected = 42
        assert solution.evalRPN(tokens) == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
