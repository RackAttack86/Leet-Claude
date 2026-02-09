"""
Tests for LeetCode Problem #678: Valid Parenthesis String
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestValidParenthesisString:
    """Test cases for Valid Parenthesis String problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        s = "()"
        assert solution.checkValidString(s) == True

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        s = "(*)"
        assert solution.checkValidString(s) == True

    def test_example_3(self, solution):
        """Example 3 from problem description"""
        s = "(*))"
        assert solution.checkValidString(s) == True

    # Edge cases
    def test_empty_like_string(self, solution):
        """Single asterisk treated as empty"""
        s = "*"
        assert solution.checkValidString(s) == True

    def test_only_asterisks(self, solution):
        """String with only asterisks"""
        s = "***"
        assert solution.checkValidString(s) == True

    def test_asterisks_as_parentheses(self, solution):
        """Asterisks acting as both ( and )"""
        s = "**"
        assert solution.checkValidString(s) == True

    def test_asterisk_as_open(self, solution):
        """Asterisk needs to be open parenthesis"""
        s = "*)"
        assert solution.checkValidString(s) == True

    def test_asterisk_as_close(self, solution):
        """Asterisk needs to be close parenthesis"""
        s = "(*"
        assert solution.checkValidString(s) == True

    def test_too_many_close(self, solution):
        """Too many closing parentheses"""
        s = "()))"
        assert solution.checkValidString(s) == False

    def test_too_many_open(self, solution):
        """Too many opening parentheses"""
        s = "((("
        assert solution.checkValidString(s) == False

    def test_close_before_open(self, solution):
        """Closing before opening"""
        s = ")("
        assert solution.checkValidString(s) == False

    def test_complex_valid(self, solution):
        """Complex valid string"""
        s = "((*)(*))"
        assert solution.checkValidString(s) == True

    def test_single_open(self, solution):
        """Single open parenthesis"""
        s = "("
        assert solution.checkValidString(s) == False

    def test_single_close(self, solution):
        """Single close parenthesis"""
        s = ")"
        assert solution.checkValidString(s) == False

    def test_asterisk_cannot_fix(self, solution):
        """Asterisks cannot fix the imbalance"""
        s = "(*)))"
        assert solution.checkValidString(s) == False

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
