"""
Tests for LeetCode Problem #40: Combination Sum II
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestCombinationSumIi:
    """Test cases for Combination Sum II problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1: candidates = [10,1,2,7,6,1,5], target = 8"""
        result = solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
        expected = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
        result_set = {tuple(sorted(x)) for x in result}
        expected_set = {tuple(sorted(x)) for x in expected}
        assert result_set == expected_set

    def test_example_2(self, solution):
        """Example 2: candidates = [2,5,2,1,2], target = 5"""
        result = solution.combinationSum2([2, 5, 2, 1, 2], 5)
        expected = [[1, 2, 2], [5]]
        result_set = {tuple(sorted(x)) for x in result}
        expected_set = {tuple(sorted(x)) for x in expected}
        assert result_set == expected_set

    # Edge cases
    def test_no_valid_combination(self, solution):
        """No valid combination exists"""
        result = solution.combinationSum2([3, 5, 7], 2)
        assert result == []

    def test_single_element_equals_target(self, solution):
        """Single element equals target"""
        result = solution.combinationSum2([5], 5)
        assert result == [[5]]

    def test_single_element_not_equal_target(self, solution):
        """Single element does not equal target"""
        result = solution.combinationSum2([5], 3)
        assert result == []

    def test_all_duplicates(self, solution):
        """All elements are duplicates"""
        result = solution.combinationSum2([2, 2, 2, 2], 4)
        expected = [[2, 2]]
        result_set = {tuple(sorted(x)) for x in result}
        expected_set = {tuple(sorted(x)) for x in expected}
        assert result_set == expected_set

    def test_all_same_elements_target_sum_all(self, solution):
        """All same elements, target is sum of all"""
        result = solution.combinationSum2([3, 3, 3], 9)
        assert result == [[3, 3, 3]]

    def test_duplicates_handling(self, solution):
        """Verify duplicates are handled correctly - no duplicate combinations"""
        result = solution.combinationSum2([1, 1, 1, 1], 2)
        # Should only have one [1, 1] combination
        assert len(result) == 1
        assert result[0] == [1, 1]

    def test_multiple_duplicates_different_values(self, solution):
        """Multiple duplicate values"""
        result = solution.combinationSum2([1, 1, 2, 2, 3, 3], 6)
        result_set = {tuple(sorted(x)) for x in result}
        # Should include [1,2,3], [1,1,2,2], [3,3], [2,2,2] - wait 2+2+2=6 but only 2 twos
        # Actually: [1,2,3]=6, [1,1,2,2]=6, [3,3]=6
        for combo in result:
            assert sum(combo) == 6
        # Verify no duplicates
        assert len(result) == len(result_set)

    def test_target_equals_sum_of_all(self, solution):
        """Target equals sum of all elements"""
        result = solution.combinationSum2([1, 2, 3], 6)
        assert [1, 2, 3] in result or sorted([1, 2, 3]) in [sorted(x) for x in result]

    def test_each_element_used_at_most_once(self, solution):
        """Verify each element is used at most once"""
        candidates = [1, 2, 3, 4, 5]
        result = solution.combinationSum2(candidates, 5)
        for combo in result:
            # Count occurrences in combo shouldn't exceed occurrences in candidates
            for val in set(combo):
                assert combo.count(val) <= candidates.count(val)

    def test_larger_target_no_solution(self, solution):
        """Target larger than sum of all elements"""
        result = solution.combinationSum2([1, 2, 3], 100)
        assert result == []

    def test_all_elements_larger_than_target(self, solution):
        """All elements larger than target"""
        result = solution.combinationSum2([10, 20, 30], 5)
        assert result == []

    def test_only_one_valid_solution(self, solution):
        """Only one valid solution exists"""
        result = solution.combinationSum2([1, 2, 3, 4, 5], 15)
        # Sum of all = 15, so only [1,2,3,4,5] should be valid
        assert len(result) == 1
        assert sorted(result[0]) == [1, 2, 3, 4, 5]

    def test_result_uniqueness(self, solution):
        """All combinations should be unique"""
        result = solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
        result_tuples = [tuple(sorted(x)) for x in result]
        assert len(result_tuples) == len(set(result_tuples))

    def test_all_sums_equal_target(self, solution):
        """All combinations should sum to target"""
        target = 8
        result = solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], target)
        for combo in result:
            assert sum(combo) == target

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
