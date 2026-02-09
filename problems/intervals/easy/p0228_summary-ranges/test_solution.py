"""
Tests for LeetCode Problem #228: Summary Ranges
"""

import pytest
from solution import Solution, PROBLEM_METADATA




class TestSummaryRanges:
    """Test cases for Summary Ranges problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums = [0,1,2,4,5,7]
        expected = ["0->2","4->5","7"]
        result = solution.summaryRanges(nums)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        nums = [0,2,3,4,6,8,9]
        expected = ["0","2->4","6","8->9"]
        result = solution.summaryRanges(nums)
        assert result == expected


    def test_edge_case_empty(self, solution):
        """Test with empty input"""
        nums = []
        expected = []
        result = solution.summaryRanges(nums)
        assert result == expected


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
