"""
Tests for LeetCode Problem #218: The Skyline Problem
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestTheSkylineProblem:
    """Test cases for The Skyline Problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
        expected = [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
        assert solution.getSkyline(buildings) == expected

    def test_example_2(self, solution):
        """Example 2: Adjacent buildings with same height"""
        buildings = [[0,2,3],[2,5,3]]
        expected = [[0,3],[5,0]]
        assert solution.getSkyline(buildings) == expected

    def test_single_building(self, solution):
        """Single building"""
        buildings = [[0,5,10]]
        expected = [[0,10],[5,0]]
        assert solution.getSkyline(buildings) == expected

    def test_two_separate_buildings(self, solution):
        """Two non-overlapping buildings"""
        buildings = [[0,2,5],[3,5,8]]
        expected = [[0,5],[2,0],[3,8],[5,0]]
        assert solution.getSkyline(buildings) == expected

    def test_nested_buildings(self, solution):
        """Building completely inside another"""
        buildings = [[0,10,5],[2,6,8]]
        expected = [[0,5],[2,8],[6,5],[10,0]]
        assert solution.getSkyline(buildings) == expected

    def test_same_height_overlap(self, solution):
        """Overlapping buildings with same height"""
        buildings = [[0,3,5],[2,5,5]]
        expected = [[0,5],[5,0]]
        assert solution.getSkyline(buildings) == expected

    def test_touching_buildings(self, solution):
        """Buildings that touch at edge"""
        buildings = [[0,2,3],[2,4,4],[4,6,3]]
        expected = [[0,3],[2,4],[4,3],[6,0]]
        assert solution.getSkyline(buildings) == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
