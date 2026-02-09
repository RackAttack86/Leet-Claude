"""
Tests for LeetCode Problem #759: Employee Free Time
"""

import pytest
from solution import Solution, Interval, PROBLEM_METADATA


class TestEmployeeFreeTime:
    """Test cases for Employee Free Time problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        # schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
        schedule = [
            [Interval(1, 2), Interval(5, 6)],
            [Interval(1, 3)],
            [Interval(4, 10)]
        ]
        result = solution.employeeFreeTime(schedule)
        # Expected output: [[3,4]]
        assert len(result) == 1
        assert result[0].start == 3
        assert result[0].end == 4

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        # schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
        schedule = [
            [Interval(1, 3), Interval(6, 7)],
            [Interval(2, 4)],
            [Interval(2, 5), Interval(9, 12)]
        ]
        result = solution.employeeFreeTime(schedule)
        # Expected output: [[5,6],[7,9]]
        assert len(result) == 2
        assert result[0].start == 5
        assert result[0].end == 6
        assert result[1].start == 7
        assert result[1].end == 9

    def test_edge_case_no_free_time(self, solution):
        """Test when all employees have overlapping schedules (no free time)"""
        schedule = [
            [Interval(1, 5)],
            [Interval(2, 6)],
            [Interval(3, 7)]
        ]
        result = solution.employeeFreeTime(schedule)
        assert len(result) == 0

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
