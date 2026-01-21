"""
Tests for LeetCode Problem #66: Plus One
"""

import pytest
from .solution import Solution, PROBLEM_METADATA




class TestPlusOne:
    """Test cases for Plus One problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        digits = [1,2,3]
        expected = [1,2,4]
        result = solution.plusOne(digits)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        digits = [4,3,2,1]
        expected = [4,3,2,2]
        result = solution.plusOne(digits)
        assert result == expected


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        digits = [9]
        expected = [1,0]
        result = solution.plusOne(digits)
        assert result == expected


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
