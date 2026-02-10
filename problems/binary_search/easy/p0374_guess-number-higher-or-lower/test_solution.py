"""
Tests for LeetCode Problem #374: Guess Number Higher or Lower
"""

import pytest
import solution as sol
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestGuessNumberHigherOrLower:
    """Test cases for Guess Number Higher or Lower problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """n=10, pick=6"""
        pick = 6
        sol.guess = lambda num: 0 if num == pick else (-1 if num > pick else 1)
        assert solution.guessNumber(10) == 6

    def test_example_2(self, solution):
        """n=1, pick=1"""
        pick = 1
        sol.guess = lambda num: 0 if num == pick else (-1 if num > pick else 1)
        assert solution.guessNumber(1) == 1

    def test_example_3(self, solution):
        """n=2, pick=1"""
        pick = 1
        sol.guess = lambda num: 0 if num == pick else (-1 if num > pick else 1)
        assert solution.guessNumber(2) == 1

    def test_pick_at_end(self, solution):
        """Pick is the last number"""
        pick = 100
        sol.guess = lambda num: 0 if num == pick else (-1 if num > pick else 1)
        assert solution.guessNumber(100) == 100

    def test_large_range(self, solution):
        """Large range"""
        pick = 500000
        sol.guess = lambda num: 0 if num == pick else (-1 if num > pick else 1)
        assert solution.guessNumber(1000000) == 500000

    # Additional edge case tests
    def test_two_numbers_pick_first(self, solution):
        """Two numbers, pick is 1"""
        pick = 1
        sol.guess = lambda num: 0 if num == pick else (-1 if num > pick else 1)
        assert solution.guessNumber(2) == 1

    def test_two_numbers_pick_second(self, solution):
        """Two numbers, pick is 2"""
        pick = 2
        sol.guess = lambda num: 0 if num == pick else (-1 if num > pick else 1)
        assert solution.guessNumber(2) == 2

    def test_three_numbers_pick_first(self, solution):
        """Three numbers, pick is 1"""
        pick = 1
        sol.guess = lambda num: 0 if num == pick else (-1 if num > pick else 1)
        assert solution.guessNumber(3) == 1

    def test_three_numbers_pick_middle(self, solution):
        """Three numbers, pick is 2"""
        pick = 2
        sol.guess = lambda num: 0 if num == pick else (-1 if num > pick else 1)
        assert solution.guessNumber(3) == 2

    def test_three_numbers_pick_last(self, solution):
        """Three numbers, pick is 3"""
        pick = 3
        sol.guess = lambda num: 0 if num == pick else (-1 if num > pick else 1)
        assert solution.guessNumber(3) == 3

    def test_pick_at_quarter_position(self, solution):
        """Pick at quarter position"""
        pick = 25
        sol.guess = lambda num: 0 if num == pick else (-1 if num > pick else 1)
        assert solution.guessNumber(100) == 25

    def test_pick_at_three_quarter_position(self, solution):
        """Pick at three-quarter position"""
        pick = 75
        sol.guess = lambda num: 0 if num == pick else (-1 if num > pick else 1)
        assert solution.guessNumber(100) == 75

    def test_power_of_two_range(self, solution):
        """Power of 2 range"""
        pick = 512
        sol.guess = lambda num: 0 if num == pick else (-1 if num > pick else 1)
        assert solution.guessNumber(1024) == 512

    def test_power_of_two_minus_one_range(self, solution):
        """Power of 2 minus 1 range"""
        pick = 500
        sol.guess = lambda num: 0 if num == pick else (-1 if num > pick else 1)
        assert solution.guessNumber(1023) == 500

    def test_maximum_int_boundary(self, solution):
        """Near maximum int32 boundary - pick is max"""
        n = 2147483647  # 2^31 - 1
        pick = n
        sol.guess = lambda num: 0 if num == pick else (-1 if num > pick else 1)
        assert solution.guessNumber(n) == n

    def test_maximum_int_pick_one(self, solution):
        """Maximum int32 range with pick = 1"""
        n = 2147483647
        pick = 1
        sol.guess = lambda num: 0 if num == pick else (-1 if num > pick else 1)
        assert solution.guessNumber(n) == 1

    def test_maximum_int_pick_middle(self, solution):
        """Maximum int32 range with pick in middle"""
        n = 2147483647
        pick = n // 2
        sol.guess = lambda num: 0 if num == pick else (-1 if num > pick else 1)
        assert solution.guessNumber(n) == pick

    def test_large_range_pick_small(self, solution):
        """Large range with small pick"""
        pick = 2
        sol.guess = lambda num: 0 if num == pick else (-1 if num > pick else 1)
        assert solution.guessNumber(1000000) == 2

    def test_large_range_pick_near_end(self, solution):
        """Large range with pick near end"""
        pick = 999999
        sol.guess = lambda num: 0 if num == pick else (-1 if num > pick else 1)
        assert solution.guessNumber(1000000) == 999999

    def test_consecutive_picks(self, solution):
        """Test various pick positions"""
        for pick in [1, 5, 10, 50, 99, 100]:
            sol.guess = lambda num, p=pick: 0 if num == p else (-1 if num > p else 1)
            assert solution.guessNumber(100) == pick

    def test_medium_ranges(self, solution):
        """Test medium range values"""
        test_cases = [
            (10, 5),
            (100, 50),
            (1000, 333),
            (10000, 7777),
        ]
        for n, pick in test_cases:
            sol.guess = lambda num, p=pick: 0 if num == p else (-1 if num > p else 1)
            assert solution.guessNumber(n) == pick

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
