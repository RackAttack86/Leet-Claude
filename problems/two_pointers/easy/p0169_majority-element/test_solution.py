"""
Tests for LeetCode Problem #169: Majority Element
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA




class TestMajorityElement:
    """Test cases for Majority Element problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums = [3, 2, 3]
        assert solution.majorityElement(nums) == 3

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        nums = [2, 2, 1, 1, 1, 2, 2]
        assert solution.majorityElement(nums) == 2

    def test_single_element(self, solution):
        """Test with single element array"""
        nums = [1]
        assert solution.majorityElement(nums) == 1

    def test_all_same(self, solution):
        """Test with all same elements"""
        nums = [5, 5, 5, 5, 5]
        assert solution.majorityElement(nums) == 5

    def test_two_elements_same(self, solution):
        """Test with two same elements"""
        nums = [3, 3]
        assert solution.majorityElement(nums) == 3

    def test_majority_at_end(self, solution):
        """Test where majority element appears mostly at end"""
        nums = [1, 2, 3, 3, 3]
        assert solution.majorityElement(nums) == 3

    def test_majority_at_start(self, solution):
        """Test where majority element appears mostly at start"""
        nums = [7, 7, 7, 1, 2]
        assert solution.majorityElement(nums) == 7


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
