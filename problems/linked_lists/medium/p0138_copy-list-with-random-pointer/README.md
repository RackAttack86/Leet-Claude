# Problem 138: Copy List with Random Pointer

**Difficulty:** Medium
**Pattern:** Linked Lists
**Link:** [LeetCode](https://leetcode.com/problems/copy-list-with-random-pointer/)

## Problem Description

A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or `null`.

Construct a deep copy of the list. The deep copy should consist of exactly `n` brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the `next` and `random` pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes `X` and `Y` in the original list, where `X.random --> Y`, then for the corresponding two nodes `x` and `y` in the copied list, `x.random --> y`.

Return the head of the copied linked list.

## Constraints

- `0 <= n <= 1000`
- `-10^4 <= Node.val <= 10^4`
- `Node.random` is `null` or is pointing to some node in the linked list.

## Examples

Example 1:
```
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
```

Example 2:
```
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
```

Example 3:
```
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
```

## Approaches

### 1. Hash Map Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

```python
def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    if not head:
        return None

    # Dictionary to map original nodes to their copies
    old_to_new = {}

    # First pass: Create all new nodes
    current = head
    while current:
        old_to_new[current] = Node(current.val)
        current = current.next

    # Second pass: Set next and random pointers
    current = head
    while current:
        copy = old_to_new[current]
        copy.next = old_to_new.get(current.next)
        copy.random = old_to_new.get(current.random)
        current = current.next

    return old_to_new[head]
```

**Why this works:**
- First pass: Create all new nodes and store mapping from original to copy
- Second pass: Set next and random pointers using the mapping
- This handles the challenge that random pointers can point to any node, including nodes not yet created

## Key Insights

- The challenge is that random pointers can point to any node, including nodes not yet created
- Using a hash map allows us to create all nodes first, then link them
- The interweaving approach avoids extra space by temporarily modifying the structure
- We must handle null random pointers carefully

## Common Mistakes

- Trying to set random pointers before all nodes are created
- Not handling null random pointers
- Creating a shallow copy instead of a deep copy

## Related Problems

- Clone Graph
- Copy List with Random Pointer II
