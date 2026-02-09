"""
Tests for LeetCode Problem #1804: Implement Trie II (Prefix Tree)
"""

import pytest
from solution import Trie, PROBLEM_METADATA


class TestImplementTrieIIPrefixTree:
    """Test cases for Implement Trie II (Prefix Tree) problem"""

    def test_example_1(self):
        """Example 1 from problem description"""
        trie = Trie()
        trie.insert("apple")
        trie.insert("apple")
        assert trie.countWordsEqualTo("apple") == 2
        assert trie.countWordsStartingWith("app") == 2
        trie.erase("apple")
        assert trie.countWordsEqualTo("apple") == 1
        assert trie.countWordsStartingWith("app") == 1
        trie.erase("apple")
        assert trie.countWordsStartingWith("app") == 0

    def test_multiple_words(self):
        """Test with multiple different words"""
        trie = Trie()
        trie.insert("apple")
        trie.insert("application")
        trie.insert("banana")
        assert trie.countWordsEqualTo("apple") == 1
        assert trie.countWordsStartingWith("app") == 2
        assert trie.countWordsEqualTo("banana") == 1

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
