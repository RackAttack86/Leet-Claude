"""
Tests for LeetCode Problem #211: Design Add and Search Words Data Structure
"""

import pytest
from solution import Solution, PROBLEM_METADATA




class TestDesignAddAndSearchWordsDataStructure:
    """Test cases for Design Add and Search Words Data Structure problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        solution.addWord("bad")
        solution.addWord("dad")
        solution.addWord("mad")
        assert solution.search("pad") == False
        assert solution.search("bad") == True
        assert solution.search(".ad") == True
        assert solution.search("b..") == True

    def test_edge_case_empty(self, solution):
        """Test searching before adding any words"""
        assert solution.search("a") == False
        assert solution.search(".") == False


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
