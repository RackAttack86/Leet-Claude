# LeetCode Problem Hints & Approaches

This guide provides hints and approaches for all problems in the repository. Use this as a reference when solving problems.

## Two Pointers

### #1 Two Sum ✓ (Completed)
**Hint:** Use hash map to store complements
**Pattern:** Hash table lookup
**Key Insight:** Trade O(n) space for O(n) time instead of O(n²) brute force

### #11 Container With Most Water
**Hint:** Start with widest container, move pointer at shorter line
**Pattern:** Greedy two pointers
**Key Insight:** Area = min(height[left], height[right]) * width. Moving shorter line might increase area.

### #15 3Sum
**Hint:** Sort first, fix one element, use two pointers for remaining two
**Pattern:** Sorting + two pointers
**Key Insight:** Skip duplicates carefully to avoid duplicate triplets

### #42 Trapping Rain Water (Hard)
**Hint:** Water trapped = min(max_left, max_right) - current_height
**Pattern:** Two pointers with max tracking
**Key Insight:** Use two pointers to track max heights from both sides

### #75 Sort Colors
**Hint:** Use three pointers (left for 0s, right for 2s, current for scanning)
**Pattern:** Dutch National Flag algorithm
**Key Insight:** Partition into three regions in one pass

### #125 Valid Palindrome ✓ (Completed)
**Hint:** Two pointers from both ends, skip non-alphanumeric
**Pattern:** Converging pointers
**Key Insight:** No need to create filtered string (O(1) space)

### #167 Two Sum II
**Hint:** Use sorted property - if sum too small, move left; if too large, move right
**Pattern:** Converging pointers on sorted array
**Key Insight:** O(n) time, O(1) space (better than hash map for sorted input)

### #283 Move Zeroes
**Hint:** Slow pointer tracks position for next non-zero
**Pattern:** Fast/slow pointers
**Key Insight:** Swap elements in-place as you scan

## Sliding Window

### #3 Longest Substring Without Repeating Characters
**Hint:** Expand window while characters unique, shrink when duplicate found
**Pattern:** Variable-size sliding window
**Key Insight:** Use hash map/set to track characters in current window

### #121 Best Time to Buy and Sell Stock
**Hint:** Track minimum price seen so far, calculate profit at each step
**Pattern:** Single pass with running minimum
**Key Insight:** Max profit = price - min_price_so_far

### #424 Longest Repeating Character Replacement
**Hint:** Track most frequent character in window, check if window_size - max_freq <= k
**Pattern:** Variable-size sliding window
**Key Insight:** Can replace at most k characters to make all same

### #567 Permutation in String
**Hint:** Use fixed-size sliding window with character frequency map
**Pattern:** Fixed-size sliding window
**Key Insight:** Permutation has same character frequencies

## Binary Search

### #33 Search in Rotated Sorted Array
**Hint:** Determine which half is sorted, then decide which half to search
**Pattern:** Modified binary search
**Key Insight:** At least one half is always sorted

### #34 Find First and Last Position
**Hint:** Use binary search twice - once for leftmost, once for rightmost
**Pattern:** Binary search variants
**Key Insight:** Modify binary search to find boundaries instead of exact match

### #153 Find Minimum in Rotated Sorted Array
**Hint:** If mid > right, minimum is in right half; otherwise in left half
**Pattern:** Binary search on rotated array
**Key Insight:** Minimum is where the rotation happened

### #704 Binary Search
**Hint:** Classic binary search - compare mid with target
**Pattern:** Standard binary search
**Key Insight:** O(log n) by halving search space each iteration

## Trees

### #98 Validate Binary Search Tree
**Hint:** Use inorder traversal (should be sorted) or pass min/max bounds down
**Pattern:** Tree traversal with validation
**Key Insight:** For BST, left < node < right for all nodes

### #100 Same Tree
**Hint:** Recursively check if both nodes are equal and subtrees are same
**Pattern:** Tree recursion
**Key Insight:** Base case: both null = true, one null = false

### #102 Binary Tree Level Order Traversal
**Hint:** Use BFS with queue, process level by level
**Pattern:** BFS on tree
**Key Insight:** Track level size to separate levels

### #104 Maximum Depth of Binary Tree
**Hint:** Depth = 1 + max(depth(left), depth(right))
**Pattern:** Tree recursion
**Key Insight:** Simple recursive problem - great for beginners

### #226 Invert Binary Tree
**Hint:** Swap left and right children recursively
**Pattern:** Tree recursion
**Key Insight:** Recursively invert subtrees then swap

## BFS/DFS

### #133 Clone Graph
**Hint:** Use hash map to track old node -> new node mapping
**Pattern:** DFS/BFS with hash map
**Key Insight:** Visit each node once, create copy, recursively clone neighbors

### #200 Number of Islands
**Hint:** DFS/BFS from each land cell, marking visited cells
**Pattern:** Grid DFS/BFS
**Key Insight:** Each DFS explores one complete island

## Dynamic Programming

### #5 Longest Palindromic Substring
**Hint:** Expand around each center (consider both odd/even length palindromes)
**Pattern:** Expand around center or 2D DP
**Key Insight:** n centers (single char) + n-1 centers (between chars)

