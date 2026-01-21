"""
Batch Importer

CLI tool for importing LeetCode problems in bulk.
Includes the Top Interview 150 problem list.
"""

import argparse
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
import json
import os

from .api_client import LeetCodeClient
from .problem_parser import ProblemParser
from .pattern_mapper import PatternMapper, VALID_PATTERNS
from .solution_generator import SolutionGenerator, ReadmeGenerator
from .test_generator import TestGenerator


# Top Interview 150 Problems - (number, slug, difficulty, category_hint)
TOP_INTERVIEW_150: List[Tuple[int, str, str, str]] = [
    # Array / String
    (88, "merge-sorted-array", "Easy", "two_pointers"),
    (27, "remove-element", "Easy", "two_pointers"),
    (26, "remove-duplicates-from-sorted-array", "Easy", "two_pointers"),
    (80, "remove-duplicates-from-sorted-array-ii", "Medium", "two_pointers"),
    (169, "majority-element", "Easy", "two_pointers"),
    (189, "rotate-array", "Medium", "two_pointers"),
    (121, "best-time-to-buy-and-sell-stock", "Easy", "greedy"),
    (122, "best-time-to-buy-and-sell-stock-ii", "Medium", "greedy"),
    (55, "jump-game", "Medium", "greedy"),
    (45, "jump-game-ii", "Medium", "greedy"),
    (274, "h-index", "Medium", "two_pointers"),
    (380, "insert-delete-getrandom-o1", "Medium", "two_pointers"),
    (238, "product-of-array-except-self", "Medium", "two_pointers"),
    (134, "gas-station", "Medium", "greedy"),
    (135, "candy", "Hard", "greedy"),
    (42, "trapping-rain-water", "Hard", "two_pointers"),
    (13, "roman-to-integer", "Easy", "two_pointers"),
    (12, "integer-to-roman", "Medium", "two_pointers"),
    (58, "length-of-last-word", "Easy", "two_pointers"),
    (14, "longest-common-prefix", "Easy", "two_pointers"),
    (151, "reverse-words-in-a-string", "Medium", "two_pointers"),
    (6, "zigzag-conversion", "Medium", "two_pointers"),
    (28, "find-the-index-of-the-first-occurrence-in-a-string", "Easy", "two_pointers"),
    (68, "text-justification", "Hard", "two_pointers"),

    # Two Pointers
    (125, "valid-palindrome", "Easy", "two_pointers"),
    (392, "is-subsequence", "Easy", "two_pointers"),
    (167, "two-sum-ii-input-array-is-sorted", "Medium", "two_pointers"),
    (11, "container-with-most-water", "Medium", "two_pointers"),
    (15, "3sum", "Medium", "two_pointers"),

    # Sliding Window
    (209, "minimum-size-subarray-sum", "Medium", "sliding_window"),
    (3, "longest-substring-without-repeating-characters", "Medium", "sliding_window"),
    (30, "substring-with-concatenation-of-all-words", "Hard", "sliding_window"),
    (76, "minimum-window-substring", "Hard", "sliding_window"),

    # Matrix
    (36, "valid-sudoku", "Medium", "bfs_dfs"),
    (54, "spiral-matrix", "Medium", "bfs_dfs"),
    (48, "rotate-image", "Medium", "bfs_dfs"),
    (73, "set-matrix-zeroes", "Medium", "bfs_dfs"),
    (289, "game-of-life", "Medium", "bfs_dfs"),

    # Hashmap
    (383, "ransom-note", "Easy", "two_pointers"),
    (205, "isomorphic-strings", "Easy", "two_pointers"),
    (290, "word-pattern", "Easy", "two_pointers"),
    (242, "valid-anagram", "Easy", "two_pointers"),
    (49, "group-anagrams", "Medium", "two_pointers"),
    (1, "two-sum", "Easy", "two_pointers"),
    (202, "happy-number", "Easy", "two_pointers"),
    (219, "contains-duplicate-ii", "Easy", "sliding_window"),
    (128, "longest-consecutive-sequence", "Medium", "two_pointers"),

    # Intervals
    (228, "summary-ranges", "Easy", "intervals"),
    (56, "merge-intervals", "Medium", "intervals"),
    (57, "insert-interval", "Medium", "intervals"),
    (452, "minimum-number-of-arrows-to-burst-balloons", "Medium", "intervals"),

    # Stack
    (20, "valid-parentheses", "Easy", "stacks_queues"),
    (71, "simplify-path", "Medium", "stacks_queues"),
    (155, "min-stack", "Medium", "stacks_queues"),
    (150, "evaluate-reverse-polish-notation", "Medium", "stacks_queues"),
    (224, "basic-calculator", "Hard", "stacks_queues"),

    # Linked List
    (141, "linked-list-cycle", "Easy", "linked_lists"),
    (2, "add-two-numbers", "Medium", "linked_lists"),
    (21, "merge-two-sorted-lists", "Easy", "linked_lists"),
    (138, "copy-list-with-random-pointer", "Medium", "linked_lists"),
    (92, "reverse-linked-list-ii", "Medium", "linked_lists"),
    (25, "reverse-nodes-in-k-group", "Hard", "linked_lists"),
    (19, "remove-nth-node-from-end-of-list", "Medium", "linked_lists"),
    (82, "remove-duplicates-from-sorted-list-ii", "Medium", "linked_lists"),
    (61, "rotate-list", "Medium", "linked_lists"),
    (86, "partition-list", "Medium", "linked_lists"),
    (146, "lru-cache", "Medium", "linked_lists"),

    # Binary Tree General
    (104, "maximum-depth-of-binary-tree", "Easy", "trees"),
    (100, "same-tree", "Easy", "trees"),
    (226, "invert-binary-tree", "Easy", "trees"),
    (101, "symmetric-tree", "Easy", "trees"),
    (105, "construct-binary-tree-from-preorder-and-inorder-traversal", "Medium", "trees"),
    (106, "construct-binary-tree-from-inorder-and-postorder-traversal", "Medium", "trees"),
    (117, "populating-next-right-pointers-in-each-node-ii", "Medium", "trees"),
    (114, "flatten-binary-tree-to-linked-list", "Medium", "trees"),
    (112, "path-sum", "Easy", "trees"),
    (129, "sum-root-to-leaf-numbers", "Medium", "trees"),
    (124, "binary-tree-maximum-path-sum", "Hard", "trees"),
    (173, "binary-search-tree-iterator", "Medium", "trees"),
    (222, "count-complete-tree-nodes", "Easy", "trees"),
    (236, "lowest-common-ancestor-of-a-binary-tree", "Medium", "trees"),

    # Binary Tree BFS
    (199, "binary-tree-right-side-view", "Medium", "trees"),
    (637, "average-of-levels-in-binary-tree", "Easy", "trees"),
    (102, "binary-tree-level-order-traversal", "Medium", "trees"),
    (103, "binary-tree-zigzag-level-order-traversal", "Medium", "trees"),

    # Binary Search Tree
    (530, "minimum-absolute-difference-in-bst", "Easy", "trees"),
    (230, "kth-smallest-element-in-a-bst", "Medium", "trees"),
    (98, "validate-binary-search-tree", "Medium", "trees"),

    # Graph General
    (200, "number-of-islands", "Medium", "bfs_dfs"),
    (130, "surrounded-regions", "Medium", "graphs"),
    (133, "clone-graph", "Medium", "graphs"),
    (399, "evaluate-division", "Medium", "graphs"),
    (207, "course-schedule", "Medium", "graphs"),
    (210, "course-schedule-ii", "Medium", "graphs"),

    # Graph BFS
    (909, "snakes-and-ladders", "Medium", "graphs"),
    (433, "minimum-genetic-mutation", "Medium", "graphs"),
    (127, "word-ladder", "Hard", "graphs"),

    # Trie
    (208, "implement-trie-prefix-tree", "Medium", "tries"),
    (211, "design-add-and-search-words-data-structure", "Medium", "tries"),
    (212, "word-search-ii", "Hard", "tries"),

    # Backtracking
    (17, "letter-combinations-of-a-phone-number", "Medium", "backtracking"),
    (77, "combinations", "Medium", "backtracking"),
    (46, "permutations", "Medium", "backtracking"),
    (39, "combination-sum", "Medium", "backtracking"),
    (52, "n-queens-ii", "Hard", "backtracking"),
    (22, "generate-parentheses", "Medium", "backtracking"),
    (79, "word-search", "Medium", "backtracking"),

    # Divide & Conquer
    (108, "convert-sorted-array-to-binary-search-tree", "Easy", "trees"),
    (148, "sort-list", "Medium", "linked_lists"),
    (427, "construct-quad-tree", "Medium", "trees"),
    (23, "merge-k-sorted-lists", "Hard", "heaps"),

    # Kadane's Algorithm
    (53, "maximum-subarray", "Medium", "dynamic_programming"),
    (918, "maximum-sum-circular-subarray", "Medium", "dynamic_programming"),

    # Binary Search
    (35, "search-insert-position", "Easy", "binary_search"),
    (74, "search-a-2d-matrix", "Medium", "binary_search"),
    (162, "find-peak-element", "Medium", "binary_search"),
    (33, "search-in-rotated-sorted-array", "Medium", "binary_search"),
    (34, "find-first-and-last-position-of-element-in-sorted-array", "Medium", "binary_search"),
    (153, "find-minimum-in-rotated-sorted-array", "Medium", "binary_search"),
    (4, "median-of-two-sorted-arrays", "Hard", "binary_search"),

    # Heap / Priority Queue
    (215, "kth-largest-element-in-an-array", "Medium", "heaps"),
    (502, "ipo", "Hard", "heaps"),
    (373, "find-k-pairs-with-smallest-sums", "Medium", "heaps"),
    (295, "find-median-from-data-stream", "Hard", "heaps"),

    # Bit Manipulation
    (67, "add-binary", "Easy", "bit_manipulation"),
    (190, "reverse-bits", "Easy", "bit_manipulation"),
    (191, "number-of-1-bits", "Easy", "bit_manipulation"),
    (136, "single-number", "Easy", "bit_manipulation"),
    (137, "single-number-ii", "Medium", "bit_manipulation"),
    (201, "bitwise-and-of-numbers-range", "Medium", "bit_manipulation"),

    # Math
    (9, "palindrome-number", "Easy", "bit_manipulation"),
    (66, "plus-one", "Easy", "two_pointers"),
    (172, "factorial-trailing-zeroes", "Medium", "bit_manipulation"),
    (69, "sqrtx", "Easy", "binary_search"),
    (50, "powx-n", "Medium", "binary_search"),
    (149, "max-points-on-a-line", "Hard", "two_pointers"),

    # 1D Dynamic Programming
    (70, "climbing-stairs", "Easy", "dynamic_programming"),
    (198, "house-robber", "Medium", "dynamic_programming"),
    (139, "word-break", "Medium", "dynamic_programming"),
    (322, "coin-change", "Medium", "dynamic_programming"),
    (300, "longest-increasing-subsequence", "Medium", "dynamic_programming"),

    # Multidimensional DP
    (120, "triangle", "Medium", "dynamic_programming"),
    (64, "minimum-path-sum", "Medium", "dynamic_programming"),
    (63, "unique-paths-ii", "Medium", "dynamic_programming"),
    (5, "longest-palindromic-substring", "Medium", "dynamic_programming"),
    (97, "interleaving-string", "Medium", "dynamic_programming"),
    (72, "edit-distance", "Medium", "dynamic_programming"),
    (123, "best-time-to-buy-and-sell-stock-iii", "Hard", "dynamic_programming"),
    (188, "best-time-to-buy-and-sell-stock-iv", "Hard", "dynamic_programming"),
    (221, "maximal-square", "Medium", "dynamic_programming"),
]


