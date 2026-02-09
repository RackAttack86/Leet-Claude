# Problem 72: Edit Distance

**Difficulty:** Medium
**Pattern:** Dynamic Programming
**Link:** [LeetCode](https://leetcode.com/problems/edit-distance/)

## Problem Description

Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`.

You have the following three operations permitted on a word:

- Insert a character
- Delete a character
- Replace a character

## Constraints

- 0 <= word1.length, word2.length <= 500
- word1 and word2 consist of lowercase English letters.

## Examples

Example 1:
```
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
```

Example 2:
```
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
```

## Approaches

### 1. Dynamic Programming (Levenshtein Distance)

**Time Complexity:** O(m * n)
**Space Complexity:** O(n)

```python
def minDistance(self, word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)

    # Handle edge cases
    if m == 0:
        return n
    if n == 0:
        return m

    # Use two rows for space optimization
    prev = list(range(n + 1))  # Base case: converting "" to word2[0:j]
    curr = [0] * (n + 1)

    for i in range(1, m + 1):
        # Base case: converting word1[0:i] to ""
        curr[0] = i

        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                # Characters match, no operation needed
                curr[j] = prev[j - 1]
            else:
                # Take minimum of three operations
                curr[j] = 1 + min(
                    prev[j - 1],  # Replace
                    prev[j],      # Delete from word1
                    curr[j - 1]   # Insert into word1
                )

        # Swap rows
        prev, curr = curr, prev

    # Result is in prev because we swapped at the end
    return prev[n]
```

**Why this works:**

This is the classic Levenshtein distance algorithm. dp[i][j] represents the minimum operations to convert word1[0:i] to word2[0:j]. If characters match, no operation is needed. Otherwise, we take the minimum of three operations: replace (dp[i-1][j-1] + 1), delete (dp[i-1][j] + 1), or insert (dp[i][j-1] + 1).

## Key Insights

1. This is the classic Levenshtein distance algorithm.
2. Base cases: converting empty string to word2 requires len(word2) insertions, converting word1 to empty string requires len(word1) deletions.
3. Insert in word1 is equivalent to delete in word2 conceptually.
4. We only need the previous row to compute the current row.

## Common Mistakes

1. Forgetting the base cases for empty strings
2. Getting confused about which operation corresponds to which dp transition
3. Off-by-one errors with string indices vs dp indices

## Related Problems

- One Edit Distance
- Delete Operation for Two Strings
- Minimum ASCII Delete Sum for Two Strings
