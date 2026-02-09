# Problem 300: Longest Increasing Subsequence

**Difficulty:** Medium
**Pattern:** Dynamic Programming
**Link:** [LeetCode](https://leetcode.com/problems/longest-increasing-subsequence/)

## Problem Description

Given an integer array nums, return the length of the longest strictly increasing subsequence.

### Constraints

- 1 <= nums.length <= 2500
- -10^4 <= nums[i] <= 10^4

### Examples

**Example 1:**
```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101]
```

**Example 2:**
```
Input: nums = [0,1,0,3,2,3]
Output: 4
```

## Approaches

### 1. Binary Search (Patience Sorting)

**Time Complexity:** O(n log n)
**Space Complexity:** O(n)

```python
def lengthOfLIS(self, nums: List[int]) -> int:
    # O(n log n) solution using binary search
    tails = []

    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num

    return len(tails)
```

**Why this works:**

We maintain an array `tails` where tails[i] is the smallest ending element of all increasing subsequences of length i+1. For each number, we use binary search to find where it should be placed. If it's larger than all elements, we append it. Otherwise, we replace the first element >= num. The length of tails at the end is the LIS length.

## Key Insights

1. DP approach: dp[i] = max length ending at i
2. For each i, check all j < i where nums[j] < nums[i]
3. Binary search: maintain array of smallest tail for each length
4. Patience sorting algorithm achieves O(n log n)

## Common Mistakes

1. Using O(n^2) DP when O(n log n) is possible
2. Confusing the tails array with the actual LIS (it's not the actual sequence)
3. Using bisect_right instead of bisect_left (we want strictly increasing)

## Related Problems

- Number of Longest Increasing Subsequence
- Increasing Triplet Subsequence
- Russian Doll Envelopes

## Tags

Array, Binary Search, Dynamic Programming
