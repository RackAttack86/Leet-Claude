"""
Tests for LeetCode Problem #167: Two Sum II - Input Array Is Sorted
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA




class TestTwoSumIiInputArrayIsSorted:
    """Test cases for Two Sum II - Input Array Is Sorted problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        numbers = [2,7,11,15]
        target = 9
        expected = [1,2]
        result = solution.twoSum(numbers, target)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        numbers = [2,3,4]
        target = 6
        expected = [1,3]
        result = solution.twoSum(numbers, target)
        assert result == expected


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        numbers = [-1,0]
        target = -1
        expected = [1,2]
        result = solution.twoSum(numbers, target)
        assert result == expected


    def test_edge_case_two_elements(self, solution):
        """Test with minimal input of two elements"""
        numbers = [1, 2]
        target = 3
        expected = [1, 2]
        result = solution.twoSum(numbers, target)
        assert result == expected

    def test_edge_case_same_values(self, solution):
        """Test with duplicate values"""
        numbers = [1, 1, 2, 3]
        target = 2
        expected = [1, 2]
        result = solution.twoSum(numbers, target)
        assert result == expected


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
