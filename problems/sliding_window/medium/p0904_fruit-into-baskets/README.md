# Problem 904: Fruit Into Baskets

**Difficulty:** Medium
**Pattern:** Sliding Window
**Link:** [LeetCode](https://leetcode.com/problems/fruit-into-baskets/)

## Problem Description

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

- You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
- Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
- Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Given the integer array fruits, return the maximum number of fruits you can pick.

### Constraints

- 1 <= fruits.length <= 10^5
- 0 <= fruits[i] < fruits.length

### Examples

**Example 1:**
```
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
```

**Example 2:**
```
Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
```

**Example 3:**
```
Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
```

## Approaches

### 1. Sliding Window with Hash Map

**Time Complexity:** O(n)
**Space Complexity:** O(1) - at most 3 fruit types tracked

```python
def totalFruit(self, fruits: List[int]) -> int:
    fruit_count = {}
    max_fruits = 0
    left = 0

    for right in range(len(fruits)):
        # Add fruit to window
        fruit = fruits[right]
        fruit_count[fruit] = fruit_count.get(fruit, 0) + 1

        # Shrink window while we have more than 2 fruit types
        while len(fruit_count) > 2:
            left_fruit = fruits[left]
            fruit_count[left_fruit] -= 1
            if fruit_count[left_fruit] == 0:
                del fruit_count[left_fruit]
            left += 1

        # Update maximum
        max_fruits = max(max_fruits, right - left + 1)

    return max_fruits
```

**Why this works:**

This problem is equivalent to finding the longest subarray with at most 2 distinct elements. We use a sliding window with a hash map to track the count of each fruit type in the current window. When we have more than 2 types, we shrink the window from the left until we have at most 2 types again.

## Key Insights

- Find longest subarray with at most 2 distinct elements
- Use hash map to track fruit types in window
- Expand window and contract when types > 2
- Classic sliding window pattern

## Common Mistakes

- Not removing fruits from the hash map when their count reaches 0
- Using a set instead of a map (need counts to know when to fully remove)
- Not considering all possible starting positions

## Related Problems

- Longest Substring with At Most Two Distinct Characters
- Longest Substring with At Most K Distinct Characters

## Tags

Array, Hash Table, Sliding Window
