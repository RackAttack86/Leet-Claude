"""
Tests for LeetCode Problem #399: Evaluate Division
"""

import pytest
from .solution import Solution, PROBLEM_METADATA




class TestEvaluateDivision:
    """Test cases for Evaluate Division problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        equations = [["a","b"]
        values = [2.0,3.0]
        queries = [["a","c"]
        expected = [6.00000,0.50000,-1.00000,1.00000,-1.00000]
        result = solution.calcEquation(equations, values, queries)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        equations = [["a","b"]
        values = [1.5,2.5,5.0]
        queries = [["a","c"]
        expected = [3.75000,0.40000,5.00000,0.20000]
        result = solution.calcEquation(equations, values, queries)
        assert result == expected


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        equations = [["a","b"]
        values = [0.5]
        queries = [["a","b"]
        expected = [0.50000,2.00000,-1.00000,-1.00000]
        result = solution.calcEquation(equations, values, queries)
        assert result == expected


    def test_edge_case_empty(self, solution):
        """Test with empty/minimal input"""
        # TODO: Implement edge case test
        pass


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
