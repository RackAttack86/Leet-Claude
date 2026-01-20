"""
Tests for LeetCode Problem #253: Meeting Rooms II
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestMeetingRoomsIi:
    """Test cases for Meeting Rooms II problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        intervals = [[0, 30], [5, 10], [15, 20]]
        assert solution.minMeetingRooms(intervals) == 2

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        intervals = [[7, 10], [2, 4]]
        assert solution.minMeetingRooms(intervals) == 1

    # Edge cases
    def test_single_meeting(self, solution):
        """Single meeting"""
        intervals = [[1, 5]]
        assert solution.minMeetingRooms(intervals) == 1

    def test_no_overlap(self, solution):
        """No overlapping meetings"""
        intervals = [[1, 2], [3, 4], [5, 6]]
        assert solution.minMeetingRooms(intervals) == 1

    def test_all_overlap(self, solution):
        """All meetings overlap"""
        intervals = [[1, 10], [2, 9], [3, 8], [4, 7]]
        assert solution.minMeetingRooms(intervals) == 4

    def test_back_to_back(self, solution):
        """Back to back meetings (end time = start time)"""
        intervals = [[1, 2], [2, 3], [3, 4]]
        assert solution.minMeetingRooms(intervals) == 1

    def test_same_time(self, solution):
        """Multiple meetings at same time"""
        intervals = [[1, 5], [1, 5], [1, 5]]
        assert solution.minMeetingRooms(intervals) == 3

    def test_partial_overlap(self, solution):
        """Partial overlaps"""
        intervals = [[0, 5], [4, 10], [9, 15]]
        assert solution.minMeetingRooms(intervals) == 2

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
