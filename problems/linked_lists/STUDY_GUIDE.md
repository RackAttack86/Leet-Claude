# Linked Lists Pattern - Study Guide

## Overview
A Linked List is a linear data structure where elements are stored in nodes. Each node contains data and a reference (pointer) to the next node. Unlike arrays, linked lists don't require contiguous memory and allow efficient insertion/deletion at any position.

## Types of Linked Lists

### 1. Singly Linked List
Each node points to the next node.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Creating a linked list: 1 -> 2 -> 3 -> None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
```

### 2. Doubly Linked List
Each node points to both next and previous nodes.

```python
class DoublyListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

# Creating doubly linked list: None <- 1 <-> 2 <-> 3 -> None
head = DoublyListNode(1)
second = DoublyListNode(2, prev=head)
third = DoublyListNode(3, prev=second)
head.next = second
second.next = third
```

### 3. Circular Linked List
Last node points back to the first node (or any previous node).

```python
# Creating circular linked list: 1 -> 2 -> 3 -> (back to 1)
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = head  # Makes it circular
```

## Basic Operations

### Traversal
```python
def traverse(head):
    """Visit all nodes in linked list"""
    current = head

    while current:
        print(current.val)  # Process node
        current = current.next

# Time: O(n), Space: O(1)
```

### Search
```python
def search(head, target):
    """Find node with target value"""
    current = head

    while current:
        if current.val == target:
            return current
        current = current.next

    return None  # Not found

# Time: O(n), Space: O(1)
```

### Insert at Beginning
```python
def insert_at_beginning(head, val):
    """Insert new node at the beginning"""
    new_node = ListNode(val)
    new_node.next = head
    return new_node  # New head

# Time: O(1), Space: O(1)
```

### Insert at End
```python
def insert_at_end(head, val):
    """Insert new node at the end"""
    new_node = ListNode(val)

    if not head:
        return new_node

    # Find last node
    current = head
    while current.next:
        current = current.next

    current.next = new_node
    return head

# Time: O(n), Space: O(1)
```

### Insert After Node
```python
def insert_after(node, val):
    """Insert new node after given node"""
    if not node:
        return

    new_node = ListNode(val)
    new_node.next = node.next
    node.next = new_node

# Time: O(1), Space: O(1)
```

### Delete Node by Value
```python
def delete_node(head, target):
    """Delete first node with target value"""
    # Handle deletion of head
    if head and head.val == target:
        return head.next

    # Find node before target
    current = head
    while current and current.next:
        if current.next.val == target:
            current.next = current.next.next
            return head
        current = current.next

    return head

# Time: O(n), Space: O(1)
```

## Common Patterns and Techniques

### 1. Dummy Head/Sentinel Node
Use a dummy node to simplify edge cases (empty list, deleting head).

```python
def remove_elements(head, val):
    """Remove all nodes with given value using dummy head"""
    dummy = ListNode(0)
    dummy.next = head
    current = dummy

    while current.next:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next

    return dummy.next

# Time: O(n), Space: O(1)
# Example: 1->2->6->3->4->5->6, val=6 -> 1->2->3->4->5
```

```python
def merge_two_sorted_lists(l1, l2):
    """Merge two sorted linked lists using dummy head"""
    dummy = ListNode(0)
    current = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # Attach remaining nodes
    current.next = l1 if l1 else l2

    return dummy.next

# Time: O(n + m), Space: O(1)
```

### 2. Two Pointers (Fast and Slow)
Use two pointers moving at different speeds to solve various problems.

**Find Middle of Linked List:**
```python
def find_middle(head):
    """Find middle node (slow-fast pointer technique)"""
    if not head:
        return None

    slow = fast = head

    # Fast moves 2 steps, slow moves 1 step
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow  # Slow is at middle when fast reaches end

# Time: O(n), Space: O(1)
# Example: 1->2->3->4->5 -> returns node with value 3
# Example: 1->2->3->4 -> returns node with value 3 (second middle)
```

**Detect Cycle (Floyd's Algorithm):**
```python
def has_cycle(head):
    """Detect if linked list has a cycle"""
    if not head or not head.next:
        return False

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True  # Cycle detected

    return False  # No cycle

