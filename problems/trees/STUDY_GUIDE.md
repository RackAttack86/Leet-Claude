# Trees Pattern - Study Guide

## Overview
A Tree is a hierarchical data structure consisting of nodes connected by edges. Each tree has a root node, and every node has zero or more child nodes. Trees are fundamental to many algorithms and are used to represent hierarchical relationships.

## Tree Terminology

- **Root**: The topmost node with no parent
- **Parent**: A node that has children
- **Child**: A node with a parent
- **Leaf**: A node with no children
- **Siblings**: Nodes with the same parent
- **Ancestor**: A node's parent, grandparent, etc.
- **Descendant**: A node's child, grandchild, etc.
- **Depth**: Distance from root to node
- **Height**: Distance from node to deepest leaf
- **Level**: All nodes at the same depth

## Binary Tree Definition

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Creating a simple tree:
#       1
#      / \
#     2   3
#    / \
#   4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
```

## Tree Traversal Methods

### 1. Depth-First Search (DFS)

**Inorder Traversal (Left -> Root -> Right):**
```python
def inorder_recursive(root):
    """Inorder: Left, Root, Right"""
    result = []

    def traverse(node):
        if not node:
            return
        traverse(node.left)
        result.append(node.val)
        traverse(node.right)

    traverse(root)
    return result

# Time: O(n), Space: O(h) where h is height


def inorder_iterative(root):
    """Iterative inorder using stack"""
    result = []
    stack = []
    current = root

    while current or stack:
        # Go to leftmost node
        while current:
            stack.append(current)
            current = current.left

        # Process node
        current = stack.pop()
        result.append(current.val)

        # Move to right subtree
        current = current.right

    return result

# Time: O(n), Space: O(h)
# For BST, inorder gives sorted order
```

**Preorder Traversal (Root -> Left -> Right):**
```python
def preorder_recursive(root):
    """Preorder: Root, Left, Right"""
    result = []

    def traverse(node):
        if not node:
            return
        result.append(node.val)
        traverse(node.left)
        traverse(node.right)

    traverse(root)
    return result

# Time: O(n), Space: O(h)


def preorder_iterative(root):
    """Iterative preorder using stack"""
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)

        # Push right first so left is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result

# Time: O(n), Space: O(h)
# Used for: copying tree, prefix expressions
```

**Postorder Traversal (Left -> Right -> Root):**
```python
def postorder_recursive(root):
    """Postorder: Left, Right, Root"""
    result = []

    def traverse(node):
        if not node:
            return
        traverse(node.left)
        traverse(node.right)
        result.append(node.val)

    traverse(root)
    return result

# Time: O(n), Space: O(h)


def postorder_iterative(root):
    """Iterative postorder using two stacks"""
    if not root:
        return []

    result = []
    stack1 = [root]
    stack2 = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    # stack2 has reverse postorder
    return [node.val for node in reversed(stack2)]

# Time: O(n), Space: O(h)
# Used for: deleting tree, postfix expressions
```

### 2. Breadth-First Search (Level Order)

```python
def level_order(root):
    """Level order traversal using queue"""
    if not root:
        return []

    from collections import deque

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result

# Time: O(n), Space: O(w) where w is max width
# Example:     1
#            /   \
#           2     3
#          / \   /
#         4   5 6
# Output: [[1], [2,3], [4,5,6]]
```

## Common Tree Patterns

### 1. Tree Properties and Measurements

**Calculate Tree Height:**
```python
def max_depth(root):
    """Calculate maximum depth/height of tree"""
    if not root:
        return 0

    left_height = max_depth(root.left)
    right_height = max_depth(root.right)

    return 1 + max(left_height, right_height)

# Time: O(n), Space: O(h)
```

**Calculate Tree Diameter:**
```python
def diameter_of_binary_tree(root):
    """Longest path between any two nodes"""
    diameter = 0

    def height(node):
        nonlocal diameter
        if not node:
            return 0

        left = height(node.left)
        right = height(node.right)

        # Update diameter (path through this node)
        diameter = max(diameter, left + right)

        return 1 + max(left, right)

    height(root)
    return diameter

