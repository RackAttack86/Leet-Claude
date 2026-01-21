"""
Tests for LeetCode Problem #123: Best Time to Buy and Sell Stock III
"""

import pytest
from .solution import Solution, PROBLEM_METADATA




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


    def test_edge_case_empty(self, solution):
        """Test with empty/minimal input"""
        # TODO: Implement edge case test
        pass


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