# Time: O(n), Space: O(1)
```

**Find Cycle Start:**
```python
def detect_cycle_start(head):
    """Find the node where cycle begins"""
    if not head or not head.next:
        return None

    # Detect if cycle exists
    slow = fast = head
    has_cycle = False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            has_cycle = True
            break

    if not has_cycle:
        return None

    # Find cycle start: move slow to head, keep fast at meeting point
    # Move both one step at a time until they meet
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow  # Cycle start node

# Time: O(n), Space: O(1)
```

**Find Nth Node from End:**
```python
def nth_from_end(head, n):
    """Find nth node from the end"""
    if not head:
        return None

    # Move fast pointer n steps ahead
    fast = head
    for _ in range(n):
        if not fast:
            return None  # List shorter than n
        fast = fast.next

    # Move both pointers until fast reaches end
    slow = head
    while fast:
        slow = slow.next
        fast = fast.next

    return slow

# Time: O(n), Space: O(1)
# Example: 1->2->3->4->5, n=2 -> returns node with value 4
```

**Remove Nth Node from End:**
```python
def remove_nth_from_end(head, n):
    """Remove nth node from end of list"""
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy

    # Move fast n+1 steps ahead
    for _ in range(n + 1):
        if not fast:
            return head
        fast = fast.next

    # Move both until fast reaches end
    while fast:
        slow = slow.next
        fast = fast.next

    # Remove nth node from end
    slow.next = slow.next.next

    return dummy.next

# Time: O(n), Space: O(1)
```

### 3. Reversal Pattern
Reverse linked list or portions of it.

**Reverse Entire List (Iterative):**
```python
def reverse_list_iterative(head):
    """Reverse linked list iteratively"""
    prev = None
    current = head

    while current:
        next_node = current.next  # Save next
        current.next = prev       # Reverse link
        prev = current           # Move prev forward
        current = next_node      # Move current forward

    return prev  # New head

# Time: O(n), Space: O(1)
# Example: 1->2->3->4->5 -> 5->4->3->2->1
```

**Reverse List (Recursive):**
```python
def reverse_list_recursive(head):
    """Reverse linked list recursively"""
    # Base case: empty or single node
    if not head or not head.next:
        return head

    # Reverse rest of list
    new_head = reverse_list_recursive(head.next)

    # Reverse current link
    head.next.next = head
    head.next = None

    return new_head

# Time: O(n), Space: O(n) due to recursion stack
```

**Reverse Between Two Positions:**
```python
def reverse_between(head, left, right):
    """Reverse nodes from position left to right"""
    if not head or left == right:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    # Move prev to node before left position
    for _ in range(left - 1):
        prev = prev.next

    # Reverse from left to right
    current = prev.next
    for _ in range(right - left):
        next_node = current.next
        current.next = next_node.next
        next_node.next = prev.next
        prev.next = next_node

    return dummy.next

# Time: O(n), Space: O(1)
# Example: 1->2->3->4->5, left=2, right=4 -> 1->4->3->2->5
```

**Reverse in K-Groups:**
```python
def reverse_k_group(head, k):
    """Reverse nodes in k-groups"""
    # Count nodes
    count = 0
    current = head
    while current and count < k:
        current = current.next
        count += 1

    # If less than k nodes, return as is
    if count < k:
        return head

    # Reverse first k nodes
    prev = None
    current = head
    for _ in range(k):
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    # head is now tail of reversed group
    # Recursively reverse remaining groups
    if current:
        head.next = reverse_k_group(current, k)

    return prev  # New head of this group

