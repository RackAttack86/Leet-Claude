"""
Tests for LeetCode Problem #20: Valid Parentheses
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestValidParentheses:
    """Test cases for Valid Parentheses problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        assert solution.isValid("()") == True

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        assert solution.isValid("()[]{}") == True

    def test_example_3(self, solution):
        """Example 3 from problem description"""
        assert solution.isValid("(]") == False

    def test_empty_string(self, solution):
        """Empty string is valid"""
        assert solution.isValid("") == True

    def test_single_open(self, solution):
        """Single opening bracket"""
        assert solution.isValid("(") == False

    def test_nested(self, solution):
        """Nested brackets"""
        assert solution.isValid("{[()]}") == True

    def test_wrong_order(self, solution):
        """Wrong closing order"""
        assert solution.isValid("([)]") == False

    # Additional edge case tests
    def test_single_close(self, solution):
        """Single closing bracket"""
        assert solution.isValid(")") == False

    def test_single_open_brace(self, solution):
        """Single opening brace"""
        assert solution.isValid("{") == False

    def test_single_open_bracket(self, solution):
        """Single opening bracket"""
        assert solution.isValid("[") == False

    def test_only_opens(self, solution):
        """Only opening brackets"""
        assert solution.isValid("(((") == False
        assert solution.isValid("([{") == False

    def test_only_closes(self, solution):
        """Only closing brackets"""
        assert solution.isValid(")))") == False
        assert solution.isValid("}])") == False

    def test_deeply_nested(self, solution):
        """Deeply nested brackets"""
        assert solution.isValid("(((())))") == True
        assert solution.isValid("{{{{}}}}") == True
        assert solution.isValid("[[[[]]]]") == True

    def test_mixed_deeply_nested(self, solution):
        """Mixed deeply nested brackets"""
        assert solution.isValid("({[({[()]})]})") == True

    def test_unbalanced_extra_close(self, solution):
        """Extra closing bracket"""
        assert solution.isValid("())") == False
        assert solution.isValid("(){}]") == False

    def test_unbalanced_extra_open(self, solution):
        """Extra opening bracket"""
        assert solution.isValid("(()") == False
        assert solution.isValid("({[") == False

    def test_alternating_types(self, solution):
        """Alternating bracket types"""
        assert solution.isValid("(){}[]") == True
        assert solution.isValid("({})[]") == True

    def test_mismatched_types(self, solution):
        """Mismatched bracket types"""
        assert solution.isValid("(}") == False
        assert solution.isValid("{]") == False
        assert solution.isValid("[)") == False

    def test_close_before_open(self, solution):
        """Close bracket before matching open"""
        assert solution.isValid(")(") == False
        assert solution.isValid("}{") == False
        assert solution.isValid("][") == False

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
