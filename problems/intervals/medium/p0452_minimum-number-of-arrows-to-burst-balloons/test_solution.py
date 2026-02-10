"""
Tests for LeetCode Problem #452: Minimum Number of Arrows to Burst Balloons
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestMinimumNumberOfArrowsToBurstBalloons:
    """Test cases for Minimum Number of Arrows to Burst Balloons problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        points = [[10, 16], [2, 8], [1, 6], [7, 12]]
        assert solution.findMinArrowShots(points) == 2

    def test_example_2(self, solution):
        """Example 2 from problem description - no overlapping"""
        points = [[1, 2], [3, 4], [5, 6], [7, 8]]
        assert solution.findMinArrowShots(points) == 4

    def test_example_3(self, solution):
        """Example 3 - all overlapping at same point"""
        points = [[1, 2], [2, 3], [3, 4], [4, 5]]
        assert solution.findMinArrowShots(points) == 2

    # Edge cases
    def test_single_balloon(self, solution):
        """Single balloon - one arrow needed"""
        points = [[1, 5]]
        assert solution.findMinArrowShots(points) == 1

    def test_all_same_position(self, solution):
        """All balloons at the same position"""
        points = [[1, 5], [1, 5], [1, 5]]
        assert solution.findMinArrowShots(points) == 1

    def test_all_overlap_at_one_point(self, solution):
        """All balloons overlap at one common point"""
        points = [[1, 10], [5, 15], [8, 12]]
        assert solution.findMinArrowShots(points) == 1

    def test_no_overlapping_balloons(self, solution):
        """No overlapping - need one arrow per balloon"""
        points = [[1, 2], [4, 5], [7, 8], [10, 11]]
        assert solution.findMinArrowShots(points) == 4

    def test_two_balloons_overlapping(self, solution):
        """Two overlapping balloons"""
        points = [[1, 5], [3, 7]]
        assert solution.findMinArrowShots(points) == 1

    def test_two_balloons_not_overlapping(self, solution):
        """Two non-overlapping balloons"""
        points = [[1, 3], [5, 7]]
        assert solution.findMinArrowShots(points) == 2

    def test_touching_balloons(self, solution):
        """Balloons that touch at exactly one point"""
        points = [[1, 2], [2, 3], [3, 4]]
        assert solution.findMinArrowShots(points) == 2

    def test_nested_balloons(self, solution):
        """One balloon inside another"""
        points = [[1, 10], [3, 5]]
        assert solution.findMinArrowShots(points) == 1

    def test_large_coordinates(self, solution):
        """Large coordinate values"""
        points = [[-2147483648, 2147483647]]
        assert solution.findMinArrowShots(points) == 1

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
