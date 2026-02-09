"""
Tests for LeetCode Problem #1268: Search Suggestions System
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestSearchSuggestionsSystem:
    """Test cases for Search Suggestions System problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
        searchWord = "mouse"
        expected = [
            ["mobile", "moneypot", "monitor"],
            ["mobile", "moneypot", "monitor"],
            ["mouse", "mousepad"],
            ["mouse", "mousepad"],
            ["mouse", "mousepad"]
        ]
        assert solution.suggestedProducts(products, searchWord) == expected

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        products = ["havana"]
        searchWord = "havana"
        expected = [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]]
        assert solution.suggestedProducts(products, searchWord) == expected

    def test_edge_case_1(self, solution):
        """Test with no matching products"""
        products = ["apple", "banana", "cherry"]
        searchWord = "xyz"
        expected = [[], [], []]
        assert solution.suggestedProducts(products, searchWord) == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
