"""
Tests for LeetCode Problem #567: Permutation in String
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestPermutationInString:
    """Test cases for Permutation in String problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        s1 = "ab"
        s2 = "eidbaooo"
        assert solution.checkInclusion(s1, s2) == True

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        s1 = "ab"
        s2 = "eidboaoo"
        assert solution.checkInclusion(s1, s2) == False

    # Edge cases
    def test_edge_case_1(self, solution):
        """Test when s1 is longer than s2"""
        s1 = "abc"
        s2 = "a"
        assert solution.checkInclusion(s1, s2) == False

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
