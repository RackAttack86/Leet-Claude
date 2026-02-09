# Problem 120: Triangle

**Difficulty:** Medium
**Pattern:** Dynamic Programming
**Link:** [LeetCode](https://leetcode.com/problems/triangle/)

## Problem Description

Given a `triangle` array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index `i` on the current row, you may move to either index `i` or index `i + 1` on the next row.

## Constraints

- 1 <= triangle.length <= 200
- triangle[0].length == 1
- triangle[i].length == triangle[i - 1].length + 1
- -10^4 <= triangle[i][j] <= 10^4

## Examples

Example 1:
```
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
```

Example 2:
```
Input: triangle = [[-10]]
Output: -10
```

## Approaches

### 1. Bottom-up Dynamic Programming

**Time Complexity:** O(n^2) where n is the number of rows
**Space Complexity:** O(n)

```python
def minimumTotal(self, triangle: List[List[int]]) -> int:
    n = len(triangle)

    # Start with the bottom row as our dp array
    dp = triangle[-1][:]

    # Process from second-to-last row up to the top
    for i in range(n - 2, -1, -1):
        for j in range(len(triangle[i])):
            # Minimum path from current position is current value
            # plus minimum of the two possible next positions
            dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

    # The answer is the minimum path sum starting from the top
    return dp[0]
```

**Why this works:**

Starting from the bottom row and working upward, for each cell we compute the minimum path sum by adding the current value to the minimum of the two adjacent cells in the row below: dp[j] = triangle[i][j] + min(dp[j], dp[j+1]). The answer will be in dp[0] after processing all rows.

## Key Insights

1. Bottom-up approach is cleaner than top-down for this problem.
2. From any position (i, j), we can only reach (i+1, j) or (i+1, j+1).
3. Working bottom-up, we process each row and update in place.
4. We can use O(n) space by reusing a single array.

## Common Mistakes

1. Using top-down approach which is more complex for this problem
2. Not realizing that bottom-up simplifies the edge cases
3. Creating a new dp array for each row when in-place update works

## Related Problems

- Minimum Path Sum
- Dungeon Game
- Maximum Total Reward
