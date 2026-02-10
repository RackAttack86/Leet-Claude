"""
Tests for LeetCode Problem #27: Remove Element
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
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


    # Edge cases
    def test_empty_array(self, solution):
        """Test with empty array"""
        nums = []
        k = solution.removeElement(nums, 1)
        assert k == 0

    def test_single_element_removed(self, solution):
        """Test with single element that should be removed"""
        nums = [3]
        k = solution.removeElement(nums, 3)
        assert k == 0

    def test_single_element_kept(self, solution):
        """Test with single element that should be kept"""
        nums = [3]
        k = solution.removeElement(nums, 2)
        assert k == 1
        assert nums[:k] == [3]

    def test_all_elements_removed(self, solution):
        """Test with all elements being the target"""
        nums = [5, 5, 5, 5]
        k = solution.removeElement(nums, 5)
        assert k == 0

    def test_no_elements_removed(self, solution):
        """Test where no elements match target"""
        nums = [1, 2, 3, 4]
        k = solution.removeElement(nums, 5)
        assert k == 4
        assert sorted(nums[:k]) == [1, 2, 3, 4]

    def test_two_elements_both_removed(self, solution):
        """Test with two elements both being target"""
        nums = [7, 7]
        k = solution.removeElement(nums, 7)
        assert k == 0

    def test_two_elements_one_removed(self, solution):
        """Test with two elements one being target"""
        nums = [3, 4]
        k = solution.removeElement(nums, 3)
        assert k == 1
        assert nums[:k] == [4]

    def test_target_at_start(self, solution):
        """Test with target elements at start"""
        nums = [2, 2, 2, 3, 4, 5]
        k = solution.removeElement(nums, 2)
        assert k == 3
        assert sorted(nums[:k]) == [3, 4, 5]

    def test_target_at_end(self, solution):
        """Test with target elements at end"""
        nums = [1, 2, 3, 4, 4, 4]
        k = solution.removeElement(nums, 4)
        assert k == 3
        assert sorted(nums[:k]) == [1, 2, 3]

    def test_target_scattered(self, solution):
        """Test with target elements scattered"""
        nums = [1, 2, 1, 3, 1, 4, 1]
        k = solution.removeElement(nums, 1)
        assert k == 3
        assert sorted(nums[:k]) == [2, 3, 4]

    def test_negative_numbers(self, solution):
        """Test with negative numbers"""
        nums = [-1, -2, -3, -1, -4]
        k = solution.removeElement(nums, -1)
        assert k == 3
        assert sorted(nums[:k]) == [-4, -3, -2]

    # Parametrized tests
    @pytest.mark.parametrize("nums,val,expected_k,expected_sorted", [
        ([3, 2, 2, 3], 3, 2, [2, 2]),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 0, 1, 3, 4]),
        ([1], 1, 0, []),
        ([1], 2, 1, [1]),
        ([2, 2, 2], 2, 0, []),
        ([1, 2, 3], 4, 3, [1, 2, 3]),
    ])
    def test_parametrized(self, solution, nums, val, expected_k, expected_sorted):
        """Parametrized test for various inputs"""
        k = solution.removeElement(nums, val)
        assert k == expected_k
        assert sorted(nums[:k]) == expected_sorted

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
