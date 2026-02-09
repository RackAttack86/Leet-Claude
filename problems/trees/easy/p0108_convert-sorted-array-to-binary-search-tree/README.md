# Problem 108: Convert Sorted Array to Binary Search Tree

**Difficulty:** Easy
**Pattern:** Trees
**Link:** [LeetCode](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

## Problem Description

Given an integer array `nums` where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

## Constraints

- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- `nums` is sorted in a strictly increasing order.

## Examples

Example 1:
```
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:
```

Example 2:
```
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
```

## Approaches

### 1. Divide and Conquer (Recursive Binary Search)

**Time Complexity:** O(n) - visit each element once to create a node
**Space Complexity:** O(log n) - recursion stack depth for balanced tree

```python
def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    def buildBST(left: int, right: int) -> Optional[TreeNode]:
        if left > right:
            return None

        # Choose middle element as root (left middle for even length)
        mid = (left + right) // 2

        # Create root node with middle element
        root = TreeNode(nums[mid])

        # Recursively build left and right subtrees
        root.left = buildBST(left, mid - 1)
        root.right = buildBST(mid + 1, right)

        return root

    return buildBST(0, len(nums) - 1)
```

**Why this works:**

- Choose the middle element as the root to ensure height balance
- Recursively build left subtree from left half of array
- Recursively build right subtree from right half of array
- This guarantees the tree is height-balanced since we always split evenly

## Key Insights

- Middle element as root ensures balanced tree (equal nodes on both sides)
- Sorted array property means left half < root < right half (BST property)
- Using indices avoids creating new arrays (space efficient)

## Common Mistakes

- Not choosing the middle element as root (results in unbalanced tree)
- Off-by-one errors in the recursive indices

## Related Problems

- 109 - Convert Sorted List to Binary Search Tree
- 1382 - Balance a Binary Search Tree
