"""
Tests for LeetCode Problem #125: Valid Palindrome
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestValidPalindrome:
    """Test cases for Valid Palindrome problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        assert solution.isPalindrome("A man, a plan, a canal: Panama") == True

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        assert solution.isPalindrome("race a car") == False

    def test_example_3(self, solution):
        """Example 3 from problem description"""
        assert solution.isPalindrome(" ") == True

    # Edge cases
    def test_empty_string(self, solution):
        """Empty string is palindrome"""
        assert solution.isPalindrome("") == True

    def test_single_character(self, solution):
        """Single character is palindrome"""
        assert solution.isPalindrome("a") == True
        assert solution.isPalindrome("Z") == True

    def test_only_numbers(self, solution):
        """Only numbers"""
        assert solution.isPalindrome("12321") == True
        assert solution.isPalindrome("12345") == False

    def test_only_special_chars(self, solution):
        """Only special characters"""
        assert solution.isPalindrome(".,!@#") == True

    def test_mixed_case(self, solution):
        """Mixed case letters"""
        assert solution.isPalindrome("RaceCar") == True
        assert solution.isPalindrome("AbCbA") == True

    def test_alphanumeric_palindrome(self, solution):
        """Alphanumeric palindrome"""
        assert solution.isPalindrome("A1b2B1a") == True

    # Parametrized tests
    @pytest.mark.parametrize("s,expected", [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("", True),
        ("a", True),
        ("ab", False),
        ("aa", True),
        ("Madam", True),
        ("0P", False),
    ])
    def test_parametrized(self, solution, s, expected):
        """Parametrized test for multiple cases"""
        assert solution.isPalindrome(s) == expected

    # Test alternative solution
    def test_filter_approach(self, solution):
        """Test the filter approach"""
        assert solution.isPalindrome_filter("A man, a plan, a canal: Panama") == True
        assert solution.isPalindrome_filter("race a car") == False

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