# Time: O(n), Space: O(n/k) for recursion
# Example: 1->2->3->4->5, k=2 -> 2->1->4->3->5
# Example: 1->2->3->4->5, k=3 -> 3->2->1->4->5
```

### 4. Reordering Pattern

**Palindrome Check:**
```python
def is_palindrome(head):
    """Check if linked list is palindrome"""
    if not head or not head.next:
        return True

    # Find middle using slow-fast pointers
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    second_half = reverse_list_iterative(slow)

    # Compare first and second halves
    first_half = head
    while second_half:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True

# Time: O(n), Space: O(1)
```

**Reorder List (L0 -> Ln -> L1 -> Ln-1 ...):**
```python
def reorder_list(head):
    """Reorder list: L0→L1→...→Ln to L0→Ln→L1→Ln-1→..."""
    if not head or not head.next:
        return

    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    second = reverse_list_iterative(slow.next)
    slow.next = None  # Split list

    # Merge two halves
    first = head
    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2

# Time: O(n), Space: O(1)
# Example: 1->2->3->4 -> 1->4->2->3
# Example: 1->2->3->4->5 -> 1->5->2->4->3
```

### 5. Partitioning Pattern

**Partition List Around Value:**
```python
def partition(head, x):
    """Partition list so all nodes < x come before nodes >= x"""
    # Create two dummy heads for two partitions
    less_dummy = ListNode(0)
    greater_dummy = ListNode(0)

    less = less_dummy
    greater = greater_dummy

    current = head
    while current:
        if current.val < x:
            less.next = current
            less = less.next
        else:
            greater.next = current
            greater = greater.next
        current = current.next

    # Connect partitions
    greater.next = None  # Important: prevent cycles
    less.next = greater_dummy.next

    return less_dummy.next

# Time: O(n), Space: O(1)
# Example: 1->4->3->2->5->2, x=3 -> 1->2->2->4->3->5
```

**Odd-Even List:**
```python
def odd_even_list(head):
    """Group all odd indices together followed by even indices"""
    if not head or not head.next:
        return head

    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = even_head
    return head

# Time: O(n), Space: O(1)
# Example: 1->2->3->4->5 -> 1->3->5->2->4
```

### 6. Intersection and Union

**Find Intersection of Two Lists:**
```python
def get_intersection_node(headA, headB):
    """Find node where two lists intersect"""
    if not headA or not headB:
        return None

    # Calculate lengths
    lenA = lenB = 0
    currA, currB = headA, headB

    while currA:
        lenA += 1
        currA = currA.next

    while currB:
        lenB += 1
        currB = currB.next

    # Align starting points
    currA, currB = headA, headB
    if lenA > lenB:
        for _ in range(lenA - lenB):
            currA = currA.next
    else:
        for _ in range(lenB - lenA):
            currB = currB.next

    # Find intersection
    while currA and currB:
        if currA == currB:
            return currA
        currA = currA.next
        currB = currB.next

    return None

# Time: O(m + n), Space: O(1)


def get_intersection_elegant(headA, headB):
    """Elegant solution using two pointers"""
    if not headA or not headB:
        return None

    pA, pB = headA, headB

    # When reaching end, redirect to other list's head
    # They will meet at intersection or both reach None
    while pA != pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA

    return pA  # Intersection or None

# Time: O(m + n), Space: O(1)
```

### 7. Sorting Pattern

**Merge Sort for Linked List:**
```python
def sort_list(head):
    """Sort linked list using merge sort"""
    if not head or not head.next:
        return head

    # Find middle using slow-fast pointers
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Split list
    mid = slow.next
    slow.next = None

    # Recursively sort both halves
    left = sort_list(head)
    right = sort_list(mid)

    # Merge sorted halves
    return merge_two_sorted_lists(left, right)

# Time: O(n log n), Space: O(log n) for recursion
```

**Insertion Sort for Linked List:**
```python
def insertion_sort_list(head):
    """Sort linked list using insertion sort"""
    dummy = ListNode(0)
    current = head

    while current:
        # Find insertion position
        prev = dummy
        while prev.next and prev.next.val < current.val:
            prev = prev.next

        # Insert current node
        next_node = current.next
        current.next = prev.next
        prev.next = current
        current = next_node

    return dummy.next

