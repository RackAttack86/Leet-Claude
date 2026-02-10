"""
Tests for LeetCode Problem #380: Insert Delete GetRandom O(1)
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA




class TestInsertDeleteGetrandomO1:
    """Test cases for Insert Delete GetRandom O(1) problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        # RandomizedSet randomizedSet = new RandomizedSet();
        # randomizedSet.insert(1); // Returns true
        assert solution.insert(1) == True
        # randomizedSet.remove(2); // Returns false (2 does not exist)
        assert solution.remove(2) == False
        # randomizedSet.insert(2); // Returns true, set now contains [1,2]
        assert solution.insert(2) == True
        # randomizedSet.getRandom(); // Should return either 1 or 2
        result = solution.getRandom()
        assert result in [1, 2]
        # randomizedSet.remove(1); // Returns true, set now contains [2]
        assert solution.remove(1) == True
        # randomizedSet.insert(2); // Returns false (2 already in set)
        assert solution.insert(2) == False
        # randomizedSet.getRandom(); // Always returns 2 (only element)
        assert solution.getRandom() == 2

    def test_example_2(self, solution):
        """Test insert and remove operations"""
        assert solution.insert(1) == True
        assert solution.insert(1) == False  # Duplicate insert
        assert solution.remove(1) == True
        assert solution.remove(1) == False  # Already removed

    def test_edge_case_single_element(self, solution):
        """Test with single element"""
        assert solution.insert(42) == True
        assert solution.getRandom() == 42
        assert solution.remove(42) == True


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
