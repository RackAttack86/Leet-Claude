"""
Tests for LeetCode Problem #56: Merge Intervals
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestMergeIntervals:
    """Test cases for Merge Intervals problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expected = [[1, 6], [8, 10], [15, 18]]
        assert solution.merge(intervals) == expected

    def test_example_2(self, solution):
        """Example 2 from problem description - touching intervals"""
        intervals = [[1, 4], [4, 5]]
        expected = [[1, 5]]
        assert solution.merge(intervals) == expected

    # Edge cases
    def test_single_interval(self, solution):
        """Single interval - nothing to merge"""
        intervals = [[1, 5]]
        expected = [[1, 5]]
        assert solution.merge(intervals) == expected

    def test_all_overlapping(self, solution):
        """All intervals overlap into one"""
        intervals = [[1, 4], [2, 5], [3, 6], [4, 7]]
        expected = [[1, 7]]
        assert solution.merge(intervals) == expected

    def test_none_overlapping(self, solution):
        """No intervals overlap"""
        intervals = [[1, 2], [4, 5], [7, 8]]
        expected = [[1, 2], [4, 5], [7, 8]]
        assert solution.merge(intervals) == expected

    def test_nested_intervals(self, solution):
        """One interval completely inside another"""
        intervals = [[1, 10], [3, 5]]
        expected = [[1, 10]]
        assert solution.merge(intervals) == expected

    def test_unsorted_input(self, solution):
        """Unsorted input intervals"""
        intervals = [[8, 10], [1, 3], [2, 6], [15, 18]]
        expected = [[1, 6], [8, 10], [15, 18]]
        assert solution.merge(intervals) == expected

    def test_identical_intervals(self, solution):
        """Multiple identical intervals"""
        intervals = [[1, 5], [1, 5], [1, 5]]
        expected = [[1, 5]]
        assert solution.merge(intervals) == expected

    def test_two_intervals_no_overlap(self, solution):
        """Two intervals that don't overlap"""
        intervals = [[1, 2], [5, 6]]
        expected = [[1, 2], [5, 6]]
        assert solution.merge(intervals) == expected

    def test_two_intervals_overlap(self, solution):
        """Two intervals that overlap"""
        intervals = [[1, 5], [3, 7]]
        expected = [[1, 7]]
        assert solution.merge(intervals) == expected

    def test_point_interval(self, solution):
        """Interval where start equals end"""
        intervals = [[1, 1], [2, 2], [3, 3]]
        expected = [[1, 1], [2, 2], [3, 3]]
        assert solution.merge(intervals) == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
