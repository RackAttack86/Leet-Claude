"""
Tests for LeetCode Problem #206: Reverse Linked List
"""

import pytest
from .solution import Solution, PROBLEM_METADATA


class TestReverseLinkedList:
    """Test cases for Reverse Linked List problem"""

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
