"""
Tests for LeetCode Problem #50: Pow(x, n)
"""

import pytest
from .solution import Solution, PROBLEM_METADATA




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
        x = 2
        n = 3
        expected = 9.26100
        result = solution.myPow(x, n)
        assert result == expected


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        x = 2
        n = -2
        expected = 0.25000
        result = solution.myPow(x, n)
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
