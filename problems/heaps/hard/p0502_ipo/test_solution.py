"""
Tests for LeetCode Problem #502: IPO
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestIpo:
    """Test cases for IPO problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        k = 2
        w = 0
        profits = [1, 2, 3]
        capital = [0, 1, 1]
        assert solution.findMaximizedCapital(k, w, profits, capital) == 4

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        k = 3
        w = 0
        profits = [1, 2, 3]
        capital = [0, 1, 2]
        assert solution.findMaximizedCapital(k, w, profits, capital) == 6

    # Edge cases
    def test_single_project(self, solution):
        """Single project that can be done"""
        k = 1
        w = 0
        profits = [5]
        capital = [0]
        assert solution.findMaximizedCapital(k, w, profits, capital) == 5

    def test_no_affordable_project(self, solution):
        """No project can be started with initial capital"""
        k = 2
        w = 0
        profits = [1, 2, 3]
        capital = [1, 2, 3]
        assert solution.findMaximizedCapital(k, w, profits, capital) == 0

    def test_k_larger_than_projects(self, solution):
        """k larger than number of projects"""
        k = 10
        w = 0
        profits = [1, 2, 3]
        capital = [0, 0, 0]
        assert solution.findMaximizedCapital(k, w, profits, capital) == 6

    def test_high_initial_capital(self, solution):
        """High initial capital - can do any project"""
        k = 2
        w = 100
        profits = [1, 2, 3]
        capital = [10, 20, 30]
        # With enough capital, pick highest profits: 3 + 2 = 5, plus initial 100
        assert solution.findMaximizedCapital(k, w, profits, capital) == 105

    def test_zero_profit_projects(self, solution):
        """Projects with zero profit"""
        k = 2
        w = 0
        profits = [0, 0, 1]
        capital = [0, 0, 0]
        assert solution.findMaximizedCapital(k, w, profits, capital) == 1

    def test_sequential_unlocking(self, solution):
        """Projects unlock sequentially"""
        k = 3
        w = 1
        profits = [2, 4, 6]
        capital = [1, 3, 7]
        # Start with 1, do project 0 (+2) = 3
        # Now can do project 1 (+4) = 7
        # Now can do project 2 (+6) = 13
        assert solution.findMaximizedCapital(k, w, profits, capital) == 13

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
