"""
Tests for LeetCode Problem #70: Climbing Stairs
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestClimbingStairs:
    """Test cases for Climbing Stairs problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """n=2: Two ways (1+1 or 2)"""
        assert solution.climbStairs(2) == 2

    def test_example_2(self, solution):
        """n=3: Three ways (1+1+1, 1+2, 2+1)"""
        assert solution.climbStairs(3) == 3

    def test_one_step(self, solution):
        """n=1: Only one way"""
        assert solution.climbStairs(1) == 1

    def test_four_steps(self, solution):
        """n=4: Five ways"""
        assert solution.climbStairs(4) == 5

    def test_five_steps(self, solution):
        """n=5: Eight ways (Fibonacci pattern)"""
        assert solution.climbStairs(5) == 8

    def test_larger_input(self, solution):
        """n=10: Verify Fibonacci sequence holds"""
        assert solution.climbStairs(10) == 89

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
