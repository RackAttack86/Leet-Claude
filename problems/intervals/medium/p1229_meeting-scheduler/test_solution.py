"""
Tests for LeetCode Problem #1229: Meeting Scheduler
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestMeetingScheduler:
    """Test cases for Meeting Scheduler problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        slots1 = [[10, 50], [60, 120], [140, 210]]
        slots2 = [[0, 15], [60, 70]]
        duration = 8
        assert solution.minAvailableDuration(slots1, slots2, duration) == [60, 68]

    def test_example_2(self, solution):
        """Example 2 from problem description - no common slot"""
        slots1 = [[10, 50], [60, 120], [140, 210]]
        slots2 = [[0, 15], [60, 70]]
        duration = 12
        assert solution.minAvailableDuration(slots1, slots2, duration) == []

    # Edge cases
    def test_no_common_time(self, solution):
        """No overlapping time slots"""
        slots1 = [[1, 5], [10, 15]]
        slots2 = [[6, 9], [16, 20]]
        duration = 2
        assert solution.minAvailableDuration(slots1, slots2, duration) == []

    def test_exact_match(self, solution):
        """Intersection exactly matches required duration"""
        slots1 = [[0, 10]]
        slots2 = [[5, 15]]
        duration = 5
        assert solution.minAvailableDuration(slots1, slots2, duration) == [5, 10]

    def test_single_slot_each(self, solution):
        """Single slot from each person with overlap"""
        slots1 = [[0, 20]]
        slots2 = [[5, 15]]
        duration = 5
        assert solution.minAvailableDuration(slots1, slots2, duration) == [5, 10]

    def test_single_slot_no_overlap(self, solution):
        """Single slot from each person with no overlap"""
        slots1 = [[0, 5]]
        slots2 = [[10, 15]]
        duration = 3
        assert solution.minAvailableDuration(slots1, slots2, duration) == []

    def test_duration_too_long(self, solution):
        """Duration is longer than any overlap"""
        slots1 = [[0, 10], [20, 30]]
        slots2 = [[5, 25]]
        duration = 10
        assert solution.minAvailableDuration(slots1, slots2, duration) == []

    def test_identical_slots(self, solution):
        """Both people have identical slots"""
        slots1 = [[10, 50]]
        slots2 = [[10, 50]]
        duration = 10
        assert solution.minAvailableDuration(slots1, slots2, duration) == [10, 20]

    def test_unsorted_input(self, solution):
        """Unsorted input slots"""
        slots1 = [[60, 120], [10, 50]]
        slots2 = [[60, 70], [0, 15]]
        duration = 8
        assert solution.minAvailableDuration(slots1, slots2, duration) == [60, 68]

    def test_minimum_duration(self, solution):
        """Minimum duration of 1"""
        slots1 = [[0, 5]]
        slots2 = [[4, 10]]
        duration = 1
        assert solution.minAvailableDuration(slots1, slots2, duration) == [4, 5]

    def test_large_gap_between_slots(self, solution):
        """Large gap between available slots"""
        slots1 = [[100, 200], [500, 600]]
        slots2 = [[150, 250], [550, 650]]
        duration = 30
        assert solution.minAvailableDuration(slots1, slots2, duration) == [150, 180]

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
