"""
Tests for LeetCode Problem #121: Best Time to Buy and Sell Stock
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestBestTimeToBuyAndSellStock:
    """Test cases for Best Time to Buy and Sell Stock problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1: Buy at 1, sell at 6, profit = 5"""
        assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5

    def test_example_2(self, solution):
        """Example 2: Prices always decreasing, no profit"""
        assert solution.maxProfit([7, 6, 4, 3, 1]) == 0

    def test_single_price(self, solution):
        """Single price, no transaction possible"""
        assert solution.maxProfit([5]) == 0

    def test_two_prices_profit(self, solution):
        """Two prices with profit"""
        assert solution.maxProfit([1, 5]) == 4

    def test_two_prices_no_profit(self, solution):
        """Two prices, no profit"""
        assert solution.maxProfit([5, 1]) == 0

    def test_empty(self, solution):
        """Empty array"""
        assert solution.maxProfit([]) == 0

    def test_buy_and_sell_same_day(self, solution):
        """Same price, no profit"""
        assert solution.maxProfit([5, 5, 5, 5]) == 0

    # Additional edge case tests
    def test_ascending_prices(self, solution):
        """Strictly ascending prices - buy first, sell last"""
        assert solution.maxProfit([1, 2, 3, 4, 5]) == 4
        assert solution.maxProfit([1, 3, 5, 7, 9]) == 8

    def test_descending_prices(self, solution):
        """Strictly descending prices - no profit possible"""
        assert solution.maxProfit([5, 4, 3, 2, 1]) == 0
        assert solution.maxProfit([10, 8, 6, 4, 2]) == 0

    def test_min_at_end(self, solution):
        """Minimum price at the end"""
        assert solution.maxProfit([5, 10, 8, 6, 1]) == 5

    def test_max_at_beginning(self, solution):
        """Maximum price at the beginning"""
        assert solution.maxProfit([10, 5, 3, 2, 1]) == 0

    def test_valley_then_peak(self, solution):
        """Valley followed by peak"""
        assert solution.maxProfit([10, 2, 15, 3, 8]) == 13

    def test_multiple_valleys_and_peaks(self, solution):
        """Multiple valleys and peaks"""
        assert solution.maxProfit([3, 8, 2, 10, 1, 5]) == 8

    def test_large_profit(self, solution):
        """Large profit difference"""
        assert solution.maxProfit([1, 100]) == 99
        assert solution.maxProfit([0, 10000]) == 10000

    def test_same_min_multiple_times(self, solution):
        """Same minimum appears multiple times"""
        assert solution.maxProfit([2, 5, 2, 8, 2, 3]) == 6

    def test_same_max_multiple_times(self, solution):
        """Same maximum appears multiple times"""
        assert solution.maxProfit([1, 10, 2, 10, 3, 10]) == 9

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
