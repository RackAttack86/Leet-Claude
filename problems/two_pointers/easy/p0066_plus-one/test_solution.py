"""
Tests for LeetCode Problem #66: Plus One
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA




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


    def test_edge_case_all_nines(self, solution):
        """Test with all 9s (carry propagation)"""
        digits = [9, 9, 9]
        expected = [1, 0, 0, 0]
        result = solution.plusOne(digits)
        assert result == expected


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
