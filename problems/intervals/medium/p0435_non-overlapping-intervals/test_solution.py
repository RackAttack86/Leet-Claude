"""
Tests for LeetCode Problem #435: Non-overlapping Intervals
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestNonOverlappingIntervals:
    """Test cases for Non-overlapping Intervals problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
        expected = 1
        result = solution.eraseOverlapIntervals(intervals)
        assert result == expected

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        intervals = [[1, 2], [1, 2], [1, 2]]
        expected = 2
        result = solution.eraseOverlapIntervals(intervals)
        assert result == expected

    def test_example_3(self, solution):
        """Example 3: No overlapping intervals"""
        intervals = [[1, 2], [2, 3]]
        expected = 0
        result = solution.eraseOverlapIntervals(intervals)
        assert result == expected

    # Edge cases
    def test_single_interval(self, solution):
        """Single interval - nothing to remove"""
        intervals = [[1, 5]]
        assert solution.eraseOverlapIntervals(intervals) == 0

    def test_no_overlapping(self, solution):
        """No overlapping intervals"""
        intervals = [[1, 2], [3, 4], [5, 6], [7, 8]]
        assert solution.eraseOverlapIntervals(intervals) == 0

    def test_all_overlapping(self, solution):
        """All intervals overlap - keep only one"""
        intervals = [[1, 10], [2, 9], [3, 8], [4, 7]]
        assert solution.eraseOverlapIntervals(intervals) == 3

    def test_touching_not_overlapping(self, solution):
        """Touching intervals are not overlapping"""
        intervals = [[1, 2], [2, 3], [3, 4]]
        assert solution.eraseOverlapIntervals(intervals) == 0

    def test_two_intervals_overlapping(self, solution):
        """Two intervals that overlap"""
        intervals = [[1, 3], [2, 4]]
        assert solution.eraseOverlapIntervals(intervals) == 1

    def test_nested_intervals(self, solution):
        """One interval inside another"""
        intervals = [[1, 10], [3, 5]]
        assert solution.eraseOverlapIntervals(intervals) == 1

    def test_identical_intervals(self, solution):
        """All intervals are identical"""
        intervals = [[1, 5], [1, 5], [1, 5], [1, 5]]
        assert solution.eraseOverlapIntervals(intervals) == 3

    def test_negative_intervals(self, solution):
        """Intervals with negative values"""
        intervals = [[-5, -2], [-3, 0], [1, 3]]
        assert solution.eraseOverlapIntervals(intervals) == 1

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
