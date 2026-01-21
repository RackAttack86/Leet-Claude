"""
Tests for LeetCode Problem #188: Best Time to Buy and Sell Stock IV
"""

import pytest
from .solution import Solution, PROBLEM_METADATA




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
