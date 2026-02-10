"""
Tests for LeetCode Problem #131: Palindrome Partitioning
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestPalindromePartitioning:
    """Test cases for Palindrome Partitioning problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1: s = 'aab'"""
        result = solution.partition("aab")
        expected = [["a", "a", "b"], ["aa", "b"]]
        result_set = {tuple(x) for x in result}
        expected_set = {tuple(x) for x in expected}
        assert result_set == expected_set

    def test_example_2(self, solution):
        """Example 2: s = 'a'"""
        result = solution.partition("a")
        assert result == [["a"]]

    # Edge cases
    def test_single_char(self, solution):
        """Single character - always a palindrome"""
        result = solution.partition("x")
        assert result == [["x"]]

    def test_two_same_chars(self, solution):
        """Two same characters"""
        result = solution.partition("aa")
        expected = [["a", "a"], ["aa"]]
        result_set = {tuple(x) for x in result}
        expected_set = {tuple(x) for x in expected}
        assert result_set == expected_set

    def test_two_different_chars(self, solution):
        """Two different characters"""
        result = solution.partition("ab")
        # Only option is ['a', 'b'] since 'ab' is not a palindrome
        assert result == [["a", "b"]]

    def test_all_same_chars(self, solution):
        """All same characters - multiple palindrome partitions"""
        result = solution.partition("aaa")
        # Possible: ["a","a","a"], ["a","aa"], ["aa","a"], ["aaa"]
        expected = [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]
        result_set = {tuple(x) for x in result}
        expected_set = {tuple(x) for x in expected}
        assert result_set == expected_set

    def test_no_multi_char_palindromes(self, solution):
        """String with no multi-character palindromes possible"""
        result = solution.partition("abc")
        # Only possible partition is ["a", "b", "c"]
        assert result == [["a", "b", "c"]]

    def test_entire_string_palindrome(self, solution):
        """Entire string is a palindrome"""
        result = solution.partition("aba")
        # Partitions: ["a","b","a"], ["aba"]
        expected = [["a", "b", "a"], ["aba"]]
        result_set = {tuple(x) for x in result}
        expected_set = {tuple(x) for x in expected}
        assert result_set == expected_set

    def test_longer_palindrome_string(self, solution):
        """Longer palindrome string"""
        result = solution.partition("racecar")
        # "racecar" is a palindrome, plus individual chars
        # Check that the full string is one of the partitions
        full_string_partition = ["racecar"]
        assert full_string_partition in result

    def test_nested_palindromes(self, solution):
        """String with nested palindromes"""
        result = solution.partition("abba")
        # "abba" is palindrome, "bb" is palindrome
        expected_partitions = [
            ["a", "b", "b", "a"],
            ["a", "bb", "a"],
            ["abba"]
        ]
        for exp in expected_partitions:
            assert exp in result

    def test_all_partitions_valid_palindromes(self, solution):
        """Verify all partitions contain only palindromes"""
        result = solution.partition("aabb")
        for partition in result:
            for substring in partition:
                assert substring == substring[::-1], f"{substring} is not a palindrome"

    def test_partitions_cover_full_string(self, solution):
        """Verify each partition covers the entire string"""
        s = "abcba"
        result = solution.partition(s)
        for partition in result:
            assert "".join(partition) == s

    def test_max_length_string(self, solution):
        """Longer string - checking it doesn't timeout"""
        # Use a string that has many partitions
        s = "aaaaaa"  # 6 chars
        result = solution.partition(s)
        # Should have multiple partitions
        assert len(result) > 1
        # All partitions should be valid
        for partition in result:
            assert "".join(partition) == s

    def test_alternating_chars(self, solution):
        """Alternating characters - limited palindromes"""
        result = solution.partition("abab")
        # Only palindromes possible are single chars
        # Plus "aba" is in there: a-bab? no. ab-ab? no.
        # Actually: a,b,a,b is one. aba,b? no "aba" requires positions 0-2
        # s[0:3] = "aba" is palindrome
        for partition in result:
            for substring in partition:
                assert substring == substring[::-1]

    def test_single_char_repeated_max_constraint(self, solution):
        """Maximum constraint with repeated char"""
        s = "a" * 10
        result = solution.partition(s)
        # Should include partition of all a's
        assert [s] in result
        # Should include all individual chars
        assert ["a"] * 10 in result

    def test_mixed_palindromes(self, solution):
        """Mix of various palindrome possibilities"""
        result = solution.partition("ababa")
        # Contains: "a", "b", "aba", "bab", "ababa"
        # Check full string is palindrome and in result
        assert ["ababa"] in result
        # Verify count of partitions
        assert len(result) >= 1

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
