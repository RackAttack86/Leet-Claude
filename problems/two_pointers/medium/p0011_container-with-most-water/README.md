# Problem 11: Container With Most Water

**Difficulty:** Medium
**Pattern:** Two Pointers
**Link:** [LeetCode](https://leetcode.com/problems/container-with-most-water/)

## Problem Description

Given an array of heights representing vertical lines, find two lines that form a container with the x-axis that holds the maximum amount of water.

### Understanding the Problem
- You pick two bars from the array
- Water fills between them up to the height of the **shorter bar**
- Water amount = **width × height**
  - Width = distance between bars (right index - left index)
  - Height = minimum of the two bar heights

### Visual Example
```
[1, 8, 6, 2, 5, 4, 8, 3, 7]
     |                   |
     |~~~~~~~~~~~~~~~~~~~|  ← Water fills to height 7

Width = 8 - 1 = 7
Height = min(8, 7) = 7
Water = 7 × 7 = 49
```

## Approaches

### 1. Brute Force

**Time Complexity:** O(n²)
**Space Complexity:** O(1)

Use nested loops to check every possible pair of bars. Calculate water for each pair and track the maximum. Simple but slow for large arrays.

### 2. Two Pointers + Greedy (Optimal)

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def maxArea(height):
    max_output = 0
    l = 0
    r = len(height) - 1

    while l < r:
        width = r - l
        h = min(height[l], height[r])
        max_output = max(max_output, width * h)

        if height[l] >= height[r]:
            r = r - 1
        else:
            l = l + 1

    return max_output
```

**Why this works:**
- Start with pointers at both ends (maximum width)
- Calculate current water amount
- **Greedy rule**: Always move the pointer at the shorter bar
- Continue until pointers meet

Moving the taller bar can never improve the result because width decreases while height stays the same (limited by shorter bar). Moving the shorter bar gives a chance to find a taller bar that compensates for lost width.

## Key Insights

1. **Water is limited by the shorter bar** - The container can only hold water up to the height of the shorter side

2. **Greedy strategy is optimal** - Moving the shorter bar is provably correct because:
   - Moving the taller bar guarantees no improvement (less width, same height limit)
   - Moving the shorter bar provides potential for finding a taller bar

3. **Equal heights** - When both bars are equal height, you can move either pointer

4. **Why it's called "Greedy"** - The algorithm makes local decisions without backtracking:
   - Decisively moves one pointer based on current state
   - Never reconsiders eliminated pairs
   - Trusts that local optimization leads to global optimum

## Common Mistakes

- Multiplying heights instead of taking the minimum
- Moving the wrong pointer (moving taller instead of shorter)
- Moving left pointer backwards (decreasing index) instead of forward
- Comparing pointer indices instead of the heights at those indices

## Related Problems

- Trapping Rain Water (harder variation)
- Two Sum (similar two-pointer pattern)

## Tags

Array, Two Pointers, Greedy
