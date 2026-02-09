# Problem 2: Add Two Numbers

**Difficulty:** Medium
**Pattern:** Linked Lists
**Link:** [LeetCode](https://leetcode.com/problems/add-two-numbers/)

## Problem Description

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

## Constraints

- The number of nodes in each linked list is in the range `[1, 100]`.
- It is guaranteed that the list represents a number that does not have leading zeros.

## Examples

Example 1:
```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

Example 2:
```
Input: l1 = [0], l2 = [0]
Output: [0]
```

Example 3:
```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

## Approaches

### 1. Elementary Math with Carry

**Time Complexity:** O(max(m, n))
**Space Complexity:** O(max(m, n))

```python
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        # Get values from current nodes, or 0 if the list is exhausted
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # Calculate sum and carry
        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10

        # Create new node with the digit
        current.next = ListNode(digit)
        current = current.next

        # Move to next nodes if they exist
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next
```

**Why this works:**
- Traverse both lists simultaneously, adding corresponding digits along with any carry
- Use a dummy head node to simplify result list construction
- Handle lists of different lengths by treating missing nodes as 0
- Don't forget to handle the final carry if it exists

## Key Insights

- Digits are stored in reverse order, which naturally aligns with addition from least significant digit
- Using a dummy head simplifies edge cases and eliminates special handling for the first node
- The carry can only be 0 or 1 since max sum is 9 + 9 + 1 = 19

## Common Mistakes

- Forgetting to handle the final carry
- Not handling lists of different lengths
- Creating a cycle in the result list

## Related Problems

- Multiply Strings
- Add Binary