# Time: O(n), Space: O(h)
```

**Check if Balanced:**
```python
def is_balanced(root):
    """Check if tree is height-balanced (heights differ by at most 1)"""
    def check_height(node):
        if not node:
            return 0

        left_height = check_height(node.left)
        if left_height == -1:
            return -1

        right_height = check_height(node.right)
        if right_height == -1:
            return -1

        # Check if current node is balanced
        if abs(left_height - right_height) > 1:
            return -1

        return 1 + max(left_height, right_height)

    return check_height(root) != -1

# Time: O(n), Space: O(h)
```

**Count Nodes:**
```python
def count_nodes(root):
    """Count total number of nodes"""
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

# Time: O(n), Space: O(h)


def count_nodes_complete_tree(root):
    """Optimized count for complete binary tree"""
    if not root:
        return 0

    def get_height(node, go_left):
        height = 0
        while node:
            height += 1
            node = node.left if go_left else node.right
        return height

    left_height = get_height(root, True)
    right_height = get_height(root, False)

    # If heights are same, tree is perfect
    if left_height == right_height:
        return (1 << left_height) - 1  # 2^h - 1

    # Otherwise, count recursively
    return 1 + count_nodes_complete_tree(root.left) + count_nodes_complete_tree(root.right)

# Time: O(log²n), Space: O(log n)
```

### 2. Tree Comparison and Validation

**Same Tree:**
```python
def is_same_tree(p, q):
    """Check if two trees are identical"""
    if not p and not q:
        return True
    if not p or not q:
        return False

    return (p.val == q.val and
            is_same_tree(p.left, q.left) and
            is_same_tree(p.right, q.right))

# Time: O(n), Space: O(h)
```

**Symmetric Tree:**
```python
def is_symmetric(root):
    """Check if tree is mirror of itself"""
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False

        return (left.val == right.val and
                is_mirror(left.left, right.right) and
                is_mirror(left.right, right.left))

    return is_mirror(root, root) if root else True

# Time: O(n), Space: O(h)
```

**Subtree Check:**
```python
def is_subtree(root, subRoot):
    """Check if subRoot is subtree of root"""
    if not root:
        return False

    if is_same_tree(root, subRoot):
        return True

    return (is_subtree(root.left, subRoot) or
            is_subtree(root.right, subRoot))

# Time: O(m*n) where m, n are tree sizes, Space: O(h)
```

### 3. Path Problems

**Path Sum:**
```python
def has_path_sum(root, target_sum):
    """Check if root-to-leaf path sums to target"""
    if not root:
        return False

    # Leaf node
    if not root.left and not root.right:
        return root.val == target_sum

    remaining = target_sum - root.val
    return (has_path_sum(root.left, remaining) or
            has_path_sum(root.right, remaining))

# Time: O(n), Space: O(h)
```

**All Root-to-Leaf Paths:**
```python
def binary_tree_paths(root):
    """Return all root-to-leaf paths"""
    if not root:
        return []

    paths = []

    def dfs(node, path):
        if not node.left and not node.right:
            paths.append(path + str(node.val))
            return

        path += str(node.val) + "->"

        if node.left:
            dfs(node.left, path)
        if node.right:
            dfs(node.right, path)

    dfs(root, "")
    return paths

# Time: O(n), Space: O(h)
# Example: [1,2,3,null,5] -> ["1->2->5", "1->3"]
```

**Maximum Path Sum:**
```python
def max_path_sum(root):
    """Find maximum path sum (path can start and end anywhere)"""
    max_sum = float('-inf')

    def max_gain(node):
        nonlocal max_sum
        if not node:
            return 0

        # Max sum extending to left and right
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)

        # Path through current node
        current_max = node.val + left_gain + right_gain

        max_sum = max(max_sum, current_max)

        # Return max sum extending through this node
        return node.val + max(left_gain, right_gain)

    max_gain(root)
    return max_sum

# Time: O(n), Space: O(h)
```

### 4. Lowest Common Ancestor (LCA)

```python
def lowest_common_ancestor(root, p, q):
    """Find LCA of two nodes in binary tree"""
    if not root or root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    # Both found in different subtrees
    if left and right:
        return root

    # Return whichever is not None
    return left if left else right

