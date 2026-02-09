# Problem 9: Palindrome Number

**Difficulty:** Easy
**Pattern:** Bit Manipulation
**Link:** [LeetCode](https://leetcode.com/problems/palindrome-number/)

## Problem Description

Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

## Constraints

- `-2^31 <= x <= 2^31 - 1`

## Examples

Example 1:
```
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
```

Example 2:
```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

Example 3:
```
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

## Approaches

### 1. Reverse Half of the Number

**Time Complexity:** O(log10(n)) - We process half the digits
**Space Complexity:** O(1) - Only using a few integer variables

```python
def isPalindrome(self, x: int) -> bool:
    # Negative numbers are not palindromes
    # Numbers ending in 0 (except 0 itself) are not palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_half = 0
    while x > reversed_half:
        # Build reversed number from the right half
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

    # For even length: x == reversed_half
    # For odd length: x == reversed_half // 10 (ignore middle digit)
    return x == reversed_half or x == reversed_half // 10
```

**Why this works:**
Instead of reversing the entire number (which could overflow), we only reverse the second half and compare it with the first half. We stop when the reversed number becomes >= the remaining original number.

## Key Insights

1. Negative numbers are never palindromes (the minus sign)
2. Numbers ending in 0 (except 0 itself) cannot be palindromes
3. We only need to reverse half the number to check palindrome property
4. For odd-length numbers, we can ignore the middle digit (reversed // 10)
5. Avoids string conversion for O(1) space solution

## Common Mistakes

- Not handling negative numbers
- Not handling numbers ending in 0
- Integer overflow when reversing the entire number

## Related Problems

- Reverse Integer
- Palindrome Linked List
