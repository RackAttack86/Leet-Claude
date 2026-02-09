# Problem 21: Merge Two Sorted Lists

**Difficulty:** Easy
**Pattern:** Linked Lists
**Link:** [LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/)

## Problem Description

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

## Constraints

- The number of nodes in both lists is in the range [0, 50]
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order

## Examples

Example 1:
```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

Example 2:
```
Input: list1 = [], list2 = []
Output: []
```

Example 3:
```
Input: list1 = [], list2 = [0]
Output: [0]
```

## Approaches

### 1. Two Pointers Merge

**Time Complexity:** O(m + n)
**Space Complexity:** O(1)

```python
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    current = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    current.next = list1 if list1 else list2
    return dummy.next
```

**Why this works:**
- Use a dummy node to simplify handling the head of the result list
- Compare values from both lists and link the smaller node
- Handle remaining nodes in either list at the end

## Key Insights

- Use dummy node to simplify
- Compare values and link smaller node
- Handle remaining nodes in either list
- Classic merge pattern

## Common Mistakes

- Forgetting to handle the remaining nodes after one list is exhausted
- Not using a dummy node (makes handling the head more complex)

## Related Problems

- Merge k Sorted Lists
- Sort List

## Tags

Linked List, Recursion
