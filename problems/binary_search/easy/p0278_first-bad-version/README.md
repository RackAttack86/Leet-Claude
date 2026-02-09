# Problem 278: First Bad Version

**Difficulty:** Easy
**Pattern:** Binary Search
**Link:** [LeetCode](https://leetcode.com/problems/first-bad-version/)

## Problem Description

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

### Constraints
- 1 <= bad <= n <= 2^31 - 1

### Examples
- Input: n = 5, bad = 4 -> Output: 4
  - call isBadVersion(3) -> false
  - call isBadVersion(5) -> true
  - call isBadVersion(4) -> true
  - Then 4 is the first bad version.

## Approaches

### 1. Binary Search

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

```python
def firstBadVersion(self, n: int) -> int:
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left
```

**Why this works:**
This is a classic binary search for finding the first occurrence. If the current version is bad, the first bad version is at mid or to its left, so we set right = mid. If the current version is good, the first bad version must be to the right, so we set left = mid + 1. The loop terminates when left == right, which is the first bad version.

## Key Insights

- Classic binary search for first occurrence
- If version is bad, search left half (including mid)
- If version is good, search right half
- Minimize API calls by halving search space each time

## Common Mistakes

- Using left <= right instead of left < right (can cause infinite loop)
- Integer overflow when computing mid (use left + (right - left) // 2)
- Off-by-one errors with 1-indexed versions

## Related Problems

- Search Insert Position (#35)
- Find First and Last Position of Element in Sorted Array (#34)

## Tags

Binary Search, Interactive
