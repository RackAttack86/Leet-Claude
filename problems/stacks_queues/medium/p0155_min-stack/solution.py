"""
LeetCode Problem #155: Min Stack
Difficulty: Medium
Pattern: Stacks Queues
Link: https://leetcode.com/problems/min-stack/

Problem:
--------
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement the MinStack class:
- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Constraints:
-----------
- -2^31 <= val <= 2^31 - 1
- Methods pop, top and getMin operations will always be called on non-empty stacks
- At most 3 * 10^4 calls will be made to push, pop, top, and getMin

Examples:
---------
Example 1:
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
"""

from typing import List, Optional


class MinStack:
    """
    Solution to LeetCode Problem #155: Min Stack

    Approach: Stack with pairs storing (value, current_min)
    Time Complexity: O(1) for all operations
    Space Complexity: O(n)

    Key Insights:
    - Store (value, current_min) pairs
    - Each element knows the minimum at that point
    - Update min on push by comparing with previous min
    """

    def __init__(self):
        """
        Initialize the stack.
        Each element stores (value, min_so_far).
        """
        self.stack = []

    def push(self, val: int) -> None:
        """
        Push element onto stack with current minimum.
        """
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_min = min(val, self.stack[-1][1])
            self.stack.append((val, current_min))

    def pop(self) -> None:
        """
        Remove the top element from stack.
        """
        self.stack.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.stack[-1][0]

    def getMin(self) -> int:
        """
        Retrieve the minimum element in O(1).
        """
        return self.stack[-1][1]


class Solution:
    """
    Wrapper class for compatibility with test framework.
    """
    pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 155,
    "name": "Min Stack",
    "difficulty": "Medium",
    "pattern": "Stacks Queues",
    "topics": ["Stack", "Design"],
    "url": "https://leetcode.com/problems/min-stack/",
    "companies": ["Amazon", "Microsoft", "Bloomberg", "Apple", "Google", "Facebook"],
    "time_complexity": "O(1)",
    "space_complexity": "O(n)",
}
