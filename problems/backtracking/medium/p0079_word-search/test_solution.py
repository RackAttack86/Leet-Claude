"""
Tests for LeetCode Problem #79: Word Search
"""

import pytest
try:
    from user_solution import Solution
    from solution import PROBLEM_METADATA
except ImportError:
    from solution import Solution, PROBLEM_METADATA


class TestWordSearch:
    """Test cases for Word Search problem"""

    @pytest.fixture
    def solution(self):
        """Create a Solution instance for each test"""
        return Solution()

    def test_example_1(self, solution):
        """Example 1: word = 'ABCCED'"""
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        assert solution.exist(board, "ABCCED") is True

    def test_example_2(self, solution):
        """Example 2: word = 'SEE'"""
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        assert solution.exist(board, "SEE") is True

    def test_example_3(self, solution):
        """Example 3: word = 'ABCB'"""
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        assert solution.exist(board, "ABCB") is False

    # Edge cases
    def test_single_cell_board_found(self, solution):
        """Single cell board - word found"""
        board = [["A"]]
        assert solution.exist(board, "A") is True

    def test_single_cell_board_not_found(self, solution):
        """Single cell board - word not found"""
        board = [["A"]]
        assert solution.exist(board, "B") is False

    def test_single_row_board(self, solution):
        """Single row board"""
        board = [["A", "B", "C", "D"]]
        assert solution.exist(board, "ABCD") is True
        assert solution.exist(board, "DCBA") is True
        assert solution.exist(board, "ABCE") is False

    def test_single_column_board(self, solution):
        """Single column board"""
        board = [["A"], ["B"], ["C"], ["D"]]
        assert solution.exist(board, "ABCD") is True
        assert solution.exist(board, "DCBA") is True
        assert solution.exist(board, "ABCE") is False

    def test_word_not_found(self, solution):
        """Word does not exist in board"""
        board = [["A", "B", "C"], ["D", "E", "F"]]
        assert solution.exist(board, "XYZ") is False

    def test_word_at_edges(self, solution):
        """Word found at board edges"""
        board = [["A", "B", "C"], ["H", "X", "D"], ["G", "F", "E"]]
        # Perimeter: ABCDEFGH
        assert solution.exist(board, "ABCDEFGH") is True

    def test_word_at_corners(self, solution):
        """Word starting from each corner"""
        board = [["A", "B"], ["C", "D"]]
        assert solution.exist(board, "AB") is True
        assert solution.exist(board, "AC") is True
        assert solution.exist(board, "BD") is True
        assert solution.exist(board, "CD") is True

    def test_cannot_reuse_cell(self, solution):
        """Same cell cannot be used twice"""
        board = [["A", "B"], ["C", "D"]]
        assert solution.exist(board, "ABA") is False  # Would need to reuse A

    def test_single_letter_word(self, solution):
        """Single letter word"""
        board = [["A", "B", "C"], ["D", "E", "F"]]
        assert solution.exist(board, "E") is True
        assert solution.exist(board, "Z") is False

    def test_word_longer_than_cells(self, solution):
        """Word longer than total cells"""
        board = [["A", "B"], ["C", "D"]]
        assert solution.exist(board, "ABCDE") is False

    def test_zigzag_path(self, solution):
        """Word requires zigzag path"""
        board = [["A", "B", "C"], ["F", "E", "D"], ["G", "H", "I"]]
        # Path: A -> B -> E -> D -> C is not valid (not adjacent)
        # Path: A -> B -> C -> D -> E -> F -> G -> H -> I
        assert solution.exist(board, "ABCDEF") is True

    def test_all_same_letters(self, solution):
        """Board with all same letters"""
        board = [["A", "A", "A"], ["A", "A", "A"]]
        assert solution.exist(board, "AAAAAA") is True
        assert solution.exist(board, "AAAAAAA") is False  # Only 6 cells

    def test_word_requires_backtracking(self, solution):
        """Word that requires backtracking due to false starts"""
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        # Path exists but requires backtracking from false starts with multiple C's
        assert solution.exist(board, "ABCCED") is True
        # Word that doesn't exist - requires backtracking to confirm
        assert solution.exist(board, "ABCESEEDCBA") is False

    def test_uppercase_and_lowercase(self, solution):
        """Case sensitivity - uppercase and lowercase are different"""
        board = [["a", "B"], ["C", "d"]]
        assert solution.exist(board, "aB") is True
        assert solution.exist(board, "AB") is False
        assert solution.exist(board, "ab") is False

    def test_max_word_length(self, solution):
        """Maximum word length (15 characters)"""
        board = [["A", "B", "C", "D", "E", "F"],
                 ["L", "K", "J", "I", "H", "G"],
                 ["M", "N", "O", "P", "Q", "R"]]
        # Path: A-B-C-D-E-F-G-H-I-J-K-L-M-N-O = 15 chars
        assert solution.exist(board, "ABCDEFGHIJKLMNO") is True

    def test_6x6_board_max_size(self, solution):
        """Maximum board size 6x6"""
        board = [["A"] * 6 for _ in range(6)]
        assert solution.exist(board, "A" * 15) is True

    # Metadata validation
    def test_metadata_exists(self):
        """Verify problem metadata is complete"""
        required_fields = ["number", "name", "difficulty", "pattern", "url"]
        for field in required_fields:
            assert field in PROBLEM_METADATA
            assert PROBLEM_METADATA[field] is not None
