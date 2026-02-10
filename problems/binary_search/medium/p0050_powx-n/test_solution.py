"""
Tests for LeetCode Problem #50: Pow(x, n)
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA




class TestPowxN:
    """Test cases for Pow(x, n) problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        x = 2
        n = 10
        expected = 1024.00000
        result = solution.myPow(x, n)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        x = 2.1
        n = 3
        expected = 9.261
        result = solution.myPow(x, n)
        assert abs(result - expected) < 1e-5


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        x = 2
        n = -2
        expected = 0.25000
        result = solution.myPow(x, n)
        assert result == expected


    def test_edge_case_zero_exponent(self, solution):
        """Test with n = 0, should return 1"""
        x = 5.0
        n = 0
        expected = 1.0
        result = solution.myPow(x, n)
        assert result == expected

    def test_edge_case_one_exponent(self, solution):
        """Test with n = 1, should return x"""
        x = 3.5
        n = 1
        expected = 3.5
        result = solution.myPow(x, n)
        assert abs(result - expected) < 1e-5


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
