"""
Tests for LeetCode Problem #763: Partition Labels
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestPartitionLabels:
    """Test cases for Partition Labels problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        s = "ababcbacadefegdehijhklij"
        assert solution.partitionLabels(s) == [9, 7, 8]

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        s = "eccbbbbdec"
        assert solution.partitionLabels(s) == [10]

    # Edge cases
    def test_single_char(self, solution):
        """Single character string"""
        s = "a"
        assert solution.partitionLabels(s) == [1]

    def test_all_same_char(self, solution):
        """All characters are the same"""
        s = "aaaaa"
        assert solution.partitionLabels(s) == [5]

    def test_all_unique_chars(self, solution):
        """Each character appears only once"""
        s = "abcdef"
        assert solution.partitionLabels(s) == [1, 1, 1, 1, 1, 1]

    def test_two_distinct_groups(self, solution):
        """Two distinct groups of characters"""
        s = "abab"
        assert solution.partitionLabels(s) == [4]

    def test_alternating_chars(self, solution):
        """Alternating characters force one partition"""
        s = "abababab"
        assert solution.partitionLabels(s) == [8]

    def test_separate_pairs(self, solution):
        """Separate pairs of characters"""
        s = "aabbcc"
        assert solution.partitionLabels(s) == [2, 2, 2]

    def test_first_char_at_end(self, solution):
        """First character also appears at the end"""
        s = "abcda"
        assert solution.partitionLabels(s) == [5]

    def test_two_chars(self, solution):
        """Just two characters"""
        s = "ab"
        assert solution.partitionLabels(s) == [1, 1]

    def test_nested_ranges(self, solution):
        """Character ranges that are nested"""
        s = "abacdcd"
        assert solution.partitionLabels(s) == [3, 4]

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
