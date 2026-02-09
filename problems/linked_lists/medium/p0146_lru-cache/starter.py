"""
LeetCode Problem #146: LRU Cache
Difficulty: Medium
Pattern: Linked Lists
Link: https://leetcode.com/problems/lru-cache/

Problem:
--------
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the `LRUCache` class:

- `LRUCache(int capacity)` Initialize the LRU cache with positive size `capacity`.

- `int get(int key)` Return the value of the `key` if the key exists, otherwise return `-1`.

- `void put(int key, int value)` Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, evict the least recently used key.

The functions `get` and `put` must each run in `O(1)` average time complexity.

Constraints:
-----------
- of a Least Recently Used (LRU) cache.

Examples:
---------
Example 1:
```

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

```
"""

from typing import List, Optional
from collections import Counter, defaultdict


class DLLNode:
    """Doubly Linked List Node for LRU Cache."""
    def __init__(self, key: int = 0, val: int = 0):
        pass

class LRUCache:
    """
    Solution to LeetCode Problem #146: LRU Cache

    Approach: Hash Map + Doubly Linked List
    - Hash map provides O(1) access to any node by key
    - Doubly linked list maintains order of usage (most recent at head, least recent at tail)
    - On access (get/put), move the node to the head of the list
    - On capacity overflow, remove from the tail (least recently used)

    Time Complexity: O(1) for both get and put operations
    Space Complexity: O(capacity) for storing the cache entries

    Key Insights:
    - Doubly linked list allows O(1) removal from any position (unlike singly linked list)
    - Sentinel/dummy head and tail nodes simplify edge case handling
    - Storing key in node allows us to remove from hash map when evicting
    - Moving to head on every access naturally maintains LRU order
    """
    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with the given capacity.
        """
        pass

    def _add_to_head(self, node: DLLNode) -> None:
        """Add a node right after the head (most recently used position)."""
        pass

    def _remove_node(self, node: DLLNode) -> None:
        """Remove a node from the doubly linked list."""
        pass

    def _move_to_head(self, node: DLLNode) -> None:
        """Move an existing node to the head (mark as most recently used)."""
        pass

    def _pop_tail(self) -> DLLNode:
        """Remove and return the least recently used node (before tail)."""
        pass

    def get(self, key: int) -> int:
        """
        Get the value of the key if it exists, otherwise return -1.
        """
        pass

    def put(self, key: int, value: int) -> None:
        """
        Update or insert a key-value pair.
        Evict LRU entry if capacity is exceeded.
        """
        pass



PROBLEM_METADATA = {
    "number": 146,
    "name": "LRU Cache",
    "difficulty": "Medium",
    "pattern": "Linked Lists",
    "topics": ['Hash Table', 'Linked List', 'Design', 'Doubly-Linked List'],
    "url": "https://leetcode.com/problems/lru-cache/",
    "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple", "Bloomberg", "Oracle", "Uber", "LinkedIn", "Snapchat", "Twitter"],
    "time_complexity": "O(1)",
    "space_complexity": "O(capacity)",
}