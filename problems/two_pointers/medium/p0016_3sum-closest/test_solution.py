"""
Tests for LeetCode Problem #16: 3Sum Closest
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class Test3sumClosest:
    """Test cases for 3Sum Closest problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums = [-1, 2, 1, -4]
        target = 1
        expected = 2
        result = solution.threeSumClosest(nums, target)
        assert result == expected

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        nums = [0, 0, 0]
        target = 1
        expected = 0
        result = solution.threeSumClosest(nums, target)
        assert result == expected

    # Edge cases
    def test_exact_match(self, solution):
        """Test when exact target sum exists"""
        nums = [1, 1, 1, 0]
        target = 3
        expected = 3
        result = solution.threeSumClosest(nums, target)
        assert result == expected

    def test_minimum_length(self, solution):
        """Array with exactly 3 elements"""
        nums = [1, 2, 3]
        target = 6
        expected = 6
        result = solution.threeSumClosest(nums, target)
        assert result == expected

    def test_negative_numbers(self, solution):
        """Array with negative numbers"""
        nums = [-5, -3, -1, 0, 2, 4]
        target = -2
        expected = -2  # Exact match: -5 + -1 + 4 = -2 or -3 + -1 + 2 = -2
        result = solution.threeSumClosest(nums, target)
        assert result == expected

    def test_all_negative(self, solution):
        """All negative numbers"""
        nums = [-10, -5, -3]
        target = -20
        expected = -18  # -10 + -5 + -3
        result = solution.threeSumClosest(nums, target)
        assert result == expected

    def test_all_positive(self, solution):
        """All positive numbers"""
        nums = [1, 2, 4, 8, 16, 32]
        target = 82
        expected = 56  # 8 + 16 + 32
        result = solution.threeSumClosest(nums, target)
        assert result == expected

    def test_duplicates(self, solution):
        """Array with duplicate values"""
        nums = [0, 2, 1, -3, 2]
        target = 1
        result = solution.threeSumClosest(nums, target)
        # Multiple possible sums close to 1: 0+2+(-3)=-1, 0+1+2=3, 0+2+(-3)=-1
        assert result == 0 or result == 1

    def test_large_target(self, solution):
        """Target much larger than possible sums"""
        nums = [1, 2, 3]
        target = 1000
        expected = 6  # Closest possible is 1+2+3
        result = solution.threeSumClosest(nums, target)
        assert result == expected

    def test_small_target(self, solution):
        """Target much smaller than possible sums"""
        nums = [10, 20, 30]
        target = -1000
        expected = 60  # Closest possible is 10+20+30
        result = solution.threeSumClosest(nums, target)
        assert result == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
