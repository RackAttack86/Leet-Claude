# Problem 677: Map Sum Pairs

**Difficulty:** Medium
**Pattern:** Tries
**Link:** [LeetCode](https://leetcode.com/problems/map-sum-pairs/)

## Problem Description

Design a map that allows you to do the following:

- Maps a string key to a given value.
- Returns the sum of the values that have a key with a prefix equal to a given string.

Implement the MapSum class:

- `MapSum()` Initializes the MapSum object.
- `void insert(String key, int val)` Inserts the key-val pair into the map. If the key already existed, the original key-value pair will be overridden to the new one.
- `int sum(String prefix)` Returns the sum of all the pairs' value whose key starts with the prefix.

**Constraints:**
- 1 <= key.length, prefix.length <= 50
- key and prefix consist of only lowercase English letters
- 1 <= val <= 1000
- At most 50 calls will be made to insert and sum

**Example:**
```
Input
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
Output
[null, null, 3, null, 5]

Explanation
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);
mapSum.sum("ap");           // return 3 (apple = 3)
mapSum.insert("app", 2);
mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)
```

## Approaches

### 1. Trie with Cumulative Value Storage

**Time Complexity:** O(m) for both operations where m is key/prefix length
**Space Complexity:** O(n * m)

```python
class TrieNode:
    """Node in the Trie data structure."""
    def __init__(self):
        self.children = {}
        self.value = 0  # Sum of values of all keys that pass through this node


class MapSum:
    def __init__(self):
        """Initialize the MapSum object."""
        self.root = TrieNode()
        self.map = {}  # Store key -> value for handling updates

    def insert(self, key: str, val: int) -> None:
        """Insert the key-val pair into the map."""
        # Calculate the delta (difference from previous value if key exists)
        delta = val - self.map.get(key, 0)
        self.map[key] = val

        # Update the trie with the delta
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.value += delta

    def sum(self, prefix: str) -> int:
        """Return the sum of all pairs' values whose key starts with the prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.value
```

**Why this works:**
Each Trie node stores the cumulative sum of all values for keys that pass through it. When inserting, we calculate the delta (new value minus old value if key existed) and add this delta to every node along the path. This way, querying the sum for a prefix is O(m) - just traverse to the prefix node and return its stored value. The HashMap tracks previous values to correctly compute deltas for updates.

## Key Insights

- Store cumulative values along the path in Trie nodes
- Track previous values with HashMap to handle updates correctly
- When updating, adjust by delta (new - old) along the path
- Sum query is just traversing to prefix node and returning its value
- This approach avoids DFS traversal during sum queries

## Common Mistakes

- Not handling key updates correctly (need to track previous values)
- Using DFS for sum instead of storing cumulative values (less efficient)
- Forgetting to update all nodes along the path

## Related Problems

- 208 - Implement Trie
- 211 - Design Add and Search Words Data Structure
- 1804 - Implement Trie II

## Tags

Hash Table, String, Design, Trie
