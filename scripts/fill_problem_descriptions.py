"""
Script to fill in TODO problem descriptions in solution.py files
"""

import os
import re
from pathlib import Path

# Problem descriptions mapped by problem number
PROBLEM_DATA = {
    # Two Pointers - Part A
    11: {
        "description": "You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).\n\nFind two lines that together with the x-axis form a container, such that the container contains the most water.\n\nReturn the maximum amount of water a container can store.\n\nNotice that you may not slant the container.",
        "constraints": ["n == height.length", "2 <= n <= 10^5", "0 <= height[i] <= 10^4"],
        "examples": [
            'Input: height = [1,8,6,2,5,4,8,3,7]\nOutput: 49\nExplanation: The vertical lines are at indices 1 and 8 with heights 8 and 7. Area = min(8,7) * (8-1) = 7 * 7 = 49',
            'Input: height = [1,1]\nOutput: 1'
        ],
        "approach": "Two Pointers (greedy)",
        "time": "O(n)",
        "space": "O(1)",
        "insights": ["Start with widest container", "Move pointer with smaller height inward", "Width decreases so need taller heights to improve"],
        "topics": ["Array", "Two Pointers", "Greedy"],
        "companies": ["Amazon", "Facebook", "Microsoft", "Google", "Apple"]
    },
    15: {
        "description": "Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.\n\nNotice that the solution set must not contain duplicate triplets.",
        "constraints": ["3 <= nums.length <= 3000", "-10^5 <= nums[i] <= 10^5"],
        "examples": [
            'Input: nums = [-1,0,1,2,-1,-4]\nOutput: [[-1,-1,2],[-1,0,1]]',
            'Input: nums = [0,1,1]\nOutput: []',
            'Input: nums = [0,0,0]\nOutput: [[0,0,0]]'
        ],
        "approach": "Sorting + Two Pointers",
        "time": "O(n^2)",
        "space": "O(1) or O(n) depending on sorting",
        "insights": ["Sort array first", "Fix one element, use two pointers for remaining two", "Skip duplicates carefully"],
        "topics": ["Array", "Two Pointers", "Sorting"],
        "companies": ["Amazon", "Facebook", "Microsoft", "Google", "Apple"]
    },
    42: {
        "description": "Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.",
        "constraints": ["n == height.length", "1 <= n <= 2 * 10^4", "0 <= height[i] <= 10^5"],
        "examples": [
            'Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]\nOutput: 6\nExplanation: The elevation map traps 6 units of rain water.',
            'Input: height = [4,2,0,3,2,5]\nOutput: 9'
        ],
        "approach": "Two Pointers or Dynamic Programming",
        "time": "O(n)",
        "space": "O(1) for two pointers, O(n) for DP",
        "insights": ["Water trapped = min(max_left, max_right) - current_height", "Two pointers: move from side with smaller max", "Or precompute max left/right arrays"],
        "topics": ["Array", "Two Pointers", "Dynamic Programming", "Stack", "Monotonic Stack"],
        "companies": ["Amazon", "Facebook", "Microsoft", "Google", "Apple", "Bloomberg"]
    },
    75: {
        "description": "Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.\n\nWe will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.\n\nYou must solve this problem without using the library's sort function.",
        "constraints": ["n == nums.length", "1 <= n <= 300", "nums[i] is either 0, 1, or 2"],
        "examples": [
            'Input: nums = [2,0,2,1,1,0]\nOutput: [0,0,1,1,2,2]',
            'Input: nums = [2,0,1]\nOutput: [0,1,2]'
        ],
        "approach": "Dutch National Flag (Three Pointers)",
        "time": "O(n)",
        "space": "O(1)",
        "insights": ["Use three pointers: low, mid, high", "Swap 0s to front, 2s to back", "One pass solution"],
        "topics": ["Array", "Two Pointers", "Sorting"],
        "companies": ["Microsoft", "Amazon", "Facebook", "Apple"]
    },
    167: {
        "description": "Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.\n\nReturn the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.\n\nThe tests are generated such that there is exactly one solution. You may not use the same element twice.\n\nYour solution must use only constant extra space.",
        "constraints": ["2 <= numbers.length <= 3 * 10^4", "-1000 <= numbers[i] <= 1000", "numbers is sorted in non-decreasing order", "-1000 <= target <= 1000", "The tests are generated such that there is exactly one solution"],
        "examples": [
            'Input: numbers = [2,7,11,15], target = 9\nOutput: [1,2]\nExplanation: 2 + 7 = 9. Return [1, 2].',
            'Input: numbers = [2,3,4], target = 6\nOutput: [1,3]',
            'Input: numbers = [2,-1,0], target = -1\nOutput: [1,2]'
        ],
        "approach": "Two Pointers",
        "time": "O(n)",
        "space": "O(1)",
        "insights": ["Array is sorted - use two pointers", "If sum < target, move left pointer right", "If sum > target, move right pointer left"],
        "topics": ["Array", "Two Pointers", "Binary Search"],
        "companies": ["Amazon", "Facebook", "Microsoft", "Adobe"]
    },
    283: {
        "description": "Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.\n\nNote that you must do this in-place without making a copy of the array.",
        "constraints": ["1 <= nums.length <= 10^4", "-2^31 <= nums[i] <= 2^31 - 1"],
        "examples": [
            'Input: nums = [0,1,0,3,12]\nOutput: [1,3,12,0,0]',
            'Input: nums = [0]\nOutput: [0]'
        ],
        "approach": "Two Pointers (in-place)",
        "time": "O(n)",
        "space": "O(1)",
        "insights": ["Keep pointer for next non-zero position", "Swap non-zero elements forward", "Two passes: move non-zeros, then fill zeros"],
        "topics": ["Array", "Two Pointers"],
        "companies": ["Facebook", "Amazon", "Microsoft", "Bloomberg"]
    },

    # Two Pointers - Part B
    344: {
        "description": "Write a function that reverses a string. The input string is given as an array of characters s.\n\nYou must do this by modifying the input array in-place with O(1) extra memory.",
        "constraints": ["1 <= s.length <= 10^5", "s[i] is a printable ascii character"],
        "examples": [
            'Input: s = ["h","e","l","l","o"]\nOutput: ["o","l","l","e","h"]',
            'Input: s = ["H","a","n","n","a","h"]\nOutput: ["h","a","n","n","a","H"]'
        ],
        "approach": "Two Pointers (In-place swap)",
        "time": "O(n)",
        "space": "O(1)",
        "insights": ["Use two pointers from both ends", "Swap characters while moving towards center", "In-place modification with O(1) space"],
        "topics": ["Two Pointers", "String"],
        "companies": ["Facebook", "Amazon", "Microsoft", "Google"]
    },
    977: {
        "description": "Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.",
        "constraints": ["1 <= nums.length <= 10^4", "-10^4 <= nums[i] <= 10^4", "nums is sorted in non-decreasing order"],
        "examples": [
            'Input: nums = [-4,-1,0,3,10]\nOutput: [0,1,9,16,100]\nExplanation: After squaring, [16,1,0,9,100]. After sorting, [0,1,9,16,100]',
            'Input: nums = [-7,-3,2,3,11]\nOutput: [4,9,9,49,121]'
        ],
        "approach": "Two Pointers (from both ends)",
        "time": "O(n)",
        "space": "O(n)",
        "insights": ["Largest squares come from either end (most negative or most positive)", "Use two pointers to compare absolute values", "Fill result array from right to left with larger values"],
        "topics": ["Array", "Two Pointers", "Sorting"],
        "companies": ["Facebook", "Amazon", "Microsoft"]
    },

    # Backtracking
    17: {
        "description": "Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.\n\nA mapping of digits to letters (just like on telephone buttons) is given below. Note that 1 does not map to any letters.",
        "constraints": ["0 <= digits.length <= 4", "digits[i] is a digit in the range ['2', '9']"],
        "examples": [
            'Input: digits = "23"\nOutput: ["ad","ae","af","bd","be","bf","cd","ce","cf"]',
            'Input: digits = ""\nOutput: []',
            'Input: digits = "2"\nOutput: ["a","b","c"]'
        ],
        "approach": "Backtracking",
        "time": "O(4^n) where n is length of digits",
        "space": "O(n) for recursion depth",
        "insights": ["Map each digit to its letters", "Use backtracking to generate all combinations", "Each digit adds 3-4 possibilities"],
        "topics": ["Hash Table", "String", "Backtracking"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
    22: {
        "description": "Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.",
        "constraints": ["1 <= n <= 8"],
        "examples": [
            'Input: n = 3\nOutput: ["((()))","(()())","(())()","()(())","()()()"]',
            'Input: n = 1\nOutput: ["()"]'
        ],
        "approach": "Backtracking with constraints",
        "time": "O(4^n / sqrt(n)) - Catalan number",
        "space": "O(n)",
        "insights": ["Add '(' if count < n", "Add ')' if ')' count < '(' count", "Backtrack to build all valid combinations"],
        "topics": ["String", "Dynamic Programming", "Backtracking"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
    40: {
        "description": "Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.\n\nEach number in candidates may only be used once in the combination. The solution set must not contain duplicate combinations.",
        "constraints": ["1 <= candidates.length <= 100", "1 <= candidates[i] <= 50", "1 <= target <= 30"],
        "examples": [
            'Input: candidates = [10,1,2,7,6,1,5], target = 8\nOutput: [[1,1,6],[1,2,5],[1,7],[2,6]]',
            'Input: candidates = [2,5,2,1,2], target = 5\nOutput: [[1,2,2],[5]]'
        ],
        "approach": "Backtracking with duplicate skipping",
        "time": "O(2^n)",
        "space": "O(n)",
        "insights": ["Sort array first", "Skip duplicates at same recursion level", "Each element used at most once"],
        "topics": ["Array", "Backtracking"],
        "companies": ["Amazon", "Facebook", "Microsoft"]
    },
    77: {
        "description": "Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].\n\nYou may return the answer in any order.",
        "constraints": ["1 <= n <= 20", "1 <= k <= n"],
        "examples": [
            'Input: n = 4, k = 2\nOutput: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]',
            'Input: n = 1, k = 1\nOutput: [[1]]'
        ],
        "approach": "Backtracking",
        "time": "O(C(n,k) * k) = O(n! / (k! * (n-k)!))",
        "space": "O(k)",
        "insights": ["Choose k elements from 1 to n", "Backtrack with start index to avoid duplicates", "Stop when combination has k elements"],
        "topics": ["Backtracking"],
        "companies": ["Amazon", "Facebook", "Microsoft", "Google"]
    },
    79: {
        "description": "Given an m x n grid of characters board and a string word, return true if word exists in the grid.\n\nThe word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.",
        "constraints": ["m == board.length", "n = board[i].length", "1 <= m, n <= 6", "1 <= word.length <= 15", "board and word consists of only lowercase and uppercase English letters"],
        "examples": [
            'Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"\nOutput: true',
            'Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"\nOutput: true',
            'Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"\nOutput: false'
        ],
        "approach": "DFS Backtracking",
        "time": "O(M * N * 4^L) where L is word length",
        "space": "O(L)",
        "insights": ["DFS from each cell", "Mark visited cells", "Backtrack to explore all paths"],
        "topics": ["Array", "Backtracking", "Matrix"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Bloomberg"]
    },
    90: {
        "description": "Given an integer array nums that may contain duplicates, return all possible subsets (the power set).\n\nThe solution set must not contain duplicate subsets. Return the solution in any order.",
        "constraints": ["1 <= nums.length <= 10", "-10 <= nums[i] <= 10"],
        "examples": [
            'Input: nums = [1,2,2]\nOutput: [[],[1],[1,2],[1,2,2],[2],[2,2]]',
            'Input: nums = [0]\nOutput: [[],[0]]'
        ],
        "approach": "Backtracking with duplicate handling",
        "time": "O(2^n)",
        "space": "O(n)",
        "insights": ["Sort array first", "Skip duplicates at same level", "Include each subset once"],
        "topics": ["Array", "Backtracking", "Bit Manipulation"],
        "companies": ["Amazon", "Facebook", "Microsoft"]
    },
    131: {
        "description": "Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.",
        "constraints": ["1 <= s.length <= 16", "s contains only lowercase English letters"],
        "examples": [
            'Input: s = "aab"\nOutput: [["a","a","b"],["aa","b"]]',
            'Input: s = "a"\nOutput: [["a"]]'
        ],
        "approach": "Backtracking with palindrome checking",
        "time": "O(n * 2^n)",
        "space": "O(n)",
        "insights": ["Try all possible partitions", "Check if each substring is palindrome", "Backtrack to build all valid partitions"],
        "topics": ["String", "Dynamic Programming", "Backtracking"],
        "companies": ["Amazon", "Facebook", "Microsoft", "Google"]
    },

    # Binary Search
    35: {
        "description": "Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.\n\nYou must write an algorithm with O(log n) runtime complexity.",
        "constraints": ["1 <= nums.length <= 10^4", "-10^4 <= nums[i] <= 10^4", "nums contains distinct values sorted in ascending order", "-10^4 <= target <= 10^4"],
        "examples": [
            'Input: nums = [1,3,5,6], target = 5\nOutput: 2',
            'Input: nums = [1,3,5,6], target = 2\nOutput: 1',
            'Input: nums = [1,3,5,6], target = 7\nOutput: 4'
        ],
        "approach": "Binary Search",
        "time": "O(log n)",
        "space": "O(1)",
        "insights": ["Standard binary search", "When not found, left pointer is insert position", "Handle edge cases at boundaries"],
        "topics": ["Array", "Binary Search"],
        "companies": ["Amazon", "Microsoft", "Bloomberg"]
    },
    69: {
        "description": "Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.\n\nYou must not use any built-in exponent function or operator.",
        "constraints": ["0 <= x <= 2^31 - 1"],
        "examples": [
            'Input: x = 4\nOutput: 2\nExplanation: The square root of 4 is 2.',
            'Input: x = 8\nOutput: 2\nExplanation: The square root of 8 is 2.82842..., rounded down to 2.'
        ],
        "approach": "Binary Search on answer space",
        "time": "O(log n)",
        "space": "O(1)",
        "insights": ["Search for answer in range [0, x]", "Use mid * mid <= x to check", "Be careful with integer overflow"],
        "topics": ["Math", "Binary Search"],
        "companies": ["Facebook", "Amazon", "Microsoft", "Google"]
    },
    162: {
        "description": "A peak element is an element that is strictly greater than its neighbors.\n\nGiven a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.\n\nYou may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.\n\nYou must write an algorithm that runs in O(log n) time.",
        "constraints": ["1 <= nums.length <= 1000", "-2^31 <= nums[i] <= 2^31 - 1", "nums[i] != nums[i + 1] for all valid i"],
        "examples": [
            'Input: nums = [1,2,3,1]\nOutput: 2\nExplanation: 3 is a peak element.',
            'Input: nums = [1,2,1,3,5,6,4]\nOutput: 5\nExplanation: 6 is a peak element.'
        ],
        "approach": "Binary Search",
        "time": "O(log n)",
        "space": "O(1)",
        "insights": ["If mid element is increasing, peak must be on right", "If mid element is decreasing, peak must be on left or at mid", "At least one peak always exists"],
        "topics": ["Array", "Binary Search"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google"]
    },
    278: {
        "description": "You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.\n\nSuppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.\n\nYou are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.",
        "constraints": ["1 <= bad <= n <= 2^31 - 1"],
        "examples": [
            'Input: n = 5, bad = 4\nOutput: 4\nExplanation:\ncall isBadVersion(3) -> false\ncall isBadVersion(5) -> true\ncall isBadVersion(4) -> true\nThen 4 is the first bad version.'
        ],
        "approach": "Binary Search",
        "time": "O(log n)",
        "space": "O(1)",
        "insights": ["Classic binary search for first occurrence", "If version is bad, search left half", "If version is good, search right half"],
        "topics": ["Binary Search", "Interactive"],
        "companies": ["Facebook", "Amazon", "Microsoft", "Google"]
    },
    374: {
        "description": "We are playing the Guess Game. The game is as follows:\n\nI pick a number from 1 to n. You have to guess which number I picked.\n\nEvery time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.\n\nYou call a pre-defined API int guess(int num), which returns three possible results:\n\n-1: Your guess is higher than the number I picked (i.e. num > pick).\n1: Your guess is lower than the number I picked (i.e. num < pick).\n0: your guess is equal to the number I picked (i.e. num == pick).\n\nReturn the number that I picked.",
        "constraints": ["1 <= n <= 2^31 - 1", "1 <= pick <= n"],
        "examples": [
            'Input: n = 10, pick = 6\nOutput: 6',
            'Input: n = 1, pick = 1\nOutput: 1',
            'Input: n = 2, pick = 1\nOutput: 1'
        ],
        "approach": "Binary Search",
        "time": "O(log n)",
        "space": "O(1)",
        "insights": ["Standard binary search", "Use guess() API to adjust search range", "Similar to finding target in sorted array"],
        "topics": ["Binary Search", "Interactive"],
        "companies": ["Google", "Amazon", "Microsoft"]
    },
    875: {
        "description": "Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.\n\nKoko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.\n\nKoko likes to eat slowly but still wants to finish eating all the bananas before the guards return.\n\nReturn the minimum integer k such that she can eat all the bananas within h hours.",
        "constraints": ["1 <= piles.length <= 10^4", "piles.length <= h <= 10^9", "1 <= piles[i] <= 10^9"],
        "examples": [
            'Input: piles = [3,6,7,11], h = 8\nOutput: 4',
            'Input: piles = [30,11,23,4,20], h = 5\nOutput: 30',
            'Input: piles = [30,11,23,4,20], h = 6\nOutput: 23'
        ],
        "approach": "Binary Search on answer",
        "time": "O(n * log m) where m is max pile size",
        "space": "O(1)",
        "insights": ["Binary search on eating speed (1 to max(piles))", "For each speed, calculate hours needed", "Find minimum speed that works"],
        "topics": ["Array", "Binary Search"],
        "companies": ["Amazon", "Google", "Microsoft"]
    },

    # Bit Manipulation
    190: {
        "description": "Reverse bits of a given 32 bits unsigned integer.",
        "constraints": ["The input must be a binary string of length 32"],
        "examples": [
            'Input: n = 00000010100101000001111010011100\nOutput:    964176192 (00111001011110000010100101000000)',
            'Input: n = 11111111111111111111111111111101\nOutput:   3221225471 (10111111111111111111111111111111)'
        ],
        "approach": "Bit manipulation",
        "time": "O(1)",
        "space": "O(1)",
        "insights": ["Process each bit from right to left", "Shift result left and add current bit", "Use bitwise operations"],
        "topics": ["Divide and Conquer", "Bit Manipulation"],
        "companies": ["Apple", "Amazon", "Microsoft"]
    },
    201: {
        "description": "Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.",
        "constraints": ["0 <= left <= right <= 2^31 - 1"],
        "examples": [
            'Input: left = 5, right = 7\nOutput: 4',
            'Input: left = 0, right = 0\nOutput: 0',
            'Input: left = 1, right = 2147483647\nOutput: 0'
        ],
        "approach": "Find common prefix",
        "time": "O(log n)",
        "space": "O(1)",
        "insights": ["AND of range is common binary prefix", "Right shift both until they're equal", "Left shift result to restore position"],
        "topics": ["Bit Manipulation"],
        "companies": ["Amazon", "Microsoft", "Google"]
    },
    231: {
        "description": "Given an integer n, return true if it is a power of two. Otherwise, return false.\n\nAn integer n is a power of two, if there exists an integer x such that n == 2^x.",
        "constraints": ["-2^31 <= n <= 2^31 - 1"],
        "examples": [
            'Input: n = 1\nOutput: true\nExplanation: 2^0 = 1',
            'Input: n = 16\nOutput: true\nExplanation: 2^4 = 16',
            'Input: n = 3\nOutput: false'
        ],
        "approach": "Bit manipulation trick",
        "time": "O(1)",
        "space": "O(1)",
        "insights": ["Power of 2 has exactly one bit set", "Use n & (n-1) == 0 to check", "Must also check n > 0"],
        "topics": ["Math", "Bit Manipulation", "Recursion"],
        "companies": ["Amazon", "Microsoft", "Google"]
    },
    268: {
        "description": "Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.",
        "constraints": ["n == nums.length", "1 <= n <= 10^4", "0 <= nums[i] <= n", "All the numbers of nums are unique"],
        "examples": [
            'Input: nums = [3,0,1]\nOutput: 2\nExplanation: n = 3 since there are 3 numbers, so all numbers are in range [0,3]. 2 is missing.',
            'Input: nums = [0,1]\nOutput: 2',
            'Input: nums = [9,6,4,2,3,5,7,0,1]\nOutput: 8'
        ],
        "approach": "XOR or Math (sum)",
        "time": "O(n)",
        "space": "O(1)",
        "insights": ["XOR all indices and values", "Missing number remains after XOR", "Or use expected sum - actual sum"],
        "topics": ["Array", "Hash Table", "Math", "Binary Search", "Bit Manipulation", "Sorting"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google"]
    },
    342: {
        "description": "Given an integer n, return true if it is a power of four. Otherwise, return false.\n\nAn integer n is a power of four, if there exists an integer x such that n == 4^x.",
        "constraints": ["-2^31 <= n <= 2^31 - 1"],
        "examples": [
            'Input: n = 16\nOutput: true',
            'Input: n = 5\nOutput: false',
            'Input: n = 1\nOutput: true'
        ],
        "approach": "Bit manipulation",
        "time": "O(1)",
        "space": "O(1)",
        "insights": ["Must be power of 2 first", "Power of 4 has 1 bit at even position", "Use (n & 0x55555555) != 0"],
        "topics": ["Math", "Bit Manipulation", "Recursion"],
        "companies": ["Google", "Amazon"]
    },
    371: {
        "description": "Given two integers a and b, return the sum of the two integers without using the operators + and -.",
        "constraints": ["-1000 <= a, b <= 1000"],
        "examples": [
            'Input: a = 1, b = 2\nOutput: 3',
            'Input: a = 2, b = 3\nOutput: 5'
        ],
        "approach": "Bit manipulation (XOR and carry)",
        "time": "O(1)",
        "space": "O(1)",
        "insights": ["XOR gives sum without carry", "AND gives carry positions", "Shift carry left and repeat"],
        "topics": ["Math", "Bit Manipulation"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google"]
    },
    461: {
        "description": "The Hamming distance between two integers is the number of positions at which the corresponding bits are different.\n\nGiven two integers x and y, return the Hamming distance between them.",
        "constraints": ["0 <= x, y <= 2^31 - 1"],
        "examples": [
            'Input: x = 1, y = 4\nOutput: 2\nExplanation:\n1   (0 0 0 1)\n4   (0 1 0 0)\n       ^   ^\nThe above arrows point to positions where bits are different.'
        ],
        "approach": "XOR and count bits",
        "time": "O(1)",
        "space": "O(1)",
        "insights": ["XOR gives differing bits", "Count 1s in XOR result", "Use Brian Kernighan's algorithm"],
        "topics": ["Bit Manipulation"],
        "companies": ["Facebook", "Amazon", "Microsoft"]
    },
    136: {
        "description": "Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.\n\nYou must implement a solution with O(n) time complexity and O(1) space complexity.",
        "constraints": ["1 <= nums.length <= 3 * 10^4", "-3 * 10^4 <= nums[i] <= 3 * 10^4", "Each element in the array appears twice except for one element which appears only once"],
        "examples": [
            'Input: nums = [2,2,1]\nOutput: 1',
            'Input: nums = [4,1,2,1,2]\nOutput: 4',
            'Input: nums = [1]\nOutput: 1'
        ],
        "approach": "XOR all elements",
        "time": "O(n)",
        "space": "O(1)",
        "insights": ["XOR of two equal numbers is 0", "XOR of 0 and any number is that number", "XOR all elements to find single one"],
        "topics": ["Array", "Bit Manipulation"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google"]
    },
    191: {
        "description": "Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).",
        "constraints": ["The input must be a binary string of length 32"],
        "examples": [
            'Input: n = 00000000000000000000000000001011\nOutput: 3\nExplanation: The input binary string has three \'1\' bits.',
            'Input: n = 00000000000000000000000010000000\nOutput: 1',
            'Input: n = 11111111111111111111111111111101\nOutput: 31'
        ],
        "approach": "Brian Kernighan's algorithm",
        "time": "O(k) where k is number of 1 bits",
        "space": "O(1)",
        "insights": ["n & (n-1) removes rightmost 1 bit", "Count how many times we can do this", "Or use built-in bit_count()"],
        "topics": ["Divide and Conquer", "Bit Manipulation"],
        "companies": ["Apple", "Amazon", "Microsoft"]
    },
    338: {
        "description": "Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.",
        "constraints": ["0 <= n <= 10^5"],
        "examples": [
            'Input: n = 2\nOutput: [0,1,1]\nExplanation:\n0 --> 0\n1 --> 1\n2 --> 10',
            'Input: n = 5\nOutput: [0,1,1,2,1,2]\nExplanation:\n0 --> 0\n1 --> 1\n2 --> 10\n3 --> 11\n4 --> 100\n5 --> 101'
        ],
        "approach": "Dynamic Programming with bit manipulation",
        "time": "O(n)",
        "space": "O(1) excluding output",
        "insights": ["ans[i] = ans[i >> 1] + (i & 1)", "Each number's count relates to i/2", "Or use ans[i] = ans[i & (i-1)] + 1"],
        "topics": ["Dynamic Programming", "Bit Manipulation"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google"]
    },

    # Dynamic Programming
    5: {
        "description": "Given a string s, return the longest palindromic substring in s.",
        "constraints": ["1 <= s.length <= 1000", "s consist of only digits and English letters"],
        "examples": [
            'Input: s = "babad"\nOutput: "bab"\nExplanation: "aba" is also a valid answer.',
            'Input: s = "cbbd"\nOutput: "bb"'
        ],
        "approach": "Expand around center or DP",
        "time": "O(n^2)",
        "space": "O(1) for expand around center, O(n^2) for DP",
        "insights": ["Each center can expand to form palindrome", "Check both odd and even length palindromes", "DP approach: dp[i][j] = s[i]==s[j] and dp[i+1][j-1]", "Manacher's algorithm achieves O(n) but complex"],
        "topics": ["String", "Dynamic Programming"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
    62: {
        "description": "There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either down or right at any point in time.\n\nGiven the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.",
        "constraints": ["1 <= m, n <= 100"],
        "examples": [
            'Input: m = 3, n = 7\nOutput: 28',
            'Input: m = 3, n = 2\nOutput: 3\nExplanation: From top-left corner, there are 3 ways to reach bottom-right corner:\n1. Right -> Down -> Down\n2. Down -> Down -> Right\n3. Down -> Right -> Down'
        ],
        "approach": "Dynamic Programming or Math (combinations)",
        "time": "O(m * n)",
        "space": "O(n) with space optimization",
        "insights": ["dp[i][j] = dp[i-1][j] + dp[i][j-1]", "Can optimize to 1D array", "Math solution: C(m+n-2, m-1)", "Each cell's paths = sum of paths from top and left"],
        "topics": ["Math", "Dynamic Programming", "Combinatorics"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Bloomberg"]
    },
    70: {
        "description": "You are climbing a staircase. It takes n steps to reach the top.\n\nEach time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?",
        "constraints": ["1 <= n <= 45"],
        "examples": [
            'Input: n = 2\nOutput: 2\nExplanation: There are two ways to climb to the top.\n1. 1 step + 1 step\n2. 2 steps',
            'Input: n = 3\nOutput: 3\nExplanation: There are three ways to climb to the top.\n1. 1 step + 1 step + 1 step\n2. 1 step + 2 steps\n3. 2 steps + 1 step'
        ],
        "approach": "Dynamic Programming (Fibonacci)",
        "time": "O(n)",
        "space": "O(1) with space optimization",
        "insights": ["This is Fibonacci sequence", "dp[i] = dp[i-1] + dp[i-2]", "Can optimize to O(1) space with two variables", "Ways to reach step n = ways to n-1 + ways to n-2"],
        "topics": ["Math", "Dynamic Programming", "Memoization"],
        "companies": ["Amazon", "Microsoft", "Google", "Adobe", "Apple"]
    },
    91: {
        "description": "A message containing letters from A-Z can be encoded into numbers using the following mapping:\n\n'A' -> \"1\"\n'B' -> \"2\"\n...\n'Z' -> \"26\"\n\nTo decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, \"11106\" can be mapped into:\n\n\"AAJF\" with the grouping (1 1 10 6)\n\"KJF\" with the grouping (11 10 6)\n\nNote that the grouping (1 11 06) is invalid because \"06\" cannot be mapped into 'F' since \"6\" is different from \"06\".\n\nGiven a string s containing only digits, return the number of ways to decode it.",
        "constraints": ["1 <= s.length <= 100", "s contains only digits and may contain leading zero(s)"],
        "examples": [
            'Input: s = "12"\nOutput: 2\nExplanation: "12" could be decoded as "AB" (1 2) or "L" (12).',
            'Input: s = "226"\nOutput: 3\nExplanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).'
        ],
        "approach": "Dynamic Programming",
        "time": "O(n)",
        "space": "O(1) with space optimization",
        "insights": ["Similar to climbing stairs with conditions", "dp[i] depends on single digit (dp[i-1]) and two digits (dp[i-2])", "Handle leading zeros and invalid two-digit numbers", "Two-digit valid if 10 <= num <= 26"],
        "topics": ["String", "Dynamic Programming"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
    139: {
        "description": "Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.\n\nNote that the same word in the dictionary may be reused multiple times in the segmentation.",
        "constraints": ["1 <= s.length <= 300", "1 <= wordDict.length <= 1000", "1 <= wordDict[i].length <= 20", "s and wordDict[i] consist of only lowercase English letters", "All strings in wordDict are unique"],
        "examples": [
            'Input: s = "leetcode", wordDict = ["leet","code"]\nOutput: true\nExplanation: Return true because "leetcode" can be segmented as "leet code".',
            'Input: s = "applepenapple", wordDict = ["apple","pen"]\nOutput: true\nExplanation: Return true because "applepenapple" can be segmented as "apple pen apple".'
        ],
        "approach": "Dynamic Programming",
        "time": "O(n^2 * m) where m is average word length",
        "space": "O(n)",
        "insights": ["dp[i] = true if s[0:i] can be segmented", "For each position, check if any word matches ending at that position", "Use set for O(1) word lookup", "dp[i] = any(dp[j] and s[j:i] in wordDict)"],
        "topics": ["Array", "Hash Table", "String", "Dynamic Programming", "Trie", "Memoization"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
    198: {
        "description": "You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.\n\nGiven an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.",
        "constraints": ["1 <= nums.length <= 100", "0 <= nums[i] <= 400"],
        "examples": [
            'Input: nums = [1,2,3,1]\nOutput: 4\nExplanation: Rob house 1 (money = 1) and then rob house 3 (money = 3). Total = 1 + 3 = 4.',
            'Input: nums = [2,7,9,3,1]\nOutput: 12\nExplanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1). Total = 2 + 9 + 1 = 12.'
        ],
        "approach": "Dynamic Programming",
        "time": "O(n)",
        "space": "O(1) with space optimization",
        "insights": ["dp[i] = max(dp[i-1], dp[i-2] + nums[i])", "Either rob current house or skip it", "Can optimize to O(1) space with two variables", "Classic DP with non-adjacent constraint"],
        "topics": ["Array", "Dynamic Programming"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
    213: {
        "description": "You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.\n\nGiven an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.",
        "constraints": ["1 <= nums.length <= 100", "0 <= nums[i] <= 1000"],
        "examples": [
            'Input: nums = [2,3,2]\nOutput: 3\nExplanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent.',
            'Input: nums = [1,2,3,1]\nOutput: 4\nExplanation: Rob house 1 (money = 1) and then rob house 3 (money = 3). Total = 1 + 3 = 4.'
        ],
        "approach": "Dynamic Programming (House Robber with circle)",
        "time": "O(n)",
        "space": "O(1)",
        "insights": ["Cannot rob both first and last house", "Run House Robber I twice: [0:n-1] and [1:n]", "Take maximum of both results", "Reduces to House Robber I problem"],
        "topics": ["Array", "Dynamic Programming"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google"]
    },
    300: {
        "description": "Given an integer array nums, return the length of the longest strictly increasing subsequence.",
        "constraints": ["1 <= nums.length <= 2500", "-10^4 <= nums[i] <= 10^4"],
        "examples": [
            'Input: nums = [10,9,2,5,3,7,101,18]\nOutput: 4\nExplanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.',
            'Input: nums = [0,1,0,3,2,3]\nOutput: 4',
            'Input: nums = [7,7,7,7,7,7,7]\nOutput: 1'
        ],
        "approach": "Dynamic Programming or Binary Search",
        "time": "O(n^2) for DP, O(n log n) for binary search",
        "space": "O(n)",
        "insights": ["DP: dp[i] = max length ending at i", "For each i, check all j < i where nums[j] < nums[i]", "Binary search: maintain array of smallest tail for each length", "Patience sorting algorithm for O(n log n)"],
        "topics": ["Array", "Binary Search", "Dynamic Programming"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
    322: {
        "description": "You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.\n\nReturn the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.\n\nYou may assume that you have an infinite number of each kind of coin.",
        "constraints": ["1 <= coins.length <= 12", "1 <= coins[i] <= 2^31 - 1", "0 <= amount <= 10^4"],
        "examples": [
            'Input: coins = [1,2,5], amount = 11\nOutput: 3\nExplanation: 11 = 5 + 5 + 1',
            'Input: coins = [2], amount = 3\nOutput: -1',
            'Input: coins = [1], amount = 0\nOutput: 0'
        ],
        "approach": "Dynamic Programming (unbounded knapsack)",
        "time": "O(amount * n) where n is number of coins",
        "space": "O(amount)",
        "insights": ["dp[i] = minimum coins to make amount i", "dp[i] = min(dp[i], dp[i-coin] + 1) for each coin", "Initialize dp with infinity except dp[0] = 0", "Bottom-up DP is more efficient than top-down"],
        "topics": ["Array", "Dynamic Programming", "Breadth-First Search"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
    416: {
        "description": "Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal.",
        "constraints": ["1 <= nums.length <= 200", "1 <= nums[i] <= 100"],
        "examples": [
            'Input: nums = [1,5,11,5]\nOutput: true\nExplanation: The array can be partitioned as [1, 5, 5] and [11].',
            'Input: nums = [1,2,3,5]\nOutput: false\nExplanation: The array cannot be partitioned into equal sum subsets.'
        ],
        "approach": "Dynamic Programming (0/1 knapsack)",
        "time": "O(n * sum)",
        "space": "O(sum) with space optimization",
        "insights": ["Reduce to subset sum problem for target = sum/2", "If sum is odd, return false", "dp[i] = can we make sum i", "dp[i] = dp[i] or dp[i-num] for each num"],
        "topics": ["Array", "Dynamic Programming"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Adobe"]
    },

    # Sliding Window
    3: {
        "description": "Given a string s, find the length of the longest substring without repeating characters.",
        "constraints": ["0 <= s.length <= 5 * 10^4", "s consists of English letters, digits, symbols and spaces"],
        "examples": [
            'Input: s = "abcabcbb"\nOutput: 3\nExplanation: The answer is "abc", with the length of 3.',
            'Input: s = "bbbbb"\nOutput: 1\nExplanation: The answer is "b", with the length of 1.'
        ],
        "approach": "Sliding Window with hash map",
        "time": "O(n)",
        "space": "O(min(m, n)) where m is charset size",
        "insights": ["Use hash map to track character positions", "Expand window with right pointer", "Contract window when duplicate found", "Track maximum window size"],
        "topics": ["Hash Table", "String", "Sliding Window"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
    121: {
        "description": "You are given an array prices where prices[i] is the price of a given stock on the ith day.\n\nYou want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.\n\nReturn the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.",
        "constraints": ["1 <= prices.length <= 10^5", "0 <= prices[i] <= 10^4"],
        "examples": [
            'Input: prices = [7,1,5,3,6,4]\nOutput: 5\nExplanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.',
            'Input: prices = [7,6,4,3,1]\nOutput: 0\nExplanation: In this case, no transactions are done and the max profit = 0.'
        ],
        "approach": "One pass tracking minimum price",
        "time": "O(n)",
        "space": "O(1)",
        "insights": ["Track minimum price seen so far", "Calculate profit at each step", "Update maximum profit", "Single pass solution"],
        "topics": ["Array", "Dynamic Programming"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
    209: {
        "description": "Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.",
        "constraints": ["1 <= target <= 10^9", "1 <= nums.length <= 10^5", "1 <= nums[i] <= 10^4"],
        "examples": [
            'Input: target = 7, nums = [2,3,1,2,4,3]\nOutput: 2\nExplanation: The subarray [4,3] has the minimal length under the problem constraint.',
            'Input: target = 4, nums = [1,4,4]\nOutput: 1'
        ],
        "approach": "Sliding Window",
        "time": "O(n)",
        "space": "O(1)",
        "insights": ["Expand window by moving right pointer", "Contract window when sum >= target", "Track minimum window size", "Each element visited at most twice"],
        "topics": ["Array", "Binary Search", "Sliding Window", "Prefix Sum"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google"]
    },
    424: {
        "description": "You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.\n\nReturn the length of the longest substring containing the same letter you can get after performing the above operations.",
        "constraints": ["1 <= s.length <= 10^5", "s consists of only uppercase English letters", "0 <= k <= s.length"],
        "examples": [
            'Input: s = "ABAB", k = 2\nOutput: 4\nExplanation: Replace the two \'A\'s with two \'B\'s or vice versa.',
            'Input: s = "AABABBA", k = 1\nOutput: 4\nExplanation: Replace the one \'A\' in the middle with \'B\' and form "AABBBBA".'
        ],
        "approach": "Sliding Window with character frequency",
        "time": "O(n)",
        "space": "O(1) - only 26 uppercase letters",
        "insights": ["Window valid if length - max_freq <= k", "Track frequency of each character", "Expand window and contract when invalid", "Max frequency character determines replacements needed"],
        "topics": ["Hash Table", "String", "Sliding Window"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google"]
    },
    438: {
        "description": "Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.\n\nAn Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.",
        "constraints": ["1 <= s.length, p.length <= 3 * 10^4", "s and p consist of lowercase English letters"],
        "examples": [
            'Input: s = "cbaebabacd", p = "abc"\nOutput: [0,6]\nExplanation:\nThe substring with start index = 0 is "cba", which is an anagram of "abc".\nThe substring with start index = 6 is "bac", which is an anagram of "abc".',
            'Input: s = "abab", p = "ab"\nOutput: [0,1,2]\nExplanation:\nThe substring with start index = 0 is "ab", which is an anagram of "ab".\nThe substring with start index = 1 is "ba", which is an anagram of "ab".\nThe substring with start index = 2 is "ab", which is an anagram of "ab".'
        ],
        "approach": "Sliding Window with character frequency",
        "time": "O(n)",
        "space": "O(1) - only 26 lowercase letters",
        "insights": ["Fixed window size = len(p)", "Compare character frequencies", "Slide window and update frequencies", "Use counter or array for frequencies"],
        "topics": ["Hash Table", "String", "Sliding Window"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google"]
    },
    567: {
        "description": "Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.\n\nIn other words, return true if one of s1's permutations is the substring of s2.",
        "constraints": ["1 <= s1.length, s2.length <= 10^4", "s1 and s2 consist of lowercase English letters"],
        "examples": [
            'Input: s1 = "ab", s2 = "eidbaooo"\nOutput: true\nExplanation: s2 contains one permutation of s1 ("ba").',
            'Input: s1 = "ab", s2 = "eidboaoo"\nOutput: false'
        ],
        "approach": "Sliding Window with character frequency",
        "time": "O(n)",
        "space": "O(1) - only 26 lowercase letters",
        "insights": ["Fixed window size = len(s1)", "Compare character frequencies in window", "Slide window through s2", "Similar to finding anagrams"],
        "topics": ["Hash Table", "Two Pointers", "String", "Sliding Window"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google"]
    },
    643: {
        "description": "You are given an integer array nums consisting of n elements, and an integer k.\n\nFind a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10^-5 will be accepted.",
        "constraints": ["n == nums.length", "1 <= k <= n <= 10^5", "-10^4 <= nums[i] <= 10^4"],
        "examples": [
            'Input: nums = [1,12,-5,-6,50,3], k = 4\nOutput: 12.75000\nExplanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75',
            'Input: nums = [5], k = 1\nOutput: 5.00000'
        ],
        "approach": "Sliding Window",
        "time": "O(n)",
        "space": "O(1)",
        "insights": ["Fixed window size k", "Calculate initial sum of first k elements", "Slide window: add new element, remove old element", "Track maximum sum"],
        "topics": ["Array", "Sliding Window"],
        "companies": ["Amazon", "Microsoft", "Google"]
    },
    713: {
        "description": "Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.",
        "constraints": ["1 <= nums.length <= 3 * 10^4", "1 <= nums[i] <= 1000", "0 <= k <= 10^6"],
        "examples": [
            'Input: nums = [10,5,2,6], k = 100\nOutput: 8\nExplanation: The 8 subarrays that have product less than 100 are:\n[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]',
            'Input: nums = [1,2,3], k = 0\nOutput: 0'
        ],
        "approach": "Sliding Window",
        "time": "O(n)",
        "space": "O(1)",
        "insights": ["Expand window while product < k", "Contract window when product >= k", "For window [left, right], adds (right - left + 1) subarrays", "All positive numbers simplify the problem"],
        "topics": ["Array", "Sliding Window"],
        "companies": ["Amazon", "Facebook", "Google"]
    },
    904: {
        "description": "You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.\n\nYou want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:\n\nYou only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.\nStarting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.\nOnce you reach a tree with fruit that cannot fit in your baskets, you must stop.\n\nGiven the integer array fruits, return the maximum number of fruits you can pick.",
        "constraints": ["1 <= fruits.length <= 10^5", "0 <= fruits[i] < fruits.length"],
        "examples": [
            'Input: fruits = [1,2,1]\nOutput: 3\nExplanation: We can pick from all 3 trees.',
            'Input: fruits = [0,1,2,2]\nOutput: 3\nExplanation: We can pick from trees [1,2,2].'
        ],
        "approach": "Sliding Window with hash map",
        "time": "O(n)",
        "space": "O(1) - at most 3 fruit types tracked",
        "insights": ["Find longest subarray with at most 2 distinct elements", "Use hash map to track fruit types in window", "Expand window and contract when types > 2", "Classic sliding window pattern"],
        "topics": ["Array", "Hash Table", "Sliding Window"],
        "companies": ["Amazon", "Facebook", "Google"]
    },
    1004: {
        "description": "Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.",
        "constraints": ["1 <= nums.length <= 10^5", "nums[i] is either 0 or 1", "0 <= k <= nums.length"],
        "examples": [
            'Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2\nOutput: 6\nExplanation: [1,1,1,0,0,1,1,1,1,1,1]\nBolded numbers were flipped from 0 to 1. The longest subarray is underlined.',
            'Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3\nOutput: 10\nExplanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]'
        ],
        "approach": "Sliding Window",
        "time": "O(n)",
        "space": "O(1)",
        "insights": ["Track count of zeros in window", "Expand window with right pointer", "Contract window when zeros > k", "Window size gives consecutive 1's after flips"],
        "topics": ["Array", "Binary Search", "Sliding Window", "Prefix Sum"],
        "companies": ["Amazon", "Microsoft", "Google"]
    },

    # Trees
    98: {
        "description": "Given the root of a binary tree, determine if it is a valid binary search tree (BST).\n\nA valid BST is defined as follows:\n\nThe left subtree of a node contains only nodes with keys less than the node's key.\nThe right subtree of a node contains only nodes with keys greater than the node's key.\nBoth the left and right subtrees must also be binary search trees.",
        "constraints": ["The number of nodes in the tree is in the range [1, 10^4]", "-2^31 <= Node.val <= 2^31 - 1"],
        "examples": [
            'Input: root = [2,1,3]\nOutput: true',
            'Input: root = [5,1,4,null,null,3,6]\nOutput: false\nExplanation: The root node\'s value is 5 but its right child\'s value is 4.'
        ],
        "approach": "Recursive with range validation or Inorder traversal",
        "time": "O(n)",
        "space": "O(h) where h is height",
        "insights": ["Pass valid range (min, max) down recursion", "Left subtree must be in (min, root.val)", "Right subtree must be in (root.val, max)", "Inorder traversal of BST is sorted"],
        "topics": ["Tree", "Depth-First Search", "Binary Search Tree", "Binary Tree"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
    100: {
        "description": "Given the roots of two binary trees p and q, write a function to check if they are the same or not.\n\nTwo binary trees are considered the same if they are structurally identical, and the nodes have the same value.",
        "constraints": ["The number of nodes in both trees is in the range [0, 100]", "-10^4 <= Node.val <= 10^4"],
        "examples": [
            'Input: p = [1,2,3], q = [1,2,3]\nOutput: true',
            'Input: p = [1,2], q = [1,null,2]\nOutput: false'
        ],
        "approach": "Recursive DFS",
        "time": "O(n)",
        "space": "O(h) where h is height",
        "insights": ["Base case: both null returns true", "If one null or values differ, return false", "Recursively check left and right subtrees", "Simple recursive pattern"],
        "topics": ["Tree", "Depth-First Search", "Binary Tree", "Breadth-First Search"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google"]
    },
    102: {
        "description": "Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).",
        "constraints": ["The number of nodes in the tree is in the range [0, 2000]", "-1000 <= Node.val <= 1000"],
        "examples": [
            'Input: root = [3,9,20,null,null,15,7]\nOutput: [[3],[9,20],[15,7]]',
            'Input: root = [1]\nOutput: [[1]]'
        ],
        "approach": "BFS with queue",
        "time": "O(n)",
        "space": "O(n)",
        "insights": ["Use queue for BFS", "Process level by level", "Track level size before processing", "Classic BFS pattern"],
        "topics": ["Tree", "Breadth-First Search", "Binary Tree"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
    104: {
        "description": "Given the root of a binary tree, return its maximum depth.\n\nA binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.",
        "constraints": ["The number of nodes in the tree is in the range [0, 10^4]", "-100 <= Node.val <= 100"],
        "examples": [
            'Input: root = [3,9,20,null,null,15,7]\nOutput: 3',
            'Input: root = [1,null,2]\nOutput: 2'
        ],
        "approach": "Recursive DFS",
        "time": "O(n)",
        "space": "O(h) where h is height",
        "insights": ["Base case: null node has depth 0", "Depth = 1 + max(left_depth, right_depth)", "Simple recursive solution", "Can also use BFS"],
        "topics": ["Tree", "Depth-First Search", "Binary Tree", "Breadth-First Search"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
    110: {
        "description": "Given a binary tree, determine if it is height-balanced.\n\nA height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.",
        "constraints": ["The number of nodes in the tree is in the range [0, 5000]", "-10^4 <= Node.val <= 10^4"],
        "examples": [
            'Input: root = [3,9,20,null,null,15,7]\nOutput: true',
            'Input: root = [1,2,2,3,3,null,null,4,4]\nOutput: false'
        ],
        "approach": "Recursive DFS with height calculation",
        "time": "O(n)",
        "space": "O(h) where h is height",
        "insights": ["Calculate height while checking balance", "Return -1 if unbalanced for early exit", "Check |left_height - right_height| <= 1", "Bottom-up approach more efficient"],
        "topics": ["Tree", "Depth-First Search", "Binary Tree"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google"]
    },
    226: {
        "description": "Given the root of a binary tree, invert the tree, and return its root.",
        "constraints": ["The number of nodes in the tree is in the range [0, 100]", "-100 <= Node.val <= 100"],
        "examples": [
            'Input: root = [4,2,7,1,3,6,9]\nOutput: [4,7,2,9,6,3,1]',
            'Input: root = [2,1,3]\nOutput: [2,3,1]'
        ],
        "approach": "Recursive DFS",
        "time": "O(n)",
        "space": "O(h) where h is height",
        "insights": ["Swap left and right children recursively", "Base case: null node returns null", "Simple recursive pattern", "Can also use BFS"],
        "topics": ["Tree", "Depth-First Search", "Binary Tree", "Breadth-First Search"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
    235: {
        "description": "Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.\n\nAccording to the definition of LCA on Wikipedia: The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).",
        "constraints": ["The number of nodes in the tree is in the range [2, 10^5]", "-10^9 <= Node.val <= 10^9", "All Node.val are unique", "p != q", "p and q will exist in the BST"],
        "examples": [
            'Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8\nOutput: 6\nExplanation: The LCA of nodes 2 and 8 is 6.',
            'Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4\nOutput: 2\nExplanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself.'
        ],
        "approach": "BST property traversal",
        "time": "O(h) where h is height",
        "space": "O(1) for iterative, O(h) for recursive",
        "insights": ["Use BST property for direction", "If both < root, go left", "If both > root, go right", "Otherwise, root is LCA"],
        "topics": ["Tree", "Depth-First Search", "Binary Search Tree", "Binary Tree"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google"]
    },
    297: {
        "description": "Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.\n\nDesign an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.",
        "constraints": ["The number of nodes in the tree is in the range [0, 10^4]", "-1000 <= Node.val <= 1000"],
        "examples": [
            'Input: root = [1,2,3,null,null,4,5]\nOutput: [1,2,3,null,null,4,5]',
            'Input: root = []\nOutput: []'
        ],
        "approach": "BFS or DFS with delimiter",
        "time": "O(n) for both serialize and deserialize",
        "space": "O(n)",
        "insights": ["Use preorder DFS or level-order BFS", "Encode null nodes explicitly", "Use delimiter to separate values", "Deserialize using queue or recursion"],
        "topics": ["String", "Tree", "Depth-First Search", "Breadth-First Search", "Design", "Binary Tree"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Bloomberg"]
    },
    543: {
        "description": "Given the root of a binary tree, return the length of the diameter of the tree.\n\nThe diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.\n\nThe length of a path between two nodes is represented by the number of edges between them.",
        "constraints": ["The number of nodes in the tree is in the range [1, 10^4]", "-100 <= Node.val <= 100"],
        "examples": [
            'Input: root = [1,2,3,4,5]\nOutput: 3\nExplanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].',
            'Input: root = [1,2]\nOutput: 1'
        ],
        "approach": "DFS with height calculation",
        "time": "O(n)",
        "space": "O(h) where h is height",
        "insights": ["Diameter at node = left_height + right_height", "Track maximum diameter globally", "Return height to parent", "Path doesn't need to go through root"],
        "topics": ["Tree", "Depth-First Search", "Binary Tree"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
    572: {
        "description": "Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.\n\nA subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.",
        "constraints": ["The number of nodes in the root tree is in the range [1, 2000]", "The number of nodes in the subRoot tree is in the range [1, 1000]", "-10^4 <= root.val <= 10^4", "-10^4 <= subRoot.val <= 10^4"],
        "examples": [
            'Input: root = [3,4,5,1,2], subRoot = [4,1,2]\nOutput: true',
            'Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]\nOutput: false'
        ],
        "approach": "DFS with subtree matching",
        "time": "O(m * n) where m and n are tree sizes",
        "space": "O(h) where h is height",
        "insights": ["Check if trees are same at each node", "Use isSameTree helper function", "Recursively check all nodes in root", "Can optimize with tree hashing"],
        "topics": ["Tree", "Depth-First Search", "Binary Tree", "String Matching", "Hash Function"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google"]
    },

    # Linked Lists
    19: {
        "description": "Given the head of a linked list, remove the nth node from the end of the list and return its head.",
        "constraints": ["The number of nodes in the list is sz", "1 <= sz <= 30", "0 <= Node.val <= 100", "1 <= n <= sz"],
        "examples": [
            'Input: head = [1,2,3,4,5], n = 2\nOutput: [1,2,3,5]',
            'Input: head = [1], n = 1\nOutput: []'
        ],
        "approach": "Two pointers with gap of n",
        "time": "O(L) where L is list length",
        "space": "O(1)",
        "insights": ["Use two pointers n steps apart", "Move both until fast reaches end", "Slow pointer will be at node before target", "Use dummy node to handle edge cases"],
        "topics": ["Linked List", "Two Pointers"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
    21: {
        "description": "You are given the heads of two sorted linked lists list1 and list2.\n\nMerge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.\n\nReturn the head of the merged linked list.",
        "constraints": ["The number of nodes in both lists is in the range [0, 50]", "-100 <= Node.val <= 100", "Both list1 and list2 are sorted in non-decreasing order"],
        "examples": [
            'Input: list1 = [1,2,4], list2 = [1,3,4]\nOutput: [1,1,2,3,4,4]',
            'Input: list1 = [], list2 = []\nOutput: []'
        ],
        "approach": "Two pointers merge",
        "time": "O(m + n)",
        "space": "O(1)",
        "insights": ["Use dummy node to simplify", "Compare values and link smaller node", "Handle remaining nodes in either list", "Classic merge pattern"],
        "topics": ["Linked List", "Recursion"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
    83: {
        "description": "Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.",
        "constraints": ["The number of nodes in the list is in the range [0, 300]", "-100 <= Node.val <= 100", "The list is guaranteed to be sorted in ascending order"],
        "examples": [
            'Input: head = [1,1,2]\nOutput: [1,2]',
            'Input: head = [1,1,2,3,3]\nOutput: [1,2,3]'
        ],
        "approach": "Single pointer traversal",
        "time": "O(n)",
        "space": "O(1)",
        "insights": ["Compare current with next node", "Skip duplicates by updating next pointer", "Continue until end of list", "Simple one-pass solution"],
        "topics": ["Linked List"],
        "companies": ["Amazon", "Microsoft", "Facebook"]
    },
    86: {
        "description": "Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.\n\nYou should preserve the original relative order of the nodes in each of the two partitions.",
        "constraints": ["The number of nodes in the list is in the range [0, 200]", "-100 <= Node.val <= 100", "-200 <= x <= 200"],
        "examples": [
            'Input: head = [1,4,3,2,5,2], x = 3\nOutput: [1,2,2,4,3,5]',
            'Input: head = [2,1], x = 2\nOutput: [1,2]'
        ],
        "approach": "Two dummy lists",
        "time": "O(n)",
        "space": "O(1)",
        "insights": ["Create two separate lists: less and greater", "Traverse and append to appropriate list", "Connect less list to greater list", "Use dummy nodes for simplicity"],
        "topics": ["Linked List", "Two Pointers"],
        "companies": ["Amazon", "Microsoft", "Google"]
    },
    92: {
        "description": "Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.",
        "constraints": ["The number of nodes in the list is n", "1 <= n <= 500", "-500 <= Node.val <= 500", "1 <= left <= right <= n"],
        "examples": [
            'Input: head = [1,2,3,4,5], left = 2, right = 4\nOutput: [1,4,3,2,5]',
            'Input: head = [5], left = 1, right = 1\nOutput: [5]'
        ],
        "approach": "Iterative reversal with markers",
        "time": "O(n)",
        "space": "O(1)",
        "insights": ["Find node before left position", "Reverse nodes between left and right", "Reconnect reversed portion", "Use dummy node for edge cases"],
        "topics": ["Linked List"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google"]
    },
    141: {
        "description": "Given head, the head of a linked list, determine if the linked list has a cycle in it.\n\nThere is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.\n\nReturn true if there is a cycle in the linked list. Otherwise, return false.",
        "constraints": ["The number of the nodes in the list is in the range [0, 10^4]", "-10^5 <= Node.val <= 10^5", "pos is -1 or a valid index in the linked-list"],
        "examples": [
            'Input: head = [3,2,0,-4], pos = 1\nOutput: true\nExplanation: There is a cycle, where tail connects to the second node.',
            'Input: head = [1], pos = -1\nOutput: false'
        ],
        "approach": "Floyd's Cycle Detection (fast and slow pointers)",
        "time": "O(n)",
        "space": "O(1)",
        "insights": ["Use fast and slow pointers", "Fast moves 2 steps, slow moves 1 step", "If cycle exists, they will meet", "Classic tortoise and hare algorithm"],
        "topics": ["Hash Table", "Linked List", "Two Pointers"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
    143: {
        "description": "You are given the head of a singly linked-list. The list can be represented as:\n\nL0 → L1 → … → Ln - 1 → Ln\n\nReorder the list to be on the following form:\n\nL0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …\n\nYou may not modify the values in the list's nodes. Only nodes themselves may be changed.",
        "constraints": ["The number of nodes in the list is in the range [1, 5 * 10^4]", "1 <= Node.val <= 1000"],
        "examples": [
            'Input: head = [1,2,3,4]\nOutput: [1,4,2,3]',
            'Input: head = [1,2,3,4,5]\nOutput: [1,5,2,4,3]'
        ],
        "approach": "Find middle, reverse second half, merge",
        "time": "O(n)",
        "space": "O(1)",
        "insights": ["Find middle using slow/fast pointers", "Reverse second half of list", "Merge two halves alternately", "Three-step approach"],
        "topics": ["Linked List", "Two Pointers", "Stack", "Recursion"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google"]
    },
    160: {
        "description": "Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.",
        "constraints": ["The number of nodes of listA is in the m", "The number of nodes of listB is in the n", "1 <= m, n <= 3 * 10^4", "1 <= Node.val <= 10^5", "0 <= skipA < m", "0 <= skipB < n"],
        "examples": [
            'Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3\nOutput: Intersected at \'8\'',
            'Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2\nOutput: No intersection'
        ],
        "approach": "Two pointers with length alignment",
        "time": "O(m + n)",
        "space": "O(1)",
        "insights": ["Two pointers traverse both lists", "When reaching end, switch to other list", "They will meet at intersection or null", "Clever pointer switching eliminates length difference"],
        "topics": ["Hash Table", "Linked List", "Two Pointers"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Bloomberg"]
    },
    206: {
        "description": "Given the head of a singly linked list, reverse the list, and return the reversed list.",
        "constraints": ["The number of nodes in the list is the range [0, 5000]", "-5000 <= Node.val <= 5000"],
        "examples": [
            'Input: head = [1,2,3,4,5]\nOutput: [5,4,3,2,1]',
            'Input: head = [1,2]\nOutput: [2,1]'
        ],
        "approach": "Iterative with three pointers",
        "time": "O(n)",
        "space": "O(1) for iterative, O(n) for recursive",
        "insights": ["Use prev, curr, next pointers", "Reverse links one by one", "Can also solve recursively", "Classic linked list problem"],
        "topics": ["Linked List", "Recursion"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
    234: {
        "description": "Given the head of a singly linked list, return true if it is a palindrome or false otherwise.",
        "constraints": ["The number of nodes in the list is in the range [1, 10^5]", "0 <= Node.val <= 9"],
        "examples": [
            'Input: head = [1,2,2,1]\nOutput: true',
            'Input: head = [1,2]\nOutput: false'
        ],
        "approach": "Find middle, reverse second half, compare",
        "time": "O(n)",
        "space": "O(1)",
        "insights": ["Find middle using slow/fast pointers", "Reverse second half", "Compare first and second halves", "Can restore list after checking"],
        "topics": ["Linked List", "Two Pointers", "Stack", "Recursion"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },

    # Intervals
    56: {
        "description": "Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.",
        "constraints": ["1 <= intervals.length <= 10^4", "intervals[i].length == 2", "0 <= starti <= endi <= 10^4"],
        "examples": [
            'Input: intervals = [[1,3],[2,6],[8,10],[15,18]]\nOutput: [[1,6],[8,10],[15,18]]\nExplanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].',
            'Input: intervals = [[1,4],[4,5]]\nOutput: [[1,5]]\nExplanation: Intervals [1,4] and [4,5] are considered overlapping.'
        ],
        "approach": "Sort and merge",
        "time": "O(n log n)",
        "space": "O(n) for output",
        "insights": ["Sort intervals by start time", "Merge if current.start <= prev.end", "Track end of current merged interval", "Classic interval merge pattern"],
        "topics": ["Array", "Sorting"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Bloomberg"]
    },
    57: {
        "description": "You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.\n\nInsert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).\n\nReturn intervals after the insertion.",
        "constraints": ["0 <= intervals.length <= 10^4", "intervals[i].length == 2", "0 <= starti <= endi <= 10^5", "intervals is sorted by starti in ascending order", "newInterval.length == 2", "0 <= start <= end <= 10^5"],
        "examples": [
            'Input: intervals = [[1,3],[6,9]], newInterval = [2,5]\nOutput: [[1,5],[6,9]]',
            'Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]\nOutput: [[1,2],[3,10],[12,16]]\nExplanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].'
        ],
        "approach": "Three-way split: before, merge, after",
        "time": "O(n)",
        "space": "O(n) for output",
        "insights": ["Add all intervals before newInterval", "Merge overlapping intervals", "Add all intervals after newInterval", "Linear time since already sorted"],
        "topics": ["Array"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "LinkedIn"]
    },
    252: {
        "description": "Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.",
        "constraints": ["0 <= intervals.length <= 10^4", "intervals[i].length == 2", "0 <= starti < endi <= 10^6"],
        "examples": [
            'Input: intervals = [[0,30],[5,10],[15,20]]\nOutput: false',
            'Input: intervals = [[7,10],[2,4]]\nOutput: true'
        ],
        "approach": "Sort and check consecutive overlaps",
        "time": "O(n log n)",
        "space": "O(1)",
        "insights": ["Sort intervals by start time", "Check if any consecutive intervals overlap", "Overlap if prev.end > curr.start", "Simple one-pass after sorting"],
        "topics": ["Array", "Sorting"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Bloomberg"]
    },
    253: {
        "description": "Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.",
        "constraints": ["1 <= intervals.length <= 10^4", "0 <= starti < endi <= 10^6"],
        "examples": [
            'Input: intervals = [[0,30],[5,10],[15,20]]\nOutput: 2',
            'Input: intervals = [[7,10],[2,4]]\nOutput: 1'
        ],
        "approach": "Min heap or chronological ordering",
        "time": "O(n log n)",
        "space": "O(n)",
        "insights": ["Use min heap to track end times", "Add meeting, remove finished ones", "Heap size = rooms needed at any time", "Or use start/end time arrays"],
        "topics": ["Array", "Two Pointers", "Greedy", "Sorting", "Heap (Priority Queue)", "Prefix Sum"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Bloomberg"]
    },
    435: {
        "description": "Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.",
        "constraints": ["1 <= intervals.length <= 10^5", "intervals[i].length == 2", "-5 * 10^4 <= starti < endi <= 5 * 10^4"],
        "examples": [
            'Input: intervals = [[1,2],[2,3],[3,4],[1,3]]\nOutput: 1\nExplanation: [1,3] can be removed and the rest of the intervals are non-overlapping.',
            'Input: intervals = [[1,2],[1,2],[1,2]]\nOutput: 2\nExplanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.'
        ],
        "approach": "Greedy: sort by end time",
        "time": "O(n log n)",
        "space": "O(1)",
        "insights": ["Sort by end time", "Greedily keep intervals with earliest end", "Count intervals that don't overlap", "Answer = total - kept"],
        "topics": ["Array", "Dynamic Programming", "Greedy", "Sorting"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google"]
    },
    452: {
        "description": "There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.\n\nArrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.\n\nGiven the array points, return the minimum number of arrows that must be shot to burst all balloons.",
        "constraints": ["1 <= points.length <= 10^5", "points[i].length == 2", "-2^31 <= xstart < xend <= 2^31 - 1"],
        "examples": [
            'Input: points = [[10,16],[2,8],[1,6],[7,12]]\nOutput: 2\nExplanation: The balloons can be burst by 2 arrows:\n- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].\n- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].',
            'Input: points = [[1,2],[3,4],[5,6],[7,8]]\nOutput: 4'
        ],
        "approach": "Greedy: sort by end",
        "time": "O(n log n)",
        "space": "O(1)",
        "insights": ["Sort by end coordinate", "Shoot arrow at end of first balloon", "Skip balloons within range", "Similar to interval scheduling"],
        "topics": ["Array", "Greedy", "Sorting"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google"]
    },
    495: {
        "description": "Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, Ashe gets poisoned for a exactly duration seconds. More formally, an attack at second t will mean Ashe is poisoned during the inclusive time interval [t, t + duration - 1]. If Teemo attacks again before the poison effect ends, the timer for it is reset, and the poison effect will end duration seconds after the new attack.\n\nYou are given a non-decreasing integer array timeSeries, where timeSeries[i] denotes that Teemo attacks Ashe at second timeSeries[i], and an integer duration.\n\nReturn the total number of seconds that Ashe is poisoned.",
        "constraints": ["1 <= timeSeries.length <= 10^4", "0 <= timeSeries[i], duration <= 10^7", "timeSeries is sorted in non-decreasing order"],
        "examples": [
            'Input: timeSeries = [1,4], duration = 2\nOutput: 4\nExplanation: Teemo\'s attacks on Ashe go as follows:\n- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.\n- At second 4, Teemo attacks, and Ashe is poisoned for seconds 4 and 5.\nAshe is poisoned for seconds 1, 2, 4, and 5, which is 4 seconds in total.',
            'Input: timeSeries = [1,2], duration = 2\nOutput: 3\nExplanation: At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.\nAt second 2 however, Teemo attacks again and resets the poison timer. Ashe is poisoned for seconds 2 and 3.\nAshe is poisoned for seconds 1, 2, and 3, which is 3 seconds in total.'
        ],
        "approach": "Interval simulation",
        "time": "O(n)",
        "space": "O(1)",
        "insights": ["If gap >= duration, add full duration", "Otherwise add gap between attacks", "Track overlapping poison effects", "Simple one-pass solution"],
        "topics": ["Array", "Simulation"],
        "companies": ["Amazon", "Google"]
    },
    759: {
        "description": "We are given a list schedule of employees, which represents the working time for each employee.\n\nEach employee has a list of non-overlapping Intervals, and these intervals are in sorted order.\n\nReturn the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.",
        "constraints": ["1 <= schedule.length, schedule[i].length <= 50", "0 <= schedule[i].start < schedule[i].end <= 10^8"],
        "examples": [
            'Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]\nOutput: [[3,4]]\nExplanation: There are a total of three employees, and all common free time intervals would be [-inf, 1], [3, 4], [10, inf].',
            'Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]\nOutput: [[5,6],[7,9]]'
        ],
        "approach": "Merge all intervals, find gaps",
        "time": "O(n log n) where n is total intervals",
        "space": "O(n)",
        "insights": ["Flatten and sort all intervals", "Merge overlapping intervals", "Gaps between merged intervals are free time", "Similar to merge intervals"],
        "topics": ["Array", "Sorting", "Heap (Priority Queue)"],
        "companies": ["Amazon", "Google", "Uber"]
    },
    986: {
        "description": "You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.\n\nReturn the intersection of these two interval lists.\n\nA closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.\n\nThe intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].",
        "constraints": ["0 <= firstList.length, secondList.length <= 1000", "firstList.length + secondList.length >= 1", "0 <= starti < endi <= 10^9", "endi < starti+1", "0 <= startj < endj <= 10^9", "endj < startj+1"],
        "examples": [
            'Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]\nOutput: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]',
            'Input: firstList = [[1,3],[5,9]], secondList = []\nOutput: []'
        ],
        "approach": "Two pointers",
        "time": "O(m + n)",
        "space": "O(1) excluding output",
        "insights": ["Use two pointers for both lists", "Intersection exists if max(start) <= min(end)", "Move pointer with smaller end time", "Classic merge pattern"],
        "topics": ["Array", "Two Pointers"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google"]
    },
    1229: {
        "description": "Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.\n\nReturn the minimum number of conference rooms required.\n\nNote: This is a premium problem, similar to meeting rooms II but with two people's schedules.",
        "constraints": ["1 <= slots1.length, slots2.length <= 1000", "slots1[i].length, slots2[i].length == 2", "slots1[i][0] < slots1[i][1]", "slots2[i][0] < slots2[i][1]", "0 <= slots1[i][j], slots2[i][j], duration <= 10^9"],
        "examples": [
            'Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8\nOutput: [60,68]',
            'Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12\nOutput: []'
        ],
        "approach": "Two pointers with intersection check",
        "time": "O(m + n)",
        "space": "O(1)",
        "insights": ["Find intersection of intervals", "Check if intersection >= duration", "Move pointer with earlier end time", "Return first valid slot"],
        "topics": ["Array", "Two Pointers", "Sorting"],
        "companies": ["Amazon", "Google", "Microsoft"]
    },

    # Heaps
    23: {
        "description": "You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.\n\nMerge all the linked-lists into one sorted linked-list and return it.",
        "constraints": ["k == lists.length", "0 <= k <= 10^4", "0 <= lists[i].length <= 500", "-10^4 <= lists[i][j] <= 10^4", "lists[i] is sorted in ascending order", "The sum of lists[i].length will not exceed 10^4"],
        "examples": [
            'Input: lists = [[1,4,5],[1,3,4],[2,6]]\nOutput: [1,1,2,3,4,4,5,6]\nExplanation: The linked-lists are:\n[\n  1->4->5,\n  1->3->4,\n  2->6\n]\nmerging them into one sorted list:\n1->1->2->3->4->4->5->6',
            'Input: lists = []\nOutput: []'
        ],
        "approach": "Min heap with k pointers",
        "time": "O(N log k) where N is total nodes",
        "space": "O(k) for heap",
        "insights": ["Use min heap to track smallest elements", "Add head of each list to heap", "Pop min, add next node from that list", "More efficient than merging pairs"],
        "topics": ["Linked List", "Divide and Conquer", "Heap (Priority Queue)", "Merge Sort"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
    215: {
        "description": "Given an integer array nums and an integer k, return the kth largest element in the array.\n\nNote that it is the kth largest element in the sorted order, not the kth distinct element.\n\nCan you solve it without sorting?",
        "constraints": ["1 <= k <= nums.length <= 10^5", "-10^4 <= nums[i] <= 10^4"],
        "examples": [
            'Input: nums = [3,2,1,5,6,4], k = 2\nOutput: 5',
            'Input: nums = [3,2,3,1,2,4,5,5,6], k = 4\nOutput: 4'
        ],
        "approach": "Min heap of size k or Quickselect",
        "time": "O(n log k) for heap, O(n) average for quickselect",
        "space": "O(k) for heap, O(1) for quickselect",
        "insights": ["Maintain min heap of k largest elements", "Heap top is kth largest", "Quickselect is faster but harder to implement", "Can also sort in O(n log n)"],
        "topics": ["Array", "Divide and Conquer", "Sorting", "Heap (Priority Queue)", "Quickselect"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
    295: {
        "description": "The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.\n\nImplement the MedianFinder class:\n\nMedianFinder() initializes the MedianFinder object.\nvoid addNum(int num) adds the integer num from the data stream to the data structure.\ndouble findMedian() returns the median of all elements so far.",
        "constraints": ["-10^5 <= num <= 10^5", "There will be at least one element in the data structure before calling findMedian", "At most 5 * 10^4 calls will be made to addNum and findMedian"],
        "examples": [
            'Input:\n["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]\n[[], [1], [2], [], [3], []]\nOutput:\n[null, null, null, 1.5, null, 2.0]',
        ],
        "approach": "Two heaps (max heap for smaller half, min heap for larger half)",
        "time": "O(log n) for addNum, O(1) for findMedian",
        "space": "O(n)",
        "insights": ["Max heap stores smaller half", "Min heap stores larger half", "Keep heaps balanced (size diff <= 1)", "Median is top of heap(s)"],
        "topics": ["Two Pointers", "Design", "Sorting", "Heap (Priority Queue)", "Data Stream"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
    347: {
        "description": "Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.",
        "constraints": ["1 <= nums.length <= 10^5", "-10^4 <= nums[i] <= 10^4", "k is in the range [1, the number of unique elements in the array]", "It is guaranteed that the answer is unique"],
        "examples": [
            'Input: nums = [1,1,1,2,2,3], k = 2\nOutput: [1,2]',
            'Input: nums = [1], k = 1\nOutput: [1]'
        ],
        "approach": "Hash map + heap or bucket sort",
        "time": "O(n log k) for heap, O(n) for bucket sort",
        "space": "O(n)",
        "insights": ["Count frequencies with hash map", "Use min heap of size k for top k", "Bucket sort: group by frequency", "Heap approach is more general"],
        "topics": ["Array", "Hash Table", "Divide and Conquer", "Sorting", "Heap (Priority Queue)", "Bucket Sort", "Counting", "Quickselect"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
    373: {
        "description": "You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.\n\nDefine a pair (u, v) which consists of one element from the first array and one element from the second array.\n\nReturn the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.",
        "constraints": ["1 <= nums1.length, nums2.length <= 10^5", "-10^9 <= nums1[i], nums2[i] <= 10^9", "nums1 and nums2 both are sorted in non-decreasing order", "1 <= k <= 10^4", "k <= nums1.length * nums2.length"],
        "examples": [
            'Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3\nOutput: [[1,2],[1,4],[1,6]]\nExplanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]',
            'Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2\nOutput: [[1,1],[1,1]]'
        ],
        "approach": "Min heap with careful exploration",
        "time": "O(k log k)",
        "space": "O(k)",
        "insights": ["Start with (0,0) pair", "Add next candidates to heap", "For (i,j), consider (i+1,j) and (i,j+1)", "Use set to avoid duplicates"],
        "topics": ["Array", "Heap (Priority Queue)"],
        "companies": ["Amazon", "Google", "Uber"]
    },
    378: {
        "description": "Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.\n\nNote that it is the kth smallest element in the sorted order, not the kth distinct element.",
        "constraints": ["n == matrix.length == matrix[i].length", "1 <= n <= 300", "-10^9 <= matrix[i][j] <= 10^9", "All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order", "1 <= k <= n^2"],
        "examples": [
            'Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8\nOutput: 13\nExplanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13',
            'Input: matrix = [[-5]], k = 1\nOutput: -5'
        ],
        "approach": "Min heap or binary search",
        "time": "O(k log n) for heap, O(n log(max-min)) for binary search",
        "space": "O(n) for heap",
        "insights": ["Heap: Start with first element of each row", "Binary search on value range", "Count elements <= mid to find position", "Both approaches have merits"],
        "topics": ["Array", "Binary Search", "Sorting", "Heap (Priority Queue)", "Matrix"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google"]
    },
    502: {
        "description": "Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.\n\nYou are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.\n\nInitially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.\n\nPick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.",
        "constraints": ["1 <= k <= 10^5", "0 <= w <= 10^9", "n == profits.length", "n == capital.length", "1 <= n <= 10^5", "0 <= profits[i] <= 10^4", "0 <= capital[i] <= 10^9"],
        "examples": [
            'Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]\nOutput: 4\nExplanation: Since your initial capital is 0, you can only start the project indexed 0.\nAfter finishing it you will obtain profit 1 and your capital becomes 1.\nWith capital 1, you can either start the project indexed 1 or the project indexed 2.\nSince you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.\nTherefore, output the final maximized capital, which is 0 + 1 + 3 = 4.',
            'Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]\nOutput: 6'
        ],
        "approach": "Two heaps (min heap for capital, max heap for profit)",
        "time": "O(n log n)",
        "space": "O(n)",
        "insights": ["Sort projects by capital requirement", "Use max heap for available projects", "Greedily pick highest profit", "Add newly affordable projects after each pick"],
        "topics": ["Array", "Greedy", "Sorting", "Heap (Priority Queue)"],
        "companies": ["Amazon", "Google"]
    },
    630: {
        "description": "There are n different online courses numbered from 1 to n. You are given an array courses where courses[i] = [durationi, lastDayi] indicate that the ith course should be taken continuously for durationi days and must be finished before or on lastDayi.\n\nYou will start on the 1st day and you cannot take two or more courses simultaneously.\n\nReturn the maximum number of courses that you can take.",
        "constraints": ["1 <= courses.length <= 10^4", "1 <= durationi, lastDayi <= 10^4"],
        "examples": [
            'Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]\nOutput: 3\nExplanation:\nThere are totally 4 courses, but you can take 3 courses at most:\nFirst, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.\nSecond, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day.\nThird, take the 2nd course, it costs 200 days so you will finish it on the 1300th day.\nThe 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.',
            'Input: courses = [[1,2]]\nOutput: 1'
        ],
        "approach": "Greedy with max heap",
        "time": "O(n log n)",
        "space": "O(n)",
        "insights": ["Sort by end time", "Use max heap to track durations", "If current course doesn't fit, replace longest", "Greedy swapping maximizes count"],
        "topics": ["Array", "Greedy", "Heap (Priority Queue)"],
        "companies": ["Amazon", "Google"]
    },
    767: {
        "description": "Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.\n\nReturn any possible rearrangement of s or return \"\" if not possible.",
        "constraints": ["1 <= s.length <= 500", "s consists of lowercase English letters"],
        "examples": [
            'Input: s = "aab"\nOutput: "aba"',
            'Input: s = "aaab"\nOutput: ""'
        ],
        "approach": "Max heap with frequency",
        "time": "O(n log k) where k is unique characters",
        "space": "O(k)",
        "insights": ["Count character frequencies", "Use max heap to prioritize most frequent", "Place highest frequency char, then second highest", "If any char frequency > (n+1)/2, impossible"],
        "topics": ["Hash Table", "String", "Greedy", "Sorting", "Heap (Priority Queue)", "Counting"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google"]
    },

    # Greedy
    45: {
        "description": "You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].\n\nEach element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:\n\n0 <= j <= nums[i] and\ni + j < n\n\nReturn the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].",
        "constraints": ["1 <= nums.length <= 10^4", "0 <= nums[i] <= 1000", "It's guaranteed that you can reach nums[n - 1]"],
        "examples": [
            'Input: nums = [2,3,1,1,4]\nOutput: 2\nExplanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.',
            'Input: nums = [2,3,0,1,4]\nOutput: 2'
        ],
        "approach": "Greedy with range tracking",
        "time": "O(n)",
        "space": "O(1)",
        "insights": ["Track current jump end and farthest reachable", "Increment jumps when reaching current end", "Update farthest as you iterate", "BFS-like level order traversal"],
        "topics": ["Array", "Dynamic Programming", "Greedy"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
    55: {
        "description": "You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.\n\nReturn true if you can reach the last index, or false otherwise.",
        "constraints": ["1 <= nums.length <= 10^4", "0 <= nums[i] <= 10^5"],
        "examples": [
            'Input: nums = [2,3,1,1,4]\nOutput: true\nExplanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.',
            'Input: nums = [3,2,1,0,4]\nOutput: false\nExplanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.'
        ],
        "approach": "Greedy tracking max reach",
        "time": "O(n)",
        "space": "O(1)",
        "insights": ["Track maximum reachable position", "If current index > max reach, return false", "Update max reach at each step", "Simple one-pass solution"],
        "topics": ["Array", "Dynamic Programming", "Greedy"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
    122: {
        "description": "You are given an integer array prices where prices[i] is the price of a given stock on the ith day.\n\nOn each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.\n\nFind and return the maximum profit you can achieve.",
        "constraints": ["1 <= prices.length <= 3 * 10^4", "0 <= prices[i] <= 10^4"],
        "examples": [
            'Input: prices = [7,1,5,3,6,4]\nOutput: 7\nExplanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.\nThen buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.\nTotal profit is 4 + 3 = 7.',
            'Input: prices = [1,2,3,4,5]\nOutput: 4\nExplanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.\nTotal profit is 4.'
        ],
        "approach": "Greedy: sum all positive differences",
        "time": "O(n)",
        "space": "O(1)",
        "insights": ["Capture every upward movement", "Add profit whenever price increases", "Multiple transactions allowed", "Sum all positive price differences"],
        "topics": ["Array", "Dynamic Programming", "Greedy"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Bloomberg"]
    },
    134: {
        "description": "There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].\n\nYou have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.\n\nGiven two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.",
        "constraints": ["n == gas.length == cost.length", "1 <= n <= 10^5", "0 <= gas[i], cost[i] <= 10^4"],
        "examples": [
            'Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]\nOutput: 3\nExplanation:\nStart at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4\nTravel to station 4. Your tank = 4 - 1 + 5 = 8\nTravel to station 0. Your tank = 8 - 2 + 1 = 7\nTravel to station 1. Your tank = 7 - 3 + 2 = 6\nTravel to station 2. Your tank = 6 - 4 + 3 = 5\nTravel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.\nTherefore, return 3 as the starting index.',
            'Input: gas = [2,3,4], cost = [3,4,3]\nOutput: -1\nExplanation:\nYou can\'t start at station 0 or 1, as there is not enough gas to travel to the next station.\nLet\'s start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4\nTravel to station 0. Your tank = 4 - 3 + 2 = 3\nTravel to station 1. Your tank = 3 - 3 + 3 = 3\nYou cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.\nTherefore, you can\'t travel around the circuit once no matter where you start.'
        ],
        "approach": "Greedy with total and current tank",
        "time": "O(n)",
        "space": "O(1)",
        "insights": ["If total gas < total cost, impossible", "If tank becomes negative, start can't be before current", "Reset start position when tank negative", "One pass solution"],
        "topics": ["Array", "Greedy"],
        "companies": ["Amazon", "Microsoft", "Google"]
    },
    406: {
        "description": "You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order). Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people in front who have a height greater than or equal to hi.\n\nReconstruct and return the queue that is represented by the input array people. The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] is the attributes of the jth person in the queue (queue[0] is the person at the front of the queue).",
        "constraints": ["1 <= people.length <= 2000", "0 <= hi <= 10^6", "0 <= ki < people.length", "It is guaranteed that the queue can be reconstructed"],
        "examples": [
            'Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]\nOutput: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]\nExplanation:\nPerson 0 has height 5 with no other people taller or the same height in front.\nPerson 1 has height 7 with no other people taller or the same height in front.\nPerson 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.\nPerson 3 has height 6 with one person taller or the same height in front, which is person 1.\nPerson 4 has height 4 with four people taller or the same height in front, which are persons 0, 1, 2, and 3.\nPerson 5 has height 7 with one person taller or the same height in front, which is person 1.',
            'Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]\nOutput: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]'
        ],
        "approach": "Sort by height desc, insert by k",
        "time": "O(n^2)",
        "space": "O(n)",
        "insights": ["Sort by height descending, k ascending", "Insert each person at position k", "Taller people processed first don't affect shorter", "Greedy insertion works due to sorting"],
        "topics": ["Array", "Binary Indexed Tree", "Segment Tree", "Sorting"],
        "companies": ["Amazon", "Google", "Microsoft"]
    },
    621: {
        "description": "You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.\n\nReturn the minimum number of intervals required to complete all tasks.",
        "constraints": ["1 <= tasks.length <= 10^4", "tasks[i] is an uppercase English letter", "0 <= n <= 100"],
        "examples": [
            'Input: tasks = ["A","A","A","B","B","B"], n = 2\nOutput: 8\nExplanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.',
            'Input: tasks = ["A","C","A","B","D","B"], n = 1\nOutput: 6\nExplanation: A possible sequence is: A -> B -> C -> D -> A -> B.'
        ],
        "approach": "Greedy with frequency calculation",
        "time": "O(n)",
        "space": "O(1) - only 26 letters",
        "insights": ["Find max frequency and count of max freq tasks", "Formula: max((max_freq - 1) * (n + 1) + count, len(tasks))", "Schedule most frequent task first with gaps", "Fill gaps with other tasks"],
        "topics": ["Array", "Hash Table", "Greedy", "Sorting", "Heap (Priority Queue)", "Counting"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google"]
    },
    678: {
        "description": "Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.\n\nThe following rules define a valid string:\n\nAny left parenthesis '(' must have a corresponding right parenthesis ')'.\nAny right parenthesis ')' must have a corresponding left parenthesis '('.\nLeft parenthesis '(' must go before the corresponding right parenthesis ')'.\n'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string \"\".",
        "constraints": ["1 <= s.length <= 100", "s[i] is '(', ')' or '*'"],
        "examples": [
            'Input: s = "()"\nOutput: true',
            'Input: s = "(*)"\nOutput: true',
            'Input: s = "(*))"\nOutput: true'
        ],
        "approach": "Greedy with range tracking",
        "time": "O(n)",
        "space": "O(1)",
        "insights": ["Track range of possible open parentheses count", "low = minimum opens, high = maximum opens", "'*' can be (, ), or empty", "Valid if low <= 0 and high >= 0 at end"],
        "topics": ["String", "Dynamic Programming", "Stack", "Greedy"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google"]
    },
    763: {
        "description": "You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.\n\nNote that the partition is done so that after concatenating all the parts in order, the resultant string should be s.\n\nReturn a list of integers representing the size of these parts.",
        "constraints": ["1 <= s.length <= 500", "s consists of lowercase English letters"],
        "examples": [
            'Input: s = "ababcbacadefegdehijhklij"\nOutput: [9,7,8]\nExplanation:\nThe partition is "ababcbaca", "defegde", "hijhklij".\nThis is a partition so that each letter appears in at most one part.\nA partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.',
            'Input: s = "eccbbbbdec"\nOutput: [10]'
        ],
        "approach": "Greedy with last occurrence",
        "time": "O(n)",
        "space": "O(1) - only 26 letters",
        "insights": ["Record last occurrence of each character", "Expand partition end to include all occurrences", "Create new partition when reaching partition end", "One pass solution"],
        "topics": ["Hash Table", "Two Pointers", "String", "Greedy"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google"]
    },
    881: {
        "description": "You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.\n\nReturn the minimum number of boats to carry every given person.",
        "constraints": ["1 <= people.length <= 5 * 10^4", "1 <= people[i] <= limit <= 3 * 10^4"],
        "examples": [
            'Input: people = [1,2], limit = 3\nOutput: 1\nExplanation: 1 boat (1, 2)',
            'Input: people = [3,2,2,1], limit = 3\nOutput: 3\nExplanation: 3 boats (1, 2), (2) and (3)',
            'Input: people = [3,5,3,4], limit = 5\nOutput: 4\nExplanation: 4 boats (3), (3), (4), (5)'
        ],
        "approach": "Two pointers after sorting",
        "time": "O(n log n)",
        "space": "O(1)",
        "insights": ["Sort array", "Use two pointers from both ends", "Pair lightest with heaviest if possible", "Greedy pairing minimizes boats"],
        "topics": ["Array", "Two Pointers", "Greedy", "Sorting"],
        "companies": ["Amazon", "Microsoft", "Google"]
    },
    1647: {
        "description": "A string s is called good if there are no two different characters in s that have the same frequency.\n\nGiven a string s, return the minimum number of characters you need to delete to make s good.\n\nThe frequency of a character in a string is the number of times it appears in the string. For example, in the string \"aab\", the frequency of 'a' is 2, while the frequency of 'b' is 1.",
        "constraints": ["1 <= s.length <= 10^5", "s contains only lowercase English letters"],
        "examples": [
            'Input: s = "aab"\nOutput: 0\nExplanation: s is already good.',
            'Input: s = "aaabbbcc"\nOutput: 2\nExplanation: You can delete two \'b\'s resulting in the good string "aaabcc".\nAnother way it to delete one \'b\' and one \'c\' resulting in the good string "aaabbc".',
            'Input: s = "ceabaacb"\nOutput: 2\nExplanation: You can delete both \'c\'s resulting in the good string "eabaab".\nNote that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).'
        ],
        "approach": "Greedy with frequency set",
        "time": "O(n)",
        "space": "O(1) - only 26 letters",
        "insights": ["Count character frequencies", "Use set to track used frequencies", "Decrease frequency until unique or zero", "Greedy approach finds minimum deletions"],
        "topics": ["Hash Table", "String", "Greedy", "Sorting"],
        "companies": ["Amazon", "Google"]
    },

    # Graphs
    207: {
        "description": "There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.\n\nFor example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.\n\nReturn true if you can finish all courses. Otherwise, return false.",
        "constraints": ["1 <= numCourses <= 2000", "0 <= prerequisites.length <= 5000", "prerequisites[i].length == 2", "0 <= ai, bi < numCourses", "All the pairs prerequisites[i] are unique"],
        "examples": [
            'Input: numCourses = 2, prerequisites = [[1,0]]\nOutput: true\nExplanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.',
            'Input: numCourses = 2, prerequisites = [[1,0],[0,1]]\nOutput: false\nExplanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.'
        ],
        "approach": "Topological Sort (DFS or BFS/Kahn's algorithm)",
        "time": "O(V + E)",
        "space": "O(V + E)",
        "insights": ["Detect cycle in directed graph", "Use DFS with three states: unvisited, visiting, visited", "Or use BFS with indegree counting", "No cycle means valid topological ordering"],
        "topics": ["Depth-First Search", "Breadth-First Search", "Graph", "Topological Sort"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
    210: {
        "description": "There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.\n\nFor example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.\n\nReturn the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.",
        "constraints": ["1 <= numCourses <= 2000", "0 <= prerequisites.length <= numCourses * (numCourses - 1)", "prerequisites[i].length == 2", "0 <= ai, bi < numCourses", "ai != bi", "All the pairs [ai, bi] are distinct"],
        "examples": [
            'Input: numCourses = 2, prerequisites = [[1,0]]\nOutput: [0,1]\nExplanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].',
            'Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]\nOutput: [0,2,1,3]\nExplanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.\nSo one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].'
        ],
        "approach": "Topological Sort",
        "time": "O(V + E)",
        "space": "O(V + E)",
        "insights": ["Return topological order if valid", "Use Kahn's algorithm (BFS) or DFS post-order", "Track visited nodes to detect cycles", "Return empty array if cycle detected"],
        "topics": ["Depth-First Search", "Breadth-First Search", "Graph", "Topological Sort"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google"]
    },
    261: {
        "description": "You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.\n\nReturn true if the edges of the given graph make up a valid tree, and false otherwise.",
        "constraints": ["1 <= n <= 2000", "0 <= edges.length <= 5000", "edges[i].length == 2", "0 <= ai, bi < n", "ai != bi", "There are no self-loops or repeated edges"],
        "examples": [
            'Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]\nOutput: true',
            'Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]\nOutput: false'
        ],
        "approach": "Union Find or DFS",
        "time": "O(E)",
        "space": "O(n)",
        "insights": ["Valid tree has n-1 edges", "Must be connected and acyclic", "Use Union Find to detect cycles", "Or DFS to check connectivity and cycles"],
        "topics": ["Depth-First Search", "Breadth-First Search", "Union Find", "Graph"],
        "companies": ["Amazon", "Facebook", "Google"]
    },
    323: {
        "description": "You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.\n\nReturn the number of connected components in the graph.",
        "constraints": ["1 <= n <= 2000", "1 <= edges.length <= 5000", "edges[i].length == 2", "0 <= ai <= bi < n", "ai != bi", "There are no repeated edges"],
        "examples": [
            'Input: n = 5, edges = [[0,1],[1,2],[3,4]]\nOutput: 2',
            'Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]\nOutput: 1'
        ],
        "approach": "Union Find or DFS",
        "time": "O(E * α(n)) for Union Find",
        "space": "O(n)",
        "insights": ["Start with n components", "Union connected nodes", "Count remaining distinct roots", "Classic Union Find application"],
        "topics": ["Depth-First Search", "Breadth-First Search", "Union Find", "Graph"],
        "companies": ["Amazon", "Facebook", "Google", "LinkedIn"]
    },
    684: {
        "description": "In this problem, a tree is an undirected graph that is connected and has no cycles.\n\nYou are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.\n\nReturn an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.",
        "constraints": ["n == edges.length", "3 <= n <= 1000", "edges[i].length == 2", "1 <= ai < bi <= edges.length", "ai != bi", "There are no repeated edges", "The given graph is connected"],
        "examples": [
            'Input: edges = [[1,2],[1,3],[2,3]]\nOutput: [2,3]',
            'Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]\nOutput: [1,4]'
        ],
        "approach": "Union Find",
        "time": "O(n * α(n))",
        "space": "O(n)",
        "insights": ["Process edges one by one", "Use Union Find to track connectivity", "First edge that connects already-connected nodes is answer", "Return last such edge found"],
        "topics": ["Union Find", "Graph"],
        "companies": ["Amazon", "Google", "Bloomberg"]
    },
    743: {
        "description": "You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.\n\nWe will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.",
        "constraints": ["1 <= k <= n <= 100", "1 <= times.length <= 6000", "times[i].length == 3", "1 <= ui, vi <= n", "ui != vi", "0 <= wi <= 100", "All the pairs (ui, vi) are unique"],
        "examples": [
            'Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2\nOutput: 2',
            'Input: times = [[1,2,1]], n = 2, k = 1\nOutput: 1',
            'Input: times = [[1,2,1]], n = 2, k = 2\nOutput: -1'
        ],
        "approach": "Dijkstra's shortest path",
        "time": "O(E log V)",
        "space": "O(V + E)",
        "insights": ["Find shortest path to all nodes", "Use Dijkstra with min heap", "Answer is max of all shortest paths", "Return -1 if any node unreachable"],
        "topics": ["Depth-First Search", "Breadth-First Search", "Graph", "Heap (Priority Queue)", "Shortest Path"],
        "companies": ["Amazon", "Microsoft", "Google"]
    },
    785: {
        "description": "There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:\n\nThere are no self-edges (graph[u] does not contain u).\nThere are no parallel edges (graph[u] does not contain duplicate values).\nIf v is in graph[u], then u is in graph[v] (the graph is undirected).\nThe graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.\n\nA graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.\n\nReturn true if and only if it is bipartite.",
        "constraints": ["graph.length == n", "1 <= n <= 100", "0 <= graph[u].length < n", "0 <= graph[u][i] <= n - 1", "graph[u] does not contain u", "All the values of graph[u] are unique", "If graph[u] contains v, then graph[v] contains u"],
        "examples": [
            'Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]\nOutput: false\nExplanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.',
            'Input: graph = [[1,3],[0,2],[1,3],[0,2]]\nOutput: true\nExplanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.'
        ],
        "approach": "BFS/DFS with coloring",
        "time": "O(V + E)",
        "space": "O(V)",
        "insights": ["Try to color graph with 2 colors", "Adjacent nodes must have different colors", "Use BFS or DFS to assign colors", "If conflict found, not bipartite"],
        "topics": ["Depth-First Search", "Breadth-First Search", "Union Find", "Graph"],
        "companies": ["Amazon", "Facebook", "Google", "LinkedIn"]
    },
    797: {
        "description": "Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.\n\nThe graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).",
        "constraints": ["n == graph.length", "2 <= n <= 15", "0 <= graph[i][j] < n", "graph[i][j] != i (i.e., there will be no self-loops)", "All the elements of graph[i] are unique", "The input graph is guaranteed to be a DAG"],
        "examples": [
            'Input: graph = [[1,2],[3],[3],[]]\nOutput: [[0,1,3],[0,2,3]]\nExplanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.',
            'Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]\nOutput: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]'
        ],
        "approach": "DFS backtracking",
        "time": "O(2^V * V)",
        "space": "O(V)",
        "insights": ["Use DFS to explore all paths", "Backtrack to find all possibilities", "Add path when reaching target", "DAG guarantees termination"],
        "topics": ["Backtracking", "Depth-First Search", "Breadth-First Search", "Graph"],
        "companies": ["Amazon", "Google", "Facebook"]
    },
    1091: {
        "description": "Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.\n\nA clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:\n\nAll the visited cells of the path are 0.\nAll the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).\n\nThe length of a clear path is the number of visited cells of this path.",
        "constraints": ["n == grid.length", "n == grid[i].length", "1 <= n <= 100", "grid[i][j] is 0 or 1"],
        "examples": [
            'Input: grid = [[0,1],[1,0]]\nOutput: 2',
            'Input: grid = [[0,0,0],[1,1,0],[1,1,0]]\nOutput: 4',
            'Input: grid = [[1,0,0],[1,1,0],[1,1,0]]\nOutput: -1'
        ],
        "approach": "BFS for shortest path",
        "time": "O(n^2)",
        "space": "O(n^2)",
        "insights": ["BFS guarantees shortest path", "8 directions of movement", "Mark visited cells", "Return -1 if target unreachable"],
        "topics": ["Array", "Breadth-First Search", "Matrix"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google"]
    },
    1135: {
        "description": "There are n cities labeled from 1 to n. You are given the integer n and an array connections where connections[i] = [xi, yi, costi] indicates that the cost of connecting city xi and city yi (bidirectional connection) is costi.\n\nReturn the minimum cost to connect all the n cities such that there is at least one path between each pair of cities. If it is impossible to connect all the n cities, return -1.\n\nThe cost is the sum of the connections' costs used.",
        "constraints": ["1 <= n <= 10^4", "1 <= connections.length <= 10^4", "connections[i].length == 3", "1 <= xi, yi <= n", "xi != yi", "0 <= costi <= 10^5"],
        "examples": [
            'Input: n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]\nOutput: 6\nExplanation: Choosing any 2 edges will connect all cities so we choose the minimum 2.',
            'Input: n = 4, connections = [[1,2,3],[3,4,4]]\nOutput: -1\nExplanation: There is no way to connect all cities even if all edges are used.'
        ],
        "approach": "Minimum Spanning Tree (Kruskal's or Prim's)",
        "time": "O(E log E)",
        "space": "O(V)",
        "insights": ["Sort edges by cost", "Use Union Find to build MST", "Add edge if it connects new components", "Check if all nodes connected at end"],
        "topics": ["Union Find", "Graph", "Minimum Spanning Tree"],
        "companies": ["Amazon", "Google"]
    },

    # BFS/DFS
    130: {
        "description": "Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.\n\nA region is captured by flipping all 'O's into 'X's in that surrounded region.",
        "constraints": ["m == board.length", "n == board[i].length", "1 <= m, n <= 200", "board[i][j] is 'X' or 'O'"],
        "examples": [
            'Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]\nOutput: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]\nExplanation: Notice that an \'O\' should not be flipped if it is on the border, or adjacent to an \'O\' that should not be flipped.',
            'Input: board = [["X"]]\nOutput: [["X"]]'
        ],
        "approach": "DFS/BFS from borders",
        "time": "O(m * n)",
        "space": "O(m * n) for recursion stack",
        "insights": ["Mark border-connected O's", "DFS/BFS from all border O's", "Flip unmarked O's to X", "Restore marked O's"],
        "topics": ["Array", "Depth-First Search", "Breadth-First Search", "Union Find", "Matrix"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google"]
    },
    133: {
        "description": "Given a reference of a node in a connected undirected graph.\n\nReturn a deep copy (clone) of the graph.\n\nEach node in the graph contains a value (int) and a list (List[Node]) of its neighbors.",
        "constraints": ["The number of nodes in the graph is in the range [0, 100]", "1 <= Node.val <= 100", "Node.val is unique for each node", "There are no repeated edges and no self-loops in the graph", "The Graph is connected and all nodes can be visited starting from the given node"],
        "examples": [
            'Input: adjList = [[2,4],[1,3],[2,4],[1,3]]\nOutput: [[2,4],[1,3],[2,4],[1,3]]\nExplanation: There are 4 nodes in the graph.',
            'Input: adjList = [[]]\nOutput: [[]]\nExplanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.'
        ],
        "approach": "DFS or BFS with hash map",
        "time": "O(V + E)",
        "space": "O(V)",
        "insights": ["Use hash map to track cloned nodes", "DFS/BFS to traverse graph", "Clone node and neighbors recursively", "Hash map prevents infinite loops"],
        "topics": ["Hash Table", "Depth-First Search", "Breadth-First Search", "Graph"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
    200: {
        "description": "Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.\n\nAn island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.",
        "constraints": ["m == grid.length", "n == grid[i].length", "1 <= m, n <= 300", "grid[i][j] is '0' or '1'"],
        "examples": [
            'Input: grid = [\n  ["1","1","1","1","0"],\n  ["1","1","0","1","0"],\n  ["1","1","0","0","0"],\n  ["0","0","0","0","0"]\n]\nOutput: 1',
            'Input: grid = [\n  ["1","1","0","0","0"],\n  ["1","1","0","0","0"],\n  ["0","0","1","0","0"],\n  ["0","0","0","1","1"]\n]\nOutput: 3'
        ],
        "approach": "DFS or BFS",
        "time": "O(m * n)",
        "space": "O(m * n) for recursion/queue",
        "insights": ["DFS/BFS from each unvisited land cell", "Mark visited cells", "Count number of DFS/BFS calls", "Classic connected components problem"],
        "topics": ["Array", "Depth-First Search", "Breadth-First Search", "Union Find", "Matrix"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
    286: {
        "description": "You are given an m x n grid rooms initialized with these three possible values.\n\n-1: A wall or an obstacle.\n0: A gate.\nINF: Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.\n\nFill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.",
        "constraints": ["m == rooms.length", "n == rooms[i].length", "1 <= m, n <= 250", "rooms[i][j] is -1, 0, or 2^31 - 1"],
        "examples": [
            'Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]\nOutput: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]',
            'Input: rooms = [[-1]]\nOutput: [[-1]]'
        ],
        "approach": "Multi-source BFS",
        "time": "O(m * n)",
        "space": "O(m * n)",
        "insights": ["Start BFS from all gates simultaneously", "Update distances level by level", "Each cell visited once", "Multi-source BFS is efficient"],
        "topics": ["Array", "Breadth-First Search", "Matrix"],
        "companies": ["Amazon", "Facebook", "Google"]
    },
    417: {
        "description": "There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.\n\nThe island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).\n\nThe island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.\n\nReturn a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.",
        "constraints": ["m == heights.length", "n == heights[r].length", "1 <= m, n <= 200", "0 <= heights[r][c] <= 10^5"],
        "examples": [
            'Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]\nOutput: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]\nExplanation: The following cells can flow to the Pacific and Atlantic oceans:\n[[0,4]: [0,4] -> Pacific Ocean\n[1,3]: [1,3] -> [0,3] -> Pacific Ocean\n...',
            'Input: heights = [[1]]\nOutput: [[0,0]]\nExplanation: The water can flow from the only cell to both oceans.'
        ],
        "approach": "DFS from ocean borders",
        "time": "O(m * n)",
        "space": "O(m * n)",
        "insights": ["DFS from Pacific and Atlantic borders", "Mark cells reachable from each ocean", "Find intersection of both sets", "Reverse thinking: ocean to cells"],
        "topics": ["Array", "Depth-First Search", "Breadth-First Search", "Matrix"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google"]
    },
    542: {
        "description": "Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.\n\nThe distance between two adjacent cells is 1.",
        "constraints": ["m == mat.length", "n == mat[i].length", "1 <= m, n <= 10^4", "1 <= m * n <= 10^4", "mat[i][j] is either 0 or 1", "There is at least one 0 in mat"],
        "examples": [
            'Input: mat = [[0,0,0],[0,1,0],[0,0,0]]\nOutput: [[0,0,0],[0,1,0],[0,0,0]]',
            'Input: mat = [[0,0,0],[0,1,0],[1,1,1]]\nOutput: [[0,0,0],[0,1,0],[1,2,1]]'
        ],
        "approach": "Multi-source BFS",
        "time": "O(m * n)",
        "space": "O(m * n)",
        "insights": ["Start BFS from all 0s simultaneously", "Update distances level by level", "Similar to walls and gates", "BFS guarantees shortest distance"],
        "topics": ["Array", "Dynamic Programming", "Breadth-First Search", "Matrix"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google"]
    },
    994: {
        "description": "You are given an m x n grid where each cell can have one of three values:\n\n0 representing an empty cell,\n1 representing a fresh orange, or\n2 representing a rotten orange.\n\nEvery minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.\n\nReturn the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.",
        "constraints": ["m == grid.length", "n == grid[i].length", "1 <= m, n <= 10", "grid[i][j] is 0, 1, or 2"],
        "examples": [
            'Input: grid = [[2,1,1],[1,1,0],[0,1,1]]\nOutput: 4',
            'Input: grid = [[2,1,1],[0,1,1],[1,0,1]]\nOutput: -1\nExplanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.'
        ],
        "approach": "Multi-source BFS",
        "time": "O(m * n)",
        "space": "O(m * n)",
        "insights": ["Start BFS from all rotten oranges", "Track time/levels of BFS", "Count fresh oranges remaining", "Return -1 if fresh oranges remain"],
        "topics": ["Array", "Breadth-First Search", "Matrix"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Bloomberg"]
    },
    1162: {
        "description": "Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.\n\nThe distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.",
        "constraints": ["n == grid.length", "n == grid[i].length", "1 <= n <= 100", "grid[i][j] is 0 or 1"],
        "examples": [
            'Input: grid = [[1,0,1],[0,0,0],[1,0,1]]\nOutput: 2\nExplanation: The cell (1, 1) is as far as possible from all the land with distance 2.',
            'Input: grid = [[1,0,0],[0,0,0],[0,0,0]]\nOutput: 4\nExplanation: The cell (2, 2) is as far as possible from all the land with distance 4.'
        ],
        "approach": "Multi-source BFS",
        "time": "O(n^2)",
        "space": "O(n^2)",
        "insights": ["Start BFS from all land cells", "Find maximum distance to any water", "BFS calculates distances correctly", "Return -1 if all land or all water"],
        "topics": ["Array", "Dynamic Programming", "Breadth-First Search", "Matrix"],
        "companies": ["Amazon", "Google"]
    },
    1197: {
        "description": "In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].\n\nA knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.\n\nReturn the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.",
        "constraints": ["| x| + |y| <= 300"],
        "examples": [
            'Input: x = 2, y = 1\nOutput: 1\nExplanation: [0, 0] -> [2, 1]',
            'Input: x = 5, y = 5\nOutput: 4\nExplanation: [0, 0] -> [2, 1] -> [4, 2] -> [3, 4] -> [5, 5]'
        ],
        "approach": "BFS for shortest path",
        "time": "O(max(|x|, |y|)^2)",
        "space": "O(max(|x|, |y|)^2)",
        "insights": ["Use BFS to find shortest path", "8 possible knight moves", "Track visited positions", "Can optimize with symmetry"],
        "topics": ["Breadth-First Search"],
        "companies": ["Amazon", "Google"]
    },

    # Stacks/Queues
    20: {
        "description": "Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.\n\nAn input string is valid if:\n\nOpen brackets must be closed by the same type of brackets.\nOpen brackets must be closed in the correct order.\nEvery close bracket has a corresponding open bracket of the same type.",
        "constraints": ["1 <= s.length <= 10^4", "s consists of parentheses only '()[]{}'"],
        "examples": [
            'Input: s = "()"\nOutput: true',
            'Input: s = "()[]{}"\nOutput: true',
            'Input: s = "(]"\nOutput: false'
        ],
        "approach": "Stack",
        "time": "O(n)",
        "space": "O(n)",
        "insights": ["Push opening brackets to stack", "Pop and match with closing brackets", "Stack must be empty at end", "Classic stack application"],
        "topics": ["String", "Stack"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
    71: {
        "description": "Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.\n\nIn a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.\n\nThe canonical path should have the following format:\n\nThe path starts with a single slash '/'.\nAny two directories are separated by a single slash '/'.\nThe path does not end with a trailing '/'.\nThe path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')\n\nReturn the simplified canonical path.",
        "constraints": ["1 <= path.length <= 3000", "path consists of English letters, digits, period '.', slash '/' or '_'", "path is a valid absolute Unix path"],
        "examples": [
            'Input: path = "/home/"\nOutput: "/home"\nExplanation: Note that there is no trailing slash after the last directory name.',
            'Input: path = "/../"\nOutput: "/"\nExplanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.',
            'Input: path = "/home//foo/"\nOutput: "/home/foo"\nExplanation: In the canonical path, multiple consecutive slashes are replaced by a single one.'
        ],
        "approach": "Stack",
        "time": "O(n)",
        "space": "O(n)",
        "insights": ["Split path by '/'", "Use stack to track directories", "'..' pops from stack", "Ignore '.' and empty strings"],
        "topics": ["String", "Stack"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google"]
    },
    84: {
        "description": "Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.",
        "constraints": ["1 <= heights.length <= 10^5", "0 <= heights[i] <= 10^4"],
        "examples": [
            'Input: heights = [2,1,5,6,2,3]\nOutput: 10\nExplanation: The above is a histogram where width of each bar is 1.\nThe largest rectangle is shown in the red area, which has an area = 10 units.',
            'Input: heights = [2,4]\nOutput: 4'
        ],
        "approach": "Monotonic stack",
        "time": "O(n)",
        "space": "O(n)",
        "insights": ["Use stack to track indices", "Maintain increasing heights in stack", "Calculate area when popping", "Classic monotonic stack problem"],
        "topics": ["Array", "Stack", "Monotonic Stack"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Bloomberg"]
    },
    150: {
        "description": "You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.\n\nEvaluate the expression. Return an integer that represents the value of the expression.\n\nNote that:\n\nThe valid operators are '+', '-', '*', and '/'.\nEach operand may be an integer or another expression.\nThe division between two integers always truncates toward zero.\nThere will not be any division by zero.\nThe input represents a valid arithmetic expression in a reverse polish notation.\nThe answer and all the intermediate calculations can be represented in a 32-bit integer.",
        "constraints": ["1 <= tokens.length <= 10^4", "tokens[i] is either an operator: '+', '-', '*', or '/', or an integer in the range [-200, 200]"],
        "examples": [
            'Input: tokens = ["2","1","+","3","*"]\nOutput: 9\nExplanation: ((2 + 1) * 3) = 9',
            'Input: tokens = ["4","13","5","/","+"]\nOutput: 6\nExplanation: (4 + (13 / 5)) = 6'
        ],
        "approach": "Stack",
        "time": "O(n)",
        "space": "O(n)",
        "insights": ["Push numbers to stack", "Pop two operands for operators", "Push result back to stack", "Final stack element is answer"],
        "topics": ["Array", "Math", "Stack"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google"]
    },
    155: {
        "description": "Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.\n\nImplement the MinStack class:\n\nMinStack() initializes the stack object.\nvoid push(int val) pushes the element val onto the stack.\nvoid pop() removes the element on the top of the stack.\nint top() gets the top element of the stack.\nint getMin() retrieves the minimum element in the stack.\n\nYou must implement a solution with O(1) time complexity for each function.",
        "constraints": ["-2^31 <= val <= 2^31 - 1", "Methods pop, top and getMin operations will always be called on non-empty stacks", "At most 3 * 10^4 calls will be made to push, pop, top, and getMin"],
        "examples": [
            'Input\n["MinStack","push","push","push","getMin","pop","top","getMin"]\n[[],[-2],[0],[-3],[],[],[],[]]\n\nOutput\n[null,null,null,null,-3,null,0,-2]\n\nExplanation\nMinStack minStack = new MinStack();\nminStack.push(-2);\nminStack.push(0);\nminStack.push(-3);\nminStack.getMin(); // return -3\nminStack.pop();\nminStack.top();    // return 0\nminStack.getMin(); // return -2'
        ],
        "approach": "Two stacks or stack with pairs",
        "time": "O(1) for all operations",
        "space": "O(n)",
        "insights": ["Store (value, current_min) pairs", "Or use two stacks: main and min", "Update min on push", "Pop from both stacks together"],
        "topics": ["Stack", "Design"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
    225: {
        "description": "Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).",
        "constraints": ["1 <= x <= 9", "At most 100 calls will be made to push, pop, top, and empty", "All the calls to pop and top are valid"],
        "examples": [
            'Input\n["MyStack", "push", "push", "top", "pop", "empty"]\n[[], [1], [2], [], [], []]\nOutput\n[null, null, null, 2, 2, false]\n\nExplanation\nMyStack myStack = new MyStack();\nmyStack.push(1);\nmyStack.push(2);\nmyStack.top(); // return 2\nmyStack.pop(); // return 2\nmyStack.empty(); // return False'
        ],
        "approach": "Single queue or two queues",
        "time": "O(n) for push, O(1) for others",
        "space": "O(n)",
        "insights": ["Use one queue, rotate on push", "Or use two queues, transfer on pop", "Make push expensive or pop expensive", "Queue as underlying structure"],
        "topics": ["Stack", "Design", "Queue"],
        "companies": ["Amazon", "Microsoft", "Bloomberg"]
    },
    232: {
        "description": "Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).",
        "constraints": ["1 <= x <= 9", "At most 100 calls will be made to push, pop, peek, and empty", "All the calls to pop and peek are valid"],
        "examples": [
            'Input\n["MyQueue", "push", "push", "peek", "pop", "empty"]\n[[], [1], [2], [], [], []]\nOutput\n[null, null, null, 1, 1, false]\n\nExplanation\nMyQueue myQueue = new MyQueue();\nmyQueue.push(1); // queue is: [1]\nmyQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)\nmyQueue.peek(); // return 1\nmyQueue.pop(); // return 1, queue is [2]\nmyQueue.empty(); // return false'
        ],
        "approach": "Two stacks: input and output",
        "time": "O(1) amortized for all operations",
        "space": "O(n)",
        "insights": ["Use input stack for push", "Use output stack for pop/peek", "Transfer when output empty", "Amortized O(1) time"],
        "topics": ["Stack", "Design", "Queue"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Bloomberg"]
    },
    496: {
        "description": "The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.\n\nYou are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.\n\nFor each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.\n\nReturn an array ans of length nums1.length such that ans[i] is the next greater element as described above.",
        "constraints": ["1 <= nums1.length <= nums2.length <= 1000", "0 <= nums1[i], nums2[i] <= 10^4", "All integers in nums1 and nums2 are unique", "All the integers of nums1 also appear in nums2"],
        "examples": [
            'Input: nums1 = [4,1,2], nums2 = [1,3,4,2]\nOutput: [-1,3,-1]\nExplanation: The next greater element for each value of nums1 is as follows:\n- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.\n- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.\n- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.',
            'Input: nums1 = [2,4], nums2 = [1,2,3,4]\nOutput: [3,-1]\nExplanation: The next greater element for each value of nums1 is as follows:\n- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.\n- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.'
        ],
        "approach": "Monotonic stack + hash map",
        "time": "O(n + m)",
        "space": "O(n)",
        "insights": ["Use monotonic decreasing stack", "Build next greater map for nums2", "Lookup in map for nums1 elements", "Stack maintains potential next greater elements"],
        "topics": ["Array", "Hash Table", "Stack", "Monotonic Stack"],
        "companies": ["Amazon", "Google"]
    },
    503: {
        "description": "Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.\n\nThe next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.",
        "constraints": ["1 <= nums.length <= 10^4", "-10^9 <= nums[i] <= 10^9"],
        "examples": [
            'Input: nums = [1,2,1]\nOutput: [2,-1,2]\nExplanation: The first 1\'s next greater number is 2; \nThe number 2 can\'t find next greater number. \nThe second 1\'s next greater number needs to search circularly, which is also 2.',
            'Input: nums = [1,2,3,4,3]\nOutput: [2,3,4,-1,4]'
        ],
        "approach": "Monotonic stack with circular traversal",
        "time": "O(n)",
        "space": "O(n)",
        "insights": ["Process array twice for circular effect", "Use monotonic decreasing stack", "Store indices in stack", "Update result when finding greater element"],
        "topics": ["Array", "Stack", "Monotonic Stack"],
        "companies": ["Amazon", "Microsoft", "Google"]
    },
    739: {
        "description": "Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.",
        "constraints": ["1 <= temperatures.length <= 10^5", "30 <= temperatures[i] <= 100"],
        "examples": [
            'Input: temperatures = [73,74,75,71,69,72,76,73]\nOutput: [1,1,4,2,1,1,0,0]',
            'Input: temperatures = [30,40,50,60]\nOutput: [1,1,1,0]',
            'Input: temperatures = [30,60,90]\nOutput: [1,1,0]'
        ],
        "approach": "Monotonic stack",
        "time": "O(n)",
        "space": "O(n)",
        "insights": ["Use monotonic decreasing stack", "Store indices in stack", "Calculate days difference when finding warmer", "Classic next greater element variant"],
        "topics": ["Array", "Stack", "Monotonic Stack"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Bloomberg"]
    },

    # Tries
    208: {
        "description": "A trie (pronounced as \"try\") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.\n\nImplement the Trie class:\n\nTrie() Initializes the trie object.\nvoid insert(String word) Inserts the string word into the trie.\nboolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.\nboolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.",
        "constraints": ["1 <= word.length, prefix.length <= 2000", "word and prefix consist only of lowercase English letters", "At most 3 * 10^4 calls in total will be made to insert, search, and startsWith"],
        "examples": [
            'Input\n["Trie", "insert", "search", "search", "startsWith", "insert", "search"]\n[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]\nOutput\n[null, null, true, false, true, null, true]\n\nExplanation\nTrie trie = new Trie();\ntrie.insert("apple");\ntrie.search("apple");   // return True\ntrie.search("app");     // return False\ntrie.startsWith("app"); // return True\ntrie.insert("app");\ntrie.search("app");     // return True'
        ],
        "approach": "Trie with TrieNode structure",
        "time": "O(m) for all operations where m is word length",
        "space": "O(n * m) where n is number of words",
        "insights": ["Each node has 26 children (a-z)", "Mark end of word with flag", "Traverse character by character", "Efficient for prefix queries"],
        "topics": ["Hash Table", "String", "Design", "Trie"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
    211: {
        "description": "Design a data structure that supports adding new words and finding if a string matches any previously added string.\n\nImplement the WordDictionary class:\n\nWordDictionary() Initializes the object.\nvoid addWord(word) Adds word to the data structure, it can be matched later.\nbool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.",
        "constraints": ["1 <= word.length <= 25", "word in addWord consists of lowercase English letters", "word in search consist of '.' or lowercase English letters", "There will be at most 2 dots in word for search queries", "At most 10^4 calls will be made to addWord and search"],
        "examples": [
            'Input\n["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]\nOutput\n[null,null,null,null,false,true,true,true]\n\nExplanation\nWordDictionary wordDictionary = new WordDictionary();\nwordDictionary.addWord("bad");\nwordDictionary.addWord("dad");\nwordDictionary.addWord("mad");\nwordDictionary.search("pad"); // return False\nwordDictionary.search("bad"); // return True\nwordDictionary.search(".ad"); // return True\nwordDictionary.search("b.."); // return True'
        ],
        "approach": "Trie with DFS for wildcard matching",
        "time": "O(m) for addWord, O(26^m) worst case for search",
        "space": "O(n * m)",
        "insights": ["Use Trie for storage", "DFS with backtracking for '.' wildcard", "Try all children when encountering '.'", "Regular Trie with recursive search"],
        "topics": ["String", "Depth-First Search", "Design", "Trie"],
        "companies": ["Amazon", "Facebook", "Google", "Microsoft"]
    },
    648: {
        "description": "In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root \"help\" is followed by the word \"ful\", we can form a derivative \"helpful\".\n\nGiven a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.\n\nReturn the sentence after the replacement.",
        "constraints": ["1 <= dictionary.length <= 1000", "1 <= dictionary[i].length <= 100", "dictionary[i] consists of only lower-case letters", "1 <= sentence.length <= 10^6", "sentence consists of only lower-case letters and spaces", "The number of words in sentence is in the range [1, 1000]", "The length of each word in sentence is in the range [1, 1000]", "Every two consecutive words in sentence will be separated by exactly one space", "sentence does not have leading or trailing spaces"],
        "examples": [
            'Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"\nOutput: "the cat was rat by the bat"',
            'Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"\nOutput: "a a b c"'
        ],
        "approach": "Trie",
        "time": "O(n + m) where n is dictionary size, m is sentence length",
        "space": "O(n)",
        "insights": ["Build Trie from dictionary roots", "For each word, find shortest root prefix", "Replace word with root if found", "Trie enables efficient prefix matching"],
        "topics": ["Array", "Hash Table", "String", "Trie"],
        "companies": ["Amazon", "Google", "Microsoft"]
    },
    677: {
        "description": "Design a map that allows you to do the following:\n\nMaps a string key to a given value.\nReturns the sum of the values that have a key with a prefix equal to a given string.\n\nImplement the MapSum class:\n\nMapSum() Initializes the MapSum object.\nvoid insert(String key, int val) Inserts the key-val pair into the map. If the key already existed, the original key-value pair will be overridden to the new one.\nint sum(String prefix) Returns the sum of all the pairs' value whose key starts with the prefix.",
        "constraints": ["1 <= key.length, prefix.length <= 50", "key and prefix consist of only lowercase English letters", "1 <= val <= 1000", "At most 50 calls will be made to insert and sum"],
        "examples": [
            'Input\n["MapSum", "insert", "sum", "insert", "sum"]\n[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]\nOutput\n[null, null, 3, null, 5]\n\nExplanation\nMapSum mapSum = new MapSum();\nmapSum.insert("apple", 3);  \nmapSum.sum("ap");           // return 3 (apple = 3)\nmapSum.insert("app", 2);    \nmapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)'
        ],
        "approach": "Trie with value storage",
        "time": "O(m) for both operations where m is key/prefix length",
        "space": "O(n * m)",
        "insights": ["Store values in Trie nodes", "Track previous values for updates", "DFS to sum all values with prefix", "HashMap to handle key updates"],
        "topics": ["Hash Table", "String", "Design", "Trie"],
        "companies": ["Amazon", "Google"]
    },
    720: {
        "description": "Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.\n\nIf there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.\n\nNote that the word should be built from left to right with each additional character being added to the end of a previous word.",
        "constraints": ["1 <= words.length <= 1000", "1 <= words[i].length <= 30", "words[i] consists of lowercase English letters"],
        "examples": [
            'Input: words = ["w","wo","wor","worl","world"]\nOutput: "world"\nExplanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".',
            'Input: words = ["a","banana","app","appl","ap","apply","apple"]\nOutput: "apple"\nExplanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".'
        ],
        "approach": "Trie or Set",
        "time": "O(n * m) where n is words count, m is average length",
        "space": "O(n * m)",
        "insights": ["Sort words by length and lexicographically", "Check if all prefixes exist", "Use set for O(1) lookup", "Or build Trie and DFS"],
        "topics": ["Array", "Hash Table", "String", "Trie", "Sorting"],
        "companies": ["Amazon", "Google"]
    },
    745: {
        "description": "Design a special dictionary that searches the words in it by a prefix and a suffix.\n\nImplement the WordFilter class:\n\nWordFilter(string[] words) Initializes the object with the words in the dictionary.\nf(string pref, string suff) Returns the index of the word in the dictionary, which has the prefix pref and the suffix suff. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.",
        "constraints": ["1 <= words.length <= 10^4", "1 <= words[i].length <= 7", "1 <= pref.length, suff.length <= 7", "words[i], pref and suff consist of lowercase English letters only", "At most 10^4 calls will be made to the function f"],
        "examples": [
            'Input\n["WordFilter", "f"]\n[[["apple"]], ["a", "e"]]\nOutput\n[null, 0]\nExplanation\nWordFilter wordFilter = new WordFilter(["apple"]);\nwordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = "e".'
        ],
        "approach": "Trie with combined keys or two Tries",
        "time": "O(n * m^2) for constructor, O(p + s) for query",
        "space": "O(n * m^2)",
        "insights": ["Store suffix#prefix combinations in Trie", "For word 'apple', store 'e#apple', 'le#apple', etc.", "Or use two Tries and intersect results", "Trade space for query speed"],
        "topics": ["Array", "Hash Table", "String", "Design", "Trie"],
        "companies": ["Amazon", "Google"]
    },
    820: {
        "description": "A valid encoding of an array of words is any reference string s and array of indices indices such that:\n\nwords.length == indices.length\nThe reference string s ends with the '#' character.\nFor each index indices[i], the substring of s starting from indices[i] and up to (but not including) the next '#' character is equal to words[i].\n\nGiven an array of words, return the length of the shortest reference string s possible of any valid encoding of words.",
        "constraints": ["1 <= words.length <= 2000", "1 <= words[i].length <= 7", "words[i] consists of only lowercase letters"],
        "examples": [
            'Input: words = ["time", "me", "bell"]\nOutput: 10\nExplanation: A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].\nwords[0] = "time", the substring of s starting from indices[0] = 0 to the next \'#\' is underlined in "time#bell#"\nwords[1] = "me", the substring of s starting from indices[1] = 2 to the next \'#\' is underlined in "time#bell#"\nwords[2] = "bell", the substring of s starting from indices[2] = 5 to the next \'#\' is underlined in "time#bell#"',
            'Input: words = ["t"]\nOutput: 2\nExplanation: A valid encoding would be s = "t#" and indices = [0].'
        ],
        "approach": "Reverse Trie or suffix checking",
        "time": "O(n * m)",
        "space": "O(n * m)",
        "insights": ["Build Trie in reverse (suffix tree)", "Words that are suffixes share encoding", "Only count leaf nodes", "Remove words that are suffixes of others"],
        "topics": ["Array", "Hash Table", "String", "Trie"],
        "companies": ["Amazon", "Google"]
    },
    1268: {
        "description": "You are given an array of strings products and a string searchWord.\n\nDesign a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.\n\nReturn a list of lists of the suggested products after each character of searchWord is typed.",
        "constraints": ["1 <= products.length <= 1000", "1 <= products[i].length <= 3000", "1 <= sum(products[i].length) <= 2 * 10^4", "All the strings of products are unique", "products[i] consists of lowercase English letters", "1 <= searchWord.length <= 1000", "searchWord consists of lowercase English letters"],
        "examples": [
            'Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"\nOutput: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]',
            'Input: products = ["havana"], searchWord = "havana"\nOutput: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]'
        ],
        "approach": "Trie or sorting with binary search",
        "time": "O(n * m + k) for Trie where k is searchWord length",
        "space": "O(n * m)",
        "insights": ["Sort products and use binary search", "Or build Trie with sorted suggestions at each node", "Return top 3 lexicographically smallest", "Sorting approach is simpler"],
        "topics": ["Array", "String", "Binary Search", "Trie", "Sorting", "Heap (Priority Queue)"],
        "companies": ["Amazon", "Microsoft"]
    },
    1804: {
        "description": "A trie (pronounced as \"try\") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.\n\nImplement the Trie class:\n\nTrie() Initializes the trie object.\nvoid insert(String word) Inserts the string word into the trie.\nint countWordsEqualTo(String word) Returns the number of instances of the string word in the trie.\nint countWordsStartingWith(String prefix) Returns the number of strings in the trie that have the string prefix as a prefix.\nvoid erase(String word) Erases the string word from the trie.",
        "constraints": ["1 <= word.length, prefix.length <= 2000", "word and prefix consist only of lowercase English letters", "At most 3 * 10^4 calls in total will be made to insert, countWordsEqualTo, countWordsStartingWith, and erase", "It is guaranteed that for any function call to erase, the string word will exist in the trie"],
        "examples": [
            'Input\n["Trie", "insert", "insert", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsStartingWith"]\n[[], ["apple"], ["apple"], ["apple"], ["app"], ["apple"], ["apple"], ["app"], ["apple"], ["app"]]\nOutput\n[null, null, null, 2, 2, null, 1, 1, null, 0]'
        ],
        "approach": "Trie with counters",
        "time": "O(m) for all operations where m is word length",
        "space": "O(n * m)",
        "insights": ["Track word count and prefix count at each node", "Increment counters on insert", "Decrement counters on erase", "Return appropriate counter for queries"],
        "topics": ["Hash Table", "String", "Design", "Trie"],
        "companies": ["Amazon", "Google"]
    },

    # Binary Search (additional problems)
    33: {
        "description": "There is an integer array nums sorted in ascending order (with distinct values).\n\nPrior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].\n\nGiven the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.\n\nYou must write an algorithm with O(log n) runtime complexity.",
        "constraints": ["1 <= nums.length <= 5000", "-10^4 <= nums[i] <= 10^4", "All values of nums are unique", "nums is an ascending array that is possibly rotated", "-10^4 <= target <= 10^4"],
        "examples": [
            'Input: nums = [4,5,6,7,0,1,2], target = 0\nOutput: 4',
            'Input: nums = [4,5,6,7,0,1,2], target = 3\nOutput: -1',
            'Input: nums = [1], target = 0\nOutput: -1'
        ],
        "approach": "Modified binary search",
        "time": "O(log n)",
        "space": "O(1)",
        "insights": ["One half is always sorted", "Check which half is sorted", "Determine if target is in sorted half", "Adjust search range accordingly"],
        "topics": ["Array", "Binary Search"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
    34: {
        "description": "Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.\n\nIf target is not found in the array, return [-1, -1].\n\nYou must write an algorithm with O(log n) runtime complexity.",
        "constraints": ["0 <= nums.length <= 10^5", "-10^9 <= nums[i] <= 10^9", "nums is a non-decreasing array", "-10^9 <= target <= 10^9"],
        "examples": [
            'Input: nums = [5,7,7,8,8,10], target = 8\nOutput: [3,4]',
            'Input: nums = [5,7,7,8,8,10], target = 6\nOutput: [-1,-1]',
            'Input: nums = [], target = 0\nOutput: [-1,-1]'
        ],
        "approach": "Binary search twice (first and last position)",
        "time": "O(log n)",
        "space": "O(1)",
        "insights": ["Find leftmost position with binary search", "Find rightmost position with binary search", "Modify binary search to find boundaries", "Two separate binary searches"],
        "topics": ["Array", "Binary Search"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Bloomberg"]
    },
    153: {
        "description": "Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:\n\n[4,5,6,7,0,1,2] if it was rotated 4 times.\n[0,1,2,4,5,6,7] if it was rotated 7 times.\n\nNotice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].\n\nGiven the sorted rotated array nums of unique elements, return the minimum element of this array.\n\nYou must write an algorithm that runs in O(log n) time.",
        "constraints": ["n == nums.length", "1 <= n <= 5000", "-5000 <= nums[i] <= 5000", "All the integers of nums are unique", "nums is sorted and rotated between 1 and n times"],
        "examples": [
            'Input: nums = [3,4,5,1,2]\nOutput: 1\nExplanation: The original array was [1,2,3,4,5] rotated 3 times.',
            'Input: nums = [4,5,6,7,0,1,2]\nOutput: 0\nExplanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.',
            'Input: nums = [11,13,15,17]\nOutput: 11\nExplanation: The original array was [11,13,15,17] and it was rotated 4 times.'
        ],
        "approach": "Binary search",
        "time": "O(log n)",
        "space": "O(1)",
        "insights": ["Compare mid with right", "If mid > right, minimum is in right half", "If mid < right, minimum is in left half or mid", "Minimum is at rotation point"],
        "topics": ["Array", "Binary Search"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Bloomberg"]
    },
    704: {
        "description": "Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.\n\nYou must write an algorithm with O(log n) runtime complexity.",
        "constraints": ["1 <= nums.length <= 10^4", "-10^4 < nums[i], target < 10^4", "All the integers in nums are unique", "nums is sorted in ascending order"],
        "examples": [
            'Input: nums = [-1,0,3,5,9,12], target = 9\nOutput: 4\nExplanation: 9 exists in nums and its index is 4',
            'Input: nums = [-1,0,3,5,9,12], target = 2\nOutput: -1\nExplanation: 2 does not exist in nums so return -1'
        ],
        "approach": "Standard binary search",
        "time": "O(log n)",
        "space": "O(1)",
        "insights": ["Classic binary search implementation", "Compare mid with target", "Adjust left or right pointer", "Template for all binary search problems"],
        "topics": ["Array", "Binary Search"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },

    # Backtracking (additional problems)
    39: {
        "description": "Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.\n\nThe same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.\n\nThe test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.",
        "constraints": ["1 <= candidates.length <= 30", "2 <= candidates[i] <= 40", "All elements of candidates are distinct", "1 <= target <= 40"],
        "examples": [
            'Input: candidates = [2,3,6,7], target = 7\nOutput: [[2,2,3],[7]]\nExplanation:\n2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.\n7 is a candidate, and 7 = 7.\nThese are the only two combinations.',
            'Input: candidates = [2,3,5], target = 8\nOutput: [[2,2,2,2],[2,3,3],[3,5]]'
        ],
        "approach": "Backtracking with repetition allowed",
        "time": "O(n^(T/M)) where T is target, M is minimum candidate",
        "space": "O(T/M) for recursion depth",
        "insights": ["Can reuse same element", "Use index to avoid duplicates in different order", "Backtrack when sum exceeds target", "Include element and recurse with same index"],
        "topics": ["Array", "Backtracking"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
    46: {
        "description": "Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.",
        "constraints": ["1 <= nums.length <= 6", "-10 <= nums[i] <= 10", "All the integers of nums are unique"],
        "examples": [
            'Input: nums = [1,2,3]\nOutput: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]',
            'Input: nums = [0,1]\nOutput: [[0,1],[1,0]]',
            'Input: nums = [1]\nOutput: [[1]]'
        ],
        "approach": "Backtracking with swapping or used array",
        "time": "O(n! * n)",
        "space": "O(n)",
        "insights": ["Use backtracking to generate permutations", "Track used elements or use swapping", "Add to result when permutation complete", "Classic backtracking problem"],
        "topics": ["Array", "Backtracking"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
    78: {
        "description": "Given an integer array nums of unique elements, return all possible subsets (the power set).\n\nThe solution set must not contain duplicate subsets. Return the solution in any order.",
        "constraints": ["1 <= nums.length <= 10", "-10 <= nums[i] <= 10", "All the numbers of nums are unique"],
        "examples": [
            'Input: nums = [1,2,3]\nOutput: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]',
            'Input: nums = [0]\nOutput: [[],[0]]'
        ],
        "approach": "Backtracking or iterative",
        "time": "O(2^n * n)",
        "space": "O(n) for recursion",
        "insights": ["Each element has two choices: include or exclude", "Backtrack with start index", "Add current subset at each step", "2^n total subsets"],
        "topics": ["Array", "Backtracking", "Bit Manipulation"],
        "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple"]
    },
}


def fill_problem_todo(file_path, problem_num):
    """Fill TODO markers in a solution file"""
    if problem_num not in PROBLEM_DATA:
        print(f"Skipping {problem_num} - no data available")
        return False

    data = PROBLEM_DATA[problem_num]

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace problem description
        content = re.sub(
            r'\[TODO: Add problem description\]',
            data['description'],
            content
        )

        # Replace constraints
        constraints_text = '\n'.join(f'- {c}' for c in data['constraints'])
        content = re.sub(
            r'\[TODO: Add constraints\]',
            constraints_text,
            content
        )

        # Replace examples
        examples_text = '\n\n'.join(data['examples'])
        content = re.sub(
            r'\[TODO: Add examples\]',
            examples_text,
            content
        )

        # Replace approach
        content = re.sub(
            r'Approach: \[TODO: Describe approach\]',
            f"Approach: {data['approach']}",
            content
        )

        # Replace time complexity
        content = re.sub(
            r'Time Complexity: O\(\?\)',
            f"Time Complexity: {data['time']}",
            content
        )

        # Replace space complexity
        content = re.sub(
            r'Space Complexity: O\(\?\)',
            f"Space Complexity: {data['space']}",
            content
        )

        # Replace key insights
        insights_text = '\n    '.join(f'- {i}' for i in data['insights'])
        content = re.sub(
            r'Key Insights:\n    \[TODO: Add key insights\]',
            f"Key Insights:\n    {insights_text}",
            content
        )

        # Replace topics in metadata
        topics_str = str(data['topics'])
        content = re.sub(
            r'"topics": \[\],  # TODO: Add topics',
            f'"topics": {topics_str},',
            content
        )

        # Replace companies in metadata
        companies_str = str(data['companies'])
        content = re.sub(
            r'"companies": \[\],  # TODO: Add companies',
            f'"companies": {companies_str},',
            content
        )

        # Replace time complexity in metadata
        content = re.sub(
            r'"time_complexity": "O\(\?\)"',
            f'"time_complexity": "{data["time"]}"',
            content
        )

        # Replace space complexity in metadata
        content = re.sub(
            r'"space_complexity": "O\(\?\)"',
            f'"space_complexity": "{data["space"]}"',
            content
        )

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"[OK] Filled {problem_num}: {file_path.name}")
        return True

    except Exception as e:
        print(f"[ERROR] Error processing {problem_num}: {e}")
        return False


def main():
    """Main function to process all files"""
    problems_dir = Path(__file__).parent.parent / 'problems'

    # Find all solution.py files
    solution_files = list(problems_dir.glob('**/solution.py'))

    filled = 0
    skipped = 0

    for file_path in solution_files:
        # Extract problem number from path
        match = re.search(r'p(\d+)_', str(file_path))
        if match:
            problem_num = int(match.group(1))
            if fill_problem_todo(file_path, problem_num):
                filled += 1
            else:
                skipped += 1

    print(f"\n{'='*60}")
    print(f"Filled: {filled} files")
    print(f"Skipped: {skipped} files (no data available)")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
