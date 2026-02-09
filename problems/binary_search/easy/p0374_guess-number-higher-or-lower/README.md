# Problem 374: Guess Number Higher or Lower

**Difficulty:** Easy
**Pattern:** Binary Search
**Link:** [LeetCode](https://leetcode.com/problems/guess-number-higher-or-lower/)

## Problem Description

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

- -1: Your guess is higher than the number I picked (i.e. num > pick).
- 1: Your guess is lower than the number I picked (i.e. num < pick).
- 0: your guess is equal to the number I picked (i.e. num == pick).

Return the number that I picked.

### Constraints
- 1 <= n <= 2^31 - 1
- 1 <= pick <= n

### Examples
- Input: n = 10, pick = 6 -> Output: 6
- Input: n = 1, pick = 1 -> Output: 1
- Input: n = 2, pick = 1 -> Output: 1

## Approaches

### 1. Binary Search

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

```python
def guessNumber(self, n: int) -> int:
    left, right = 1, n
    while left <= right:
        mid = (left + right) // 2
        result = guess(mid)
        if result == 0:
            return mid
        elif result == -1:  # Mid is too high
            right = mid - 1
        else:  # result == 1, Mid is too low
            left = mid + 1
    return left
```

**Why this works:**
Standard binary search using the guess() API to adjust the search range. The API tells us whether to search higher or lower, allowing us to eliminate half the search space with each guess.

## Key Insights

- Standard binary search
- Use guess() API to adjust search range
- Similar to finding target in sorted array
- Note the API return values: -1 means guess is too high, 1 means too low

## Common Mistakes

- Confusing the API return values (-1 means your guess is higher, not lower)
- Integer overflow when computing mid with large n

## Related Problems

- Binary Search (#704)
- First Bad Version (#278)
- Guess Number Higher or Lower II (#375)

## Tags

Binary Search, Interactive
