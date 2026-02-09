"""
Tests for LeetCode Problem #149: Max Points on a Line
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestMaxPointsOnALine:
    """Test cases for Max Points on a Line problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        points = [[1,1],[2,2],[3,3]]
        expected = 3
        result = solution.maxPoints(points)
        assert result == expected

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
        expected = 4
        result = solution.maxPoints(points)
        assert result == expected

    def test_single_point(self, solution):
        """Test with single point"""
        points = [[0,0]]
        expected = 1
        result = solution.maxPoints(points)
        assert result == expected

    def test_two_points(self, solution):
        """Test with two points"""
        points = [[0,0],[1,1]]
        expected = 2
        result = solution.maxPoints(points)
        assert result == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