# Time: O(n), Space: O(h)
```

**LCA in BST:**
```python
def lca_bst(root, p, q):
    """LCA in Binary Search Tree (more efficient)"""
    while root:
        # Both in left subtree
        if p.val < root.val and q.val < root.val:
            root = root.left
        # Both in right subtree
        elif p.val > root.val and q.val > root.val:
            root = root.right
        # Split or one matches root
        else:
            return root

    return None

# Time: O(h), Space: O(1)
```

### 5. Tree Construction

**Build from Inorder and Preorder:**
```python
def build_tree_pre_in(preorder, inorder):
    """Build tree from preorder and inorder traversals"""
    if not preorder or not inorder:
        return None

    # First element in preorder is root
    root_val = preorder[0]
    root = TreeNode(root_val)

    # Find root in inorder to split left and right
    mid = inorder.index(root_val)

    # Recursively build subtrees
    root.left = build_tree_pre_in(preorder[1:mid+1], inorder[:mid])
    root.right = build_tree_pre_in(preorder[mid+1:], inorder[mid+1:])

    return root

# Time: O(n²) due to list slicing, Space: O(n)
# Can optimize to O(n) using indices instead of slicing
```

**Build from Inorder and Postorder:**
```python
def build_tree_post_in(inorder, postorder):
    """Build tree from inorder and postorder traversals"""
    if not inorder or not postorder:
        return None

    # Last element in postorder is root
    root_val = postorder[-1]
    root = TreeNode(root_val)

    # Find root in inorder
    mid = inorder.index(root_val)

    # Recursively build subtrees
    root.left = build_tree_post_in(inorder[:mid], postorder[:mid])
    root.right = build_tree_post_in(inorder[mid+1:], postorder[mid:-1])

    return root

# Time: O(n²), Space: O(n)
```

### 6. Binary Search Tree (BST) Operations

**Validate BST:**
```python
def is_valid_bst(root):
    """Check if tree is valid BST"""
    def validate(node, min_val, max_val):
        if not node:
            return True

        if node.val <= min_val or node.val >= max_val:
            return False

        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))

    return validate(root, float('-inf'), float('inf'))

# Time: O(n), Space: O(h)
```

**BST Search:**
```python
def search_bst(root, val):
    """Search for value in BST"""
    while root:
        if val == root.val:
            return root
        elif val < root.val:
            root = root.left
        else:
            root = root.right

    return None

# Time: O(h), Space: O(1)
```

**BST Insert:**
```python
def insert_into_bst(root, val):
    """Insert value into BST"""
    if not root:
        return TreeNode(val)

    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)

    return root

# Time: O(h), Space: O(h) for recursion


def insert_into_bst_iterative(root, val):
    """Iterative BST insert"""
    if not root:
        return TreeNode(val)

    current = root
    while True:
        if val < current.val:
            if not current.left:
                current.left = TreeNode(val)
                break
            current = current.left
        else:
            if not current.right:
                current.right = TreeNode(val)
                break
            current = current.right

    return root

# Time: O(h), Space: O(1)
```

**BST Delete:**
```python
def delete_node(root, key):
    """Delete node from BST"""
    if not root:
        return None

    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        # Node to delete found
        # Case 1: No children or one child
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        # Case 2: Two children
        # Find inorder successor (smallest in right subtree)
        min_node = root.right
        while min_node.left:
            min_node = min_node.left

        # Replace value with successor
        root.val = min_node.val

        # Delete successor
        root.right = delete_node(root.right, min_node.val)

    return root

# Time: O(h), Space: O(h)
```

**Kth Smallest in BST:**
```python
def kth_smallest(root, k):
    """Find kth smallest element in BST"""
    stack = []
    current = root

    while True:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        k -= 1

        if k == 0:
            return current.val

        current = current.right

# Time: O(h + k), Space: O(h)
```

### 7. Tree Modification

**Invert/Mirror Tree:**
```python
def invert_tree(root):
    """Invert binary tree (mirror)"""
    if not root:
        return None

    # Swap children
    root.left, root.right = root.right, root.left

    # Recursively invert subtrees
    invert_tree(root.left)
    invert_tree(root.right)

    return root

