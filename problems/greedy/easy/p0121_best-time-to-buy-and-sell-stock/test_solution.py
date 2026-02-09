"""
Tests for LeetCode Problem #121: Best Time to Buy and Sell Stock
"""

import pytest
from solution import Solution, PROBLEM_METADATA




class TestBestTimeToBuyAndSellStock:
    """Test cases for Best Time to Buy and Sell Stock problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        prices = [7,1,5,3,6,4]
        expected = 5
        result = solution.maxProfit(prices)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        prices = [7,6,4,3,1]
        expected = 0
        result = solution.maxProfit(prices)
        assert result == expected


    def test_edge_case_single_price(self, solution):
        """Test with single price (minimal input)"""
        prices = [5]
        expected = 0  # Cannot buy and sell with single price
        result = solution.maxProfit(prices)
        assert result == expected


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
