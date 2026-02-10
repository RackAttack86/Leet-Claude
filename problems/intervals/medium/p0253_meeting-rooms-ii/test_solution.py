"""
Tests for LeetCode Problem #253: Meeting Rooms II
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
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
        """Example 2 from problem description - no overlap"""
        intervals = [[7, 10], [2, 4]]
        assert solution.minMeetingRooms(intervals) == 1

    # Edge cases
    def test_single_meeting(self, solution):
        """Single meeting - one room needed"""
        intervals = [[0, 30]]
        assert solution.minMeetingRooms(intervals) == 1

    def test_all_same_time(self, solution):
        """All meetings at the same time"""
        intervals = [[0, 10], [0, 10], [0, 10]]
        assert solution.minMeetingRooms(intervals) == 3

    def test_sequential_meetings(self, solution):
        """Meetings one after another (no overlap)"""
        intervals = [[0, 5], [5, 10], [10, 15]]
        assert solution.minMeetingRooms(intervals) == 1

    def test_all_overlapping(self, solution):
        """All meetings overlap - need one room per meeting"""
        intervals = [[1, 10], [2, 9], [3, 8], [4, 7]]
        assert solution.minMeetingRooms(intervals) == 4

    def test_two_meetings_overlap(self, solution):
        """Two overlapping meetings"""
        intervals = [[1, 5], [3, 7]]
        assert solution.minMeetingRooms(intervals) == 2

    def test_two_meetings_no_overlap(self, solution):
        """Two non-overlapping meetings"""
        intervals = [[1, 3], [5, 7]]
        assert solution.minMeetingRooms(intervals) == 1

    def test_back_to_back_meetings(self, solution):
        """Meetings end exactly when others start"""
        intervals = [[1, 5], [5, 10], [2, 6], [6, 10]]
        assert solution.minMeetingRooms(intervals) == 2

    def test_nested_meetings(self, solution):
        """Nested meetings (one inside another)"""
        intervals = [[0, 30], [5, 10], [15, 20]]
        assert solution.minMeetingRooms(intervals) == 2

    def test_unsorted_input(self, solution):
        """Unsorted input intervals"""
        intervals = [[15, 20], [0, 30], [5, 10]]
        assert solution.minMeetingRooms(intervals) == 2

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
