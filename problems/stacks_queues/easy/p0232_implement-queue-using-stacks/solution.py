"""
LeetCode Problem #232: Implement Queue using Stacks
Difficulty: Easy
Pattern: Stacks Queues
Link: https://leetcode.com/problems/implement-queue-using-stacks/

Problem:
--------
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Constraints:
-----------
- 1 <= x <= 9
- At most 100 calls will be made to push, pop, peek, and empty
- All the calls to pop and peek are valid

Examples:
---------
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
"""

from typing import List, Optional


class MyQueue:
    """
    Solution to LeetCode Problem #232: Implement Queue using Stacks

    Approach: Two stacks: input and output
    Time Complexity: O(1) amortized for all operations
    Space Complexity: O(n)

    Key Insights:
    - Use input stack for push
    - Use output stack for pop/peek
    - Transfer when output empty
    - Amortized O(1) time
    """

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


# Alias for compatibility
Solution = MyQueue


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 232,
    "name": "Implement Queue using Stacks",
    "difficulty": "Easy",
    "pattern": "Stacks Queues",
    "topics": ['Stack', 'Design', 'Queue'],
    "url": "https://leetcode.com/problems/implement-queue-using-stacks/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google', 'Bloomberg'],
    "time_complexity": "O(1) amortized for all operations",
    "space_complexity": "O(n)",
}
