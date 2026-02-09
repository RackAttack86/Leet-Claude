"""
Tests for LeetCode Problem #207: Course Schedule
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestCourseSchedule:
    """Test cases for Course Schedule problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        assert solution.canFinish(2, [[1, 0]]) == True

    def test_example_2(self, solution):
        """Example 2 from problem description - cycle detected"""
        assert solution.canFinish(2, [[1, 0], [0, 1]]) == False

    # Edge cases
    def test_single_course_no_prerequisites(self, solution):
        """Single course with no prerequisites"""
        assert solution.canFinish(1, []) == True

    def test_no_prerequisites(self, solution):
        """Multiple courses with no prerequisites"""
        assert solution.canFinish(5, []) == True

    def test_linear_chain(self, solution):
        """Linear dependency chain: 0 -> 1 -> 2 -> 3"""
        prereqs = [[1, 0], [2, 1], [3, 2]]
        assert solution.canFinish(4, prereqs) == True

    def test_simple_cycle_three_nodes(self, solution):
        """Cycle with 3 nodes: 0 -> 1 -> 2 -> 0"""
        prereqs = [[1, 0], [2, 1], [0, 2]]
        assert solution.canFinish(3, prereqs) == False

    def test_self_loop(self, solution):
        """Self-loop: course depends on itself (implicit, need prereq)"""
        # Note: Problem states ai != bi, but testing behavior
        prereqs = [[0, 0]]  # Course 0 requires course 0
        # This would create a cycle of length 1
        assert solution.canFinish(1, prereqs) == False

    def test_disconnected_components_valid(self, solution):
        """Multiple disconnected components, all valid"""
        prereqs = [[1, 0], [3, 2]]  # Two independent chains
        assert solution.canFinish(4, prereqs) == True

    def test_disconnected_with_cycle(self, solution):
        """Disconnected components, one has cycle"""
        prereqs = [[1, 0], [3, 2], [2, 3]]  # First chain valid, second has cycle
        assert solution.canFinish(4, prereqs) == False

    def test_diamond_dag(self, solution):
        """Diamond DAG: 0 -> 1,2 -> 3"""
        prereqs = [[1, 0], [2, 0], [3, 1], [3, 2]]
        assert solution.canFinish(4, prereqs) == True

    def test_complex_dag(self, solution):
        """Complex DAG with multiple paths"""
        prereqs = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3], [5, 3], [5, 4]]
        assert solution.canFinish(6, prereqs) == True

    def test_cycle_in_larger_graph(self, solution):
        """Cycle exists in a larger graph"""
        prereqs = [[1, 0], [2, 1], [3, 2], [1, 3]]  # Creates cycle
        assert solution.canFinish(4, prereqs) == False

    def test_all_courses_independent(self, solution):
        """All courses are independent - no edges"""
        assert solution.canFinish(10, []) == True

    def test_two_courses_one_depends(self, solution):
        """Two courses, one depends on the other"""
        assert solution.canFinish(2, [[0, 1]]) == True
        assert solution.canFinish(2, [[1, 0]]) == True

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
