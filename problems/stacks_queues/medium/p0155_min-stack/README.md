# Problem 155: Min Stack

**Difficulty:** Medium
**Pattern:** Stacks Queues
**Link:** [LeetCode](https://leetcode.com/problems/min-stack/)

## Problem Description

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

### Constraints

- -2^31 <= val <= 2^31 - 1
- Methods pop, top and getMin operations will always be called on non-empty stacks
- At most 3 * 10^4 calls will be made to push, pop, top, and getMin

### Examples

```
Input:
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
Output:
[null,null,null,null,-3,null,0,-2]

Explanation:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

## Approaches

### 1. Stack with Pairs

**Time Complexity:** O(1) for all operations
**Space Complexity:** O(n)

```python
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_min = min(val, self.stack[-1][1])
            self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
```

**Why this works:**

We store pairs of (value, current_min) where current_min is the minimum value in the stack at the time this element was pushed. When we push a new element, we compute the new minimum as the smaller of the new value and the previous minimum. This way, getMin() always returns the minimum in O(1) by looking at the top of the stack.

## Key Insights

- Store (value, current_min) pairs
- Each element knows the minimum at that point
- Update min on push by comparing with previous min
- All operations are O(1)

## Common Mistakes

- Using a separate variable for min (doesn't work after pop)
- Scanning the entire stack to find min (not O(1))
- Not updating the min correctly on push

## Related Problems

- Implement Stack using Queues
- Implement Queue using Stacks
- Max Stack

## Tags

Stack, Design
