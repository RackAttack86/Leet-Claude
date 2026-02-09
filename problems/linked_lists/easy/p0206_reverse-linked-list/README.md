# Problem 206: Reverse Linked List

**Difficulty:** Easy
**Pattern:** Linked Lists
**Link:** [LeetCode](https://leetcode.com/problems/reverse-linked-list/)

## Problem Description

Given the head of a singly linked list, reverse the list, and return the reversed list.

## Constraints

- The number of nodes in the list is the range [0, 5000]
- -5000 <= Node.val <= 5000

## Examples

Example 1:
```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

Example 2:
```
Input: head = [1,2]
Output: [2,1]
```

Example 3:
```
Input: head = []
Output: []
```

## Approaches

### 1. Iterative with Three Pointers

**Time Complexity:** O(n)
**Space Complexity:** O(1) for iterative, O(n) for recursive

```python
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev
```

**Why this works:**
- Use prev, curr, next pointers to reverse links one by one
- Save the next node before reversing the current link
- Move all pointers forward after each reversal
- prev ends up pointing to the new head

## Key Insights

- Use prev, curr, next pointers
- Reverse links one by one
- Can also solve recursively
- Classic linked list problem

## Common Mistakes

- Losing reference to the next node before reversing
- Returning head instead of prev (new head)

## Related Problems

- Reverse Linked List II
- Palindrome Linked List

## Tags

Linked List, Recursion
