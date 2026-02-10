"""
Tests for LeetCode Problem #188: Best Time to Buy and Sell Stock IV
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA




class TestBestTimeToBuyAndSellStockIv:
    """Test cases for Best Time to Buy and Sell Stock IV problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        k = 2
        prices = [2,4,1]
        expected = 2
        result = solution.maxProfit(k, prices)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        k = 2
        prices = [3,2,6,5,0,3]
        expected = 7
        result = solution.maxProfit(k, prices)
        assert result == expected


    def test_k_equals_zero(self, solution):
        """Edge case: k=0, no transactions allowed"""
        k = 0
        prices = [1, 2, 3, 4, 5]
        expected = 0
        result = solution.maxProfit(k, prices)
        assert result == expected

    def test_empty_prices(self, solution):
        """Edge case: empty prices list"""
        k = 2
        prices = []
        expected = 0
        result = solution.maxProfit(k, prices)
        assert result == expected

    def test_single_price(self, solution):
        """Edge case: single price - no transaction possible"""
        k = 2
        prices = [5]
        expected = 0
        result = solution.maxProfit(k, prices)
        assert result == expected

    def test_k_larger_than_needed(self, solution):
        """Edge case: k larger than n/2 (unlimited transactions)"""
        k = 100
        prices = [1, 2, 3, 4, 5]
        expected = 4  # Buy at 1, sell at 5 (or capture all increases: 1+1+1+1)
        result = solution.maxProfit(k, prices)
        assert result == expected

    def test_k_equals_one(self, solution):
        """Edge case: k=1, at most one transaction"""
        k = 1
        prices = [3, 2, 6, 5, 0, 3]
        expected = 4  # Buy at 2, sell at 6
        result = solution.maxProfit(k, prices)
        assert result == expected

    def test_all_decreasing(self, solution):
        """Edge case: all prices decreasing - no profit"""
        k = 3
        prices = [5, 4, 3, 2, 1]
        expected = 0
        result = solution.maxProfit(k, prices)
        assert result == expected

    def test_all_increasing(self, solution):
        """Edge case: all prices increasing"""
        k = 2
        prices = [1, 2, 3, 4, 5]
        expected = 4  # One transaction: buy at 1, sell at 5
        result = solution.maxProfit(k, prices)
        assert result == expected

    def test_constant_prices(self, solution):
        """Edge case: all prices same"""
        k = 2
        prices = [5, 5, 5, 5]
        expected = 0
        result = solution.maxProfit(k, prices)
        assert result == expected

    def test_multiple_small_profits(self, solution):
        """Test capturing multiple small profits with large k"""
        k = 10
        prices = [1, 2, 1, 2, 1, 2, 1, 2]
        expected = 4  # Buy/sell at each 1->2 transition
        result = solution.maxProfit(k, prices)
        assert result == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