class BatchImporter:
    """Imports LeetCode problems in bulk."""

    def __init__(self, problems_dir: Optional[Path] = None):
        """
        Initialize the batch importer.

        Args:
            problems_dir: Path to problems directory (default: problems/)
        """
        self.problems_dir = problems_dir or Path("problems")
        self.client = LeetCodeClient(rate_limit_delay=1.5)
        self.parser = ProblemParser()
        self.mapper = PatternMapper()
        self.solution_gen = SolutionGenerator()
        self.test_gen = TestGenerator()
        self.readme_gen = ReadmeGenerator()

    def import_problem(
        self,
        slug: str,
        pattern_override: Optional[str] = None,
        skip_existing: bool = True
    ) -> bool:
        """
        Import a single problem by slug.

        Args:
            slug: Problem URL slug (e.g., "two-sum")
            pattern_override: Override the auto-detected pattern
            skip_existing: If True, skip problems that already exist

        Returns:
            True if successful, False otherwise
        """
        print(f"Fetching problem: {slug}...")

        # Fetch from API
        raw_data = self.client.fetch_problem(slug)
        if not raw_data:
            print(f"  Failed to fetch {slug}")
            return False

        # Parse problem data
        problem_data = self.parser.parse(raw_data)

        # Determine pattern
        if pattern_override and pattern_override in VALID_PATTERNS:
            problem_data["pattern"] = pattern_override
        else:
            problem_data["pattern"] = self.mapper.map_to_pattern(
                problem_data["number"],
                problem_data["topics"]
            )

        # Create directory path
        difficulty = problem_data["difficulty"].lower()
        problem_dir = (
            self.problems_dir /
            problem_data["pattern"] /
            difficulty /
            f"p{problem_data['number']:04d}_{slug}"
        )

        if problem_dir.exists():
            if skip_existing:
                print(f"  Skipping (already exists): {problem_dir}")
                return True
            else:
                print(f"  Directory already exists: {problem_dir}")
                return False

        # Ensure parent directories exist
        problem_dir.mkdir(parents=True, exist_ok=True)

        # Generate and write files
        try:
            # __init__.py
            (problem_dir / "__init__.py").touch()

            # solution.py
            solution_content = self.solution_gen.generate(problem_data)
            (problem_dir / "solution.py").write_text(solution_content, encoding="utf-8")

            # test_solution.py
            test_content = self.test_gen.generate(problem_data)
            (problem_dir / "test_solution.py").write_text(test_content, encoding="utf-8")

            # README.md
            readme_content = self.readme_gen.generate(problem_data)
            (problem_dir / "README.md").write_text(readme_content, encoding="utf-8")

            print(f"  Created: {problem_dir}")
            return True

        except Exception as e:
            print(f"  Error creating files: {e}")
            # Clean up partial directory
            if problem_dir.exists():
                import shutil
                shutil.rmtree(problem_dir)
            return False

    def import_by_number(
        self,
        problem_number: int,
        pattern_override: Optional[str] = None,
        skip_existing: bool = True
    ) -> bool:
        """
        Import a problem by its number.

        Args:
            problem_number: LeetCode problem number
            pattern_override: Override the auto-detected pattern
            skip_existing: If True, skip problems that already exist

        Returns:
            True if successful, False otherwise
        """
        # First check if it's in our Top 150 list
        for num, slug, _, hint in TOP_INTERVIEW_150:
            if num == problem_number:
                return self.import_problem(
                    slug,
                    pattern_override=pattern_override or hint,
                    skip_existing=skip_existing
                )

        # Otherwise, need to look up the slug
        print(f"Looking up problem #{problem_number}...")
        slug = self.client.get_slug_from_number(problem_number)

        if slug:
            return self.import_problem(
                slug,
                pattern_override=pattern_override,
                skip_existing=skip_existing
            )

        print(f"Problem #{problem_number} not found")
        return False

    def import_top_150(self, skip_existing: bool = True) -> Dict[str, int]:
        """
        Import all Top Interview 150 problems.

        Args:
            skip_existing: If True, skip problems that already exist

        Returns:
            Statistics dict with success/failed/skipped counts
        """
        stats = {"success": 0, "failed": 0, "skipped": 0}

        print(f"Importing Top Interview 150 problems...")
        print(f"Total problems: {len(TOP_INTERVIEW_150)}")

        for i, (number, slug, difficulty, pattern_hint) in enumerate(TOP_INTERVIEW_150, 1):
            print(f"\n[{i}/{len(TOP_INTERVIEW_150)}] Problem #{number}: {slug}")

            success = self.import_problem(
                slug,
                pattern_override=pattern_hint,
                skip_existing=skip_existing
            )

            if success:
                stats["success"] += 1
            else:
                stats["failed"] += 1

        print(f"\n{'='*50}")
        print(f"Import complete!")
        print(f"  Success: {stats['success']}")
        print(f"  Failed: {stats['failed']}")

        return stats

    def import_high_acceptance(
        self,
        limit: int = 100,
        min_acceptance: float = 50.0,
        skip_existing: bool = True
    ) -> Dict[str, int]:
        """
        Import high-acceptance, non-premium problems.

        Args:
            limit: Maximum number of problems to import
            min_acceptance: Minimum acceptance rate (0-100)
            skip_existing: If True, skip problems that already exist

        Returns:
            Statistics dict
        """
        stats = {"success": 0, "failed": 0, "skipped": 0}

        print(f"Fetching high-acceptance problems (>{min_acceptance}%)...")

        # Get all non-premium problems
        problems = self.client.fetch_all_problems(
            exclude_premium=True,
            min_acceptance=min_acceptance
        )

        # Sort by acceptance rate (highest first)
        problems.sort(key=lambda p: p.get("acRate", 0), reverse=True)

        # Limit to requested count
        problems = problems[:limit]

        print(f"Found {len(problems)} problems to import")

        for i, problem in enumerate(problems, 1):
            slug = problem.get("titleSlug")
            number = problem.get("questionFrontendId")
            ac_rate = problem.get("acRate", 0)

            print(f"\n[{i}/{len(problems)}] #{number}: {slug} ({ac_rate:.1f}%)")

            success = self.import_problem(slug, skip_existing=skip_existing)

            if success:
                stats["success"] += 1
            else:
                stats["failed"] += 1

        print(f"\n{'='*50}")
        print(f"Import complete!")
        print(f"  Success: {stats['success']}")
        print(f"  Failed: {stats['failed']}")

        return stats

    def import_batch(
        self,
        numbers: Optional[List[int]] = None,
        slugs: Optional[List[str]] = None,
        pattern_override: Optional[str] = None,
        skip_existing: bool = True
    ) -> Dict[str, int]:
        """
        Import a batch of problems.

        Args:
            numbers: List of problem numbers to import
            slugs: List of problem slugs to import
            pattern_override: Override pattern for all problems
            skip_existing: If True, skip problems that already exist

        Returns:
            Statistics dict
        """
        stats = {"success": 0, "failed": 0, "skipped": 0}

        if slugs:
            for slug in slugs:
                success = self.import_problem(
                    slug,
                    pattern_override=pattern_override,
                    skip_existing=skip_existing
                )
                if success:
                    stats["success"] += 1
                else:
                    stats["failed"] += 1

        if numbers:
            for number in numbers:
                success = self.import_by_number(
                    number,
                    pattern_override=pattern_override,
                    skip_existing=skip_existing
                )
                if success:
                    stats["success"] += 1
                else:
                    stats["failed"] += 1

        return stats


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Import LeetCode problems",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Import all Top Interview 150 problems
  python -m scripts.leetcode_fetcher.batch_importer --top-150

  # Import single problem by slug
  python -m scripts.leetcode_fetcher.batch_importer --slug two-sum

  # Import by problem number
  python -m scripts.leetcode_fetcher.batch_importer --number 1

  # Import multiple problems
  python -m scripts.leetcode_fetcher.batch_importer --numbers "1,15,23,121"

  # Import high-acceptance problems
  python -m scripts.leetcode_fetcher.batch_importer --high-acceptance --limit 50

  # Override pattern
  python -m scripts.leetcode_fetcher.batch_importer --number 23 --pattern heaps
        """
    )

    parser.add_argument(
        "--top-150",
        action="store_true",
        help="Import all Top Interview 150 problems"
    )
    parser.add_argument(
        "--high-acceptance",
        action="store_true",
        help="Import high-acceptance non-premium problems"
    )
    parser.add_argument(
        "--slug", "-s",
        help="Import single problem by slug"
    )
    parser.add_argument(
        "--number", "-n",
        type=int,
        help="Import single problem by number"
    )
    parser.add_argument(
        "--numbers",
        help="Comma-separated list of problem numbers"
    )
    parser.add_argument(
        "--pattern", "-p",
        choices=VALID_PATTERNS,
        help="Override pattern for the problem(s)"
    )
    parser.add_argument(
        "--limit", "-l",
        type=int,
        default=100,
        help="Limit for batch imports (default: 100)"
    )
    parser.add_argument(
        "--min-acceptance",
        type=float,
        default=50.0,
        help="Minimum acceptance rate for --high-acceptance (default: 50)"
    )
    parser.add_argument(
        "--no-skip",
        action="store_true",
        help="Don't skip existing problems"
    )
    parser.add_argument(
        "--problems-dir",
        type=Path,
        default=Path("problems"),
        help="Path to problems directory"
    )

    args = parser.parse_args()

    # Initialize importer
    importer = BatchImporter(problems_dir=args.problems_dir)
    skip_existing = not args.no_skip

    # Execute based on arguments
    if args.top_150:
        importer.import_top_150(skip_existing=skip_existing)

    elif args.high_acceptance:
        importer.import_high_acceptance(
            limit=args.limit,
            min_acceptance=args.min_acceptance,
            skip_existing=skip_existing
        )

    elif args.slug:
        importer.import_problem(
            args.slug,
            pattern_override=args.pattern,
            skip_existing=skip_existing
        )

    elif args.number:
        importer.import_by_number(
            args.number,
            pattern_override=args.pattern,
            skip_existing=skip_existing
        )

    elif args.numbers:
        numbers = [int(n.strip()) for n in args.numbers.split(",")]
        importer.import_batch(
            numbers=numbers,
            pattern_override=args.pattern,
            skip_existing=skip_existing
        )

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
