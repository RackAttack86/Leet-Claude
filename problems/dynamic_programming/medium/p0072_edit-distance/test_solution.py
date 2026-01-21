"""
Tests for LeetCode Problem #72: Edit Distance
"""

import pytest
from .solution import Solution, PROBLEM_METADATA




class TestEditDistance:
    """Test cases for Edit Distance problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        word1 = "horse"
        word2 = "ros"
        expected = 3
        result = solution.minDistance(word1, word2)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        word1 = "intention"
        word2 = "execution"
        expected = 5
        result = solution.minDistance(word1, word2)
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
