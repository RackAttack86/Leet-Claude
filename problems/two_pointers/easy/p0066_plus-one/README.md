# Problem 66: Plus One

**Difficulty:** Easy
**Pattern:** Two Pointers
**Link:** [LeetCode](https://leetcode.com/problems/plus-one/)

## Problem Description

You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the `i^th` digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading `0`'s.

Increment the large integer by one and return the resulting array of digits.

## Constraints

- 1 <= digits.length <= 100
- 0 <= digits[i] <= 9
- `digits` does not contain any leading `0`'s.

## Examples

Example 1:
```
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
```

Example 2:
```
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
```

Example 3:
```
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
```

## Approaches

### 1. Right-to-Left Carry Propagation

**Time Complexity:** O(n) where n is the number of digits
**Space Complexity:** O(1) in-place, or O(n) if we need to add a new digit

```python
def plusOne(self, digits: List[int]) -> List[int]:
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0

    # If we're here, all digits were 9 (e.g., 999 -> 1000)
    return [1] + digits
```

**Why this works:**
Start from the rightmost digit and add 1. If digit becomes 10, set it to 0 and carry 1 to the next position. If no carry remains, we're done. If we've processed all digits and still have carry, prepend 1.

## Key Insights

- Start from the rightmost digit and add 1
- If digit becomes 10, set it to 0 and carry 1 to the next position
- If no carry remains, we're done
- If we've processed all digits and still have carry, prepend 1

## Common Mistakes

- Not handling the all-9s case (e.g., 999 -> 1000)
- Converting to integer and back (may overflow for large arrays)
- Forgetting to handle the carry properly

## Related Problems

- Add Binary
- Add Two Numbers
