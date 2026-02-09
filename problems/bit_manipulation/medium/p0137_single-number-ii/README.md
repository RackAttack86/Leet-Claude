# Problem 137: Single Number II

**Difficulty:** Medium
**Pattern:** Bit Manipulation
**Link:** [LeetCode](https://leetcode.com/problems/single-number-ii/)

## Problem Description

Given an integer array `nums` where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`
- Each element in `nums` appears exactly three times except for one element which appears once.

## Examples

Example 1:
```
Input: nums = [2,2,3,2]
Output: 3
```

Example 2:
```
Input: nums = [0,1,0,1,0,1,99]
Output: 99
```

## Approaches

### 1. Bit Manipulation with Two State Variables

**Time Complexity:** O(n) - single pass through the array
**Space Complexity:** O(1) - only two integer variables used

```python
def singleNumber(self, nums: List[int]) -> int:
    ones = 0  # Bits that have appeared 1 time (mod 3)
    twos = 0  # Bits that have appeared 2 times (mod 3)

    for num in nums:
        # Update twos: add bits that are in ones AND in num (appearing 2nd time)
        twos |= (ones & num)

        # Update ones: XOR with num (toggle bits)
        ones ^= num

        # Find bits that are in both ones and twos (appeared 3 times)
        # These need to be cleared from both
        common_mask = ones & twos

        # Clear the bits that appeared 3 times
        ones &= ~common_mask
        twos &= ~common_mask

    # After processing, 'ones' contains bits of the number appearing once
    return ones
```

**Why this works:**
We use two variables to track the count of each bit position modulo 3:
- 'ones' stores bits that have appeared 1 time (mod 3)
- 'twos' stores bits that have appeared 2 times (mod 3)

When a bit appears 3 times, it's cleared from both. At the end, 'ones' contains only the bits of the single element.

## Key Insights

1. We need to count bits modulo 3, not modulo 2 (unlike Single Number I)
2. Use two bit masks to represent three states: 00 (0 times), 01 (1 time), 10 (2 times)
3. When count reaches 3, we reset to 0 (00 state)
4. At the end, 'ones' contains the bits of the single element
5. The state transitions: 00 -> 01 -> 10 -> 00 (cycles every 3)

## Common Mistakes

- Trying to use simple XOR like in Single Number I
- Not understanding the state machine for counting mod 3
- Off-by-one errors in state transitions

## Related Problems

- Single Number
- Single Number III
