"""
Tests for LeetCode Problem #135: Candy
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA




class TestCandy:
    """Test cases for Candy problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        ratings = [1,0,2]
        expected = 5
        result = solution.candy(ratings)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        ratings = [1,2,2]
        expected = 4
        result = solution.candy(ratings)
        assert result == expected


    def test_edge_case_single_child(self, solution):
        """Test with single child (minimal input)"""
        ratings = [5]
        expected = 1  # Single child gets 1 candy
        result = solution.candy(ratings)
        assert result == expected


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
