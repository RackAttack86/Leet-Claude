"""
Tests for LeetCode Problem #283: Move Zeroes
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestMoveZeroes:
    """Test cases for Move Zeroes problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums = [0, 1, 0, 3, 12]
        expected = [1, 3, 12, 0, 0]
        solution.moveZeroes(nums)
        assert nums == expected

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        nums = [0]
        expected = [0]
        solution.moveZeroes(nums)
        assert nums == expected

    def test_edge_case_no_zeroes(self, solution):
        """Test with array containing no zeroes"""
        nums = [1, 2, 3]
        expected = [1, 2, 3]
        solution.moveZeroes(nums)
        assert nums == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
