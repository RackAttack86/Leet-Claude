# Problem 224: Basic Calculator

**Difficulty:** Hard
**Pattern:** Stacks Queues
**Link:** [LeetCode](https://leetcode.com/problems/basic-calculator/)

## Problem Description

Given a string `s` representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as `eval()`.

## Constraints

- 1 <= s.length <= 3 * 10^5
- s consists of digits, '+', '-', '(', ')', and ' '.
- s represents a valid expression.
- '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
- '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
- There will be no two consecutive operators in the input.
- Every number and running calculation will fit in a signed 32-bit integer.

## Examples

**Example 1:**
```
Input: s = "1 + 1"
Output: 2
```

**Example 2:**
```
Input: s = " 2-1 + 2 "
Output: 3
```

**Example 3:**
```
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
```

## Approaches

### 1. Stack-based Evaluation with Sign Tracking

**Time Complexity:** O(n)
**Space Complexity:** O(n)

```python
def calculate(self, s: str) -> int:
    stack = []
    result = 0
    num = 0
    sign = 1  # 1 for positive, -1 for negative

    i = 0
    while i < len(s):
        char = s[i]

        if char.isdigit():
            # Build multi-digit number
            num = num * 10 + int(char)
        elif char == '+':
            # Add previous number with its sign, prepare for next
            result += sign * num
            num = 0
            sign = 1
        elif char == '-':
            # Add previous number with its sign, prepare for negative
            result += sign * num
            num = 0
            sign = -1
        elif char == '(':
            # Save current state and reset for sub-expression
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif char == ')':
            # Complete current sub-expression
            result += sign * num
            num = 0
            # Pop sign and previous result, combine
            result = stack.pop() * result  # Apply saved sign
            result += stack.pop()  # Add to saved result
        # Skip spaces

        i += 1

    # Don't forget the last number
    result += sign * num

    return result
```

**Why this works:**

We track a running result and current sign. When we encounter:
- Digits: Build the number
- '+' or '-': Add the previous number to result and update sign
- '(': Push current result and sign to stack, reset for sub-expression
- ')': Complete sub-expression, pop sign and previous result, combine them

The stack saves the state before each nested expression, allowing us to correctly handle any depth of parentheses.

## Key Insights

1. Only + and - operators, so we can track a running result with sign
2. Parentheses require saving state - use stack to store (result, sign)
3. Unary minus is handled by treating it as 0 - value
4. Spaces can be skipped during processing
5. The sign before a parenthesis affects the entire sub-expression

## Common Mistakes

- Forgetting to process the last number after the loop
- Not handling unary minus correctly
- Not saving both result and sign when entering parentheses
- Getting the order wrong when popping from the stack

## Related Problems

- Basic Calculator II
- Basic Calculator III
- Evaluate Reverse Polish Notation
