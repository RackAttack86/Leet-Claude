"""
Tests for LeetCode Problem #268: Missing Number
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestMissingNumber:
    """Test cases for Missing Number problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """[3,0,1] is missing 2"""
        assert solution.missingNumber([3, 0, 1]) == 2

    def test_example_2(self, solution):
        """[0,1] is missing 2"""
        assert solution.missingNumber([0, 1]) == 2

    def test_example_3(self, solution):
        """[9,6,4,2,3,5,7,0,1] is missing 8"""
        assert solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8

    def test_missing_zero(self, solution):
        """[1] is missing 0"""
        assert solution.missingNumber([1]) == 0

    def test_missing_last(self, solution):
        """[0,1,2] is missing 3"""
        assert solution.missingNumber([0, 1, 2]) == 3

    def test_single_element_zero(self, solution):
        """[0] is missing 1"""
        assert solution.missingNumber([0]) == 1

    def test_two_elements_missing_middle(self, solution):
        """[0, 2] is missing 1"""
        assert solution.missingNumber([0, 2]) == 1

    def test_reversed_order(self, solution):
        """Array in descending order"""
        assert solution.missingNumber([3, 2, 0]) == 1

    def test_missing_from_large_array(self, solution):
        """Larger array missing from middle"""
        nums = list(range(100))
        nums.remove(50)
        assert solution.missingNumber(nums) == 50

    def test_missing_first_element(self, solution):
        """Missing 0 from larger array"""
        assert solution.missingNumber([1, 2, 3, 4, 5]) == 0

    def test_missing_last_element_large(self, solution):
        """Missing n from larger array"""
        assert solution.missingNumber([0, 1, 2, 3, 4]) == 5

    def test_random_order(self, solution):
        """Random order array"""
        assert solution.missingNumber([8, 3, 5, 2, 4, 6, 0, 1]) == 7

    def test_power_of_two_missing(self, solution):
        """Power of 2 is the missing number"""
        assert solution.missingNumber([0, 1, 3, 4, 5, 6, 7, 8]) == 2
        assert solution.missingNumber([0, 1, 2, 3, 5, 6, 7, 8]) == 4
        assert solution.missingNumber([0, 1, 2, 3, 4, 5, 6, 7]) == 8

    def test_consecutive_starting_from_one(self, solution):
        """Array starts from 1 (missing 0)"""
        assert solution.missingNumber([1]) == 0
        assert solution.missingNumber([2, 1]) == 0

    def test_single_even_number(self, solution):
        """Single even number - odd missing"""
        assert solution.missingNumber([0]) == 1
        assert solution.missingNumber([2, 0]) == 1

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
