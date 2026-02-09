"""
LeetCode Problem #72: Edit Distance
Difficulty: Medium
Pattern: Dynamic Programming
Link: https://leetcode.com/problems/edit-distance/

Problem:
--------
Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`.

You have the following three operations permitted on a word:

- Insert a character

- Delete a character

- Replace a character

Constraints:
-----------
- `0
- word1` and `word2` consist of lowercase English letters.

Examples:
---------
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
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #72: Edit Distance

    Approach: Dynamic Programming (Levenshtein Distance)
    - dp[i][j] represents the minimum operations to convert word1[0:i] to word2[0:j].
    - If word1[i-1] == word2[j-1], no operation needed: dp[i][j] = dp[i-1][j-1]
    - Otherwise, take minimum of three operations:
      * Replace: dp[i-1][j-1] + 1
      * Delete from word1: dp[i-1][j] + 1
      * Insert into word1: dp[i][j-1] + 1
    - Optimize space from O(m*n) to O(n) using two rows.

    Time Complexity: O(m * n)
    Space Complexity: O(n) - using space-optimized approach

    Key Insights:
    1. This is the classic Levenshtein distance algorithm.
    2. Base cases: converting empty string to word2 requires len(word2) insertions,
       converting word1 to empty string requires len(word1) deletions.
    3. Insert in word1 is equivalent to delete in word2 conceptually.
    4. We only need the previous row to compute the current row.
    """

    def minDistance(self, word1: str, word2: str) -> int:
        """
        Calculate the minimum edit distance (Levenshtein distance) between two strings.

        Args:
            word1: Source string to convert from
            word2: Target string to convert to

        Returns:
            Minimum number of operations (insert, delete, replace) needed
        """
        m, n = len(word1), len(word2)

        # Handle edge cases
        if m == 0:
            return n
        if n == 0:
            return m

        # Use two rows for space optimization
        # prev represents dp[i-1], curr represents dp[i]
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


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 72,
    "name": "Edit Distance",
    "difficulty": "Medium",
    "pattern": "Dynamic Programming",
    "topics": ['String', 'Dynamic Programming'],
    "url": "https://leetcode.com/problems/edit-distance/",
    "companies": ["Amazon", "Google", "Microsoft", "Facebook", "Bloomberg", "Apple", "LinkedIn", "Uber", "Oracle", "ByteDance"],
    "time_complexity": "O(m * n)",
    "space_complexity": "O(n)",
}
