# Problem 875: Koko Eating Bananas

**Difficulty:** Medium
**Pattern:** Binary Search
**Link:** [LeetCode](https://leetcode.com/problems/koko-eating-bananas/)

## Problem Description

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

### Constraints
- 1 <= piles.length <= 10^4
- piles.length <= h <= 10^9
- 1 <= piles[i] <= 10^9

### Examples
- Input: piles = [3,6,7,11], h = 8 -> Output: 4
- Input: piles = [30,11,23,4,20], h = 5 -> Output: 30
- Input: piles = [30,11,23,4,20], h = 6 -> Output: 23

## Approaches

### 1. Binary Search on Answer

**Time Complexity:** O(n * log m) where m is max pile size
**Space Complexity:** O(1)

```python
def minEatingSpeed(self, piles: List[int], h: int) -> int:
    def canFinish(speed):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / speed)
        return hours <= h

    left, right = 1, max(piles)

    while left < right:
        mid = (left + right) // 2
        if canFinish(mid):
            right = mid
        else:
            left = mid + 1

    return left
```

**Why this works:**
We binary search on the eating speed k in the range [1, max(piles)]. For each speed, we check if Koko can finish all bananas in h hours. If she can, we try a smaller speed (search left). If she can't, we need a faster speed (search right). The minimum valid speed is our answer.

## Key Insights

- Binary search on eating speed (1 to max(piles))
- For each speed, calculate total hours needed using ceiling division
- Find minimum speed that allows finishing within h hours
- This is "binary search on answer" pattern

## Common Mistakes

- Using floor division instead of ceiling for hours calculation
- Wrong search range (minimum is 1, not 0)
- Not using the correct binary search template for finding minimum

## Related Problems

- Capacity To Ship Packages Within D Days (#1011)
- Minimize Max Distance to Gas Station (#774)

## Tags

Array, Binary Search
