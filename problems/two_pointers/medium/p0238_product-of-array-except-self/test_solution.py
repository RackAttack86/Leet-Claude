"""
Tests for LeetCode Problem #238: Product of Array Except Self
"""

import pytest
from solution import Solution, PROBLEM_METADATA




class TestProductOfArrayExceptSelf:
    """Test cases for Product of Array Except Self problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums = [1,2,3,4]
        expected = [24,12,8,6]
        result = solution.productExceptSelf(nums)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        nums = [-1,1,0,-3,3]
        expected = [0,0,9,0,0]
        result = solution.productExceptSelf(nums)
        assert result == expected


    def test_edge_case_two_elements(self, solution):
        """Test with minimal input of two elements"""
        nums = [1, 2]
        expected = [2, 1]
        result = solution.productExceptSelf(nums)
        assert result == expected

    def test_edge_case_with_ones(self, solution):
        """Test with array containing all ones"""
        nums = [1, 1, 1, 1]
        expected = [1, 1, 1, 1]
        result = solution.productExceptSelf(nums)
        assert result == expected


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
