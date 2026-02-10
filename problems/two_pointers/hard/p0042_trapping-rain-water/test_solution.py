"""
Tests for LeetCode Problem #42: Trapping Rain Water
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestTrappingRainWater:
    """Test cases for Trapping Rain Water problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        height = [0,1,0,2,1,0,1,3,2,1,2,1]
        expected = 6
        result = solution.solve(height)
        assert result == expected

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        height = [4,2,0,3,2,5]
        expected = 9
        result = solution.solve(height)
        assert result == expected

    def test_no_water(self, solution):
        """Test with no water trapped"""
        height = [1,2,3,4,5]
        expected = 0
        result = solution.solve(height)
        assert result == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
