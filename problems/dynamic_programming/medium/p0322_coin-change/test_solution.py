"""
Tests for LeetCode Problem #322: Coin Change
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestCoinChange:
    """Test cases for Coin Change problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        coins = [1, 2, 5]
        amount = 11
        assert solution.coinChange(coins, amount) == 3

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        coins = [2]
        amount = 3
        assert solution.coinChange(coins, amount) == -1

    # Edge cases
    def test_edge_case_1(self, solution):
        """Test with amount = 0"""
        coins = [1, 2, 5]
        amount = 0
        assert solution.coinChange(coins, amount) == 0

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
