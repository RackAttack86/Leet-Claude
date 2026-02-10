"""
Tests for LeetCode Problem #677: Map Sum Pairs
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestMapSumPairs:
    """Test cases for Map Sum Pairs problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        mapSum = solution.solve()
        mapSum.insert("apple", 3)
        assert mapSum.sum("ap") == 3
        mapSum.insert("app", 2)
        assert mapSum.sum("ap") == 5

    def test_example_2(self, solution):
        """Test updating an existing key"""
        mapSum = solution.solve()
        mapSum.insert("apple", 3)
        assert mapSum.sum("ap") == 3
        mapSum.insert("apple", 2)  # Update existing key
        assert mapSum.sum("ap") == 2

    def test_edge_case_1(self, solution):
        """Test with no matching prefix"""
        mapSum = solution.solve()
        mapSum.insert("apple", 3)
        assert mapSum.sum("b") == 0

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
