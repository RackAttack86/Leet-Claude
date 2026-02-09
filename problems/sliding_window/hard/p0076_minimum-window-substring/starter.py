"""
LeetCode Problem #76: Minimum Window Substring
Difficulty: Hard
Pattern: Sliding Window
Link: https://leetcode.com/problems/minimum-window-substring/

Problem:
--------
Given two strings `s` and `t` of lengths `m` and `n` respectively, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

The testcases will be generated such that the answer is unique.

Constraints:
-----------
- `m == s.length
- n == t.length
- s` and `t` consist of uppercase and lowercase English letters.

Examples:
---------
Example 1:
```

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

```

Example 2:
```

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

```

Example 3:
```

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

```
"""

from typing import List, Optional
from collections import Counter, defaultdict


class Solution:
    """
    Solution to LeetCode Problem #76: Minimum Window Substring

    Approach: Two-Pointer Sliding Window with Character Frequency Tracking
    - Use a hash map to count required characters from t
    - Expand window by moving right pointer to include characters
    - When window contains all required characters, contract from left to find minimum
    - Track "formed" count to efficiently know when window is valid
    - Use "have" and "need" counters for unique characters with sufficient frequency

    Time Complexity: O(|s| + |t|)
        - We traverse string s at most twice (once with right, once with left pointer)
        - Building the frequency map for t takes O(|t|)
        - Each character comparison and hash map operation is O(1)

    Space Complexity: O(|s| + |t|)
        - In the worst case, the window could be the entire string s
        - Hash maps store at most O(52) unique characters (uppercase + lowercase letters)
        - Effectively O(1) for character frequency maps since alphabet is fixed

    Key Insights:
    1. Expand window until all characters of t are covered
    2. Contract window from left while maintaining validity to find minimum
    3. Use "have" counter to track unique chars that meet required frequency
    4. When have == need, we have a valid window - try to minimize it
    5. The key optimization is using "have/need" to avoid checking all chars each time
    """
    def minWindow(self, s: str, t: str) -> str:
        """
        Find the minimum window in s that contains all characters of t.
        """
        pass



PROBLEM_METADATA = {
    "number": 76,
    "name": "Minimum Window Substring",
    "difficulty": "Hard",
    "pattern": "Sliding Window",
    "topics": ['Hash Table', 'String', 'Sliding Window'],
    "url": "https://leetcode.com/problems/minimum-window-substring/",
    "companies": ["Facebook", "Amazon", "Google", "Microsoft", "LinkedIn", "Apple", "Uber", "Airbnb", "Bloomberg"],
    "time_complexity": "O(|s| + |t|)",
    "space_complexity": "O(|s| + |t|)",
}