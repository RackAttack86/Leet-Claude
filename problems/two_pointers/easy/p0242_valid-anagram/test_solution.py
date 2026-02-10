"""
Tests for LeetCode Problem #242: Valid Anagram
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA




class TestValidAnagram:
    """Test cases for Valid Anagram problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        s = "anagram"
        t = "nagaram"
        expected = True
        result = solution.isAnagram(s, t)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        s = "rat"
        t = "car"
        expected = False
        result = solution.isAnagram(s, t)
        assert result == expected


    def test_edge_case_single_char(self, solution):
        """Test with single character strings"""
        s = "a"
        t = "a"
        expected = True
        result = solution.isAnagram(s, t)
        assert result == expected


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
