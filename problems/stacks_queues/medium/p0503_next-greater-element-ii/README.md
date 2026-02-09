# Problem 503: Next Greater Element II

**Difficulty:** Medium
**Pattern:** Stacks Queues
**Link:** [LeetCode](https://leetcode.com/problems/next-greater-element-ii/)

## Problem Description

Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

### Constraints

- 1 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9

### Examples

**Example 1:**
```
Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number.
The second 1's next greater number needs to search circularly, which is also 2.
```

**Example 2:**
```
Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
```

## Approaches

### 1. Monotonic Stack with Circular Traversal

**Time Complexity:** O(n)
**Space Complexity:** O(n)

```python
def nextGreaterElements(self, nums: List[int]) -> List[int]:
    n = len(nums)
    result = [-1] * n
    stack = []  # Stack of indices

    # Process array twice for circular effect
    for i in range(2 * n):
        idx = i % n

        # While current element is greater than element at stack top
        while stack and nums[idx] > nums[stack[-1]]:
            result[stack.pop()] = nums[idx]

        # Only push indices from first pass (avoid duplicates)
        if i < n:
            stack.append(idx)

    return result
```

**Why this works:**

We use a monotonic decreasing stack storing indices. To handle the circular nature, we process the array twice. In the first pass, we push indices onto the stack and pop when we find greater elements. In the second pass, we only pop (don't push) to find next greater elements that wrap around. Elements remaining in the stack have no next greater element.

## Key Insights

- Process array twice for circular effect
- Use monotonic decreasing stack
- Store indices in stack
- Update result when finding greater element

## Common Mistakes

- Not handling the circular nature (only processing once)
- Pushing indices in the second pass (causes duplicates)
- Using values instead of indices in the stack

## Related Problems

- Next Greater Element I
- Daily Temperatures

## Tags

Array, Stack, Monotonic Stack
