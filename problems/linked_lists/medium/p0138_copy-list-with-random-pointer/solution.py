"""
LeetCode Problem #138: Copy List with Random Pointer
Difficulty: Medium
Pattern: Linked Lists
Link: https://leetcode.com/problems/copy-list-with-random-pointer/

Problem:
--------
A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or `null`.

Construct a deep copy of the list. The deep copy should consist of exactly `n` brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the `next` and `random` pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes `X` and `Y` in the original list, where `X.random --> Y`, then for the corresponding two nodes `x` and `y` in the copied list, `x.random --> y`.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of `n` nodes. Each node is represented as a pair of `[val, random_index]` where:

- `val`: an integer representing `Node.val`

- `random_index`: the index of the node (range from `0` to `n-1`) that the `random` pointer points to, or `null` if it does not point to any node.

Your code will only be given the `head` of the original linked list.

Constraints:
-----------
- `0
- 10^4
- Node.random` is `null` or is pointing to some node in the linked list.

Examples:
---------
Example 1:
```

Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

```

Example 2:
```

Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

```

Example 3:
```

Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

```
"""

from typing import List, Optional
from collections import Counter, defaultdict

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = x
        self.next = next
        self.random = random


class Solution:
    """
    Solution to LeetCode Problem #138: Copy List with Random Pointer

    Approach: Hash Map for O(n) Space, or Interweaving for O(1) Space

    Method 1 (Hash Map - implemented here):
    - First pass: Create all new nodes and store mapping from original to copy
    - Second pass: Set next and random pointers using the mapping

    Method 2 (Interweaving - O(1) space):
    - Interweave copied nodes with original: A -> A' -> B -> B' -> C -> C'
    - Set random pointers: copy.random = original.random.next
    - Separate the two lists

    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(n) for the hash map approach, O(1) for interweaving

    Key Insights:
    - The challenge is that random pointers can point to any node, including nodes not yet created
    - Using a hash map allows us to create all nodes first, then link them
    - The interweaving approach avoids extra space by temporarily modifying the structure
    - We must handle null random pointers carefully
    """

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Create a deep copy of a linked list with random pointers.
        Uses hash map approach for clarity.
        """
        if not head:
            return None

        # Dictionary to map original nodes to their copies
        old_to_new = {}

        # First pass: Create all new nodes
        current = head
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next

        # Second pass: Set next and random pointers
        current = head
        while current:
            copy = old_to_new[current]
            copy.next = old_to_new.get(current.next)
            copy.random = old_to_new.get(current.random)
            current = current.next

        return old_to_new[head]

    def copyRandomListO1Space(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Create a deep copy using O(1) extra space by interweaving nodes.
        """
        if not head:
            return None

        # Step 1: Create interweaved list
        # Original: A -> B -> C
        # After:    A -> A' -> B -> B' -> C -> C'
        current = head
        while current:
            copy = Node(current.val)
            copy.next = current.next
            current.next = copy
            current = copy.next

        # Step 2: Set random pointers for copied nodes
        current = head
        while current:
            copy = current.next
            if current.random:
                copy.random = current.random.next
            current = copy.next

        # Step 3: Separate the two lists
        current = head
        new_head = head.next
        while current:
            copy = current.next
            current.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            current = current.next

        return new_head


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 138,
    "name": "Copy List with Random Pointer",
    "difficulty": "Medium",
    "pattern": "Linked Lists",
    "topics": ['Hash Table', 'Linked List'],
    "url": "https://leetcode.com/problems/copy-list-with-random-pointer/",
    "companies": ["Amazon", "Microsoft", "Facebook", "Bloomberg", "Google", "Uber", "Apple"],
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
}
