# Problem 143: Reorder List

**Difficulty:** Medium
**Pattern:** Linked Lists
**Link:** [LeetCode](https://leetcode.com/problems/reorder-list/)

## Problem Description

You are given the head of a singly linked-list. The list can be represented as:

L0 -> L1 -> ... -> Ln - 1 -> Ln

Reorder the list to be on the following form:

L0 -> Ln -> L1 -> Ln - 1 -> L2 -> Ln - 2 -> ...

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

## Constraints

- The number of nodes in the list is in the range [1, 5 * 10^4]
- 1 <= Node.val <= 1000

## Examples

Example 1:
```
Input: head = [1,2,3,4]
Output: [1,4,2,3]
```

Example 2:
```
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
```

## Approaches

### 1. Find Middle, Reverse Second Half, Merge

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def reorderList(self, head: Optional[ListNode]) -> None:
    if not head or not head.next:
        return

    # Step 1: Find middle using slow/fast pointers
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse second half starting from slow.next
    second = slow.next
    slow.next = None  # Cut the list in half

    prev = None
    while second:
        next_node = second.next
        second.next = prev
        prev = second
        second = next_node
    second = prev  # prev is now head of reversed second half

    # Step 3: Merge two halves alternately
    first = head
    while second:
        # Save next pointers
        first_next = first.next
        second_next = second.next

        # Interleave
        first.next = second
        second.next = first_next

        # Move to next pair
        first = first_next
        second = second_next
```

**Why this works:**
Three-step approach:
1. Find middle of list using slow/fast pointers
2. Reverse second half
3. Merge two halves alternately

## Key Insights

- Find middle using slow/fast pointers
- Reverse second half of list
- Merge two halves alternately
- Three-step approach

## Common Mistakes

- Off-by-one error when finding middle
- Forgetting to cut the list in half before reversing
- Not handling the merge correctly for odd/even length lists

## Related Problems

- Reverse Linked List
- Palindrome Linked List

## Tags

Linked List, Two Pointers, Stack, Recursion
