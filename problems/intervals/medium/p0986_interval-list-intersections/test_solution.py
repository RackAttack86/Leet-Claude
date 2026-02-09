"""
Tests for LeetCode Problem #986: Interval List Intersections
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestIntervalListIntersections:
    """Test cases for Interval List Intersections problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
        secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
        expected = [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
        assert solution.intervalIntersection(firstList, secondList) == expected

    def test_example_2(self, solution):
        """Example 2 from problem description - empty second list"""
        firstList = [[1, 3], [5, 9]]
        secondList = []
        expected = []
        assert solution.intervalIntersection(firstList, secondList) == expected

    # Edge cases
    def test_no_intersection(self, solution):
        """No intersection between lists"""
        firstList = [[1, 2], [5, 6]]
        secondList = [[3, 4], [7, 8]]
        expected = []
        assert solution.intervalIntersection(firstList, secondList) == expected

    def test_complete_overlap(self, solution):
        """One interval completely overlaps another"""
        firstList = [[0, 10]]
        secondList = [[2, 5]]
        expected = [[2, 5]]
        assert solution.intervalIntersection(firstList, secondList) == expected

    def test_identical_intervals(self, solution):
        """Identical intervals"""
        firstList = [[1, 5], [10, 15]]
        secondList = [[1, 5], [10, 15]]
        expected = [[1, 5], [10, 15]]
        assert solution.intervalIntersection(firstList, secondList) == expected

    def test_single_point_intersection(self, solution):
        """Intervals intersect at a single point"""
        firstList = [[1, 5]]
        secondList = [[5, 10]]
        expected = [[5, 5]]
        assert solution.intervalIntersection(firstList, secondList) == expected

    def test_empty_first_list(self, solution):
        """Empty first list"""
        firstList = []
        secondList = [[1, 3], [5, 9]]
        expected = []
        assert solution.intervalIntersection(firstList, secondList) == expected

    def test_both_empty(self, solution):
        """Both lists empty"""
        firstList = []
        secondList = []
        expected = []
        assert solution.intervalIntersection(firstList, secondList) == expected

    def test_single_intervals_overlapping(self, solution):
        """Single intervals that overlap"""
        firstList = [[1, 5]]
        secondList = [[3, 7]]
        expected = [[3, 5]]
        assert solution.intervalIntersection(firstList, secondList) == expected

    def test_single_intervals_no_overlap(self, solution):
        """Single intervals that don't overlap"""
        firstList = [[1, 3]]
        secondList = [[5, 7]]
        expected = []
        assert solution.intervalIntersection(firstList, secondList) == expected

    def test_multiple_intersections_with_one(self, solution):
        """Multiple intervals from first list intersect with one from second"""
        firstList = [[0, 2], [3, 5], [6, 8]]
        secondList = [[1, 7]]
        expected = [[1, 2], [3, 5], [6, 7]]
        assert solution.intervalIntersection(firstList, secondList) == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
