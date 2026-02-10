"""
Tests for LeetCode Problem #399: Evaluate Division
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA




class TestEvaluateDivision:
    """Test cases for Evaluate Division problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        equations = [["a","b"],["b","c"]]
        values = [2.0,3.0]
        queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
        expected = [6.00000,0.50000,-1.00000,1.00000,-1.00000]
        result = solution.calcEquation(equations, values, queries)
        assert len(result) == len(expected)
        for r, e in zip(result, expected):
            assert abs(r - e) < 1e-5


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        equations = [["a","b"],["b","c"],["bc","cd"]]
        values = [1.5,2.5,5.0]
        queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
        expected = [3.75000,0.40000,5.00000,0.20000]
        result = solution.calcEquation(equations, values, queries)
        assert len(result) == len(expected)
        for r, e in zip(result, expected):
            assert abs(r - e) < 1e-5


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        equations = [["a","b"]]
        values = [0.5]
        queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
        expected = [0.50000,2.00000,-1.00000,-1.00000]
        result = solution.calcEquation(equations, values, queries)
        assert len(result) == len(expected)
        for r, e in zip(result, expected):
            assert abs(r - e) < 1e-5


    def test_self_division(self, solution):
        """Test x/x = 1 for existing variable"""
        equations = [["a","b"]]
        values = [2.0]
        queries = [["a","a"],["b","b"]]
        expected = [1.0, 1.0]
        result = solution.calcEquation(equations, values, queries)
        assert len(result) == len(expected)
        for r, e in zip(result, expected):
            assert abs(r - e) < 1e-5


    # Edge cases
    def test_unknown_variable_in_query(self, solution):
        """Query with unknown variable returns -1"""
        equations = [["a", "b"]]
        values = [2.0]
        queries = [["x", "y"], ["a", "z"]]
        expected = [-1.0, -1.0]
        result = solution.calcEquation(equations, values, queries)
        assert result == expected

    def test_single_equation(self, solution):
        """Single equation with forward and backward queries"""
        equations = [["x", "y"]]
        values = [3.0]
        queries = [["x", "y"], ["y", "x"]]
        expected = [3.0, 1.0 / 3.0]
        result = solution.calcEquation(equations, values, queries)
        for r, e in zip(result, expected):
            assert abs(r - e) < 1e-5

    def test_transitive_division(self, solution):
        """Transitive path: a/c = (a/b) * (b/c)"""
        equations = [["a", "b"], ["b", "c"], ["c", "d"]]
        values = [2.0, 3.0, 4.0]
        queries = [["a", "d"]]  # a/d = 2 * 3 * 4 = 24
        expected = [24.0]
        result = solution.calcEquation(equations, values, queries)
        assert abs(result[0] - expected[0]) < 1e-5

    def test_disconnected_components(self, solution):
        """Two separate components, cross-component query returns -1"""
        equations = [["a", "b"], ["c", "d"]]
        values = [2.0, 3.0]
        queries = [["a", "b"], ["c", "d"], ["a", "c"]]
        expected = [2.0, 3.0, -1.0]
        result = solution.calcEquation(equations, values, queries)
        for r, e in zip(result, expected):
            assert abs(r - e) < 1e-5

    def test_same_variable_unknown(self, solution):
        """x/x where x is not in any equation returns -1"""
        equations = [["a", "b"]]
        values = [2.0]
        queries = [["x", "x"]]
        expected = [-1.0]
        result = solution.calcEquation(equations, values, queries)
        assert result == expected

    def test_cyclic_graph(self, solution):
        """Graph with cycle - should still work"""
        equations = [["a", "b"], ["b", "c"], ["c", "a"]]
        values = [2.0, 3.0, 1.0 / 6.0]  # a/b=2, b/c=3, c/a=1/6
        queries = [["a", "c"], ["c", "b"]]
        # a/c = a/b * b/c = 2 * 3 = 6
        # c/b = 1/3
        expected = [6.0, 1.0 / 3.0]
        result = solution.calcEquation(equations, values, queries)
        for r, e in zip(result, expected):
            assert abs(r - e) < 1e-5

    def test_fractional_values(self, solution):
        """Equations with fractional values"""
        equations = [["a", "b"]]
        values = [0.5]
        queries = [["a", "b"], ["b", "a"]]
        expected = [0.5, 2.0]
        result = solution.calcEquation(equations, values, queries)
        for r, e in zip(result, expected):
            assert abs(r - e) < 1e-5

    def test_longer_path(self, solution):
        """Longer path requires multiple hops"""
        equations = [["a", "b"], ["b", "c"], ["c", "d"], ["d", "e"]]
        values = [2.0, 2.0, 2.0, 2.0]
        queries = [["a", "e"]]  # a/e = 2^4 = 16
        expected = [16.0]
        result = solution.calcEquation(equations, values, queries)
        assert abs(result[0] - expected[0]) < 1e-5

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
