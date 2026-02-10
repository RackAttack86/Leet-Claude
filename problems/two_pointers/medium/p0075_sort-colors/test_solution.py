"""
Tests for LeetCode Problem #75: Sort Colors
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestSortColors:
    """Test cases for Sort Colors problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums = [2, 0, 2, 1, 1, 0]
        solution.sortColors(nums)
        assert nums == [0, 0, 1, 1, 2, 2]

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        nums = [2, 0, 1]
        solution.sortColors(nums)
        assert nums == [0, 1, 2]

    def test_edge_case_single_element(self, solution):
        """Test with single element"""
        nums = [1]
        solution.sortColors(nums)
        assert nums == [1]

    def test_edge_case_all_same(self, solution):
        """Test with all same color"""
        nums = [0, 0, 0]
        solution.sortColors(nums)
        assert nums == [0, 0, 0]

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
