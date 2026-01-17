"""
Tests for LeetCode Problem #323: Number of Connected Components in an Undirected Graph
"""

import pytest
from .solution import Solution, PROBLEM_METADATA


class TestNumberOfConnectedComponentsInAnUndirectedGraph:
    """Test cases for Number of Connected Components in an Undirected Graph problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        # TODO: Implement test
        pass

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        # TODO: Implement test
        pass

    # Edge cases
    def test_edge_case_1(self, solution):
        """TODO: Describe edge case"""
        # TODO: Implement test
        pass

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
