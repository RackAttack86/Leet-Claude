"""
Tests for LeetCode Problem #503: Next Greater Element II
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestNextGreaterElementIi:
    """Test cases for Next Greater Element II problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums = [1, 2, 1]
        expected = [2, -1, 2]
        assert solution.nextGreaterElements(nums) == expected

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        nums = [1, 2, 3, 4, 3]
        expected = [2, 3, 4, -1, 4]
        assert solution.nextGreaterElements(nums) == expected

    # Edge cases
    def test_edge_case_single_element(self, solution):
        """Single element - no greater element exists"""
        nums = [5]
        expected = [-1]
        assert solution.nextGreaterElements(nums) == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
