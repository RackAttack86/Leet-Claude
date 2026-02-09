"""
Tests for LeetCode Problem #71: Simplify Path
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestSimplifyPath:
    """Test cases for Simplify Path problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        path = "/home/"
        expected = "/home"
        assert solution.simplifyPath(path) == expected

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        path = "/../"
        expected = "/"
        assert solution.simplifyPath(path) == expected

    def test_example_3(self, solution):
        """Example 3 from problem description"""
        path = "/home//foo/"
        expected = "/home/foo"
        assert solution.simplifyPath(path) == expected

    # Edge cases
    def test_edge_case_root_only(self, solution):
        """Just root directory"""
        path = "/"
        expected = "/"
        assert solution.simplifyPath(path) == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
