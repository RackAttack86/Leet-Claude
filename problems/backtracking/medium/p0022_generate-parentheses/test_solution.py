"""
Tests for LeetCode Problem #22: Generate Parentheses
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestGenerateParentheses:
    """Test cases for Generate Parentheses problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description: n = 3"""
        result = solution.generateParenthesis(3)
        expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        assert sorted(result) == sorted(expected)

    def test_example_2(self, solution):
        """Example 2 from problem description: n = 1"""
        result = solution.generateParenthesis(1)
        assert result == ["()"]

    # Edge cases
    def test_n_equals_1(self, solution):
        """n = 1: only one valid combination"""
        result = solution.generateParenthesis(1)
        assert result == ["()"]

    def test_n_equals_2(self, solution):
        """n = 2: two valid combinations"""
        result = solution.generateParenthesis(2)
        expected = ["(())", "()()"]
        assert sorted(result) == sorted(expected)

    def test_n_equals_4(self, solution):
        """n = 4: should have 14 combinations (Catalan number C4)"""
        result = solution.generateParenthesis(4)
        # C4 = 14
        assert len(result) == 14

    def test_n_equals_5(self, solution):
        """n = 5: should have 42 combinations (Catalan number C5)"""
        result = solution.generateParenthesis(5)
        # C5 = 42
        assert len(result) == 42

    def test_n_equals_8_max_constraint(self, solution):
        """n = 8: maximum constraint, should have 1430 combinations (C8)"""
        result = solution.generateParenthesis(8)
        # C8 = 1430
        assert len(result) == 1430

    def test_all_results_valid_parentheses(self, solution):
        """All generated strings should be valid parentheses"""
        result = solution.generateParenthesis(4)
        for s in result:
            count = 0
            for char in s:
                if char == '(':
                    count += 1
                else:
                    count -= 1
                assert count >= 0, f"Invalid parentheses: {s}"
            assert count == 0, f"Unbalanced parentheses: {s}"

    def test_all_results_correct_length(self, solution):
        """All results should have length 2n"""
        n = 5
        result = solution.generateParenthesis(n)
        for s in result:
            assert len(s) == 2 * n

    def test_result_uniqueness(self, solution):
        """All generated combinations should be unique"""
        result = solution.generateParenthesis(5)
        assert len(result) == len(set(result))

    def test_correct_count_of_parens(self, solution):
        """Each result should have exactly n open and n close parens"""
        n = 4
        result = solution.generateParenthesis(n)
        for s in result:
            assert s.count('(') == n
            assert s.count(')') == n

    def test_first_char_is_open(self, solution):
        """All valid strings must start with '('"""
        result = solution.generateParenthesis(4)
        for s in result:
            assert s[0] == '('

    def test_last_char_is_close(self, solution):
        """All valid strings must end with ')'"""
        result = solution.generateParenthesis(4)
        for s in result:
            assert s[-1] == ')'

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
