"""
Tests for LeetCode Problem #117: Populating Next Right Pointers in Each Node II
"""

import pytest
from .solution import Solution, PROBLEM_METADATA
from .solution import Node



class TestPopulatingNextRightPointersInEachNodeIi:
    """Test cases for Populating Next Right Pointers in Each Node II problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        root = [1,2,3,4,5,None,7]
        expected = [1,#,2,3,#,4,5,7,#]
        result = solution.connect(root)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        root = []
        expected = []
        result = solution.connect(root)
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
