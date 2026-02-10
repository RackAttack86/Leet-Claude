"""
Tests for LeetCode Problem #208: Implement Trie (Prefix Tree)
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA




class TestImplementTriePrefixTree:
    """Test cases for Implement Trie (Prefix Tree) problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        solution.insert("apple")
        assert solution.search("apple") == True
        assert solution.search("app") == False
        assert solution.startsWith("app") == True
        solution.insert("app")
        assert solution.search("app") == True

    def test_edge_case_empty(self, solution):
        """Test searching before inserting any words"""
        assert solution.search("a") == False
        assert solution.startsWith("a") == False


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
