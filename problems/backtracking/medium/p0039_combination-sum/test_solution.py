"""
Tests for LeetCode Problem #39: Combination Sum
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestCombinationSum:
    """Test cases for Combination Sum problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1: candidates = [2,3,6,7], target = 7"""
        result = solution.combinationSum([2, 3, 6, 7], 7)
        expected = [[2, 2, 3], [7]]
        # Convert to sets of tuples for comparison
        result_set = {tuple(sorted(x)) for x in result}
        expected_set = {tuple(sorted(x)) for x in expected}
        assert result_set == expected_set

    def test_example_2(self, solution):
        """Example 2: candidates = [2,3,5], target = 8"""
        result = solution.combinationSum([2, 3, 5], 8)
        expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        result_set = {tuple(sorted(x)) for x in result}
        expected_set = {tuple(sorted(x)) for x in expected}
        assert result_set == expected_set

    # Edge cases
    def test_single_candidate_equals_target(self, solution):
        """Single candidate that equals target"""
        result = solution.combinationSum([7], 7)
        assert result == [[7]]

    def test_single_candidate_divides_target(self, solution):
        """Single candidate that can be used multiple times to reach target"""
        result = solution.combinationSum([2], 6)
        assert result == [[2, 2, 2]]

    def test_no_valid_combination(self, solution):
        """No valid combination possible"""
        result = solution.combinationSum([5, 7], 3)
        assert result == []

    def test_target_smaller_than_all_candidates(self, solution):
        """Target is smaller than all candidates"""
        result = solution.combinationSum([10, 15, 20], 5)
        assert result == []

    def test_single_element_array(self, solution):
        """Single element array"""
        result = solution.combinationSum([3], 9)
        assert result == [[3, 3, 3]]

    def test_large_target_with_small_candidate(self, solution):
        """Large target with small candidate - multiple uses"""
        result = solution.combinationSum([2], 8)
        assert result == [[2, 2, 2, 2]]

    def test_multiple_ways_to_reach_target(self, solution):
        """Multiple valid combinations"""
        result = solution.combinationSum([2, 3, 5], 10)
        # Should have multiple solutions
        assert len(result) > 1
        # Verify all sums equal target
        for combo in result:
            assert sum(combo) == 10

    def test_no_duplicates_in_result(self, solution):
        """Result should not contain duplicate combinations"""
        result = solution.combinationSum([2, 3, 6, 7], 7)
        result_tuples = [tuple(sorted(x)) for x in result]
        assert len(result_tuples) == len(set(result_tuples))

    def test_candidate_larger_than_target(self, solution):
        """When some candidates are larger than target"""
        result = solution.combinationSum([2, 3, 100], 5)
        expected = [[2, 3]]
        result_set = {tuple(sorted(x)) for x in result}
        expected_set = {tuple(sorted(x)) for x in expected}
        assert result_set == expected_set

    def test_all_candidates_equal_target(self, solution):
        """All candidates equal target"""
        result = solution.combinationSum([5, 5, 5], 5)
        # Should return [[5]] - duplicates in candidates treated as one
        # Note: problem says candidates are distinct
        assert len(result) >= 1
        assert any(sum(x) == 5 for x in result)

    def test_prime_candidates(self, solution):
        """Prime number candidates"""
        result = solution.combinationSum([2, 3, 5, 7], 12)
        for combo in result:
            assert sum(combo) == 12

    def test_minimum_target(self, solution):
        """Minimum target (constraint: 1 <= target <= 40)"""
        result = solution.combinationSum([2, 3], 2)
        assert result == [[2]]

    def test_result_sums_to_target(self, solution):
        """All combinations should sum to target"""
        target = 15
        result = solution.combinationSum([2, 3, 5, 7], target)
        for combo in result:
            assert sum(combo) == target

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