# Time: O(n²), Space: O(1)
```

## Advanced Techniques

### 1. Copy List with Random Pointer
```python
class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copy_random_list(head):
    """Deep copy linked list with random pointers"""
    if not head:
        return None

    # Step 1: Create copy nodes interleaved with original
    current = head
    while current:
        copy = Node(current.val)
        copy.next = current.next
        current.next = copy
        current = copy.next

    # Step 2: Set random pointers for copied nodes
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next

    # Step 3: Separate lists
    dummy = Node(0)
    copy_prev = dummy
    current = head

    while current:
        copy = current.next
        copy_prev.next = copy
        copy_prev = copy

        current.next = copy.next
        current = current.next

    return dummy.next

# Time: O(n), Space: O(1) not counting output
```

### 2. Flatten Multilevel Doubly Linked List
```python
def flatten(head):
    """Flatten multilevel doubly linked list with child pointers"""
    if not head:
        return None

    dummy = Node(0)
    dummy.next = head

    stack = [head]
    prev = dummy

    while stack:
        current = stack.pop()

        prev.next = current
        current.prev = prev

        # Push next before child (to process child first)
        if current.next:
            stack.append(current.next)
        if current.child:
            stack.append(current.child)
            current.child = None  # Remove child pointer

        prev = current

    # Cleanup dummy connections
    dummy.next.prev = None
    return dummy.next

# Time: O(n), Space: O(n) for stack
```

### 3. Add Two Numbers Represented as Lists
```python
def add_two_numbers(l1, l2):
    """Add two numbers represented as linked lists (digits in reverse)"""
    dummy = ListNode(0)
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)

        current = current.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next

# Time: O(max(m, n)), Space: O(max(m, n))
# Example: (2->4->3) + (5->6->4) = (7->0->8) represents 342 + 465 = 807
```

## Problem-Solving Strategy

1. **Identify Pattern:**
   - Traversal/search: Simple iteration
   - Finding middle/cycle: Fast-slow pointers
   - Reversal: Three-pointer technique
   - Merging: Dummy head
   - Multiple operations: Break into steps

2. **Consider Using:**
   - Dummy head for edge cases
   - Two pointers for distance/speed problems
   - Recursion for divide-and-conquer
   - Hash map for O(1) lookups

3. **Handle Edge Cases:**
   - Empty list (head is None)
   - Single node
   - Two nodes
   - Circular list
   - Lists of different lengths

4. **Watch Out For:**
   - Null pointer access
   - Losing reference to head
   - Creating cycles unintentionally
   - Memory leaks in languages with manual memory management

## Time and Space Complexity

### Common Operations:
- **Access nth element:** O(n)
- **Search:** O(n)
- **Insert at beginning:** O(1)
- **Insert at end:** O(n) without tail pointer, O(1) with tail
- **Delete node:** O(n) to find, O(1) to delete
- **Reverse:** O(n) time, O(1) space iterative, O(n) space recursive

## Common Mistakes to Avoid

1. **Not handling None/null pointers:** Always check before accessing `.next` or `.val`
2. **Losing reference to head:** Save head before traversal if you need to return it
3. **Creating infinite loops:** Be careful when manipulating pointers
4. **Not using dummy head:** Makes code cleaner for edge cases
5. **Forgetting to update tail pointers:** When building new lists
6. **Off-by-one errors:** Especially in nth from end problems

## Practice Tips

1. **Draw it out:** Visualize pointer movements on paper
2. **Test edge cases:** Empty, single node, two nodes
3. **Use dummy heads:** Simplifies many problems
4. **Master reversal:** Fundamental technique used in many problems
5. **Understand fast-slow:** Versatile technique for many patterns
6. **Practice pointer manipulation:** Key skill for linked lists

## Related Patterns

- **Two Pointers:** Used extensively in linked list problems
- **Recursion:** Natural fit for linked list problems
- **Stack:** Can simulate recursion for iterative solutions
- **Hash Map:** For detecting cycles or finding intersections with O(n) space
