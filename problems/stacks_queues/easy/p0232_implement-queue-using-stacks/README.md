# Problem 232: Implement Queue using Stacks

**Difficulty:** Easy
**Pattern:** Stacks Queues
**Link:** [LeetCode](https://leetcode.com/problems/implement-queue-using-stacks/)

## Problem Description

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

### Constraints

- 1 <= x <= 9
- At most 100 calls will be made to push, pop, peek, and empty
- All the calls to pop and peek are valid

### Examples

```
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
```

## Approaches

### 1. Two Stacks (Input and Output)

**Time Complexity:** O(1) amortized for all operations
**Space Complexity:** O(n)

```python
class MyQueue:
    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        self.input_stack.append(x)

    def pop(self) -> int:
        self._transfer()
        return self.output_stack.pop()

    def peek(self) -> int:
        self._transfer()
        return self.output_stack[-1]

    def empty(self) -> bool:
        return len(self.input_stack) == 0 and len(self.output_stack) == 0

    def _transfer(self) -> None:
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
```

**Why this works:**

We use two stacks: input_stack for push operations and output_stack for pop/peek operations. When we need to pop or peek and output_stack is empty, we transfer all elements from input_stack to output_stack. This reverses the order, putting the oldest element on top. Each element is moved at most twice (once to each stack), giving O(1) amortized time.

## Key Insights

- Use input stack for push
- Use output stack for pop/peek
- Transfer when output empty
- Amortized O(1) time

## Common Mistakes

- Transferring elements on every pop instead of only when output is empty
- Not checking both stacks for empty()
- Not understanding amortized analysis

## Related Problems

- Implement Stack using Queues
- Min Stack

## Tags

Stack, Design, Queue
