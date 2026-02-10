"""
Tests for LeetCode Problem #224: Basic Calculator
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA




class TestBasicCalculator:
    """Test cases for Basic Calculator problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        s = "1 + 1"
        expected = 2
        result = solution.calculate(s)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        s = " 2-1 + 2 "
        expected = 3
        result = solution.calculate(s)
        assert result == expected


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        s = "(1+(4+5+2)-3)+(6+8)"
        expected = 23
        result = solution.calculate(s)
        assert result == expected


    def test_edge_case_single_number(self, solution):
        """Test with single number"""
        s = "42"
        expected = 42
        result = solution.calculate(s)
        assert result == expected


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
