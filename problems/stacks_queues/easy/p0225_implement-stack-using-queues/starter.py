"""
LeetCode Problem #225: Implement Stack using Queues
Difficulty: Easy
Pattern: Stacks Queues
Link: https://leetcode.com/problems/implement-stack-using-queues/

Problem:
--------
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Constraints:
-----------
- 1 <= x <= 9
- At most 100 calls will be made to push, pop, top, and empty
- All the calls to pop and top are valid

Examples:
---------
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
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #225: Implement Stack using Queues

    Approach: Single queue or two queues
    Time Complexity: O(n) for push, O(1) for others
    Space Complexity: O(n)

    Key Insights:
    - Use one queue, rotate on push
    - Or use two queues, transfer on pop
    - Make push expensive or pop expensive
    - Queue as underlying structure
    """
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



PROBLEM_METADATA = {
    "number": 225,
    "name": "Implement Stack using Queues",
    "difficulty": "Easy",
    "pattern": "Stacks Queues",
    "topics": ['Stack', 'Design', 'Queue'],
    "url": "https://leetcode.com/problems/implement-stack-using-queues/",
    "companies": ['Amazon', 'Microsoft', 'Bloomberg'],
    "time_complexity": "O(n) for push, O(1) for others",
    "space_complexity": "O(n)",
}