# Problem 167: Two Sum II - Input Array Is Sorted

**Difficulty:** Medium
**Pattern:** Two Pointers
**Link:** [LeetCode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

## Problem Description

Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers, `index1` and `index2`, added by one as an integer array `[index1, index2]` of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

## Constraints

- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`
- `numbers` is sorted in non-decreasing order.
- `-1000 <= target <= 1000`
- The tests are generated such that there is exactly one solution.

## Examples

Example 1:
```

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

```

Example 2:
```

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

```

Example 3:
```

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

```

## Approaches

### 1. Two Pointers

**Time Complexity:** O(n) - Single pass with two pointers
**Space Complexity:** O(1) - Only using two pointer variables

```python
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            # Return 1-indexed positions
            return [left + 1, right + 1]
        elif current_sum < target:
            # Need larger sum, move left pointer right
            left += 1
        else:
            # Need smaller sum, move right pointer left
            right -= 1

    # Problem guarantees a solution exists
    return []
```

**Why this works:**
Classic two-pointer technique. Use one pointer at the start and one at the end. If sum is too large, move right pointer left. If sum is too small, move left pointer right. The sorted property guarantees we will find the solution.

## Key Insights

1. Sorted array enables two-pointer approach
2. Moving left pointer increases sum, moving right decreases it
3. Guaranteed exactly one solution, so we will always find it
4. Return 1-indexed positions as required by the problem

## Common Mistakes

- Returning 0-indexed instead of 1-indexed positions
- Using hash map (works but doesn't meet O(1) space requirement)
- Not leveraging the sorted property of the array

## Related Problems

- Two Sum (LeetCode #1)
- 3Sum (LeetCode #15)
- Two Sum IV - Input is a BST (LeetCode #653)
