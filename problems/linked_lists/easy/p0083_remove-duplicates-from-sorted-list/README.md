# Problem 83: Remove Duplicates from Sorted List

**Difficulty:** Easy
**Pattern:** Linked Lists
**Link:** [LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

## Problem Description

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

## Constraints

- The number of nodes in the list is in the range [0, 300]
- -100 <= Node.val <= 100
- The list is guaranteed to be sorted in ascending order

## Examples

Example 1:
```
Input: head = [1,1,2]
Output: [1,2]
```

Example 2:
```
Input: head = [1,1,2,3,3]
Output: [1,2,3]
```

## Approaches

### 1. Single Pointer Traversal

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head
```

**Why this works:**
- Compare current node with next node
- If values are equal, skip the next node by updating the next pointer
- If values are different, move to the next node
- Continue until end of list

## Key Insights

- Compare current with next node
- Skip duplicates by updating next pointer
- Continue until end of list
- Simple one-pass solution

## Common Mistakes

- Moving to next node when deleting (should stay at current to check for more duplicates)
- Not handling empty list or single node cases

## Related Problems

- Remove Duplicates from Sorted List II
- Remove Duplicates from Sorted Array

## Tags

Linked List
