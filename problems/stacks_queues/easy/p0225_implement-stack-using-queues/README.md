# Problem 225: Implement Stack using Queues

**Difficulty:** Easy
**Pattern:** Stacks Queues
**Link:** [LeetCode](https://leetcode.com/problems/implement-stack-using-queues/)

## Problem Description

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

### Constraints

- 1 <= x <= 9
- At most 100 calls will be made to push, pop, top, and empty
- All the calls to pop and top are valid

### Examples

```
Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
```

## Approaches

### 1. Single Queue with Rotation

**Time Complexity:** O(n) for push, O(1) for others
**Space Complexity:** O(n)

```python
from collections import deque

class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        # Rotate all elements except the one just added
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0
```

**Why this works:**

After each push, we rotate all existing elements behind the new element. This ensures the most recently added element is always at the front of the queue, simulating stack behavior. Pop and top are O(1) since the "top" of the stack is at the front of the queue.

## Key Insights

- Use one queue, rotate on push
- Or use two queues, transfer on pop
- Make push expensive or pop expensive
- Queue as underlying structure

## Common Mistakes

- Forgetting to rotate elements after push
- Using more than two queues
- Not understanding the tradeoff between push-heavy and pop-heavy implementations

## Related Problems

- Implement Queue using Stacks
- Min Stack

## Tags

Stack, Design, Queue
