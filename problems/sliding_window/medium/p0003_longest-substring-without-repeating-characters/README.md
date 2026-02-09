# Problem 3: Longest Substring Without Repeating Characters

**Difficulty:** Medium
**Pattern:** Sliding Window
**Link:** [LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## Problem Description

Given a string s, find the length of the longest substring without repeating characters.

### Constraints

- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces

### Examples

**Example 1:**
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

**Example 2:**
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3:**
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

## Approaches

### 1. Sliding Window with Hash Map

**Time Complexity:** O(n)
**Space Complexity:** O(min(m, n)) where m is charset size

```python
def lengthOfLongestSubstring(self, s: str) -> int:
    char_index = {}  # Maps character to its last seen index
    max_length = 0
    left = 0

    for right, char in enumerate(s):
        # If character was seen and is within current window
        if char in char_index and char_index[char] >= left:
            # Move left pointer past the duplicate
            left = char_index[char] + 1

        # Update the last seen index of current character
        char_index[char] = right

        # Update maximum length
        max_length = max(max_length, right - left + 1)

    return max_length
```

**Why this works:**

We use a sliding window with a hash map to track the last seen index of each character. When we encounter a duplicate character that is within our current window, we move the left pointer past the previous occurrence of that character. This ensures our window always contains unique characters. We track the maximum window size throughout the iteration.

## Key Insights

- Use hash map to track character positions
- Expand window with right pointer
- Contract window when duplicate found (move left past the duplicate)
- Track maximum window size

## Common Mistakes

- Not checking if the duplicate is within the current window
- Removing characters from the hash map instead of just moving the left pointer
- Using a set instead of a map (requires more operations)

## Related Problems

- Longest Substring with At Most Two Distinct Characters
- Longest Substring with At Most K Distinct Characters

## Tags

Hash Table, String, Sliding Window
