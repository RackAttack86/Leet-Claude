"""
Tests for LeetCode Problem #295: Find Median from Data Stream
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestFindMedianFromDataStream:
    """Test cases for Find Median from Data Stream problem"""

    def test_example_1(self):
        """Example 1 from problem description"""
        mf = Solution()
        mf.addNum(1)
        mf.addNum(2)
        assert mf.findMedian() == 1.5
        mf.addNum(3)
        assert mf.findMedian() == 2.0

    def test_single_element(self):
        """Single element"""
        mf = Solution()
        mf.addNum(5)
        assert mf.findMedian() == 5.0

    def test_two_elements(self):
        """Two elements - even count"""
        mf = Solution()
        mf.addNum(1)
        mf.addNum(2)
        assert mf.findMedian() == 1.5

    def test_three_elements(self):
        """Three elements - odd count"""
        mf = Solution()
        mf.addNum(1)
        mf.addNum(2)
        mf.addNum(3)
        assert mf.findMedian() == 2.0

    def test_negative_numbers(self):
        """Negative numbers"""
        mf = Solution()
        mf.addNum(-1)
        mf.addNum(-2)
        mf.addNum(-3)
        assert mf.findMedian() == -2.0

    def test_mixed_numbers(self):
        """Mix of positive and negative"""
        mf = Solution()
        mf.addNum(-1)
        mf.addNum(1)
        assert mf.findMedian() == 0.0

    def test_duplicates(self):
        """Duplicate values"""
        mf = Solution()
        mf.addNum(2)
        mf.addNum(2)
        mf.addNum(2)
        assert mf.findMedian() == 2.0

    def test_sequential_adds(self):
        """Sequential additions with multiple median checks"""
        mf = Solution()
        mf.addNum(6)
        assert mf.findMedian() == 6.0
        mf.addNum(10)
        assert mf.findMedian() == 8.0
        mf.addNum(2)
        assert mf.findMedian() == 6.0
        mf.addNum(6)
        assert mf.findMedian() == 6.0
        mf.addNum(5)
        assert mf.findMedian() == 6.0

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
