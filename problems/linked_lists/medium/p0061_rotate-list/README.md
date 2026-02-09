# Problem 61: Rotate List

**Difficulty:** Medium
**Pattern:** Linked Lists
**Link:** [LeetCode](https://leetcode.com/problems/rotate-list/)

## Problem Description

Given the `head` of a linked list, rotate the list to the right by `k` places.

## Constraints

- The number of nodes in the list is in the range `[0, 500]`.
- -100 <= Node.val <= 100

## Examples

Example 1:
```
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
```

Example 2:
```
Input: head = [0,1,2], k = 4
Output: [2,0,1]
```

## Approaches

### 1. Close the Circle and Break at New Head

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    # Handle edge cases
    if not head or not head.next or k == 0:
        return head

    # Step 1: Find the length and the tail
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    # Step 2: Calculate effective rotation
    k = k % length
    if k == 0:
        return head  # No rotation needed

    # Step 3: Connect tail to head (make it circular)
    tail.next = head

    # Step 4: Find the new tail (length - k steps from head)
    steps_to_new_tail = length - k
    new_tail = head
    for _ in range(steps_to_new_tail - 1):
        new_tail = new_tail.next

    # Step 5: Break the circle
    new_head = new_tail.next
    new_tail.next = None

    return new_head
```

**Why this works:**
- First, compute the length of the list and connect tail to head (making it circular)
- Calculate effective rotation: k % length (to handle k > length)
- Find the new tail position: (length - k % length) steps from the original head
- Break the circle at this point to get the rotated list

## Key Insights

- Rotating right by k is equivalent to moving the last k nodes to the front
- k can be larger than list length, so we use k % length
- Making the list circular simplifies the rotation logic
- The new head is at position (length - k % length) from original head

## Common Mistakes

- Not handling k > length (should use k % length)
- Off-by-one error when finding new tail
- Forgetting to break the circle after rotation

## Related Problems

- Rotate Array
- Reverse Linked List
