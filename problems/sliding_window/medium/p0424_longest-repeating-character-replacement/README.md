# Problem 424: Longest Repeating Character Replacement

**Difficulty:** Medium
**Pattern:** Sliding Window
**Link:** [LeetCode](https://leetcode.com/problems/longest-repeating-character-replacement/)

## Problem Description

You are given a string s and an integer k. You can choose any character of the string and change
it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing
the above operations.

### Constraints

- 1 <= s.length <= 10^5
- s consists of only uppercase English letters
- 0 <= k <= s.length

### Examples

**Example 1:**
```
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa
```

**Example 2:**
```
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
```

## Approaches

### 1. Sliding Window with Character Frequency

**Time Complexity:** O(n)
**Space Complexity:** O(1) - only 26 uppercase letters

```python
def characterReplacement(self, s: str, k: int) -> int:
    char_count = {}
    max_freq = 0
    max_length = 0
    left = 0

    for right in range(len(s)):
        # Add character to window
        char = s[right]
        char_count[char] = char_count.get(char, 0) + 1
        max_freq = max(max_freq, char_count[char])

        # Window size - max frequency = characters that need replacement
        # If this exceeds k, shrink window
        window_size = right - left + 1
        if window_size - max_freq > k:
            char_count[s[left]] -= 1
            left += 1

        # Update max length (window_size after possible shrink)
        max_length = max(max_length, right - left + 1)

    return max_length
```

**Why this works:**

A window is valid if `(window_size - max_char_frequency) <= k`. The max_char_frequency tells us how many characters don't need replacement - we keep the most frequent character and replace the rest. If the number of characters that need replacement exceeds k, the window is invalid and we shrink it from the left.

## Key Insights

- Window valid if length - max_freq <= k
- Track frequency of each character
- Expand window and contract when invalid
- Max frequency character determines replacements needed

## Common Mistakes

- Recalculating max frequency from scratch each time (not necessary)
- Not understanding why we don't need to decrease max_freq when shrinking
- Using O(26n) by scanning all frequencies instead of tracking max

## Related Problems

- Longest Substring Without Repeating Characters
- Max Consecutive Ones III

## Tags

Hash Table, String, Sliding Window
