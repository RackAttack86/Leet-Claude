"""
Tests for LeetCode Problem #383: Ransom Note
"""

import pytest
from solution import Solution, PROBLEM_METADATA




class TestRansomNote:
    """Test cases for Ransom Note problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        ransomNote = "a"
        magazine = "b"
        expected = False
        result = solution.canConstruct(ransomNote, magazine)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        ransomNote = "aa"
        magazine = "ab"
        expected = False
        result = solution.canConstruct(ransomNote, magazine)
        assert result == expected


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        ransomNote = "aa"
        magazine = "aab"
        expected = True
        result = solution.canConstruct(ransomNote, magazine)
        assert result == expected


    def test_edge_case_single_char_match(self, solution):
        """Test with single matching character"""
        ransomNote = "a"
        magazine = "a"
        expected = True
        result = solution.canConstruct(ransomNote, magazine)
        assert result == expected


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
