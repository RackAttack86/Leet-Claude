# Problem 25: Reverse Nodes in k-Group

**Difficulty:** Hard
**Pattern:** Linked Lists
**Link:** [LeetCode](https://leetcode.com/problems/reverse-nodes-in-k-group/)

## Problem Description

Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return the modified list.

`k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

## Constraints

- The number of nodes in the list is `n`.
- 1 <= k <= n <= 5000
- 0 <= Node.val <= 1000

## Examples

Example 1:
```
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
```

Example 2:
```
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
```

## Approaches

### 1. Iterative Group Reversal

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or k == 1:
        return head

    # Dummy node to handle head changes
    dummy = ListNode(0)
    dummy.next = head
    group_prev = dummy  # Points to node before current group

    while True:
        # Check if there are k nodes remaining
        kth = self._getKth(group_prev, k)
        if not kth:
            break  # Less than k nodes remaining, leave as is

        group_next = kth.next  # Node after current group

        # Reverse the group
        prev = group_next
        curr = group_prev.next

        while curr != group_next:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # Connect the reversed group
        tmp = group_prev.next  # Old first node (now last)
        group_prev.next = kth  # Connect to new first node
        group_prev = tmp  # Move to end of current group

    return dummy.next

def _getKth(self, curr: ListNode, k: int) -> Optional[ListNode]:
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr
```

**Why this works:**
- Process the list in groups of k nodes
- For each group: check if there are k nodes, then reverse them
- Keep track of the previous group's tail to connect reversed groups
- If fewer than k nodes remain, leave them as is

## Key Insights

- Need to check if k nodes exist before reversing (don't reverse partial groups)
- After reversing a group, the first node becomes the last (new tail)
- Use a dummy node to handle the head changing
- Track group_prev (end of previous group) to connect groups together
- The original first node of a group becomes the connection point to next group

## Common Mistakes

- Reversing partial groups at the end
- Losing track of connection points between groups
- Off-by-one errors when counting k nodes
- Not using dummy node (head may change)

## Related Problems

- Reverse Linked List
- Reverse Linked List II
- Swap Nodes in Pairs

## Tags

Linked List, Recursion
