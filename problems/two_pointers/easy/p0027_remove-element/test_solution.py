"""
Tests for LeetCode Problem #27: Remove Element
"""

import pytest
from solution import Solution, PROBLEM_METADATA




class TestRemoveElement:
    """Test cases for Remove Element problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums = [3, 2, 2, 3]
        val = 3
        k = solution.removeElement(nums, val)
        assert k == 2
        assert sorted(nums[:k]) == [2, 2]

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        k = solution.removeElement(nums, val)
        assert k == 5
        assert sorted(nums[:k]) == [0, 0, 1, 3, 4]


    def test_edge_case_empty(self, solution):
        """Test with empty/minimal input"""
        # TODO: Implement edge case test
        pass


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
