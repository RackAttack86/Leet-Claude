"""
Tests for LeetCode Problem #278: First Bad Version
"""

import pytest
import solution as sol
from solution import Solution, PROBLEM_METADATA


class TestFirstBadVersion:
    """Test cases for First Bad Version problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """n=5, bad=4"""
        bad = 4
        sol.isBadVersion = lambda version: version >= bad
        assert solution.firstBadVersion(5) == 4

    def test_single_version_bad(self, solution):
        """n=1, bad=1"""
        bad = 1
        sol.isBadVersion = lambda version: version >= bad
        assert solution.firstBadVersion(1) == 1

    def test_first_is_bad(self, solution):
        """First version is bad"""
        bad = 1
        sol.isBadVersion = lambda version: version >= bad
        assert solution.firstBadVersion(10) == 1

    def test_last_is_bad(self, solution):
        """Only last version is bad"""
        bad = 10
        sol.isBadVersion = lambda version: version >= bad
        assert solution.firstBadVersion(10) == 10

    def test_middle_is_bad(self, solution):
        """Bad version in middle"""
        bad = 50
        sol.isBadVersion = lambda version: version >= bad
        assert solution.firstBadVersion(100) == 50

    def test_large_range(self, solution):
        """Large range"""
        bad = 1702766719
        sol.isBadVersion = lambda version: version >= bad
        assert solution.firstBadVersion(2126753390) == 1702766719

    # Additional edge case tests
    def test_two_versions_first_is_bad(self, solution):
        """Two versions, first is bad"""
        bad = 1
        sol.isBadVersion = lambda version: version >= bad
        assert solution.firstBadVersion(2) == 1

    def test_two_versions_second_is_bad(self, solution):
        """Two versions, second is bad"""
        bad = 2
        sol.isBadVersion = lambda version: version >= bad
        assert solution.firstBadVersion(2) == 2

    def test_three_versions_first_is_bad(self, solution):
        """Three versions, first is bad"""
        bad = 1
        sol.isBadVersion = lambda version: version >= bad
        assert solution.firstBadVersion(3) == 1

    def test_three_versions_middle_is_bad(self, solution):
        """Three versions, middle is bad"""
        bad = 2
        sol.isBadVersion = lambda version: version >= bad
        assert solution.firstBadVersion(3) == 2

    def test_three_versions_last_is_bad(self, solution):
        """Three versions, last is bad"""
        bad = 3
        sol.isBadVersion = lambda version: version >= bad
        assert solution.firstBadVersion(3) == 3

    def test_bad_at_quarter_position(self, solution):
        """Bad version at quarter position"""
        bad = 25
        sol.isBadVersion = lambda version: version >= bad
        assert solution.firstBadVersion(100) == 25

    def test_bad_at_three_quarter_position(self, solution):
        """Bad version at three-quarter position"""
        bad = 75
        sol.isBadVersion = lambda version: version >= bad
        assert solution.firstBadVersion(100) == 75

    def test_power_of_two_versions(self, solution):
        """Power of 2 versions"""
        bad = 512
        sol.isBadVersion = lambda version: version >= bad
        assert solution.firstBadVersion(1024) == 512

    def test_power_of_two_minus_one(self, solution):
        """Power of 2 minus 1 versions"""
        bad = 500
        sol.isBadVersion = lambda version: version >= bad
        assert solution.firstBadVersion(1023) == 500

    def test_maximum_int_boundary(self, solution):
        """Near maximum int32 boundary"""
        n = 2147483647  # 2^31 - 1
        bad = n
        sol.isBadVersion = lambda version: version >= bad
        assert solution.firstBadVersion(n) == n

    def test_maximum_int_first_bad(self, solution):
        """Maximum int32 with first version bad"""
        n = 2147483647
        bad = 1
        sol.isBadVersion = lambda version: version >= bad
        assert solution.firstBadVersion(n) == 1

    def test_large_n_small_bad(self, solution):
        """Large n with small bad version number"""
        bad = 2
        sol.isBadVersion = lambda version: version >= bad
        assert solution.firstBadVersion(1000000) == 2

    def test_large_n_large_bad(self, solution):
        """Large n with large bad version number near end"""
        bad = 999999
        sol.isBadVersion = lambda version: version >= bad
        assert solution.firstBadVersion(1000000) == 999999

    def test_consecutive_search(self, solution):
        """Test various positions in sequence"""
        for bad in [1, 5, 10, 50, 99, 100]:
            sol.isBadVersion = lambda version, b=bad: version >= b
            assert solution.firstBadVersion(100) == bad

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
