"""
Tests for LeetCode Problem #739: Daily Temperatures
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestDailyTemperatures:
    """Test cases for Daily Temperatures problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
        expected = [1, 1, 4, 2, 1, 1, 0, 0]
        assert solution.dailyTemperatures(temperatures) == expected

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        temperatures = [30, 40, 50, 60]
        expected = [1, 1, 1, 0]
        assert solution.dailyTemperatures(temperatures) == expected

    def test_example_3(self, solution):
        """Example 3 from problem description"""
        temperatures = [30, 60, 90]
        expected = [1, 1, 0]
        assert solution.dailyTemperatures(temperatures) == expected

    # Edge cases
    def test_edge_case_single_element(self, solution):
        """Single temperature - no warmer day"""
        temperatures = [50]
        expected = [0]
        assert solution.dailyTemperatures(temperatures) == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
