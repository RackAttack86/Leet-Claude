"""
Tests for LeetCode Problem #495: Teemo Attacking
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestTeemoAttacking:
    """Test cases for Teemo Attacking problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1: No overlap, 4 seconds total"""
        assert solution.findPoisonedDuration([1, 4], 2) == 4

    def test_example_2(self, solution):
        """Example 2: Overlap, 3 seconds total"""
        assert solution.findPoisonedDuration([1, 2], 2) == 3

    def test_single_attack(self, solution):
        """Single attack"""
        assert solution.findPoisonedDuration([5], 10) == 10

    def test_no_overlap(self, solution):
        """Multiple attacks, no overlap"""
        assert solution.findPoisonedDuration([1, 5, 9], 2) == 6

    def test_full_overlap(self, solution):
        """Consecutive attacks with reset"""
        assert solution.findPoisonedDuration([1, 2, 3, 4, 5], 5) == 9

    def test_empty(self, solution):
        """Empty time series"""
        assert solution.findPoisonedDuration([], 5) == 0

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
