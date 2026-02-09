"""
Tests for LeetCode Problem #57: Insert Interval
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestInsertInterval:
    """Test cases for Insert Interval problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        intervals = [[1, 3], [6, 9]]
        newInterval = [2, 5]
        expected = [[1, 5], [6, 9]]
        assert solution.insert(intervals, newInterval) == expected

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        newInterval = [4, 8]
        expected = [[1, 2], [3, 10], [12, 16]]
        assert solution.insert(intervals, newInterval) == expected

    # Edge cases
    def test_insert_at_start(self, solution):
        """Insert interval at the beginning (no overlap)"""
        intervals = [[5, 7], [10, 12]]
        newInterval = [1, 3]
        expected = [[1, 3], [5, 7], [10, 12]]
        assert solution.insert(intervals, newInterval) == expected

    def test_insert_at_end(self, solution):
        """Insert interval at the end (no overlap)"""
        intervals = [[1, 3], [5, 7]]
        newInterval = [10, 12]
        expected = [[1, 3], [5, 7], [10, 12]]
        assert solution.insert(intervals, newInterval) == expected

    def test_no_overlap_insert_in_middle(self, solution):
        """Insert in middle with no overlap"""
        intervals = [[1, 2], [8, 10]]
        newInterval = [4, 6]
        expected = [[1, 2], [4, 6], [8, 10]]
        assert solution.insert(intervals, newInterval) == expected

    def test_empty_intervals(self, solution):
        """Empty intervals list"""
        intervals = []
        newInterval = [5, 7]
        expected = [[5, 7]]
        assert solution.insert(intervals, newInterval) == expected

    def test_merge_all_intervals(self, solution):
        """New interval merges all existing intervals"""
        intervals = [[1, 2], [3, 4], [5, 6]]
        newInterval = [0, 10]
        expected = [[0, 10]]
        assert solution.insert(intervals, newInterval) == expected

    def test_single_interval_overlap(self, solution):
        """Single interval that overlaps"""
        intervals = [[1, 5]]
        newInterval = [3, 7]
        expected = [[1, 7]]
        assert solution.insert(intervals, newInterval) == expected

    def test_single_interval_no_overlap_before(self, solution):
        """Single interval, new interval comes before"""
        intervals = [[5, 7]]
        newInterval = [1, 3]
        expected = [[1, 3], [5, 7]]
        assert solution.insert(intervals, newInterval) == expected

    def test_single_interval_no_overlap_after(self, solution):
        """Single interval, new interval comes after"""
        intervals = [[1, 3]]
        newInterval = [5, 7]
        expected = [[1, 3], [5, 7]]
        assert solution.insert(intervals, newInterval) == expected

    def test_touching_intervals(self, solution):
        """New interval exactly touches existing"""
        intervals = [[1, 5]]
        newInterval = [5, 8]
        expected = [[1, 8]]
        assert solution.insert(intervals, newInterval) == expected

    def test_new_interval_contains_all(self, solution):
        """New interval completely contains all existing"""
        intervals = [[2, 3], [4, 5], [6, 7]]
        newInterval = [1, 10]
        expected = [[1, 10]]
        assert solution.insert(intervals, newInterval) == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
