# Problem 139: Word Break

**Difficulty:** Medium
**Pattern:** Dynamic Programming
**Link:** [LeetCode](https://leetcode.com/problems/word-break/)

## Problem Description

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

### Constraints

- 1 <= s.length <= 300
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 20
- s and wordDict[i] consist of only lowercase English letters
- All strings in wordDict are unique

### Examples

**Example 1:**
```
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```

**Example 2:**
```
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
```

## Approaches

### 1. Dynamic Programming

**Time Complexity:** O(n^2 * m) where m is average word length
**Space Complexity:** O(n)

```python
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    word_set = set(wordDict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[n]
```

**Why this works:**

dp[i] = true if s[0:i] can be segmented using the dictionary words. For each position i, we check all possible split points j where dp[j] is true and s[j:i] is in the dictionary. If we find such a split, dp[i] becomes true.

## Key Insights

1. dp[i] = true if s[0:i] can be segmented
2. For each position, check if any word matches ending at that position
3. Use set for O(1) word lookup
4. dp[i] = any(dp[j] and s[j:i] in wordDict)

## Common Mistakes

1. Not using a set for O(1) lookup of words
2. Continuing to check after finding a valid segmentation
3. Forgetting that dp[0] should be True (empty string is valid base case)

## Related Problems

- Word Break II
- Concatenated Words

## Tags

Array, Hash Table, String, Dynamic Programming, Trie, Memoization
