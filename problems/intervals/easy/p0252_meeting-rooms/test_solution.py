"""
Tests for LeetCode Problem #252: Meeting Rooms
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestMeetingRooms:
    """Test cases for Meeting Rooms problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1: Overlapping meetings, cannot attend all"""
        assert solution.canAttendMeetings([[0, 30], [5, 10], [15, 20]]) == False

    def test_example_2(self, solution):
        """Example 2: Non-overlapping meetings, can attend all"""
        assert solution.canAttendMeetings([[7, 10], [2, 4]]) == True

    def test_empty(self, solution):
        """No meetings"""
        assert solution.canAttendMeetings([]) == True

    def test_single_meeting(self, solution):
        """Single meeting"""
        assert solution.canAttendMeetings([[0, 10]]) == True

    def test_back_to_back(self, solution):
        """Back to back meetings (no gap, but not overlapping)"""
        assert solution.canAttendMeetings([[0, 5], [5, 10]]) == True

    def test_all_overlapping(self, solution):
        """All meetings overlap"""
        assert solution.canAttendMeetings([[1, 5], [2, 6], [3, 7]]) == False

    def test_same_meeting(self, solution):
        """Duplicate meeting times"""
        assert solution.canAttendMeetings([[0, 5], [0, 5]]) == False

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
