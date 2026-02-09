"""
LeetCode Problem #61: Rotate List
Difficulty: Medium
Pattern: Linked Lists
Link: https://leetcode.com/problems/rotate-list/

Problem:
--------
Given the `head` of a linked list, rotate the list to the right by `k` places.

Constraints:
-----------
- The number of nodes in the list is in the range `[0, 500]`.
- 100

Examples:
---------
Example 1:
```

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

```

Example 2:
```

Input: head = [0,1,2], k = 4
Output: [2,0,1]

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
    Solution to LeetCode Problem #61: Rotate List

    Approach: Close the Circle and Break at New Head
    - First, compute the length of the list and connect tail to head (making it circular)
    - Calculate effective rotation: k % length (to handle k > length)
    - Find the new tail position: (length - k % length) steps from the original head
    - Break the circle at this point to get the rotated list

    Time Complexity: O(n) where n is the length of the list
    Space Complexity: O(1) - only using constant extra space

    Key Insights:
    - Rotating right by k is equivalent to moving the last k nodes to the front
    - k can be larger than list length, so we use k % length
    - Making the list circular simplifies the rotation logic
    - The new head is at position (length - k % length) from original head
    """
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Rotate the list to the right by k places.
        """
        pass



PROBLEM_METADATA = {
    "number": 61,
    "name": "Rotate List",
    "difficulty": "Medium",
    "pattern": "Linked Lists",
    "topics": ['Linked List', 'Two Pointers'],
    "url": "https://leetcode.com/problems/rotate-list/",
    "companies": ["Amazon", "Microsoft", "LinkedIn", "Facebook", "Bloomberg"],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}