"""
Tests for LeetCode Problem #1162: As Far from Land as Possible
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestAsFarFromLandAsPossible:
    """Test cases for As Far from Land as Possible problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        grid = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        assert solution.maxDistance(grid) == 2

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        grid = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
        assert solution.maxDistance(grid) == 4

    # Edge cases
    def test_all_land(self, solution):
        """Grid with all land - no water"""
        grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        assert solution.maxDistance(grid) == -1

    def test_all_water(self, solution):
        """Grid with all water - no land"""
        grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        assert solution.maxDistance(grid) == -1

    def test_single_land_corner(self, solution):
        """Single land in corner"""
        grid = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
        assert solution.maxDistance(grid) == 4

    def test_single_land_center(self, solution):
        """Single land in center"""
        grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        assert solution.maxDistance(grid) == 2

    def test_single_water(self, solution):
        """Single water cell"""
        grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        assert solution.maxDistance(grid) == 1

    def test_water_in_corner(self, solution):
        """Water in corner, land elsewhere"""
        grid = [[0, 1, 1], [1, 1, 1], [1, 1, 1]]
        assert solution.maxDistance(grid) == 1

    def test_two_by_two_mixed(self, solution):
        """2x2 grid with mix"""
        grid = [[1, 0], [0, 0]]
        assert solution.maxDistance(grid) == 2

    def test_1x1_land(self, solution):
        """1x1 grid with land"""
        grid = [[1]]
        assert solution.maxDistance(grid) == -1

    def test_1x1_water(self, solution):
        """1x1 grid with water"""
        grid = [[0]]
        assert solution.maxDistance(grid) == -1

    def test_land_at_opposite_corners(self, solution):
        """Land at opposite corners"""
        grid = [
            [1, 0, 0],
            [0, 0, 0],
            [0, 0, 1]
        ]
        assert solution.maxDistance(grid) == 2

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
