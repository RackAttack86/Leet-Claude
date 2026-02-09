# Problem 160: Intersection of Two Linked Lists

**Difficulty:** Easy
**Pattern:** Linked Lists
**Link:** [LeetCode](https://leetcode.com/problems/intersection-of-two-linked-lists/)

## Problem Description

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

## Constraints

- The number of nodes of listA is in the m
- The number of nodes of listB is in the n
- 1 <= m, n <= 3 * 10^4
- 1 <= Node.val <= 10^5
- 0 <= skipA < m
- 0 <= skipB < n

## Examples

Example 1:
```
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
```

Example 2:
```
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
```

## Approaches

### 1. Two Pointers with Length Alignment

**Time Complexity:** O(m + n)
**Space Complexity:** O(1)

```python
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    if not headA or not headB:
        return None

    pA = headA
    pB = headB

    while pA != pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA

    return pA
```

**Why this works:**
- Two pointers traverse both lists
- When reaching the end of one list, switch to the head of the other list
- This eliminates the length difference between the two lists
- They will meet at the intersection point or both become null

## Key Insights

- Two pointers traverse both lists
- When reaching end, switch to other list
- They will meet at intersection or null
- Clever pointer switching eliminates length difference

## Common Mistakes

- Comparing node values instead of node references
- Not handling the case when lists don't intersect

## Related Problems

- Linked List Cycle
- Merge Two Sorted Lists

## Tags

Hash Table, Linked List, Two Pointers
