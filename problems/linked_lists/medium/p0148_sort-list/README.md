# Problem 148: Sort List

**Difficulty:** Medium
**Pattern:** Linked Lists
**Link:** [LeetCode](https://leetcode.com/problems/sort-list/)

## Problem Description

Given the `head` of a linked list, return the list after sorting it in ascending order.

## Constraints

- The number of nodes in the list is in the range `[0, 5 * 10^4]`.
- -10^5 <= Node.val <= 10^5

## Examples

Example 1:
```
Input: head = [4,2,1,3]
Output: [1,2,3,4]
```

Example 2:
```
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
```

Example 3:
```
Input: head = []
Output: []
```

## Approaches

### 1. Merge Sort (Top-Down)

**Time Complexity:** O(n log n)
**Space Complexity:** O(log n) for recursion stack

```python
def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # Base case: empty list or single node
    if not head or not head.next:
        return head

    # Split the list into two halves
    mid = self._getMid(head)
    left = head
    right = mid.next
    mid.next = None  # Break the list

    # Recursively sort both halves
    left = self.sortList(left)
    right = self.sortList(right)

    # Merge the sorted halves
    return self._merge(left, right)

def _getMid(self, head: ListNode) -> ListNode:
    slow = head
    fast = head.next  # Start fast one ahead to get left middle for even length

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def _merge(self, left: ListNode, right: ListNode) -> ListNode:
    dummy = ListNode(0)
    current = dummy

    while left and right:
        if left.val <= right.val:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next
        current = current.next

    current.next = left if left else right
    return dummy.next
```

**Why this works:**
- Use merge sort which is optimal for linked lists
- Find middle using slow/fast pointers
- Recursively sort left and right halves
- Merge the sorted halves

## Key Insights

- Merge sort is ideal for linked lists (no random access needed, no shifting elements)
- Quick sort is less efficient for linked lists due to lack of random access
- Finding middle with slow/fast pointers is a classic linked list technique
- When splitting, we must break the list by setting mid.next = None

## Common Mistakes

- Not breaking the list when splitting (causes infinite recursion)
- Off-by-one error when finding middle (use fast = head.next for left middle)
- Not handling empty list or single node base cases

## Related Problems

- Merge Two Sorted Lists
- Sort Colors

## Tags

Linked List, Two Pointers, Divide and Conquer, Sorting, Merge Sort
