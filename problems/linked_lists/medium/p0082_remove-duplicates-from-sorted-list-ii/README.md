# Problem 82: Remove Duplicates from Sorted List II

**Difficulty:** Medium
**Pattern:** Linked Lists
**Link:** [LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)

## Problem Description

Given the `head` of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

## Constraints

- The number of nodes in the list is in the range `[0, 300]`.
- -100 <= Node.val <= 100
- The list is guaranteed to be sorted in ascending order.

## Examples

Example 1:
```
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
```

Example 2:
```
Input: head = [1,1,1,2,3]
Output: [2,3]
```

## Approaches

### 1. Two Pointers with Dummy Node

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # Handle edge cases
    if not head or not head.next:
        return head

    # Create dummy node to handle edge case where head is a duplicate
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy  # prev points to the last node we're sure is not a duplicate

    current = head

    while current:
        # Check if current starts a sequence of duplicates
        if current.next and current.val == current.next.val:
            # Skip all nodes with the same value
            while current.next and current.val == current.next.val:
                current = current.next
            # Skip the last duplicate as well
            prev.next = current.next
        else:
            # No duplicate, move prev forward
            prev = prev.next

        # Move to the next node
        current = current.next

    return dummy.next
```

**Why this works:**
- Use a dummy node to handle edge cases where head needs to be removed
- Maintain a 'prev' pointer that points to the last confirmed unique node
- When duplicates are detected, skip all nodes with that value
- When a unique value is found, link it to prev and move prev forward

## Key Insights

- The list is sorted, so all duplicates are consecutive
- Using a dummy node handles the case when the first few nodes are duplicates
- We need to track the node BEFORE a potential duplicate sequence to properly relink
- When we find duplicates, we skip the entire group, not just the duplicates

## Common Mistakes

- Not skipping ALL duplicates (including the first one)
- Not using a dummy node (makes head removal complex)
- Moving prev forward when duplicates are found

## Related Problems

- Remove Duplicates from Sorted List
- Remove Duplicates from Sorted Array II
