"""
LeetCode Problem #70: Climbing Stairs
Difficulty: Easy
Pattern: Dynamic Programming
Link: https://leetcode.com/problems/climbing-stairs/

Problem:
--------
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can
you climb to the top?

Constraints:
-----------
- 1 <= n <= 45

Examples:
---------
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


class Solution:
    """
    Solution to LeetCode Problem #70: Climbing Stairs

    Approach: Dynamic Programming (Fibonacci pattern)
    Time Complexity: O(n)
    Space Complexity: O(1)

    Key Insights:
    - This is actually a Fibonacci sequence problem!
    - To reach step n, you can come from step n-1 (1 step) or n-2 (2 steps)
    - Therefore: ways(n) = ways(n-1) + ways(n-2)
    - Base cases: ways(1) = 1, ways(2) = 2
    """

    def climbStairs(self, n: int) -> int:
        """
        Calculate number of ways to climb n stairs.

        Args:
            n: Number of stairs

        Returns:
            Number of distinct ways to reach the top
        """
        if n <= 2:
            return n

        # Initialize for first two steps
        prev2 = 1  # ways to reach step 1
        prev1 = 2  # ways to reach step 2

        # Calculate for steps 3 to n
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current

        return prev1

    def climbStairs_recursive(self, n: int) -> int:
        """
        Recursive approach with memoization.
        Time: O(n), Space: O(n)
        """
        memo = {}

        def climb(step):
            if step <= 2:
                return step
            if step in memo:
                return memo[step]

            memo[step] = climb(step - 1) + climb(step - 2)
            return memo[step]

        return climb(n)

    def climbStairs_dp_array(self, n: int) -> int:
        """
        DP with array (easier to understand).
        Time: O(n), Space: O(n)
        """
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 70,
    "name": "Climbing Stairs",
    "difficulty": "Easy",
    "pattern": "Dynamic Programming",
    "topics": ["Dynamic Programming", "Math", "Memoization"],
    "url": "https://leetcode.com/problems/climbing-stairs/",
    "companies": ["Amazon", "Google", "Adobe", "Apple"],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}
