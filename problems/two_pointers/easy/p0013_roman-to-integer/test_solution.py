"""
Tests for LeetCode Problem #13: Roman to Integer
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA




class TestRomanToInteger:
    """Test cases for Roman to Integer problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        s = "III"
        expected = 3
        result = solution.romanToInt(s)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        s = "LVIII"
        expected = 58
        result = solution.romanToInt(s)
        assert result == expected


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        s = "MCMXCIV"
        expected = 1994
        result = solution.romanToInt(s)
        assert result == expected


    # Edge cases
    def test_single_character_I(self, solution):
        """Test with single character I (minimum value)"""
        assert solution.romanToInt("I") == 1

    def test_single_character_M(self, solution):
        """Test with single character M (maximum single digit)"""
        assert solution.romanToInt("M") == 1000

    def test_all_subtraction_cases(self, solution):
        """Test all six subtraction cases"""
        assert solution.romanToInt("IV") == 4
        assert solution.romanToInt("IX") == 9
        assert solution.romanToInt("XL") == 40
        assert solution.romanToInt("XC") == 90
        assert solution.romanToInt("CD") == 400
        assert solution.romanToInt("CM") == 900

    def test_repeated_characters(self, solution):
        """Test repeated characters"""
        assert solution.romanToInt("II") == 2
        assert solution.romanToInt("III") == 3
        assert solution.romanToInt("XX") == 20
        assert solution.romanToInt("XXX") == 30
        assert solution.romanToInt("CC") == 200
        assert solution.romanToInt("CCC") == 300
        assert solution.romanToInt("MM") == 2000
        assert solution.romanToInt("MMM") == 3000

    def test_maximum_value(self, solution):
        """Test maximum valid Roman numeral (3999)"""
        assert solution.romanToInt("MMMCMXCIX") == 3999

    def test_minimum_value(self, solution):
        """Test minimum valid Roman numeral (1)"""
        assert solution.romanToInt("I") == 1

    def test_complex_combinations(self, solution):
        """Test complex combinations of addition and subtraction"""
        assert solution.romanToInt("CDXLIV") == 444
        assert solution.romanToInt("DCCCXC") == 890
        assert solution.romanToInt("MMXXI") == 2021
        assert solution.romanToInt("MMXXIV") == 2024

    def test_descending_order(self, solution):
        """Test purely descending values (no subtraction)"""
        assert solution.romanToInt("MDCLXVI") == 1666
        assert solution.romanToInt("DCVI") == 606

    # Parametrized tests
    @pytest.mark.parametrize("roman,expected", [
        ("I", 1),
        ("V", 5),
        ("X", 10),
        ("L", 50),
        ("C", 100),
        ("D", 500),
        ("M", 1000),
        ("IV", 4),
        ("IX", 9),
        ("XL", 40),
        ("XC", 90),
        ("CD", 400),
        ("CM", 900),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("MMMCMXCIX", 3999),
    ])
    def test_parametrized(self, solution, roman, expected):
        """Parametrized test for various Roman numerals"""
        assert solution.romanToInt(roman) == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
