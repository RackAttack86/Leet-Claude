"""
Tests for LeetCode Problem #90: Subsets II
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestSubsetsIi:
    """Test cases for Subsets II problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1: nums = [1,2,2]"""
        result = solution.subsetsWithDup([1, 2, 2])
        expected = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
        result_set = {tuple(sorted(x)) for x in result}
        expected_set = {tuple(sorted(x)) for x in expected}
        assert result_set == expected_set

    def test_example_2(self, solution):
        """Example 2: nums = [0]"""
        result = solution.subsetsWithDup([0])
        expected = [[], [0]]
        result_set = {tuple(sorted(x)) for x in result}
        expected_set = {tuple(sorted(x)) for x in expected}
        assert result_set == expected_set

    # Edge cases
    def test_single_element(self, solution):
        """Single element array"""
        result = solution.subsetsWithDup([5])
        expected = [[], [5]]
        result_set = {tuple(sorted(x)) for x in result}
        expected_set = {tuple(sorted(x)) for x in expected}
        assert result_set == expected_set

    def test_all_duplicates(self, solution):
        """All elements are the same"""
        result = solution.subsetsWithDup([1, 1, 1])
        expected = [[], [1], [1, 1], [1, 1, 1]]
        result_set = {tuple(sorted(x)) for x in result}
        expected_set = {tuple(sorted(x)) for x in expected}
        assert result_set == expected_set

    def test_all_duplicates_large(self, solution):
        """All elements are the same - larger array"""
        result = solution.subsetsWithDup([2, 2, 2, 2])
        expected = [[], [2], [2, 2], [2, 2, 2], [2, 2, 2, 2]]
        result_set = {tuple(sorted(x)) for x in result}
        expected_set = {tuple(sorted(x)) for x in expected}
        assert result_set == expected_set

    def test_no_duplicates(self, solution):
        """Array with no duplicates - should work like regular subsets"""
        result = solution.subsetsWithDup([1, 2, 3])
        assert len(result) == 8  # 2^3

    def test_two_pairs_of_duplicates(self, solution):
        """Two pairs of duplicate values"""
        result = solution.subsetsWithDup([1, 1, 2, 2])
        # Subsets: [], [1], [1,1], [2], [2,2], [1,2], [1,1,2], [1,2,2], [1,1,2,2]
        assert len(result) == 9

    def test_negative_duplicates(self, solution):
        """Negative duplicate values"""
        result = solution.subsetsWithDup([-1, -1, 0])
        expected = [[], [-1], [-1, -1], [0], [-1, 0], [-1, -1, 0]]
        result_set = {tuple(sorted(x)) for x in result}
        expected_set = {tuple(sorted(x)) for x in expected}
        assert result_set == expected_set

    def test_empty_set_included(self, solution):
        """Empty set should always be included"""
        result = solution.subsetsWithDup([1, 2, 2])
        assert [] in result

    def test_full_set_included(self, solution):
        """Full set should always be included"""
        nums = [1, 2, 2]
        result = solution.subsetsWithDup(nums)
        full_set_exists = any(sorted(subset) == sorted(nums) for subset in result)
        assert full_set_exists

    def test_all_subsets_unique(self, solution):
        """All subsets should be unique - no duplicate subsets"""
        result = solution.subsetsWithDup([1, 2, 2, 3, 3, 3])
        result_tuples = [tuple(sorted(x)) for x in result]
        assert len(result_tuples) == len(set(result_tuples))

    def test_three_same_two_different(self, solution):
        """Three same values and two different values"""
        result = solution.subsetsWithDup([1, 1, 1, 2, 3])
        # Verify no duplicates and proper count
        result_tuples = [tuple(sorted(x)) for x in result]
        assert len(result_tuples) == len(set(result_tuples))

    def test_max_constraint(self, solution):
        """Maximum constraint: 10 elements"""
        nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        result = solution.subsetsWithDup(nums)
        # Verify no duplicates
        result_tuples = [tuple(sorted(x)) for x in result]
        assert len(result_tuples) == len(set(result_tuples))

    def test_boundary_values(self, solution):
        """Boundary values from constraints (-10 and 10)"""
        result = solution.subsetsWithDup([-10, -10, 10, 10])
        result_tuples = [tuple(sorted(x)) for x in result]
        assert len(result_tuples) == len(set(result_tuples))
        # Should have 9 unique subsets
        assert len(result) == 9

    def test_mixed_positive_negative(self, solution):
        """Mix of positive and negative with duplicates"""
        result = solution.subsetsWithDup([-1, -1, 1, 1])
        # Subsets: [], [-1], [-1,-1], [1], [1,1], [-1,1], [-1,-1,1], [-1,1,1], [-1,-1,1,1]
        assert len(result) == 9

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
