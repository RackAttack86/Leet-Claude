"""
Pattern Mapper

Maps LeetCode topics to the repository's pattern categories.
Includes manual overrides for problems that need special categorization.
"""

from typing import List, Optional, Dict


# Priority-ordered mapping: topics checked in this order, first match wins
TOPIC_TO_PATTERN: Dict[str, str] = {
    # Specific data structures (highest priority)
    "Trie": "tries",
    "Heap (Priority Queue)": "heaps",
    "Stack": "stacks_queues",
    "Queue": "stacks_queues",
    "Monotonic Stack": "stacks_queues",
    "Monotonic Queue": "stacks_queues",
    "Linked List": "linked_lists",
    "Binary Search Tree": "trees",
    "Binary Tree": "trees",
    "Tree": "trees",

    # Specific techniques
    "Sliding Window": "sliding_window",
    "Two Pointers": "two_pointers",
    "Binary Search": "binary_search",
    "Backtracking": "backtracking",
    "Dynamic Programming": "dynamic_programming",
    "Greedy": "greedy",
    "Bit Manipulation": "bit_manipulation",

    # Graph-related
    "Graph": "graphs",
    "Topological Sort": "graphs",
    "Union Find": "graphs",
    "Shortest Path": "graphs",
    "Minimum Spanning Tree": "graphs",

    # BFS/DFS (often combined with other patterns)
    "Depth-First Search": "bfs_dfs",
    "Breadth-First Search": "bfs_dfs",

    # Intervals
    "Merge Intervals": "intervals",
    "Line Sweep": "intervals",
}

# Manual overrides for specific problems that need special categorization
# Maps problem number to pattern
PROBLEM_PATTERN_OVERRIDES: Dict[int, str] = {
    # Heap problems often tagged as other things
    23: "heaps",      # Merge K Sorted Lists - tagged as Linked List
    253: "heaps",     # Meeting Rooms II
    295: "heaps",     # Find Median from Data Stream
    347: "heaps",     # Top K Frequent Elements
    373: "heaps",     # Find K Pairs with Smallest Sums
    215: "heaps",     # Kth Largest Element
    502: "heaps",     # IPO

    # Two pointer problems
    11: "two_pointers",   # Container With Most Water
    15: "two_pointers",   # 3Sum
    42: "two_pointers",   # Trapping Rain Water
    125: "two_pointers",  # Valid Palindrome
    167: "two_pointers",  # Two Sum II
    392: "two_pointers",  # Is Subsequence

    # Sliding window
    3: "sliding_window",   # Longest Substring Without Repeating Characters
    76: "sliding_window",  # Minimum Window Substring
    209: "sliding_window", # Minimum Size Subarray Sum
    30: "sliding_window",  # Substring with Concatenation of All Words

    # Binary search
    4: "binary_search",    # Median of Two Sorted Arrays
    33: "binary_search",   # Search in Rotated Sorted Array
    34: "binary_search",   # Find First and Last Position
    153: "binary_search",  # Find Minimum in Rotated Sorted Array

    # Intervals
    56: "intervals",   # Merge Intervals
    57: "intervals",   # Insert Interval
    228: "intervals",  # Summary Ranges
    452: "intervals",  # Minimum Number of Arrows

    # Dynamic programming
    5: "dynamic_programming",    # Longest Palindromic Substring
    53: "dynamic_programming",   # Maximum Subarray (Kadane's)
    70: "dynamic_programming",   # Climbing Stairs
    72: "dynamic_programming",   # Edit Distance
    97: "dynamic_programming",   # Interleaving String
    120: "dynamic_programming",  # Triangle
    121: "greedy",               # Best Time to Buy and Sell Stock (greedy works)
    122: "greedy",               # Best Time to Buy and Sell Stock II
    123: "dynamic_programming",  # Best Time to Buy and Sell Stock III
    139: "dynamic_programming",  # Word Break
    188: "dynamic_programming",  # Best Time to Buy and Sell Stock IV
    198: "dynamic_programming",  # House Robber
    221: "dynamic_programming",  # Maximal Square
    300: "dynamic_programming",  # Longest Increasing Subsequence
    322: "dynamic_programming",  # Coin Change
    918: "dynamic_programming",  # Maximum Sum Circular Subarray

    # Greedy
    45: "greedy",    # Jump Game II
    55: "greedy",    # Jump Game
    134: "greedy",   # Gas Station
    135: "greedy",   # Candy

    # Backtracking
    17: "backtracking",  # Letter Combinations of a Phone Number
    22: "backtracking",  # Generate Parentheses
    39: "backtracking",  # Combination Sum
    46: "backtracking",  # Permutations
    52: "backtracking",  # N-Queens II
    77: "backtracking",  # Combinations
    79: "backtracking",  # Word Search

    # Stack problems
    20: "stacks_queues",   # Valid Parentheses
    71: "stacks_queues",   # Simplify Path
    150: "stacks_queues",  # Evaluate Reverse Polish Notation
    155: "stacks_queues",  # Min Stack
    224: "stacks_queues",  # Basic Calculator

    # Graph problems
    127: "graphs",  # Word Ladder
    130: "graphs",  # Surrounded Regions
    133: "graphs",  # Clone Graph
    200: "bfs_dfs", # Number of Islands
    207: "graphs",  # Course Schedule
    210: "graphs",  # Course Schedule II
    399: "graphs",  # Evaluate Division
    433: "graphs",  # Minimum Genetic Mutation
    909: "graphs",  # Snakes and Ladders

    # Tries
    208: "tries",  # Implement Trie
    211: "tries",  # Design Add and Search Words
    212: "tries",  # Word Search II

    # Trees
    98: "trees",   # Validate Binary Search Tree
    100: "trees",  # Same Tree
    101: "trees",  # Symmetric Tree
    102: "trees",  # Binary Tree Level Order Traversal
    103: "trees",  # Binary Tree Zigzag Level Order Traversal
    104: "trees",  # Maximum Depth of Binary Tree
    105: "trees",  # Construct Binary Tree from Preorder and Inorder
    106: "trees",  # Construct Binary Tree from Inorder and Postorder
    108: "trees",  # Convert Sorted Array to BST
    112: "trees",  # Path Sum
    114: "trees",  # Flatten Binary Tree to Linked List
    117: "trees",  # Populating Next Right Pointers II
    124: "trees",  # Binary Tree Maximum Path Sum
    129: "trees",  # Sum Root to Leaf Numbers
    173: "trees",  # Binary Search Tree Iterator
    199: "trees",  # Binary Tree Right Side View
    222: "trees",  # Count Complete Tree Nodes
    226: "trees",  # Invert Binary Tree
    230: "trees",  # Kth Smallest Element in BST
    236: "trees",  # Lowest Common Ancestor
    530: "trees",  # Minimum Absolute Difference in BST
    637: "trees",  # Average of Levels in Binary Tree

    # Linked lists
    2: "linked_lists",    # Add Two Numbers
    19: "linked_lists",   # Remove Nth Node From End
    21: "linked_lists",   # Merge Two Sorted Lists
    25: "linked_lists",   # Reverse Nodes in k-Group
    61: "linked_lists",   # Rotate List
    82: "linked_lists",   # Remove Duplicates from Sorted List II
    86: "linked_lists",   # Partition List
    92: "linked_lists",   # Reverse Linked List II
    138: "linked_lists",  # Copy List with Random Pointer
    141: "linked_lists",  # Linked List Cycle
    146: "linked_lists",  # LRU Cache
    148: "linked_lists",  # Sort List

    # Bit manipulation
    67: "bit_manipulation",   # Add Binary
    136: "bit_manipulation",  # Single Number
    137: "bit_manipulation",  # Single Number II
    190: "bit_manipulation",  # Reverse Bits
    191: "bit_manipulation",  # Number of 1 Bits
    201: "bit_manipulation",  # Bitwise AND of Numbers Range
}


