# Problem 297: Serialize and Deserialize Binary Tree

**Difficulty:** Hard
**Pattern:** Trees
**Link:** [LeetCode](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

## Problem Description

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

## Constraints

- The number of nodes in the tree is in the range [0, 10^4]
- -1000 <= Node.val <= 1000

## Examples

Example 1:
```
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
```

Example 2:
```
Input: root = []
Output: []
```

## Approaches

### 1. BFS Level Order Traversal

**Time Complexity:** O(n) for both serialize and deserialize
**Space Complexity:** O(n)

```python
class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        if not root:
            return ""

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")

        return ",".join(result)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        if not data:
            return None

        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = deque([root])
        i = 1

        while queue and i < len(values):
            node = queue.popleft()

            if i < len(values) and values[i] != "null":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1

            if i < len(values) and values[i] != "null":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1

        return root
```

**Why this works:**

- Use level-order (BFS) traversal to serialize the tree
- Encode null nodes explicitly with "null" marker
- Use delimiter (comma) to separate values
- Deserialize by processing values in order, using queue to track parent nodes

## Key Insights

- Use preorder DFS or level-order BFS
- Encode null nodes explicitly
- Use delimiter to separate values
- Deserialize using queue or recursion

## Common Mistakes

- Not encoding null nodes (leads to ambiguous serialization)
- Not handling empty tree case
- Off-by-one errors when deserializing

## Related Problems

- 449 - Serialize and Deserialize BST
- 428 - Serialize and Deserialize N-ary Tree
- 331 - Verify Preorder Serialization of a Binary Tree

## Tags

String, Tree, Depth-First Search, Breadth-First Search, Design, Binary Tree
