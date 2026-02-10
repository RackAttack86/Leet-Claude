"""
Tests for LeetCode Problem #46: Permutations
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestPermutations:
    """Test cases for Permutations problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1: nums = [1,2,3]"""
        result = solution.permute([1, 2, 3])
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        result_set = {tuple(x) for x in result}
        expected_set = {tuple(x) for x in expected}
        assert result_set == expected_set

    def test_example_2(self, solution):
        """Example 2: nums = [0,1]"""
        result = solution.permute([0, 1])
        expected = [[0, 1], [1, 0]]
        result_set = {tuple(x) for x in result}
        expected_set = {tuple(x) for x in expected}
        assert result_set == expected_set

    # Edge cases
    def test_single_element(self, solution):
        """Single element array"""
        result = solution.permute([1])
        assert result == [[1]]

    def test_two_elements(self, solution):
        """Two elements array"""
        result = solution.permute([1, 2])
        expected = [[1, 2], [2, 1]]
        result_set = {tuple(x) for x in result}
        expected_set = {tuple(x) for x in expected}
        assert result_set == expected_set

    def test_negative_numbers(self, solution):
        """Array with negative numbers"""
        result = solution.permute([-1, 0, 1])
        assert len(result) == 6  # 3! = 6

    def test_six_elements_max_constraint(self, solution):
        """Maximum constraint: 6 elements"""
        result = solution.permute([1, 2, 3, 4, 5, 6])
        assert len(result) == 720  # 6! = 720

    def test_correct_permutation_count(self, solution):
        """Verify correct number of permutations (n!)"""
        for n in range(1, 7):
            nums = list(range(n))
            result = solution.permute(nums)
            factorial = 1
            for i in range(1, n + 1):
                factorial *= i
            assert len(result) == factorial

    def test_all_permutations_unique(self, solution):
        """All permutations should be unique"""
        result = solution.permute([1, 2, 3, 4])
        result_tuples = [tuple(x) for x in result]
        assert len(result_tuples) == len(set(result_tuples))

    def test_each_permutation_has_all_elements(self, solution):
        """Each permutation should contain all original elements"""
        nums = [1, 2, 3, 4]
        result = solution.permute(nums)
        for perm in result:
            assert sorted(perm) == sorted(nums)

    def test_permutation_length(self, solution):
        """Each permutation should have same length as input"""
        nums = [1, 2, 3, 4, 5]
        result = solution.permute(nums)
        for perm in result:
            assert len(perm) == len(nums)

    def test_zero_in_array(self, solution):
        """Array containing zero"""
        result = solution.permute([0])
        assert result == [[0]]

    def test_mixed_positive_negative(self, solution):
        """Mix of positive and negative numbers"""
        result = solution.permute([-10, 0, 10])
        assert len(result) == 6
        for perm in result:
            assert sorted(perm) == [-10, 0, 10]

    def test_boundary_values(self, solution):
        """Boundary values from constraints (-10 and 10)"""
        result = solution.permute([-10, 10])
        expected = [[-10, 10], [10, -10]]
        result_set = {tuple(x) for x in result}
        expected_set = {tuple(x) for x in expected}
        assert result_set == expected_set

    def test_consecutive_numbers(self, solution):
        """Consecutive numbers"""
        result = solution.permute([1, 2, 3])
        for perm in result:
            assert set(perm) == {1, 2, 3}

    def test_non_consecutive_numbers(self, solution):
        """Non-consecutive numbers"""
        result = solution.permute([1, 5, 10])
        assert len(result) == 6
        for perm in result:
            assert set(perm) == {1, 5, 10}

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
