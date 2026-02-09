"""
Tests for LeetCode Problem #78: Subsets
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestSubsets:
    """Test cases for Subsets problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1: nums = [1,2,3]"""
        result = solution.subsets([1, 2, 3])
        expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        result_set = {tuple(sorted(x)) for x in result}
        expected_set = {tuple(sorted(x)) for x in expected}
        assert result_set == expected_set

    def test_example_2(self, solution):
        """Example 2: nums = [0]"""
        result = solution.subsets([0])
        expected = [[], [0]]
        result_set = {tuple(sorted(x)) for x in result}
        expected_set = {tuple(sorted(x)) for x in expected}
        assert result_set == expected_set

    # Edge cases
    def test_single_element(self, solution):
        """Single element array"""
        result = solution.subsets([1])
        expected = [[], [1]]
        result_set = {tuple(sorted(x)) for x in result}
        expected_set = {tuple(sorted(x)) for x in expected}
        assert result_set == expected_set

    def test_two_elements(self, solution):
        """Two element array"""
        result = solution.subsets([1, 2])
        expected = [[], [1], [2], [1, 2]]
        result_set = {tuple(sorted(x)) for x in result}
        expected_set = {tuple(sorted(x)) for x in expected}
        assert result_set == expected_set

    def test_correct_subset_count(self, solution):
        """Verify correct number of subsets (2^n)"""
        for n in range(1, 8):
            nums = list(range(n))
            result = solution.subsets(nums)
            assert len(result) == 2 ** n

    def test_max_constraint_10_elements(self, solution):
        """Maximum constraint: 10 elements"""
        nums = list(range(10))
        result = solution.subsets(nums)
        assert len(result) == 1024  # 2^10

    def test_negative_numbers(self, solution):
        """Array with negative numbers"""
        result = solution.subsets([-1, 0, 1])
        assert len(result) == 8  # 2^3

    def test_empty_set_included(self, solution):
        """Empty set should always be included"""
        result = solution.subsets([1, 2, 3])
        assert [] in result

    def test_full_set_included(self, solution):
        """Full set should always be included"""
        nums = [1, 2, 3]
        result = solution.subsets(nums)
        # Check if full set is included (order may vary)
        full_set_exists = any(sorted(subset) == sorted(nums) for subset in result)
        assert full_set_exists

    def test_all_subsets_unique(self, solution):
        """All subsets should be unique"""
        result = solution.subsets([1, 2, 3, 4])
        result_tuples = [tuple(sorted(x)) for x in result]
        assert len(result_tuples) == len(set(result_tuples))

    def test_single_element_subsets(self, solution):
        """All single-element subsets should be present"""
        nums = [1, 2, 3, 4]
        result = solution.subsets(nums)
        result_set = {tuple(sorted(x)) for x in result}
        for num in nums:
            assert (num,) in result_set

    def test_elements_valid(self, solution):
        """All elements in subsets should be from original array"""
        nums = [1, 2, 3]
        result = solution.subsets(nums)
        nums_set = set(nums)
        for subset in result:
            for elem in subset:
                assert elem in nums_set

    def test_boundary_values(self, solution):
        """Boundary values from constraints (-10 and 10)"""
        result = solution.subsets([-10, 10])
        expected = [[], [-10], [10], [-10, 10]]
        result_set = {tuple(sorted(x)) for x in result}
        expected_set = {tuple(sorted(x)) for x in expected}
        assert result_set == expected_set

    def test_zero_in_array(self, solution):
        """Array containing zero"""
        result = solution.subsets([0])
        assert len(result) == 2
        assert [] in result
        assert [0] in result

    def test_five_elements(self, solution):
        """Five element array"""
        result = solution.subsets([1, 2, 3, 4, 5])
        assert len(result) == 32  # 2^5

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
