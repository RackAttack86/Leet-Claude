# Problem 380: Insert Delete GetRandom O(1)

**Difficulty:** Medium
**Pattern:** Two Pointers
**Link:** [LeetCode](https://leetcode.com/problems/insert-delete-getrandom-o1/)

## Problem Description

Implement the `RandomizedSet` class:

- `RandomizedSet()` Initializes the `RandomizedSet` object.

- `bool insert(int val)` Inserts an item `val` into the set if not present. Returns `true` if the item was not present, `false` otherwise.

- `bool remove(int val)` Removes an item `val` from the set if present. Returns `true` if the item was present, `false` otherwise.

- `int getRandom()` Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average `O(1)` time complexity.

## Constraints

- `-2^31 <= val <= 2^31 - 1`
- At most `2 * 10^5` calls will be made to `insert`, `remove`, and `getRandom`.
- There will be at least one element in the data structure when `getRandom` is called.

## Examples

Example 1:
```

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

```

## Approaches

### 1. Hash Map + Dynamic Array

**Time Complexity:** O(1) average for all operations
**Space Complexity:** O(n) where n is number of elements

```python
def __init__(self):
    self.val_to_index = {}  # Maps value to its index in the list
    self.values = []  # List of values for random access

def insert(self, val: int) -> bool:
    if val in self.val_to_index:
        return False

    # Add to end of list and record index in map
    self.val_to_index[val] = len(self.values)
    self.values.append(val)
    return True

def remove(self, val: int) -> bool:
    if val not in self.val_to_index:
        return False

    # Get index of element to remove
    idx = self.val_to_index[val]
    last_val = self.values[-1]

    # Move last element to the position of removed element
    self.values[idx] = last_val
    self.val_to_index[last_val] = idx

    # Remove last element
    self.values.pop()
    del self.val_to_index[val]

    return True

def getRandom(self) -> int:
    import random
    return random.choice(self.values)
```

**Why this works:**
Combine a hash map and dynamic array. The array stores values for O(1) random access. The hash map stores value-to-index mappings for O(1) insert/remove. For removal, swap with last element to avoid shifting.

## Key Insights

1. Array enables O(1) random access via random.choice
2. Hash map enables O(1) lookup for insert/remove
3. Swap-with-last trick enables O(1) removal from array
4. Must update hash map when swapping during removal

## Common Mistakes

- Not updating the index of the swapped element in the hash map
- Trying to remove the last element when it's the element being removed (edge case)
- Using a set instead of array (can't do O(1) random access)

## Related Problems

- Insert Delete GetRandom O(1) - Duplicates allowed (LeetCode #381)
- LRU Cache (LeetCode #146)
