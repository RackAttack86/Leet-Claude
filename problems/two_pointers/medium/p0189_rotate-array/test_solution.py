"""
Tests for LeetCode Problem #189: Rotate Array
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestRotateArray:
    """Test cases for Rotate Array problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1 from problem description"""
        nums = [1,2,3,4,5,6,7]
        k = 3
        expected = [5,6,7,1,2,3,4]
        solution.rotate(nums, k)  # modifies in place
        assert nums == expected

    def test_example_2(self, solution):
        """Example 2 from problem description"""
        nums = [-1,-100,3,99]
        k = 2
        expected = [3,99,-1,-100]
        solution.rotate(nums, k)  # modifies in place
        assert nums == expected

    def test_k_larger_than_length(self, solution):
        """Test when k is larger than array length"""
        nums = [1,2,3]
        k = 4  # equivalent to k=1
        expected = [3,1,2]
        solution.rotate(nums, k)
        assert nums == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
