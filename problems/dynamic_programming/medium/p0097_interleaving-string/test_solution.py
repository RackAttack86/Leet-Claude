"""
Tests for LeetCode Problem #97: Interleaving String
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA




class TestInterleavingString:
    """Test cases for Interleaving String problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbcbcac"
        expected = True
        result = solution.isInterleave(s1, s2, s3)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbbaccc"
        expected = False
        result = solution.isInterleave(s1, s2, s3)
        assert result == expected


    def test_example_3(self, solution):
        """Example 3 from problem description"""
        s1 = ""
        s2 = ""
        s3 = ""
        expected = True
        result = solution.isInterleave(s1, s2, s3)
        assert result == expected


    # Edge cases
    def test_s1_empty(self, solution):
        """s1 is empty, s3 must equal s2"""
        assert solution.isInterleave("", "abc", "abc") == True
        assert solution.isInterleave("", "abc", "ab") == False

    def test_s2_empty(self, solution):
        """s2 is empty, s3 must equal s1"""
        assert solution.isInterleave("abc", "", "abc") == True
        assert solution.isInterleave("abc", "", "ab") == False

    def test_length_mismatch(self, solution):
        """s3 length does not equal s1 + s2 length"""
        assert solution.isInterleave("a", "b", "abc") == False
        assert solution.isInterleave("abc", "def", "abcde") == False

    def test_single_char_each(self, solution):
        """Single character strings"""
        assert solution.isInterleave("a", "b", "ab") == True
        assert solution.isInterleave("a", "b", "ba") == True
        assert solution.isInterleave("a", "b", "aa") == False

    def test_same_characters(self, solution):
        """Strings with same characters"""
        assert solution.isInterleave("aa", "aa", "aaaa") == True
        assert solution.isInterleave("aa", "aa", "aaa") == False

    def test_s1_only_used(self, solution):
        """Only s1 characters in order"""
        assert solution.isInterleave("abc", "", "abc") == True

    def test_s2_only_used(self, solution):
        """Only s2 characters in order"""
        assert solution.isInterleave("", "abc", "abc") == True

    def test_alternating_chars(self, solution):
        """Alternating characters from s1 and s2"""
        assert solution.isInterleave("aaa", "bbb", "ababab") == True
        assert solution.isInterleave("aaa", "bbb", "abababab") == False

    def test_no_valid_interleaving(self, solution):
        """No valid interleaving exists"""
        assert solution.isInterleave("ab", "cd", "acdb") == True
        # cadb: c(cd) + a(ab) + d(cd) + b(ab) = valid interleaving
        assert solution.isInterleave("ab", "cd", "cadb") == True
        # cdba is NOT valid: c(cd) + d(cd) + b(ab) + a(ab) - order preserved
        assert solution.isInterleave("ab", "cd", "dcab") == False

    def test_repeated_chars_different_sources(self, solution):
        """Repeated chars that could come from either source"""
        assert solution.isInterleave("a", "a", "aa") == True

    def test_long_s1_short_s2(self, solution):
        """Long s1, short s2"""
        assert solution.isInterleave("abcde", "f", "abcdef") == True
        assert solution.isInterleave("abcde", "f", "fabcde") == True

    def test_short_s1_long_s2(self, solution):
        """Short s1, long s2"""
        assert solution.isInterleave("a", "bcdef", "abcdef") == True

    def test_wrong_character(self, solution):
        """s3 has character not in s1 or s2"""
        assert solution.isInterleave("ab", "cd", "abcx") == False


    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
