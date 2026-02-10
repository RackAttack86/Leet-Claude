"""
Tests for LeetCode Problem #17: Letter Combinations of a Phone Number
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestLetterCombinationsOfAPhoneNumber:
    """Test cases for Letter Combinations of a Phone Number problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description: digits = '23'"""
        result = solution.letterCombinations("23")
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        assert sorted(result) == sorted(expected)

    def test_example_2(self, solution):
        """Example 2 from problem description: empty string"""
        result = solution.letterCombinations("")
        assert result == []

    def test_example_3(self, solution):
        """Example 3 from problem description: single digit '2'"""
        result = solution.letterCombinations("2")
        expected = ["a", "b", "c"]
        assert sorted(result) == sorted(expected)

    # Edge cases
    def test_empty_string(self, solution):
        """Empty string should return empty list"""
        assert solution.letterCombinations("") == []

    def test_single_digit_2(self, solution):
        """Single digit '2' should return 3 letters"""
        result = solution.letterCombinations("2")
        assert sorted(result) == ["a", "b", "c"]

    def test_single_digit_7(self, solution):
        """Single digit '7' has 4 letters (pqrs)"""
        result = solution.letterCombinations("7")
        assert sorted(result) == ["p", "q", "r", "s"]

    def test_single_digit_9(self, solution):
        """Single digit '9' has 4 letters (wxyz)"""
        result = solution.letterCombinations("9")
        assert sorted(result) == ["w", "x", "y", "z"]

    def test_two_digits_with_4_letters(self, solution):
        """Digits '79' - both have 4 letters each"""
        result = solution.letterCombinations("79")
        assert len(result) == 16  # 4 * 4

    def test_three_digits(self, solution):
        """Three digits should produce correct number of combinations"""
        result = solution.letterCombinations("234")
        # 3 * 3 * 3 = 27 combinations
        assert len(result) == 27

    def test_four_digits_max_length(self, solution):
        """Maximum constraint: 4 digits"""
        result = solution.letterCombinations("2345")
        # 3 * 3 * 3 * 3 = 81 combinations
        assert len(result) == 81

    def test_all_same_digits(self, solution):
        """All same digits '222'"""
        result = solution.letterCombinations("222")
        assert len(result) == 27  # 3^3
        assert "aaa" in result
        assert "ccc" in result

    def test_digit_with_four_letters_7(self, solution):
        """Digit 7 has 4 letters (pqrs)"""
        result = solution.letterCombinations("7")
        assert len(result) == 4
        assert sorted(result) == ["p", "q", "r", "s"]

    def test_digit_with_four_letters_9(self, solution):
        """Digit 9 has 4 letters (wxyz)"""
        result = solution.letterCombinations("9")
        assert len(result) == 4
        assert sorted(result) == ["w", "x", "y", "z"]

    def test_mixed_three_and_four_letter_digits(self, solution):
        """Mix of 3-letter and 4-letter digits"""
        result = solution.letterCombinations("27")
        # 3 * 4 = 12 combinations
        assert len(result) == 12

    def test_result_uniqueness(self, solution):
        """All combinations should be unique"""
        result = solution.letterCombinations("23")
        assert len(result) == len(set(result))

    def test_result_length(self, solution):
        """Each result string should match input length"""
        digits = "234"
        result = solution.letterCombinations(digits)
        for combo in result:
            assert len(combo) == len(digits)

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
