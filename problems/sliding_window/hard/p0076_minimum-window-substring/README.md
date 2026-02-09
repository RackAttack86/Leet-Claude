# Problem 76: Minimum Window Substring

**Difficulty:** Hard
**Pattern:** Sliding Window
**Link:** [LeetCode](https://leetcode.com/problems/minimum-window-substring/)

## Problem Description

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

The testcases will be generated such that the answer is unique.

## Constraints

- m == s.length
- n == t.length
- 1 <= m, n <= 10^5
- s and t consist of uppercase and lowercase English letters.

## Examples

**Example 1:**
```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
```

**Example 2:**
```
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
```

**Example 3:**
```
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
```

## Approaches

### 1. Two-Pointer Sliding Window with Character Frequency Tracking

**Time Complexity:** O(|s| + |t|)
**Space Complexity:** O(|s| + |t|)

```python
def minWindow(self, s: str, t: str) -> str:
    if not s or not t or len(s) < len(t):
        return ""

    # Count frequency of characters needed from t
    t_count = Counter(t)
    need = len(t_count)  # Number of unique characters we need

    # Window state
    window_count = defaultdict(int)
    have = 0  # Number of unique characters with sufficient frequency

    # Result tracking
    min_len = float('inf')
    result = (0, 0)  # (start, end) of minimum window

    left = 0

    for right in range(len(s)):
        # Add character at right pointer to window
        char = s[right]
        window_count[char] += 1

        # Check if this character now meets the required frequency
        if char in t_count and window_count[char] == t_count[char]:
            have += 1

        # Try to contract window while it's still valid
        while have == need:
            # Update minimum if current window is smaller
            window_size = right - left + 1
            if window_size < min_len:
                min_len = window_size
                result = (left, right + 1)

            # Remove character at left pointer from window
            left_char = s[left]
            window_count[left_char] -= 1

            # Check if this character no longer meets required frequency
            if left_char in t_count and window_count[left_char] < t_count[left_char]:
                have -= 1

            left += 1

    return s[result[0]:result[1]] if min_len != float('inf') else ""
```

**Why this works:**

We use a hash map to count required characters from t. We expand the window by moving the right pointer and track when we have all required characters with sufficient frequency (have == need). When we have a valid window, we contract from the left to find the minimum size while maintaining validity. The key optimization is using "have/need" counters to avoid checking all characters each time.

## Key Insights

1. Expand window until all characters of t are covered
2. Contract window from left while maintaining validity to find minimum
3. Use "have" counter to track unique chars that meet required frequency
4. When have == need, we have a valid window - try to minimize it
5. The key optimization is using "have/need" to avoid checking all chars each time

## Common Mistakes

- Not handling duplicate characters in t correctly
- Checking all characters in t_count each iteration instead of using have/need
- Not considering that t might have duplicate characters
- Returning early before finding the minimum window

## Related Problems

- Substring with Concatenation of All Words
- Find All Anagrams in a String
- Permutation in String
