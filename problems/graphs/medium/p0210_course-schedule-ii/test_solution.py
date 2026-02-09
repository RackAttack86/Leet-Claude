"""
Tests for LeetCode Problem #210: Course Schedule II
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestCourseScheduleIi:
    """Test cases for Course Schedule II problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def is_valid_order(self, order, numCourses, prerequisites):
        """Helper to verify if order is valid topological sort"""
        if len(order) != numCourses:
            return False
        position = {course: i for i, course in enumerate(order)}
        for course, prereq in prerequisites:
            if position[prereq] > position[course]:
                return False
        return True

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        result = solution.findOrder(2, [[1, 0]])
        assert self.is_valid_order(result, 2, [[1, 0]])

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        prereqs = [[1, 0], [2, 0], [3, 1], [3, 2]]
        result = solution.findOrder(4, prereqs)
        assert self.is_valid_order(result, 4, prereqs)

    # Edge cases
    def test_single_course_no_prerequisites(self, solution):
        """Single course with no prerequisites"""
        result = solution.findOrder(1, [])
        assert result == [0]

    def test_no_prerequisites(self, solution):
        """Multiple courses with no prerequisites - any order valid"""
        result = solution.findOrder(3, [])
        assert len(result) == 3
        assert set(result) == {0, 1, 2}

    def test_linear_dependency(self, solution):
        """Linear dependency: 0 -> 1 -> 2 -> 3"""
        prereqs = [[1, 0], [2, 1], [3, 2]]
        result = solution.findOrder(4, prereqs)
        assert result == [0, 1, 2, 3]

    def test_cycle_returns_empty(self, solution):
        """Cycle should return empty list"""
        prereqs = [[1, 0], [0, 1]]
        result = solution.findOrder(2, prereqs)
        assert result == []

    def test_three_node_cycle(self, solution):
        """Three-node cycle returns empty"""
        prereqs = [[1, 0], [2, 1], [0, 2]]
        result = solution.findOrder(3, prereqs)
        assert result == []

    def test_diamond_dag(self, solution):
        """Diamond DAG: 0 -> 1,2 -> 3"""
        prereqs = [[1, 0], [2, 0], [3, 1], [3, 2]]
        result = solution.findOrder(4, prereqs)
        assert self.is_valid_order(result, 4, prereqs)
        assert result[0] == 0  # 0 must be first
        assert result[-1] == 3  # 3 must be last

    def test_disconnected_components(self, solution):
        """Disconnected components"""
        prereqs = [[1, 0], [3, 2]]
        result = solution.findOrder(4, prereqs)
        assert self.is_valid_order(result, 4, prereqs)

    def test_reverse_linear(self, solution):
        """Reverse linear: 3 -> 2 -> 1 -> 0"""
        prereqs = [[0, 1], [1, 2], [2, 3]]
        result = solution.findOrder(4, prereqs)
        assert result == [3, 2, 1, 0]

    def test_star_from_one_course(self, solution):
        """One course is prerequisite for all others"""
        prereqs = [[1, 0], [2, 0], [3, 0], [4, 0]]
        result = solution.findOrder(5, prereqs)
        assert result[0] == 0  # 0 must be first
        assert self.is_valid_order(result, 5, prereqs)

    def test_complex_with_many_prereqs(self, solution):
        """Complex graph with course having multiple prerequisites"""
        prereqs = [[3, 0], [3, 1], [3, 2], [4, 3]]
        result = solution.findOrder(5, prereqs)
        assert self.is_valid_order(result, 5, prereqs)
        # 0, 1, 2 before 3, and 3 before 4
        pos = {c: i for i, c in enumerate(result)}
        assert pos[0] < pos[3] and pos[1] < pos[3] and pos[2] < pos[3]
        assert pos[3] < pos[4]

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
