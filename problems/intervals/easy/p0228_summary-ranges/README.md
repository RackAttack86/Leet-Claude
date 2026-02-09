# Problem 228: Summary Ranges

**Difficulty:** Easy
**Pattern:** Intervals
**Link:** [LeetCode](https://leetcode.com/problems/summary-ranges/)

## Problem Description

You are given a sorted unique integer array `nums`.

A range `[a,b]` is the set of all integers from `a` to `b` (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of `nums` is covered by exactly one of the ranges, and there is no integer `x` such that `x` is in one of the ranges but not in `nums`.

Each range `[a,b]` in the list should be output as:

- `"a->b"` if `a != b`

- `"a"` if `a == b`

## Constraints

- `0 <= nums.length <= 20`
- `-2^31 <= nums[i] <= 2^31 - 1`
- All the values of `nums` are unique.
- `nums` is sorted in ascending order.

## Examples

Example 1:
```
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
```

Example 2:
```
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
```

## Approaches

### 1. Two-pointer Linear Scan

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def summaryRanges(self, nums: List[int]) -> List[str]:
    if not nums:
        return []

    result = []
    n = len(nums)
    start = 0  # Start index of current range

    for i in range(n):
        # Check if current range ends (next element is not consecutive or at end)
        if i == n - 1 or nums[i + 1] != nums[i] + 1:
            # Format the range
            if start == i:
                # Single element range
                result.append(str(nums[start]))
            else:
                # Multi-element range
                result.append(f"{nums[start]}->{nums[i]}")
            # Start new range from next element
            start = i + 1

    return result
```

**Why this works:**
- Use a start pointer to track the beginning of each range
- Iterate through the array, checking if the next element is consecutive
- When a break in consecutiveness is found (or at end), format the range and add to result
- Continue with the next range starting from the current position

## Key Insights

- Since the array is sorted and unique, consecutive elements differ by exactly 1
- A range ends when nums[i+1] != nums[i] + 1 or when we reach the end
- Two formatting cases: single element "a" vs range "a->b"
- Empty input returns empty output

## Common Mistakes

- Forgetting to handle single-element ranges differently from multi-element ranges
- Off-by-one errors when checking for consecutive elements
- Not handling the last range properly

## Related Problems

- Merge Intervals
- Insert Interval
