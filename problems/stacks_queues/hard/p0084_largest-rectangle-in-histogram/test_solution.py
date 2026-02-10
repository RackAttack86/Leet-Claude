"""
Tests for LeetCode Problem #84: Largest Rectangle in Histogram
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestLargestRectangleInHistogram:
    """Test cases for Largest Rectangle in Histogram problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        heights = [2, 1, 5, 6, 2, 3]
        expected = 10
        assert solution.largestRectangleArea(heights) == expected

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        heights = [2, 4]
        expected = 4
        assert solution.largestRectangleArea(heights) == expected

    # Edge cases
    def test_edge_case_single_bar(self, solution):
        """Single bar in histogram"""
        heights = [5]
        expected = 5
        assert solution.largestRectangleArea(heights) == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
