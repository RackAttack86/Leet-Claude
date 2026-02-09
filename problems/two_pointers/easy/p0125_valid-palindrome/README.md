# Problem 125: Valid Palindrome

**Difficulty:** Easy
**Pattern:** Two Pointers
**Link:** [LeetCode](https://leetcode.com/problems/valid-palindrome/)

## Problem Description

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

## Constraints

- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters

## Examples

Example 1:
```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

Example 2:
```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```

Example 3:
```
Input: s = " "
Output: true
Explanation: After removing non-alphanumeric characters, s is an empty string.
Since an empty string reads the same forward and backward, it is a palindrome.
```

## Approaches

### 1. Two Pointers (Optimal)

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    l = 0
    r = len(s) - 1
    while l < r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        elif s[l] != s[r]:
            return False
        else:
            l += 1
            r -= 1
    return True
```

**Why this works:**
Use two pointers starting from both ends. Skip non-alphanumeric characters. Compare characters in lowercase. No need to create a filtered string (saves space).

## Key Insights

- Use two pointers starting from both ends
- Skip non-alphanumeric characters
- Compare characters in lowercase
- No need to create a filtered string (saves space)

## Common Mistakes

- Creating a new filtered string (uses O(n) space)
- Not handling non-alphanumeric characters correctly
- Case sensitivity issues

## Related Problems

- Valid Palindrome II
- Palindrome Linked List

## Tags

String, Two Pointers
