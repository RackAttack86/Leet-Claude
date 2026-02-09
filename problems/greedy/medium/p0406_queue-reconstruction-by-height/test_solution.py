"""
Tests for LeetCode Problem #406: Queue Reconstruction by Height
"""

import pytest
from solution import Solution, PROBLEM_METADATA


class TestQueueReconstructionByHeight:
    """Test cases for Queue Reconstruction by Height problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
        expected = [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
        assert solution.reconstructQueue(people) == expected

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        people = [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]
        expected = [[4, 0], [5, 0], [2, 2], [3, 2], [1, 4], [6, 0]]
        assert solution.reconstructQueue(people) == expected

    # Edge cases
    def test_single_person(self, solution):
        """Single person in queue"""
        people = [[5, 0]]
        expected = [[5, 0]]
        assert solution.reconstructQueue(people) == expected

    def test_two_people_same_height(self, solution):
        """Two people with same height"""
        people = [[5, 0], [5, 1]]
        expected = [[5, 0], [5, 1]]
        assert solution.reconstructQueue(people) == expected

    def test_all_same_height(self, solution):
        """All people have the same height"""
        people = [[5, 0], [5, 1], [5, 2], [5, 3]]
        expected = [[5, 0], [5, 1], [5, 2], [5, 3]]
        assert solution.reconstructQueue(people) == expected

    def test_all_different_heights_no_one_in_front(self, solution):
        """All different heights, no one taller in front"""
        people = [[3, 0], [2, 0], [1, 0]]
        expected = [[1, 0], [2, 0], [3, 0]]
        assert solution.reconstructQueue(people) == expected

    def test_two_people_different_heights(self, solution):
        """Two people with different heights"""
        people = [[7, 0], [4, 1]]
        expected = [[7, 0], [4, 1]]
        assert solution.reconstructQueue(people) == expected

    def test_descending_k_values(self, solution):
        """People with descending k values"""
        people = [[4, 0], [5, 0], [6, 0]]
        expected = [[4, 0], [5, 0], [6, 0]]
        assert solution.reconstructQueue(people) == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
