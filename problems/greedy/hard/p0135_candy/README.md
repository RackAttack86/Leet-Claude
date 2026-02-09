# Problem 135: Candy

**Difficulty:** Hard
**Pattern:** Greedy
**Link:** [LeetCode](https://leetcode.com/problems/candy/)

## Problem Description

There are `n` children standing in a line. Each child is assigned a rating value given in the integer array `ratings`.

You are giving candies to these children subjected to the following requirements:

- Each child must have at least one candy.
- Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children.

## Examples

Example 1:
```
Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
```

Example 2:
```
Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
```

## Approaches

### 1. Two-Pass Greedy

**Time Complexity:** O(n) - two passes through the array
**Space Complexity:** O(n) - array to store candy counts

```python
def candy(self, ratings: List[int]) -> int:
    n = len(ratings)
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Initialize all children with 1 candy
    candies = [1] * n

    # Left to right pass: ensure right neighbor constraint
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Right to left pass: ensure left neighbor constraint
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)
```

**Why this works:**
First pass (left to right) ensures children with higher ratings than their left neighbor get more candies. Second pass (right to left) ensures children with higher ratings than their right neighbor get more candies while maintaining the left constraint using max().

## Key Insights

1. Each child must have at least 1 candy
2. Left-to-right pass: if rating[i] > rating[i-1], then candies[i] = candies[i-1] + 1
3. Right-to-left pass: if rating[i] > rating[i+1], then candies[i] = max(candies[i], candies[i+1] + 1)
4. The max in the second pass preserves the constraint from the first pass
5. Equal ratings don't require more candies (only strictly greater does)

## Common Mistakes

1. Not using max() in the second pass (overwriting first pass results)
2. Thinking equal ratings require equal candies (they don't)
3. Trying to solve in one pass (not possible for this problem)

## Related Problems

- 1840. Maximum Building Height
- 2371. Minimize Maximum Value in a Grid

## Tags

Array, Greedy
