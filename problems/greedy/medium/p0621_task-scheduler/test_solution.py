"""
Tests for LeetCode Problem #621: Task Scheduler
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestTaskScheduler:
    """Test cases for Task Scheduler problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 2
        assert solution.leastInterval(tasks, n) == 8

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        tasks = ["A", "C", "A", "B", "D", "B"]
        n = 1
        assert solution.leastInterval(tasks, n) == 6

    def test_example_3(self, solution):
        """Example 3 - no cooling needed"""
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 0
        assert solution.leastInterval(tasks, n) == 6

    # Edge cases
    def test_single_task_type(self, solution):
        """Only one type of task"""
        tasks = ["A", "A", "A", "A"]
        n = 2
        assert solution.leastInterval(tasks, n) == 10

    def test_single_task(self, solution):
        """Just one task"""
        tasks = ["A"]
        n = 5
        assert solution.leastInterval(tasks, n) == 1

    def test_no_cooling_needed(self, solution):
        """Cooling time is 0"""
        tasks = ["A", "B", "C", "A", "B", "C"]
        n = 0
        assert solution.leastInterval(tasks, n) == 6

    def test_all_different_tasks(self, solution):
        """All tasks are different"""
        tasks = ["A", "B", "C", "D", "E"]
        n = 3
        assert solution.leastInterval(tasks, n) == 5

    def test_many_same_tasks_high_cooling(self, solution):
        """Many of the same task with high cooling"""
        tasks = ["A", "A", "A"]
        n = 100
        assert solution.leastInterval(tasks, n) == 203

    def test_tasks_fill_cooling_gaps(self, solution):
        """Enough different tasks to fill all cooling gaps"""
        tasks = ["A", "A", "A", "B", "B", "B", "C", "C", "C"]
        n = 2
        assert solution.leastInterval(tasks, n) == 9

    def test_two_task_types(self, solution):
        """Two task types with same frequency"""
        tasks = ["A", "B", "A", "B"]
        n = 2
        assert solution.leastInterval(tasks, n) == 5

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
