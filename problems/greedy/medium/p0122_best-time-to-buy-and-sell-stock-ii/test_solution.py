"""
Tests for LeetCode Problem #122: Best Time to Buy and Sell Stock II
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestBestTimeToBuyAndSellStockIi:
    """Test cases for Best Time to Buy and Sell Stock II problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        prices = [7, 1, 5, 3, 6, 4]
        assert solution.maxProfit(prices) == 7

    def test_example_2(self, solution):
        """Example 2 from problem description - always increasing"""
        prices = [1, 2, 3, 4, 5]
        assert solution.maxProfit(prices) == 4

    def test_example_3(self, solution):
        """Example 3 - always decreasing, no profit"""
        prices = [7, 6, 4, 3, 1]
        assert solution.maxProfit(prices) == 0

    # Edge cases
    def test_single_day(self, solution):
        """Single day - no transactions possible"""
        prices = [5]
        assert solution.maxProfit(prices) == 0

    def test_two_days_profit(self, solution):
        """Two days with profit"""
        prices = [1, 5]
        assert solution.maxProfit(prices) == 4

    def test_two_days_no_profit(self, solution):
        """Two days with no profit (decreasing)"""
        prices = [5, 1]
        assert solution.maxProfit(prices) == 0

    def test_all_same_price(self, solution):
        """All prices are the same - no profit possible"""
        prices = [5, 5, 5, 5, 5]
        assert solution.maxProfit(prices) == 0

    def test_always_increasing(self, solution):
        """Strictly increasing prices"""
        prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        assert solution.maxProfit(prices) == 9

    def test_always_decreasing(self, solution):
        """Strictly decreasing prices - no profit"""
        prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        assert solution.maxProfit(prices) == 0

    def test_alternating_prices(self, solution):
        """Alternating up and down"""
        prices = [1, 5, 1, 5, 1, 5]
        assert solution.maxProfit(prices) == 12

    def test_peak_and_valley(self, solution):
        """Classic peak and valley pattern"""
        prices = [3, 2, 6, 5, 0, 3]
        assert solution.maxProfit(prices) == 7

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
