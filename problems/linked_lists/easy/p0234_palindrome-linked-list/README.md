# Problem 234: Palindrome Linked List

**Difficulty:** Easy
**Pattern:** Linked Lists
**Link:** [LeetCode](https://leetcode.com/problems/palindrome-linked-list/)

## Problem Description

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

## Constraints

- The number of nodes in the list is in the range [1, 10^5]
- 0 <= Node.val <= 9

## Examples

Example 1:
```
Input: head = [1,2,2,1]
Output: true
```

Example 2:
```
Input: head = [1,2]
Output: false
```

## Approaches

### 1. Find Middle, Reverse Second Half, Compare

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def isPalindrome(self, head: Optional[ListNode]) -> bool:
    if not head or not head.next:
        return True

    # Find middle using slow/fast pointers
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    second_half = slow.next
    prev = None
    while second_half:
        next_node = second_half.next
        second_half.next = prev
        prev = second_half
        second_half = next_node

    # Compare first and reversed second half
    first_half = head
    second_half = prev
    while second_half:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True
```

**Why this works:**
- Find the middle of the list using slow/fast pointers
- Reverse the second half of the list
- Compare the first half with the reversed second half
- If all values match, it's a palindrome

## Key Insights

- Find middle using slow/fast pointers
- Reverse second half
- Compare first and second halves
- Can restore list after checking

## Common Mistakes

- Not handling odd vs even length lists properly
- Off-by-one error when finding middle
- Not restoring the list if required

## Related Problems

- Reverse Linked List
- Palindrome Number

## Tags

Linked List, Two Pointers, Stack, Recursion
