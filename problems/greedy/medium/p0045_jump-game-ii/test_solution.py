"""
Tests for LeetCode Problem #45: Jump Game II
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestJumpGameIi:
    """Test cases for Jump Game II problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums = [2, 3, 1, 1, 4]
        assert solution.jump(nums) == 2

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        nums = [2, 3, 0, 1, 4]
        assert solution.jump(nums) == 2

    # Edge cases
    def test_single_element(self, solution):
        """Single element - already at destination, 0 jumps needed"""
        nums = [0]
        assert solution.jump(nums) == 0

    def test_single_element_with_value(self, solution):
        """Single element with non-zero value - still 0 jumps"""
        nums = [5]
        assert solution.jump(nums) == 0

    def test_can_reach_in_one_jump(self, solution):
        """First element can reach the end in one jump"""
        nums = [5, 1, 1, 1, 1]
        assert solution.jump(nums) == 1

    def test_can_reach_exactly_in_one_jump(self, solution):
        """First element exactly reaches the last index"""
        nums = [4, 0, 0, 0, 0]
        assert solution.jump(nums) == 1

    def test_two_elements(self, solution):
        """Two elements - one jump needed"""
        nums = [1, 0]
        assert solution.jump(nums) == 1

    def test_all_ones(self, solution):
        """All ones - need n-1 jumps"""
        nums = [1, 1, 1, 1, 1]
        assert solution.jump(nums) == 4

    def test_decreasing_jumps(self, solution):
        """Decreasing jump values"""
        nums = [5, 4, 3, 2, 1, 0]
        assert solution.jump(nums) == 1

    def test_large_first_jump(self, solution):
        """Large first jump that overshoots"""
        nums = [10, 1, 1, 1, 1]
        assert solution.jump(nums) == 1

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
