"""
Tests for LeetCode Problem #274: H-Index
"""

import pytest
from solution import Solution, PROBLEM_METADATA




class TestHindex:
    """Test cases for H-Index problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        citations = [3,0,6,1,5]
        expected = 3
        result = solution.hIndex(citations)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        citations = [1,3,1]
        expected = 1
        result = solution.hIndex(citations)
        assert result == expected


    def test_edge_case_single_paper(self, solution):
        """Test with single paper"""
        citations = [0]
        expected = 0
        result = solution.hIndex(citations)
        assert result == expected

    def test_edge_case_high_citations(self, solution):
        """Test with all high citations"""
        citations = [100]
        expected = 1
        result = solution.hIndex(citations)
        assert result == expected


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
