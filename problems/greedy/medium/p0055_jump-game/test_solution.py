"""
Tests for LeetCode Problem #55: Jump Game
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestJumpGame:
    """Test cases for Jump Game problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description - can reach"""
        nums = [2, 3, 1, 1, 4]
        assert solution.canJump(nums) == True

    def test_example_2(self, solution):
        """Example 2 from problem description - cannot reach"""
        nums = [3, 2, 1, 0, 4]
        assert solution.canJump(nums) == False

    # Edge cases
    def test_single_element(self, solution):
        """Single element - already at destination"""
        nums = [0]
        assert solution.canJump(nums) == True

    def test_single_element_with_value(self, solution):
        """Single element with non-zero value"""
        nums = [5]
        assert solution.canJump(nums) == True

    def test_all_zeros_except_first(self, solution):
        """All zeros except first - can't move past first zero"""
        nums = [0, 1, 2, 3]
        assert solution.canJump(nums) == False

    def test_all_zeros_except_first_can_reach(self, solution):
        """First element can jump over all zeros"""
        nums = [3, 0, 0, 0]
        assert solution.canJump(nums) == True

    def test_can_just_barely_reach(self, solution):
        """Exactly enough jump distance to reach end"""
        nums = [2, 0, 0]
        assert solution.canJump(nums) == True

    def test_one_short_of_reaching(self, solution):
        """One short of reaching the end"""
        nums = [1, 0, 1]
        assert solution.canJump(nums) == False

    def test_two_elements_can_reach(self, solution):
        """Two elements with enough jump"""
        nums = [1, 0]
        assert solution.canJump(nums) == True

    def test_two_elements_cannot_reach(self, solution):
        """Two elements but first is zero"""
        nums = [0, 1]
        assert solution.canJump(nums) == False

    def test_all_ones(self, solution):
        """All ones - can always reach"""
        nums = [1, 1, 1, 1, 1]
        assert solution.canJump(nums) == True

    def test_large_jump_at_start(self, solution):
        """Large jump at start can reach anywhere"""
        nums = [10, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        assert solution.canJump(nums) == True

    def test_zero_in_middle_blocked(self, solution):
        """Zero in middle that blocks progress"""
        nums = [1, 1, 0, 1]
        assert solution.canJump(nums) == False

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
