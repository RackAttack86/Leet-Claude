# Problem 117: Populating Next Right Pointers in Each Node II

**Difficulty:** Medium
**Pattern:** Trees
**Link:** [LeetCode](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)

## Problem Description

Given a binary tree:

```
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `NULL`.

Initially, all next pointers are set to `NULL`.

## Constraints

- The number of nodes in the tree is in the range `[0, 6000]`.
- -100 <= Node.val <= 100

## Examples

Example 1:
```
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
```

Example 2:
```
Input: root = []
Output: []
```

## Approaches

### 1. O(1) Space Using Previously Established Next Pointers

**Time Complexity:** O(n) - visit each node once
**Space Complexity:** O(1) - only use constant extra space

```python
def connect(self, root: 'Node') -> 'Node':
    if not root:
        return None

    # Start with the root level
    leftmost = root

    while leftmost:
        # Dummy node to track the start of the next level
        dummy = Node(0)
        current_child = dummy

        # Traverse current level
        current = leftmost
        while current:
            # Process left child
            if current.left:
                current_child.next = current.left
                current_child = current_child.next

            # Process right child
            if current.right:
                current_child.next = current.right
                current_child = current_child.next

            # Move to next node on current level
            current = current.next

        # Move to the next level (first node connected to dummy)
        leftmost = dummy.next

    return root
```

**Why this works:**

- Use the next pointers from the current level to traverse and connect the next level
- Use a dummy node to track the start of each new level
- Current level's next pointers help us traverse without a queue

## Key Insights

- Previous level's next pointers act as a linked list for traversal
- Use dummy node to simplify finding the leftmost node of next level
- Unlike problem 116, tree may not be perfect - handle missing children
- Process level by level using established next pointers from above level

## Common Mistakes

- Using O(n) space with BFS queue
- Not handling missing children in non-perfect binary tree

## Related Problems

- 116 - Populating Next Right Pointers in Each Node
- 102 - Binary Tree Level Order Traversal
