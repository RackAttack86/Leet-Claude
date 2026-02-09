"""
Tests for LeetCode Problem #123: Best Time to Buy and Sell Stock III
"""

import pytest
from solution import Solution, PROBLEM_METADATA




class TestBestTimeToBuyAndSellStockIii:
    """Test cases for Best Time to Buy and Sell Stock III problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        prices = [3,3,5,0,0,3,1,4]
        expected = 6
        result = solution.maxProfit(prices)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        prices = [1,2,3,4,5]
        expected = 4
        result = solution.maxProfit(prices)
        assert result == expected


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        prices = [7,6,4,3,1]
        expected = 0
        result = solution.maxProfit(prices)
        assert result == expected


    def test_single_price(self, solution):
        """Edge case: single price - no transaction possible"""
        prices = [5]
        expected = 0
        result = solution.maxProfit(prices)
        assert result == expected

    def test_two_prices_increasing(self, solution):
        """Edge case: two prices increasing - one transaction"""
        prices = [1, 5]
        expected = 4
        result = solution.maxProfit(prices)
        assert result == expected

    def test_two_prices_decreasing(self, solution):
        """Edge case: two prices decreasing - no profit"""
        prices = [5, 1]
        expected = 0
        result = solution.maxProfit(prices)
        assert result == expected

    def test_all_increasing(self, solution):
        """Edge case: all prices increasing - single transaction optimal"""
        prices = [1, 2, 3, 4, 5, 6]
        expected = 5  # Buy at 1, sell at 6
        result = solution.maxProfit(prices)
        assert result == expected

    def test_all_decreasing(self, solution):
        """Edge case: all prices decreasing - no profit"""
        prices = [6, 5, 4, 3, 2, 1]
        expected = 0
        result = solution.maxProfit(prices)
        assert result == expected

    def test_constant_prices(self, solution):
        """Edge case: all prices same - no profit"""
        prices = [5, 5, 5, 5, 5]
        expected = 0
        result = solution.maxProfit(prices)
        assert result == expected

    def test_empty_prices(self, solution):
        """Edge case: empty prices list"""
        prices = []
        expected = 0
        result = solution.maxProfit(prices)
        assert result == expected

    def test_two_distinct_peaks(self, solution):
        """Test two separate profit opportunities"""
        prices = [1, 5, 2, 8]
        expected = 10  # Buy at 1, sell at 5 (profit 4), buy at 2, sell at 8 (profit 6)
        result = solution.maxProfit(prices)
        assert result == expected

    def test_one_transaction_better(self, solution):
        """Test when one transaction is better than two"""
        prices = [1, 2, 3, 4, 5]
        expected = 4  # Buy at 1, sell at 5
        result = solution.maxProfit(prices)
        assert result == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