### #70 Climbing Stairs ✓ (Completed)
**Hint:** ways(n) = ways(n-1) + ways(n-2) (Fibonacci)
**Pattern:** 1D DP
**Key Insight:** Can reach step n from n-1 or n-2

### #198 House Robber
**Hint:** rob(i) = max(rob(i-1), rob(i-2) + nums[i])
**Pattern:** 1D DP
**Key Insight:** Either rob current house or skip it

### #300 Longest Increasing Subsequence
**Hint:** dp[i] = length of LIS ending at i
**Pattern:** 1D DP or binary search
**Key Insight:** O(n²) DP or O(n log n) with binary search + patience sorting

### #322 Coin Change
**Hint:** dp[amount] = min coins needed for that amount
**Pattern:** 1D DP (unbounded knapsack)
**Key Insight:** Try each coin for each amount, take minimum

## Backtracking

### #39 Combination Sum
**Hint:** Try including/excluding each number, allow reuse
**Pattern:** Backtracking with combinations
**Key Insight:** Can reuse same element (pass same index in recursion)

### #46 Permutations
**Hint:** Swap elements and recurse, backtrack by swapping back
**Pattern:** Backtracking with permutations
**Key Insight:** n! permutations, each element used exactly once

### #78 Subsets
**Hint:** For each element, choose to include it or not
**Pattern:** Backtracking with subsets
**Key Insight:** 2ⁿ subsets total (each element has 2 choices)

## Greedy

### #45 Jump Game II
**Hint:** Track furthest reachable position at each step
**Pattern:** Greedy with range tracking
**Key Insight:** Jump when current range ends

### #55 Jump Game
**Hint:** Track furthest position reachable, check if reaches end
**Pattern:** Greedy
**Key Insight:** Update max reach at each position

### #134 Gas Station
**Hint:** If total gas >= total cost, solution exists
**Pattern:** Greedy
**Key Insight:** Start from position where we run out of gas

## Heaps

### #215 Kth Largest Element
**Hint:** Use min heap of size k or quickselect
**Pattern:** Heap for top-k
**Key Insight:** Maintain heap of k largest elements

### #295 Find Median from Data Stream (Hard)
**Hint:** Use two heaps - max heap for smaller half, min heap for larger half
**Pattern:** Two heaps
**Key Insight:** Balance heaps so sizes differ by at most 1

### #347 Top K Frequent Elements
**Hint:** Count frequencies, use heap or bucket sort
**Pattern:** Heap for top-k
**Key Insight:** O(n log k) with heap, O(n) with bucket sort

## Tries

### #208 Implement Trie
**Hint:** Each node has children map and is_end_of_word flag
**Pattern:** Trie data structure
**Key Insight:** Prefix tree for efficient prefix matching

### #211 Design Add and Search Words
**Hint:** Like Trie but '.' matches any character (use recursion)
**Pattern:** Trie with wildcard search
**Key Insight:** For '.', try all possible children

## Intervals

### #56 Merge Intervals
**Hint:** Sort by start time, merge overlapping intervals
**Pattern:** Sorting + greedy merge
**Key Insight:** If current.start <= prev.end, they overlap

### #57 Insert Interval
**Hint:** Add non-overlapping before, merge overlapping, add non-overlapping after
**Pattern:** Three-phase processing
**Key Insight:** Don't modify input, build result

## Linked Lists

### #21 Merge Two Sorted Lists
**Hint:** Use dummy node, compare heads and link smaller one
**Pattern:** Two pointer merge
**Key Insight:** Dummy node simplifies edge cases

### #141 Linked List Cycle
**Hint:** Fast/slow pointers - if they meet, there's a cycle
**Pattern:** Floyd's cycle detection
**Key Insight:** Fast moves 2 steps, slow moves 1 step

### #206 Reverse Linked List
**Hint:** Three pointers: prev, current, next
**Pattern:** In-place pointer manipulation
**Key Insight:** Reverse one link at a time

## Stacks/Queues

### #20 Valid Parentheses
**Hint:** Use stack - push opening, pop and match for closing
**Pattern:** Stack for matching
**Key Insight:** Last opened must be first closed (LIFO)

### #155 Min Stack
**Hint:** Use auxiliary stack to track minimums
**Pattern:** Stack with extra tracking
**Key Insight:** Each element tracks minimum at that level

## Bit Manipulation

### #136 Single Number
**Hint:** XOR all numbers - duplicates cancel out
**Pattern:** XOR properties
**Key Insight:** a ⊕ a = 0, a ⊕ 0 = a

### #191 Number of 1 Bits
**Hint:** Use n & (n-1) to clear rightmost 1 bit
**Pattern:** Bit manipulation
**Key Insight:** n & (n-1) removes rightmost set bit

### #338 Counting Bits
**Hint:** bits[i] = bits[i >> 1] + (i & 1)
**Pattern:** DP with bit manipulation
**Key Insight:** Count of i = count of i//2 + last bit

## Graphs

### #207 Course Schedule
**Hint:** Detect cycle in directed graph using DFS or topological sort
**Pattern:** Cycle detection
**Key Insight:** If cycle exists, impossible to finish all courses
