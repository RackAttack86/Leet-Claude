"""
Tests for LeetCode Problem #162: Find Peak Element
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestFindPeakElement:
    """Test cases for Find Peak Element problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums = [1, 2, 3, 1]
        result = solution.findPeakElement(nums)
        assert result == 2  # Peak at index 2 (value 3)

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        nums = [1, 2, 1, 3, 5, 6, 4]
        result = solution.findPeakElement(nums)
        # Either index 1 or 5 is acceptable
        assert result in [1, 5]

    # Edge cases
    def test_ascending_order(self, solution):
        """Array in strictly ascending order - peak at end"""
        nums = [1, 2, 3, 4, 5]
        result = solution.findPeakElement(nums)
        assert result == 4  # Last element is peak

    def test_descending_order(self, solution):
        """Array in strictly descending order - peak at start"""
        nums = [5, 4, 3, 2, 1]
        result = solution.findPeakElement(nums)
        assert result == 0  # First element is peak

    def test_single_element(self, solution):
        """Single element array - that element is peak"""
        nums = [5]
        result = solution.findPeakElement(nums)
        assert result == 0

    def test_two_elements_ascending(self, solution):
        """Two elements - ascending"""
        nums = [1, 2]
        result = solution.findPeakElement(nums)
        assert result == 1

    def test_two_elements_descending(self, solution):
        """Two elements - descending"""
        nums = [2, 1]
        result = solution.findPeakElement(nums)
        assert result == 0

    def test_peak_at_start(self, solution):
        """Peak at the start (multiple peaks possible)"""
        nums = [5, 1, 2, 3, 4]
        result = solution.findPeakElement(nums)
        # Either 0 or 4 is valid
        assert result in [0, 4]

    def test_peak_at_middle(self, solution):
        """Clear peak in the middle"""
        nums = [1, 3, 2]
        result = solution.findPeakElement(nums)
        assert result == 1

    def test_multiple_peaks(self, solution):
        """Array with multiple peaks"""
        nums = [1, 3, 2, 4, 1]
        result = solution.findPeakElement(nums)
        # Index 1 (value 3) or 3 (value 4) are valid peaks
        assert result in [1, 3]

    def test_valley_pattern(self, solution):
        """Valley pattern - peaks at both ends"""
        nums = [5, 1, 5]
        result = solution.findPeakElement(nums)
        assert result in [0, 2]

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
