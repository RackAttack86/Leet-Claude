"""
Tests for LeetCode Problem #820: Short Encoding of Words
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestShortEncodingOfWords:
    """Test cases for Short Encoding of Words problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        words = ["time", "me", "bell"]
        assert solution.minimumLengthEncoding(words) == 10

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        words = ["t"]
        assert solution.minimumLengthEncoding(words) == 2

    def test_edge_case_1(self, solution):
        """Test with all words being suffixes of one word"""
        words = ["time", "ime", "me", "e"]
        assert solution.minimumLengthEncoding(words) == 5

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