# Time: O(n), Space: O(h)
```

**Flatten to Linked List:**
```python
def flatten(root):
    """Flatten tree to linked list (preorder)"""
    if not root:
        return

    # Flatten subtrees
    flatten(root.left)
    flatten(root.right)

    # Save right subtree
    right = root.right

    # Move left subtree to right
    root.right = root.left
    root.left = None

    # Attach original right subtree
    current = root
    while current.right:
        current = current.right
    current.right = right

# Time: O(n), Space: O(h)
```

**Convert BST to Greater Tree:**
```python
def convert_bst(root):
    """Convert BST where each node value = node + all greater nodes"""
    total = 0

    def reverse_inorder(node):
        nonlocal total
        if not node:
            return

        # Process right subtree first (larger values)
        reverse_inorder(node.right)

        # Update current node
        total += node.val
        node.val = total

        # Process left subtree
        reverse_inorder(node.left)

    reverse_inorder(root)
    return root

# Time: O(n), Space: O(h)
```

### 8. Serialization and Deserialization

```python
def serialize(root):
    """Serialize tree to string"""
    def encode(node):
        if not node:
            return "null,"

        return str(node.val) + "," + encode(node.left) + encode(node.right)

    return encode(root)


def deserialize(data):
    """Deserialize string to tree"""
    def decode(values):
        val = next(values)

        if val == "null":
            return None

        node = TreeNode(int(val))
        node.left = decode(values)
        node.right = decode(values)

        return node

    values = iter(data.split(","))
    return decode(values)

# Time: O(n), Space: O(n)
```

## Advanced Tree Patterns

### Morris Traversal (Space O(1))
```python
def morris_inorder(root):
    """Inorder traversal with O(1) space using threading"""
    current = root
    result = []

    while current:
        if not current.left:
            result.append(current.val)
            current = current.right
        else:
            # Find inorder predecessor
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right

            if not predecessor.right:
                # Create thread
                predecessor.right = current
                current = current.left
            else:
                # Remove thread
                predecessor.right = None
                result.append(current.val)
                current = current.right

    return result

# Time: O(n), Space: O(1) not counting output
```

## Problem-Solving Strategy

1. **Choose Traversal Method:**
   - Inorder for BST (sorted order)
   - Preorder for copying/serialization
   - Postorder for deletion/bottom-up
   - Level order for level-wise processing

2. **Recursion vs Iteration:**
   - Recursion: Cleaner code, implicit stack
   - Iteration: More control, explicit stack

3. **Consider Helper Functions:**
   - Pass additional parameters (depth, min, max)
   - Use nonlocal variables for accumulation

4. **Handle Edge Cases:**
   - Empty tree (None)
   - Single node
   - Skewed tree (like linked list)
   - Complete vs incomplete trees

## Time and Space Complexity

### Common Operations:
- **Traversal:** O(n) time, O(h) space
- **Search in BST:** O(h) time, O(1) space iterative
- **Insert/Delete in BST:** O(h) time
- **Level order:** O(n) time, O(w) space where w is max width

### Height Analysis:
- **Balanced tree:** h = O(log n)
- **Skewed tree:** h = O(n)

## Practice Tips

1. **Master recursion:** Essential for tree problems
2. **Understand base cases:** Empty node, leaf node
3. **Practice both traversals:** Recursive and iterative
4. **Draw trees:** Visualize operations on paper
5. **Test edge cases:** Empty, single node, skewed
6. **Learn BST properties:** Leverage ordering for efficiency

## Common Mistakes to Avoid

1. **Not handling None nodes:** Always check before accessing
2. **Wrong base case:** Check both None and leaf conditions
3. **Incorrect return values:** Ensure you return what's expected
4. **Modifying tree unintentionally:** Be careful with references
5. **Forgetting to update references:** Especially in insertion/deletion

## Related Patterns

- **DFS/BFS:** Core traversal techniques
- **Backtracking:** For path problems
- **Dynamic Programming:** For optimization on trees
- **Divide and Conquer:** Natural fit for tree structure
