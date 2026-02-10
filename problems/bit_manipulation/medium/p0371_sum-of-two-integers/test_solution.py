"""
Tests for LeetCode Problem #371: Sum of Two Integers
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestSumOfTwoIntegers:
    """Test cases for Sum of Two Integers problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        assert solution.getSum(1, 2) == 3

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        assert solution.getSum(2, 3) == 5

    # Edge cases
    def test_negative_plus_positive(self, solution):
        """Negative number plus positive number"""
        assert solution.getSum(-1, 5) == 4
        assert solution.getSum(-10, 3) == -7

    def test_positive_plus_negative(self, solution):
        """Positive number plus negative number"""
        assert solution.getSum(5, -3) == 2
        assert solution.getSum(10, -15) == -5

    def test_both_negative(self, solution):
        """Both numbers negative"""
        assert solution.getSum(-5, -3) == -8
        assert solution.getSum(-1, -1) == -2

    def test_zero_cases(self, solution):
        """Addition involving zero"""
        assert solution.getSum(0, 0) == 0
        assert solution.getSum(0, 5) == 5
        assert solution.getSum(5, 0) == 5
        assert solution.getSum(0, -5) == -5

    def test_boundary_values(self, solution):
        """Test with constraint boundary values"""
        assert solution.getSum(1000, 1000) == 2000
        assert solution.getSum(-1000, -1000) == -2000
        assert solution.getSum(-1000, 1000) == 0

    def test_cancel_out(self, solution):
        """Numbers that cancel each other out"""
        assert solution.getSum(100, -100) == 0
        assert solution.getSum(-50, 50) == 0

    def test_small_values(self, solution):
        """Small value additions"""
        assert solution.getSum(1, 1) == 2
        assert solution.getSum(-1, 1) == 0
        assert solution.getSum(1, -1) == 0

    def test_asymmetric_values(self, solution):
        """Asymmetric positive and negative values"""
        assert solution.getSum(-12, 7) == -5
        assert solution.getSum(7, -12) == -5

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
