# Problem 20: Valid Parentheses

**Difficulty:** Easy
**Pattern:** Stacks Queues
**Link:** [LeetCode](https://leetcode.com/problems/valid-parentheses/)

## Problem Description

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if
the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

### Constraints

- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'

### Examples

**Example 1:**
```
Input: s = "()"
Output: true
```

**Example 2:**
```
Input: s = "()[]{}"
Output: true
```

**Example 3:**
```
Input: s = "(]"
Output: false
```

## Approaches

### 1. Stack

**Time Complexity:** O(n)
**Space Complexity:** O(n)

```python
def isValid(self, s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            # Closing bracket
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            # Opening bracket
            stack.append(char)

    return len(stack) == 0
```

**Why this works:**

We use a stack to keep track of opening brackets. When we encounter an opening bracket, we push it onto the stack. When we encounter a closing bracket, we check if the top of the stack contains the matching opening bracket. If it does, we pop it; if not, the string is invalid. At the end, the stack must be empty for a valid string.

## Key Insights

- Push opening brackets to stack
- Pop and match with closing brackets
- Stack must be empty at end
- Classic stack application

## Common Mistakes

- Forgetting to check if stack is empty before popping
- Not checking that the stack is empty at the end
- Using a queue instead of a stack

## Related Problems

- Generate Parentheses
- Longest Valid Parentheses

## Tags

String, Stack
