# Problem 92: Reverse Linked List II

**Difficulty:** Medium
**Pattern:** Linked Lists
**Link:** [LeetCode](https://leetcode.com/problems/reverse-linked-list-ii/)

## Problem Description

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

## Constraints

- The number of nodes in the list is n
- 1 <= n <= 500
- -500 <= Node.val <= 500
- 1 <= left <= right <= n

## Examples

Example 1:
```
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
```

Example 2:
```
Input: head = [5], left = 1, right = 1
Output: [5]
```

## Approaches

### 1. Iterative Reversal with Markers

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if not head or left == right:
        return head

    # Create dummy node to handle edge case of reversing from head
    dummy = ListNode(0, head)

    # Move to node before the left position
    prev = dummy
    for _ in range(left - 1):
        prev = prev.next

    # Start reversing from left position
    current = prev.next

    # Reverse (right - left) connections
    for _ in range(right - left):
        # Node to be moved
        next_node = current.next
        # Skip over next_node
        current.next = next_node.next
        # Insert next_node after prev
        next_node.next = prev.next
        prev.next = next_node

    return dummy.next
```

**Why this works:**
- Find the node before the left position
- Reverse nodes between left and right by repeatedly moving the next node to after prev
- Reconnect the reversed portion with the rest of the list
- Use dummy node to handle edge case of reversing from head

## Key Insights

- Find node before left position
- Reverse nodes between left and right
- Reconnect reversed portion
- Use dummy node for edge cases

## Common Mistakes

- Off-by-one errors in position counting
- Not handling the case when left == 1 (reversing from head)
- Losing track of connection points

## Related Problems

- Reverse Linked List
- Reverse Nodes in k-Group

## Tags

Linked List
