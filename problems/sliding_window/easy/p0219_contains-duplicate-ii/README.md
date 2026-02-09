# Problem 219: Contains Duplicate II

**Difficulty:** Easy
**Pattern:** Sliding Window
**Link:** [LeetCode](https://leetcode.com/problems/contains-duplicate-ii/)

## Problem Description

Given an integer array `nums` and an integer `k`, return `true` if there are two distinct indices `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

## Constraints

- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- 0 <= k <= 10^5

## Examples

**Example 1:**
```
Input: nums = [1,2,3,1], k = 3
Output: true
```

**Example 2:**
```
Input: nums = [1,0,1,1], k = 1
Output: true
```

**Example 3:**
```
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
```

## Approaches

### 1. Sliding Window with Hash Set

**Time Complexity:** O(n)
**Space Complexity:** O(min(n, k))

```python
def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    # Edge case: if k is 0, we can never have two distinct indices with distance <= 0
    if k == 0:
        return False

    # Hash set to store elements in the current sliding window
    window = set()

    for i, num in enumerate(nums):
        # If current element already exists in window, found duplicate within distance k
        if num in window:
            return True

        # Add current element to the window
        window.add(num)

        # If window size exceeds k, remove the oldest element (leftmost in window)
        # This ensures we only keep elements within distance k from current position
        if len(window) > k:
            window.remove(nums[i - k])

    # No duplicates found within distance k
    return False
```

**Why this works:**

We use a hash set to maintain all elements within the current window of size k. As we iterate through the array, we check if the current element exists in the set. If it does, we found a duplicate within distance k and return True. If the window size exceeds k, we remove the element that falls out of the window. We add the current element to the set and continue.

## Key Insights

1. The sliding window approach naturally handles the "distance <= k" constraint
2. Using a hash set allows O(1) duplicate detection within the window
3. We only need to track elements within the current window, not their indices
4. When the window slides, we remove the oldest element (nums[i-k]) to maintain size
5. If k >= n, the window covers the entire array (just check for any duplicate)

## Common Mistakes

- Forgetting to handle the edge case when k = 0
- Not removing the oldest element when window exceeds size k
- Using O(n^2) approach by checking all pairs

## Related Problems

- Contains Duplicate
- Contains Duplicate III
