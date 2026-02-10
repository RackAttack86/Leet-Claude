"""
Tests for LeetCode Problem #77: Combinations
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestCombinations:
    """Test cases for Combinations problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1: n = 4, k = 2"""
        result = solution.combine(4, 2)
        expected = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
        result_set = {tuple(sorted(x)) for x in result}
        expected_set = {tuple(sorted(x)) for x in expected}
        assert result_set == expected_set

    def test_example_2(self, solution):
        """Example 2: n = 1, k = 1"""
        result = solution.combine(1, 1)
        assert result == [[1]]

    # Edge cases
    def test_k_equals_1(self, solution):
        """k = 1: should return n single-element combinations"""
        result = solution.combine(5, 1)
        expected = [[1], [2], [3], [4], [5]]
        result_set = {tuple(x) for x in result}
        expected_set = {tuple(x) for x in expected}
        assert result_set == expected_set

    def test_k_equals_n(self, solution):
        """k = n: only one combination containing all elements"""
        result = solution.combine(4, 4)
        assert len(result) == 1
        assert sorted(result[0]) == [1, 2, 3, 4]

    def test_n_equals_1_k_equals_1(self, solution):
        """Minimum case: n = 1, k = 1"""
        result = solution.combine(1, 1)
        assert result == [[1]]

    def test_large_n_small_k(self, solution):
        """Large n with small k"""
        result = solution.combine(10, 2)
        # C(10,2) = 45
        assert len(result) == 45

    def test_large_n_large_k(self, solution):
        """Large n with large k"""
        result = solution.combine(10, 8)
        # C(10,8) = C(10,2) = 45
        assert len(result) == 45

    def test_correct_combination_count(self, solution):
        """Verify correct number of combinations C(n,k)"""
        # C(5,2) = 10
        result = solution.combine(5, 2)
        assert len(result) == 10

        # C(6,3) = 20
        result = solution.combine(6, 3)
        assert len(result) == 20

    def test_max_constraint_n_20_k_10(self, solution):
        """Maximum constraint: n = 20, k = 10"""
        result = solution.combine(20, 10)
        # C(20,10) = 184756
        assert len(result) == 184756

    def test_all_combinations_unique(self, solution):
        """All combinations should be unique"""
        result = solution.combine(6, 3)
        result_tuples = [tuple(sorted(x)) for x in result]
        assert len(result_tuples) == len(set(result_tuples))

    def test_each_combination_has_k_elements(self, solution):
        """Each combination should have exactly k elements"""
        k = 3
        result = solution.combine(7, k)
        for combo in result:
            assert len(combo) == k

    def test_elements_in_valid_range(self, solution):
        """All elements should be in range [1, n]"""
        n = 5
        result = solution.combine(n, 3)
        for combo in result:
            for elem in combo:
                assert 1 <= elem <= n

    def test_no_duplicate_elements_in_combination(self, solution):
        """Each combination should have unique elements"""
        result = solution.combine(7, 4)
        for combo in result:
            assert len(combo) == len(set(combo))

    def test_n_equals_k_equals_n(self, solution):
        """When k equals n, should return single combination"""
        n = 5
        result = solution.combine(n, n)
        assert len(result) == 1
        assert sorted(result[0]) == list(range(1, n + 1))

    def test_symmetric_property(self, solution):
        """C(n,k) = C(n,n-k)"""
        n = 7
        k = 2
        result1 = solution.combine(n, k)
        result2 = solution.combine(n, n - k)
        assert len(result1) == len(result2)

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
