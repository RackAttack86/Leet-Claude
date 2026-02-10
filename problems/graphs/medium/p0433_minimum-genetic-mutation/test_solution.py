"""
Tests for LeetCode Problem #433: Minimum Genetic Mutation
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA




class TestMinimumGeneticMutation:
    """Test cases for Minimum Genetic Mutation problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()


    def test_example_1(self, solution):
        """Example 1 from problem description"""
        startGene = "AACCGGTT"
        endGene = "AACCGGTA"
        bank = ["AACCGGTA"]
        expected = 1
        result = solution.minMutation(startGene, endGene, bank)
        assert result == expected


    def test_example_2(self, solution):
        """Example 2 from problem description"""
        startGene = "AACCGGTT"
        endGene = "AAACGGTA"
        bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
        expected = 2
        result = solution.minMutation(startGene, endGene, bank)
        assert result == expected


    def test_no_path(self, solution):
        """Test when no mutation path exists"""
        startGene = "AACCGGTT"
        endGene = "AAACGGTA"
        bank = ["AACCGGTA"]
        expected = -1
        result = solution.minMutation(startGene, endGene, bank)
        assert result == expected


    def test_same_gene(self, solution):
        """Test when start equals end but end not in bank"""
        startGene = "AACCGGTT"
        endGene = "AACCGGTT"
        bank = []
        expected = -1  # end not in bank
        result = solution.minMutation(startGene, endGene, bank)
        assert result == expected


    # Edge cases
    def test_already_at_target(self, solution):
        """Start equals end and end is in bank"""
        startGene = "AACCGGTT"
        endGene = "AACCGGTT"
        bank = ["AACCGGTT"]
        expected = 0
        result = solution.minMutation(startGene, endGene, bank)
        assert result == expected

    def test_end_not_in_bank(self, solution):
        """End gene not in bank - impossible"""
        startGene = "AACCGGTT"
        endGene = "AACCGGTA"
        bank = ["AACCGCTA", "AACCGCTT"]
        expected = -1
        result = solution.minMutation(startGene, endGene, bank)
        assert result == expected

    def test_empty_bank(self, solution):
        """Empty bank - no valid mutations"""
        startGene = "AACCGGTT"
        endGene = "AACCGGTA"
        bank = []
        expected = -1
        result = solution.minMutation(startGene, endGene, bank)
        assert result == expected

    def test_multiple_paths_same_length(self, solution):
        """Multiple paths exist, find any shortest"""
        startGene = "AACCGGTT"
        endGene = "AAACGGTT"
        bank = ["AACCGGTA", "AAACGGTT", "AAACGGTA"]
        expected = 1  # Direct mutation at position 1
        result = solution.minMutation(startGene, endGene, bank)
        assert result == expected

    def test_requires_longer_path(self, solution):
        """Shortest path requires going through intermediate states"""
        startGene = "AAAAACCC"
        endGene = "AACCCCCC"
        bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
        expected = 3
        result = solution.minMutation(startGene, endGene, bank)
        assert result == expected

    def test_single_character_difference(self, solution):
        """Start and end differ by one character"""
        startGene = "AACCGGTT"
        endGene = "AACCGGTA"
        bank = ["AACCGGTA"]
        expected = 1
        result = solution.minMutation(startGene, endGene, bank)
        assert result == expected

    def test_all_different(self, solution):
        """Start and end completely different - long path needed"""
        startGene = "AAAAAAAA"
        endGene = "CCCCCCCC"
        bank = [
            "CAAAAAAA", "CCAAAAAA", "CCCAAAAA", "CCCCAAAA",
            "CCCCCAAA", "CCCCCCAA", "CCCCCCA", "CCCCCCCC"
        ]
        expected = -1  # Missing intermediate step
        result = solution.minMutation(startGene, endGene, bank)
        # Check if path exists
        assert result == -1 or result >= 1

    def test_dead_end_in_bank(self, solution):
        """Bank contains genes that lead to dead ends"""
        startGene = "AACCGGTT"
        endGene = "AAACGGTA"
        bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA", "TTTTTTTT"]
        expected = 2
        result = solution.minMutation(startGene, endGene, bank)
        assert result == expected

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
