"""
Tests for LeetCode Problem #219: Contains Duplicate II
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA




class TestContainsDuplicateIi:
    """Test cases for Contains Duplicate II problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums = [1,2,3,1]
        k = 3
        expected = True
        result = solution.containsNearbyDuplicate(nums, k)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        nums = [1,0,1,1]
        k = 1
        expected = True
        result = solution.containsNearbyDuplicate(nums, k)
        assert result == expected


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        nums = [1,2,3,1,2,3]
        k = 2
        expected = False
        result = solution.containsNearbyDuplicate(nums, k)
        assert result == expected


    def test_edge_case_empty(self, solution):
        """Test with empty array"""
        assert solution.containsNearbyDuplicate([], 1) == False

    def test_single_element(self, solution):
        """Single element - no duplicate possible"""
        assert solution.containsNearbyDuplicate([1], 1) == False
        assert solution.containsNearbyDuplicate([1], 0) == False

    def test_k_equals_zero(self, solution):
        """k=0 means same index required - impossible for distinct indices"""
        assert solution.containsNearbyDuplicate([1, 1], 0) == False
        assert solution.containsNearbyDuplicate([1, 2, 1], 0) == False

    def test_no_duplicates(self, solution):
        """Array with no duplicates at all"""
        assert solution.containsNearbyDuplicate([1, 2, 3, 4, 5], 3) == False
        assert solution.containsNearbyDuplicate([1, 2, 3, 4, 5], 10) == False

    def test_duplicate_at_exactly_k_distance(self, solution):
        """Duplicate at exactly k distance - should return True"""
        assert solution.containsNearbyDuplicate([1, 2, 3, 1], 3) == True
        assert solution.containsNearbyDuplicate([1, 2, 1], 2) == True

    def test_duplicate_beyond_k_distance(self, solution):
        """Duplicate exists but beyond k distance"""
        assert solution.containsNearbyDuplicate([1, 2, 3, 4, 1], 3) == False
        assert solution.containsNearbyDuplicate([1, 2, 3, 4, 5, 1], 4) == False

    def test_duplicate_within_k_distance(self, solution):
        """Duplicate within k distance"""
        assert solution.containsNearbyDuplicate([1, 2, 3, 1, 5], 5) == True
        assert solution.containsNearbyDuplicate([1, 2, 1, 4, 5], 3) == True

    def test_multiple_duplicates(self, solution):
        """Multiple duplicate pairs"""
        assert solution.containsNearbyDuplicate([1, 2, 1, 2, 1], 2) == True
        assert solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) == False

    def test_adjacent_duplicates(self, solution):
        """Adjacent duplicates (distance = 1)"""
        assert solution.containsNearbyDuplicate([1, 1], 1) == True
        assert solution.containsNearbyDuplicate([1, 1, 2, 3], 1) == True
        assert solution.containsNearbyDuplicate([1, 2, 2, 3], 1) == True

    def test_large_k(self, solution):
        """k larger than array length"""
        assert solution.containsNearbyDuplicate([1, 2, 3, 1], 10) == True
        assert solution.containsNearbyDuplicate([1, 2, 3, 4], 10) == False

    def test_all_same_elements(self, solution):
        """All elements are the same"""
        assert solution.containsNearbyDuplicate([1, 1, 1, 1], 1) == True
        assert solution.containsNearbyDuplicate([5, 5, 5, 5, 5], 2) == True

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