class PatternMapper:
    """Maps LeetCode problems to repository patterns."""

    def __init__(self, overrides: Optional[Dict[int, str]] = None):
        """
        Initialize the pattern mapper.

        Args:
            overrides: Additional pattern overrides (problem_number -> pattern)
        """
        self.overrides = {**PROBLEM_PATTERN_OVERRIDES}
        if overrides:
            self.overrides.update(overrides)

    def map_to_pattern(
        self,
        problem_number: int,
        topics: List[str]
    ) -> str:
        """
        Map a problem to its primary pattern.

        Args:
            problem_number: The LeetCode problem number
            topics: List of topic tags from LeetCode

        Returns:
            The pattern name for the repository
        """
        # Check for manual override first
        if problem_number in self.overrides:
            return self.overrides[problem_number]

        # Try to match topics in priority order
        for topic in topics:
            for topic_key, pattern in TOPIC_TO_PATTERN.items():
                if topic_key.lower() == topic.lower():
                    return pattern

        # Partial matching as fallback
        for topic in topics:
            topic_lower = topic.lower()
            for topic_key, pattern in TOPIC_TO_PATTERN.items():
                if topic_key.lower() in topic_lower or topic_lower in topic_key.lower():
                    return pattern

        # Default fallbacks based on common patterns
        topic_str = " ".join(topics).lower()

        if "array" in topic_str and "sort" in topic_str:
            return "two_pointers"
        if "matrix" in topic_str:
            return "bfs_dfs"
        if "interval" in topic_str:
            return "intervals"
        if "string" in topic_str:
            return "two_pointers"
        if "hash" in topic_str:
            return "two_pointers"  # Often hashmap + two pointers
        if "math" in topic_str:
            return "bit_manipulation"  # Math problems often grouped here

        # Ultimate fallback - put in dynamic_programming as it's versatile
        return "dynamic_programming"

    def suggest_patterns(self, topics: List[str]) -> List[str]:
        """
        Suggest possible patterns for a problem (for manual review).

        Args:
            topics: List of topic tags

        Returns:
            List of suggested pattern names
        """
        suggestions = []
        for topic in topics:
            for topic_key, pattern in TOPIC_TO_PATTERN.items():
                if topic_key.lower() in topic.lower() or topic.lower() in topic_key.lower():
                    if pattern not in suggestions:
                        suggestions.append(pattern)
        return suggestions

    def get_pattern_display_name(self, pattern: str) -> str:
        """
        Convert pattern directory name to display name.

        Args:
            pattern: Pattern directory name (e.g., "two_pointers")

        Returns:
            Display name (e.g., "Two Pointers")
        """
        return pattern.replace("_", " ").title()


# All valid patterns in the repository
VALID_PATTERNS = [
    "backtracking",
    "bfs_dfs",
    "binary_search",
    "bit_manipulation",
    "dynamic_programming",
    "graphs",
    "greedy",
    "heaps",
    "intervals",
    "linked_lists",
    "sliding_window",
    "stacks_queues",
    "trees",
    "tries",
    "two_pointers",
]
