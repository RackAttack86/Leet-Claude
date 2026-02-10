from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._push_left_nodes(root)
    def _push_left_nodes(self, node):
        pass
    def next(self):
        pass
    def hasNext(self):
        pass
