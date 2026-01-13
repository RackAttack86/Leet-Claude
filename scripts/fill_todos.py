"""
Helper script to track which problems have TODOs filled
This is a reference for tracking progress
"""

# High priority problems to fill in (most common interview questions)
HIGH_PRIORITY = [
    # Two Pointers
    ("problems/two_pointers/p0015_3sum/solution.py", "3Sum"),
    ("problems/two_pointers/p0011_container-with-most-water/solution.py", "Container With Most Water"),

    # Sliding Window
    ("problems/sliding_window/p0003_longest-substring-without-repeating-characters/solution.py", "Longest Substring"),

    # Binary Search
    ("problems/binary_search/p0704_binary-search/solution.py", "Binary Search"),
    ("problems/binary_search/p0033_search-in-rotated-sorted-array/solution.py", "Search Rotated Array"),

    # Trees
    ("problems/trees/p0226_invert-binary-tree/solution.py", "Invert Tree"),
    ("problems/trees/p0104_maximum-depth-of-binary-tree/solution.py", "Max Depth"),
    ("problems/trees/p0102_binary-tree-level-order-traversal/solution.py", "Level Order"),

    # Dynamic Programming
    ("problems/dynamic_programming/p0198_house-robber/solution.py", "House Robber"),
    ("problems/dynamic_programming/p0322_coin-change/solution.py", "Coin Change"),

    # Backtracking
    ("problems/backtracking/p0046_permutations/solution.py", "Permutations"),
    ("problems/backtracking/p0078_subsets/solution.py", "Subsets"),

    # BFS/DFS
    ("problems/bfs_dfs/p0200_number-of-islands/solution.py", "Number of Islands"),

    # Linked Lists
    ("problems/linked_lists/p0206_reverse-linked-list/solution.py", "Reverse Linked List"),
    ("problems/linked_lists/p0141_linked-list-cycle/solution.py", "Linked List Cycle"),

    # Stacks
    ("problems/stacks_queues/p0020_valid-parentheses/solution.py", "Valid Parentheses"),
]

print("High priority problems to fill:")
for path, name in HIGH_PRIORITY:
    print(f"  - {name}: {path}")
