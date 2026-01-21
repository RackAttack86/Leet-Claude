"""
Tests for LeetCode Problem #49: Group Anagrams
"""

import pytest
from .solution import Solution, PROBLEM_METADATA




class TestGroupAnagrams:
    """Test cases for Group Anagrams problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        strs = ["eat","tea","tan","ate","nat","bat"]
        expected = [["bat"],["nat","tan"],["ate","eat","tea"]]
        result = solution.groupAnagrams(strs)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        strs = [""]
        expected = [[""]]
        result = solution.groupAnagrams(strs)
        assert result == expected


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        strs = ["a"]
        expected = [["a"]]
        result = solution.groupAnagrams(strs)
        assert result == expected


    def test_edge_case_empty(self, solution):
        """Test with empty/minimal input"""
        # TODO: Implement edge case test
        pass


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
