# Problem 146: LRU Cache

**Difficulty:** Medium
**Pattern:** Linked Lists
**Link:** [LeetCode](https://leetcode.com/problems/lru-cache/)

## Problem Description

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the `LRUCache` class:

- `LRUCache(int capacity)` Initialize the LRU cache with positive size `capacity`.

- `int get(int key)` Return the value of the `key` if the key exists, otherwise return `-1`.

- `void put(int key, int value)` Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, evict the least recently used key.

The functions `get` and `put` must each run in `O(1)` average time complexity.

## Constraints

- 1 <= capacity <= 3000
- 0 <= key <= 10^4
- 0 <= value <= 10^5
- At most 2 * 10^5 calls will be made to get and put.

## Examples

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

## Approaches

### 1. Hash Map + Doubly Linked List

**Time Complexity:** O(1) for both get and put
**Space Complexity:** O(capacity)

```python
class DLLNode:
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> DLLNode
        self.head = DLLNode()  # Most recently used
        self.tail = DLLNode()  # Least recently used
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_to_head(self, node: DLLNode) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: DLLNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_head(self, node: DLLNode) -> None:
        self._remove_node(node)
        self._add_to_head(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._move_to_head(node)
        else:
            new_node = DLLNode(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
            if len(self.cache) > self.capacity:
                lru_node = self.tail.prev
                self._remove_node(lru_node)
                del self.cache[lru_node.key]
```

**Why this works:**
- Hash map provides O(1) access to any node by key
- Doubly linked list maintains order of usage (most recent at head, least recent at tail)
- On access (get/put), move the node to the head of the list
- On capacity overflow, remove from the tail (least recently used)

## Key Insights

- Doubly linked list allows O(1) removal from any position (unlike singly linked list)
- Sentinel/dummy head and tail nodes simplify edge case handling
- Storing key in node allows us to remove from hash map when evicting
- Moving to head on every access naturally maintains LRU order

## Common Mistakes

- Using singly linked list (can't remove in O(1))
- Forgetting to update hash map when evicting
- Not storing key in node (can't find key to delete from hash map)

## Related Problems

- LFU Cache
- Design HashMap
