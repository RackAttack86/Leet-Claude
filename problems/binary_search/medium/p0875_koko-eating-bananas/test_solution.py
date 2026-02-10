"""
Tests for LeetCode Problem #875: Koko Eating Bananas
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestKokoEatingBananas:
    """Test cases for Koko Eating Bananas problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        piles = [3, 6, 7, 11]
        h = 8
        assert solution.minEatingSpeed(piles, h) == 4

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        piles = [30, 11, 23, 4, 20]
        h = 5
        assert solution.minEatingSpeed(piles, h) == 30

    def test_example_3(self, solution):
        """Example 3 from problem description"""
        piles = [30, 11, 23, 4, 20]
        h = 6
        assert solution.minEatingSpeed(piles, h) == 23

    # Edge cases
    def test_single_pile(self, solution):
        """Single pile of bananas"""
        piles = [10]
        h = 5
        assert solution.minEatingSpeed(piles, h) == 2

    def test_single_pile_exact(self, solution):
        """Single pile with exactly enough hours"""
        piles = [10]
        h = 10
        assert solution.minEatingSpeed(piles, h) == 1

    def test_single_pile_one_hour(self, solution):
        """Single pile with only 1 hour"""
        piles = [10]
        h = 1
        assert solution.minEatingSpeed(piles, h) == 10

    def test_h_equals_number_of_piles(self, solution):
        """h equals exactly the number of piles - must eat max pile per hour"""
        piles = [3, 6, 7, 11]
        h = 4
        assert solution.minEatingSpeed(piles, h) == 11

    def test_h_equals_number_of_piles_2(self, solution):
        """h equals number of piles - different array"""
        piles = [1, 1, 1, 1]
        h = 4
        assert solution.minEatingSpeed(piles, h) == 1

    def test_h_much_larger_than_piles(self, solution):
        """h is much larger than total bananas"""
        piles = [1, 1, 1, 1]
        h = 1000
        assert solution.minEatingSpeed(piles, h) == 1

    def test_all_same_piles(self, solution):
        """All piles have same number of bananas"""
        piles = [5, 5, 5, 5]
        h = 8
        assert solution.minEatingSpeed(piles, h) == 3

    def test_large_pile_small_h(self, solution):
        """Very large pile with small h"""
        piles = [1000000000]
        h = 2
        assert solution.minEatingSpeed(piles, h) == 500000000

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
