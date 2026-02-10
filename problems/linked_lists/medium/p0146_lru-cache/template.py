from typing import List, Optional
from collections import Counter, defaultdict

class DLLNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = DLLNode()
        self.tail = DLLNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    def _add_to_head(self, node):
        pass
    def _remove_node(self, node):
        pass
    def _move_to_head(self, node):
        pass
    def _pop_tail(self):
        pass
    def get(self, key):
        pass
    def put(self, key, value):
        pass
