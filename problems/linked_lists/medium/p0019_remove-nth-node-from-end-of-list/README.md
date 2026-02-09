# Problem 19: Remove Nth Node From End of List

**Difficulty:** Medium
**Pattern:** Linked Lists
**Link:** [LeetCode](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

## Problem Description

Given the head of a linked list, remove the nth node from the end of the list and return its head.

## Constraints

- The number of nodes in the list is sz
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

## Examples

Example 1:
```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

Example 2:
```
Input: head = [1], n = 1
Output: []
```

## Approaches

### 1. Two Pointers with Gap of n

**Time Complexity:** O(L) where L is list length
**Space Complexity:** O(1)

```python
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # Create dummy node to handle edge case of removing head
    dummy = ListNode(0, head)
    slow = dummy
    fast = dummy

    # Move fast pointer n+1 steps ahead
    for _ in range(n + 1):
        fast = fast.next

    # Move both pointers until fast reaches end
    while fast:
        slow = slow.next
        fast = fast.next

    # Remove the nth node from end
    slow.next = slow.next.next

    return dummy.next
```

**Why this works:**
- Use two pointers with a gap of n nodes between them
- When fast pointer reaches the end, slow pointer is at the node before the target
- Uses a dummy node to handle edge case of removing the head

## Key Insights

- Use two pointers n steps apart
- Move both until fast reaches end
- Slow pointer will be at node before target
- Use dummy node to handle edge cases

## Common Mistakes

- Off-by-one error (should move fast n+1 steps, not n)
- Not handling the case when removing the head node
- Not using a dummy node

## Related Problems

- Reverse Linked List
- Middle of the Linked List

## Tags

Linked List, Two Pointers
