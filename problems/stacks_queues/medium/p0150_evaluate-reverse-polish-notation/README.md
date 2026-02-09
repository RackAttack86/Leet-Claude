# Problem 150: Evaluate Reverse Polish Notation

**Difficulty:** Medium
**Pattern:** Stacks Queues
**Link:** [LeetCode](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

## Problem Description

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
- The valid operators are '+', '-', '*', and '/'
- Each operand may be an integer or another expression
- The division between two integers always truncates toward zero
- There will not be any division by zero
- The input represents a valid arithmetic expression in a reverse polish notation
- The answer and all the intermediate calculations can be represented in a 32-bit integer

### Constraints

- 1 <= tokens.length <= 10^4
- tokens[i] is either an operator: '+', '-', '*', or '/', or an integer in the range [-200, 200]

### Examples

**Example 1:**
```
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```

**Example 2:**
```
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```

## Approaches

### 1. Stack

**Time Complexity:** O(n)
**Space Complexity:** O(n)

```python
def evalRPN(self, tokens: List[str]) -> int:
    stack = []
    operators = {'+', '-', '*', '/'}

    for token in tokens:
        if token in operators:
            # Pop two operands (order matters for - and /)
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            else:  # token == '/'
                # Truncate toward zero
                result = int(a / b)

            stack.append(result)
        else:
            # It's a number
            stack.append(int(token))

    return stack[0]
```

**Why this works:**

Reverse Polish Notation (RPN) is naturally evaluated using a stack. When we encounter a number, we push it onto the stack. When we encounter an operator, we pop two operands, apply the operator, and push the result back. The final result is the only element left on the stack.

## Key Insights

- Push numbers to stack
- Pop two operands for operators
- Push result back to stack
- Final stack element is answer

## Common Mistakes

- Getting operand order wrong for subtraction and division (b is popped first, but a - b, not b - a)
- Not truncating division toward zero correctly in Python (use int(a/b), not a//b)
- Not handling negative numbers

## Related Problems

- Basic Calculator
- Basic Calculator II

## Tags

Array, Math, Stack
