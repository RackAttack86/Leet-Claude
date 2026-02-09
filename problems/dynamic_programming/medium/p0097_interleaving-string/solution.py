"""
LeetCode Problem #97: Interleaving String
Difficulty: Medium
Pattern: Dynamic Programming
Link: https://leetcode.com/problems/interleaving-string/

Problem:
--------
Given strings `s1`, `s2`, and `s3`, find whether `s3` is formed by an interleaving of `s1` and `s2`.

An interleaving of two strings `s` and `t` is a configuration where `s` and `t` are divided into `n` and `m` substrings respectively, such that:

- `s = s1 + s2 + ... + sn`

- `t = t1 + t2 + ... + tm`

- `|n - m|

- The interleaving is `s1 + t1 + s2 + t2 + s3 + t3 + ...` or `t1 + s1 + t2 + s2 + t3 + s3 + ...`

Note: `a + b` is the concatenation of strings `a` and `b`.

Constraints:
-----------
- `0
- s1`, `s2`, and `s3` consist of lowercase English letters.

Examples:
---------
Example 1:
```

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.

```

Example 2:
```

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.

```

Example 3:
```

Input: s1 = "", s2 = "", s3 = ""
Output: true

```
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #97: Interleaving String

    Approach: Dynamic Programming with space optimization
    - dp[i][j] represents whether s3[0:i+j] can be formed by interleaving s1[0:i] and s2[0:j].
    - Transition: dp[i][j] = True if either:
      * dp[i-1][j] is True and s1[i-1] == s3[i+j-1] (take from s1)
      * dp[i][j-1] is True and s2[j-1] == s3[i+j-1] (take from s2)
    - Optimize space to O(n) using a single row.

    Time Complexity: O(m * n)
    Space Complexity: O(n) - using 1D array optimization

    Key Insights:
    1. First check if len(s1) + len(s2) == len(s3), otherwise return False immediately.
    2. At each position in s3, we must take a character from either s1 or s2.
    3. The position in s3 is determined by how many characters we've used from s1 and s2.
    4. This is similar to edit distance but with boolean decisions.
    """

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Check if s3 is formed by interleaving s1 and s2.

        Args:
            s1: First string
            s2: Second string
            s3: Target interleaved string

        Returns:
            True if s3 can be formed by interleaving s1 and s2
        """
        m, n = len(s1), len(s2)

        # Quick check: lengths must match
        if m + n != len(s3):
            return False

        # dp[j] represents whether s3[0:i+j] can be formed using s1[0:i] and s2[0:j]
        dp = [False] * (n + 1)

        # Base case and fill first row (using only s2)
        for j in range(n + 1):
            if j == 0:
                dp[j] = True
            else:
                dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        # Fill the rest
        for i in range(1, m + 1):
            # First column: using only s1
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]

            for j in range(1, n + 1):
                # Current position in s3
                k = i + j - 1

                # Can we form s3[0:k+1] by:
                # 1. Taking from s1: dp[i-1][j] was True and s1[i-1] matches s3[k]
                # 2. Taking from s2: dp[i][j-1] was True and s2[j-1] matches s3[k]
                dp[j] = (dp[j] and s1[i - 1] == s3[k]) or \
                        (dp[j - 1] and s2[j - 1] == s3[k])

        return dp[n]


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 97,
    "name": "Interleaving String",
    "difficulty": "Medium",
    "pattern": "Dynamic Programming",
    "topics": ['String', 'Dynamic Programming'],
    "url": "https://leetcode.com/problems/interleaving-string/",
    "companies": ["Amazon", "Google", "Microsoft", "Facebook", "Bloomberg", "Apple", "Uber"],
    "time_complexity": "O(m * n)",
    "space_complexity": "O(n)",
}
