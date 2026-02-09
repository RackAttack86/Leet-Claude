# Problem 438: Find All Anagrams in a String

**Difficulty:** Medium
**Pattern:** Sliding Window
**Link:** [LeetCode](https://leetcode.com/problems/find-all-anagrams-in-a-string/)

## Problem Description

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Constraints

- 1 <= s.length, p.length <= 3 * 10^4
- s and p consist of lowercase English letters

### Examples

**Example 1:**
```
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
```

**Example 2:**
```
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
```

## Approaches

### 1. Sliding Window with Character Frequency

**Time Complexity:** O(n)
**Space Complexity:** O(1) - only 26 lowercase letters

```python
def findAnagrams(self, s: str, p: str) -> List[int]:
    result = []
    len_p, len_s = len(p), len(s)

    if len_p > len_s:
        return result

    # Count characters in pattern
    p_count = [0] * 26
    s_count = [0] * 26

    for char in p:
        p_count[ord(char) - ord('a')] += 1

    # Initialize first window
    for i in range(len_p):
        s_count[ord(s[i]) - ord('a')] += 1

    if s_count == p_count:
        result.append(0)

    # Slide window
    for i in range(len_p, len_s):
        # Add new character to window
        s_count[ord(s[i]) - ord('a')] += 1
        # Remove old character from window
        s_count[ord(s[i - len_p]) - ord('a')] -= 1

        if s_count == p_count:
            result.append(i - len_p + 1)

    return result
```

**Why this works:**

We use a fixed-size sliding window of length len(p). Two strings are anagrams if and only if they have the same character frequencies. We maintain a frequency array for the current window and compare it with the pattern's frequency array. As we slide the window, we add the new character and remove the old character from our frequency count.

## Key Insights

- Fixed window size = len(p)
- Compare character frequencies
- Slide window and update frequencies
- Use counter or array for frequencies

## Common Mistakes

- Not handling the case when p is longer than s
- Recalculating the entire window frequency each time
- Using string comparison instead of frequency arrays

## Related Problems

- Permutation in String
- Minimum Window Substring

## Tags

Hash Table, String, Sliding Window
