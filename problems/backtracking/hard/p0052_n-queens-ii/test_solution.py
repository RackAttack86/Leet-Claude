"""
Tests for LeetCode Problem #52: N-Queens II
"""

import pytest
from solution import Solution, PROBLEM_METADATA




class TestNqueensIi:
    """Test cases for N-Queens II problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        n = 4
        expected = 2
        result = solution.totalNQueens(n)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        n = 1
        expected = 1
        result = solution.totalNQueens(n)
        assert result == expected


    def test_n_equals_1(self, solution):
        """Edge case: n=1 has exactly 1 solution"""
        n = 1
        expected = 1
        result = solution.totalNQueens(n)
        assert result == expected

    def test_n_equals_2(self, solution):
        """Edge case: n=2 has no valid solution"""
        n = 2
        expected = 0
        result = solution.totalNQueens(n)
        assert result == expected

    def test_n_equals_3(self, solution):
        """Edge case: n=3 has no valid solution"""
        n = 3
        expected = 0
        result = solution.totalNQueens(n)
        assert result == expected

    def test_n_equals_5(self, solution):
        """Test n=5 has 10 solutions"""
        n = 5
        expected = 10
        result = solution.totalNQueens(n)
        assert result == expected

    def test_n_equals_6(self, solution):
        """Test n=6 has 4 solutions"""
        n = 6
        expected = 4
        result = solution.totalNQueens(n)
        assert result == expected

    def test_n_equals_7(self, solution):
        """Test n=7 has 40 solutions"""
        n = 7
        expected = 40
        result = solution.totalNQueens(n)
        assert result == expected

    def test_n_equals_8(self, solution):
        """Test n=8 (classic 8-queens problem) has 92 solutions"""
        n = 8
        expected = 92
        result = solution.totalNQueens(n)
        assert result == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
