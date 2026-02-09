# Problem 86: Partition List

**Difficulty:** Medium
**Pattern:** Linked Lists
**Link:** [LeetCode](https://leetcode.com/problems/partition-list/)

## Problem Description

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

## Constraints

- The number of nodes in the list is in the range [0, 200]
- -100 <= Node.val <= 100
- -200 <= x <= 200

## Examples

Example 1:
```
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
```

Example 2:
```
Input: head = [2,1], x = 2
Output: [1,2]
```

## Approaches

### 1. Two Dummy Lists

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
    # Create dummy heads for two partitions
    less_dummy = ListNode(0)
    greater_dummy = ListNode(0)

    less = less_dummy
    greater = greater_dummy

    # Traverse and partition nodes
    current = head
    while current:
        if current.val < x:
            less.next = current
            less = less.next
        else:
            greater.next = current
            greater = greater.next
        current = current.next

    # Connect the two partitions
    greater.next = None  # Important: terminate greater list
    less.next = greater_dummy.next

    return less_dummy.next
```

**Why this works:**
- Create two separate lists: one for nodes less than x, one for nodes >= x
- Traverse the original list and append each node to the appropriate list
- Connect the less list to the greater list
- Important: terminate the greater list to avoid cycles

## Key Insights

- Create two separate lists: less and greater
- Traverse and append to appropriate list
- Connect less list to greater list
- Use dummy nodes for simplicity

## Common Mistakes

- Forgetting to terminate the greater list (causes cycle)
- Not preserving relative order within each partition

## Related Problems

- Sort Colors
- Odd Even Linked List

## Tags

Linked List, Two Pointers
