"""
Tests for LeetCode Problem #202: Happy Number
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA




class TestHappyNumber:
    """Test cases for Happy Number problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        n = 19
        expected = True
        result = solution.isHappy(n)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        n = 2
        expected = False
        result = solution.isHappy(n)
        assert result == expected


    def test_edge_case_one(self, solution):
        """Test with n = 1 (already happy)"""
        n = 1
        expected = True
        result = solution.isHappy(n)
        assert result == expected


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
