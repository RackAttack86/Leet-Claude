"""
Tests for LeetCode Problem #881: Boats to Save People
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestBoatsToSavePeople:
    """Test cases for Boats to Save People problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        people = [1, 2]
        limit = 3
        assert solution.numRescueBoats(people, limit) == 1

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        people = [3, 2, 2, 1]
        limit = 3
        assert solution.numRescueBoats(people, limit) == 3

    def test_example_3(self, solution):
        """Example 3 from problem description"""
        people = [3, 5, 3, 4]
        limit = 5
        assert solution.numRescueBoats(people, limit) == 4

    # Edge cases
    def test_single_person(self, solution):
        """Single person - one boat needed"""
        people = [3]
        limit = 5
        assert solution.numRescueBoats(people, limit) == 1

    def test_all_same_weight(self, solution):
        """All people have the same weight"""
        people = [3, 3, 3, 3]
        limit = 6
        assert solution.numRescueBoats(people, limit) == 2

    def test_all_same_weight_no_pairing(self, solution):
        """All same weight but can't pair (each needs own boat)"""
        people = [5, 5, 5, 5]
        limit = 5
        assert solution.numRescueBoats(people, limit) == 4

    def test_one_person_per_boat(self, solution):
        """Each person needs their own boat (all at limit)"""
        people = [3, 3, 3]
        limit = 3
        assert solution.numRescueBoats(people, limit) == 3

    def test_all_can_pair(self, solution):
        """All people can pair up"""
        people = [1, 1, 1, 1]
        limit = 3
        assert solution.numRescueBoats(people, limit) == 2

    def test_two_people_fit(self, solution):
        """Two people exactly fit in one boat"""
        people = [2, 3]
        limit = 5
        assert solution.numRescueBoats(people, limit) == 1

    def test_two_people_dont_fit(self, solution):
        """Two people don't fit in one boat"""
        people = [3, 3]
        limit = 5
        assert solution.numRescueBoats(people, limit) == 2

    def test_mixed_weights(self, solution):
        """Mixed weights requiring optimal pairing"""
        people = [1, 2, 3, 4, 5]
        limit = 6
        assert solution.numRescueBoats(people, limit) == 3

    def test_all_weight_one(self, solution):
        """All people weigh 1"""
        people = [1, 1, 1, 1, 1]
        limit = 2
        assert solution.numRescueBoats(people, limit) == 3

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
