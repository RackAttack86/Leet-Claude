"""
LeetCode Problem #2: Add Two Numbers
Difficulty: Medium
Pattern: Linked Lists
Link: https://leetcode.com/problems/add-two-numbers/

Problem:
--------
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Constraints:
-----------
- The number of nodes in each linked list is in the range `[1, 100]`.
- It is guaranteed that the list represents a number that does not have leading zeros.

Examples:
---------
Example 1:
```

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

```

Example 2:
```

Input: l1 = [0], l2 = [0]
Output: [0]

```

Example 3:
```

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

```
"""

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        pass

class Node:
    def __init__(self, val=0, neighbors=None):
        pass

class Solution:
    """
    Solution to LeetCode Problem #2: Add Two Numbers

    Approach: Elementary Math with Carry
    - Traverse both lists simultaneously, adding corresponding digits along with any carry
    - Use a dummy head node to simplify result list construction
    - Handle lists of different lengths by treating missing nodes as 0
    - Don't forget to handle the final carry if it exists

    Time Complexity: O(max(m, n)) where m and n are the lengths of the two lists
    Space Complexity: O(max(m, n)) for the result list (O(1) auxiliary space)

    Key Insights:
    - Digits are stored in reverse order, which naturally aligns with addition from least significant digit
    - Using a dummy head simplifies edge cases and eliminates special handling for the first node
    - The carry can only be 0 or 1 since max sum is 9 + 9 + 1 = 19
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Add two numbers represented as linked lists with digits in reverse order.
        """
        pass



PROBLEM_METADATA = {
    "number": 2,
    "name": "Add Two Numbers",
    "difficulty": "Medium",
    "pattern": "Linked Lists",
    "topics": ['Linked List', 'Math', 'Recursion'],
    "url": "https://leetcode.com/problems/add-two-numbers/",
    "companies": ["Amazon", "Microsoft", "Google", "Facebook", "Apple", "Bloomberg", "Adobe", "Uber"],
    "time_complexity": "O(max(m, n))",
    "space_complexity": "O(max(m, n))",
}