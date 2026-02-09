# Problem 189: Rotate Array

**Difficulty:** Medium
**Pattern:** Two Pointers
**Link:** [LeetCode](https://leetcode.com/problems/rotate-array/)

## Problem Description

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

## Constraints

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`

## Examples

Example 1:
```

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

```

Example 2:
```

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

```

## Approaches

### 1. Three-Step Reversal

**Time Complexity:** O(n) - Each element is reversed at most twice
**Space Complexity:** O(1) - In-place reversal with no extra array

```python
def rotate(self, nums: List[int], k: int) -> None:
    n = len(nums)
    k = k % n  # Handle k larger than array length

    def reverse(left: int, right: int) -> None:
        """Reverse elements in-place between left and right indices."""
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    # Step 1: Reverse entire array
    reverse(0, n - 1)
    # Step 2: Reverse first k elements
    reverse(0, k - 1)
    # Step 3: Reverse remaining elements
    reverse(k, n - 1)
```

**Why this works:**
Three-step reversal algorithm. First reverse the entire array, then reverse the first k elements, then reverse the remaining elements. This achieves in-place rotation with O(1) extra space.

## Key Insights

1. k can be larger than n, so we use k % n
2. Reverse entire array: [1,2,3,4,5,6,7] -> [7,6,5,4,3,2,1]
3. Reverse first k: [5,6,7,4,3,2,1]
4. Reverse rest: [5,6,7,1,2,3,4]
5. Two-pointer technique for reversing subarrays in-place

## Common Mistakes

- Not handling k > n case (use k % n)
- Using extra O(n) space instead of in-place reversal
- Off-by-one errors in reverse function boundaries

## Related Problems

- Reverse String (LeetCode #344)
- Rotate List (LeetCode #61)
