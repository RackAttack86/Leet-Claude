"""
Common data structures used in LeetCode problems
"""

from typing import Optional, List


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"

    @staticmethod
    def from_list(values: List[int]) -> Optional['ListNode']:
        """Create a linked list from a Python list"""
        if not values:
            return None

        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next

        return head

    def to_list(self) -> List[int]:
        """Convert linked list to Python list"""
        result = []
        current = self
        while current:
            result.append(current.val)
            current = current.next
        return result


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"

    @staticmethod
    def from_list(values: List[Optional[int]]) -> Optional['TreeNode']:
        """Create binary tree from level-order list (LeetCode format)"""
        if not values or values[0] is None:
            return None

        root = TreeNode(values[0])
        queue = [root]
        i = 1

        while queue and i < len(values):
            node = queue.pop(0)

            # Left child
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1

            # Right child
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1

        return root

    def to_list(self) -> List[Optional[int]]:
        """Convert binary tree to level-order list"""
        if not self:
            return []

        result = []
        queue = [self]

        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        # Remove trailing None values
        while result and result[-1] is None:
            result.pop()

        return result


class Node:
    """Definition for a graph/N-ary tree node."""

    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return f"Node({self.val})"
