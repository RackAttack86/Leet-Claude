"""
Tests for LeetCode Problem #745: Prefix and Suffix Search
"""

import pytest
from solution import WordFilter, PROBLEM_METADATA


class TestPrefixAndSuffixSearch:
    """Test cases for Prefix and Suffix Search problem"""

    def test_example_1(self):
        """Example 1 from problem description"""
        wordFilter = WordFilter(["apple"])
        assert wordFilter.f("a", "e") == 0

    def test_example_2(self):
        """Test with multiple words"""
        wordFilter = WordFilter(["apple", "maple", "apply"])
        assert wordFilter.f("a", "e") == 1  # "maple" is at index 1, has prefix "a" and suffix "e"
        assert wordFilter.f("app", "y") == 2  # "apply" is at index 2

    def test_edge_case_1(self):
        """Test with no matching word"""
        wordFilter = WordFilter(["apple", "banana"])
        assert wordFilter.f("xyz", "abc") == -1

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
