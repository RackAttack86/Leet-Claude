"""
Tests for LeetCode Problem #630: Course Schedule III
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestCourseScheduleIii:
    """Test cases for Course Schedule III problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
        assert solution.scheduleCourse(courses) == 3

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        courses = [[1, 2]]
        assert solution.scheduleCourse(courses) == 1

    # Edge cases
    def test_single_course(self, solution):
        """Single course that fits"""
        courses = [[5, 10]]
        assert solution.scheduleCourse(courses) == 1

    def test_single_course_doesnt_fit(self, solution):
        """Single course that doesn't fit"""
        courses = [[10, 5]]
        assert solution.scheduleCourse(courses) == 0

    def test_all_courses_fit(self, solution):
        """All courses can be taken sequentially"""
        courses = [[1, 2], [1, 3], [1, 4]]
        assert solution.scheduleCourse(courses) == 3

    def test_no_courses_fit(self, solution):
        """No course can be taken (duration > deadline)"""
        courses = [[5, 3], [6, 4], [7, 5]]
        assert solution.scheduleCourse(courses) == 0

    def test_greedy_replacement(self, solution):
        """Need to replace a longer course with shorter one"""
        courses = [[5, 5], [4, 6], [2, 6]]
        # Can take [5,5] at day 5, but then can replace with [2,6] to fit more
        assert solution.scheduleCourse(courses) == 2

    def test_same_deadline(self, solution):
        """Multiple courses with same deadline"""
        courses = [[1, 5], [2, 5], [3, 5]]
        # Can take courses with duration 1 and 2 (total 3 <= 5)
        assert solution.scheduleCourse(courses) == 2

    def test_tight_schedule(self, solution):
        """Courses that fit exactly"""
        courses = [[1, 1], [1, 2], [1, 3]]
        assert solution.scheduleCourse(courses) == 3

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
