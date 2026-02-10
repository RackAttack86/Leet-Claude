"""
Tests for LeetCode Problem #11: Container With Most Water
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestContainerWithMostWater:
    """Test cases for Container With Most Water problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        result = solution.maxArea(height)
        assert result == 49, f"Expected 49 but got {result}"

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        height = [1, 1]
        result = solution.maxArea(height)
        assert result == 1, f"Expected 1 but got {result}"

    # Edge cases
    def test_edge_case_1(self, solution):
        """Test with two different heights"""
        height = [1, 2]
        result = solution.maxArea(height)
        assert result == 1, f"Expected 1 but got {result}"

    def test_edge_case_2(self, solution):
        """Test with increasing heights"""
        height = [1, 2, 3, 4, 5]
        result = solution.maxArea(height)
        assert result == 6, f"Expected 6 but got {result}"

    def test_edge_case_3(self, solution):
        """Test with all same heights"""
        height = [5, 5, 5, 5]
        result = solution.maxArea(height)
        assert result == 15, f"Expected 15 but got {result}"

    def test_edge_case_4(self, solution):
        """Test with tall bars at edges"""
        height = [8, 1, 1, 1, 8]
        result = solution.maxArea(height)
        assert result == 32, f"Expected 32 but got {result}"

    def test_edge_case_5(self, solution):
        """Test with decreasing heights"""
        height = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        result = solution.maxArea(height)
        assert result == 20, f"Expected 20 but got {result}"

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
