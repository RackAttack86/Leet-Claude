"""
Tests for LeetCode Problem #138: Copy List with Random Pointer
"""

import pytest
from .solution import Solution, PROBLEM_METADATA
from .solution import Node



class TestCopyListWithRandomPointer:
    """Test cases for Copy List with Random Pointer problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        head = [[7,None]
        expected = [[7,null],[13,0],[11,4],[10,2],[1,0]]
        result = solution.copyRandomList(head)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        head = [[1,1]
        expected = [[1,1],[2,1]]
        result = solution.copyRandomList(head)
        assert result == expected


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        head = [[3,None]
        expected = [[3,null],[3,0],[3,null]]
        result = solution.copyRandomList(head)
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
