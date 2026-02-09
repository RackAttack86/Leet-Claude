# Problem 141: Linked List Cycle

**Difficulty:** Easy
**Pattern:** Linked Lists
**Link:** [LeetCode](https://leetcode.com/problems/linked-list-cycle/)

## Problem Description

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

## Constraints

- The number of the nodes in the list is in the range [0, 10^4]
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked-list

## Examples

Example 1:
```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

Example 2:
```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```

Example 3:
```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

## Approaches

### 1. Floyd's Cycle Detection (Tortoise and Hare)

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def hasCycle(self, head: Optional[ListNode]) -> bool:
    if not head or not head.next:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False
```

**Why this works:**
- Use fast and slow pointers where fast moves 2 steps and slow moves 1 step
- If there is a cycle, the fast pointer will eventually catch up to the slow pointer
- If there is no cycle, the fast pointer will reach the end

## Key Insights

- Use fast and slow pointers
- Fast moves 2 steps, slow moves 1 step
- If cycle exists, they will meet
- Classic tortoise and hare algorithm

## Common Mistakes

- Not checking if fast.next exists before accessing fast.next.next
- Comparing node values instead of node references

## Related Problems

- Linked List Cycle II (find start of cycle)
- Happy Number (uses similar concept)

## Tags

Hash Table, Linked List, Two Pointers
