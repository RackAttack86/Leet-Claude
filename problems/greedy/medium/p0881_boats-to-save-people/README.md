# Problem 881: Boats to Save People

**Difficulty:** Medium
**Pattern:** Greedy
**Link:** [LeetCode](https://leetcode.com/problems/boats-to-save-people/)

## Problem Description

You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

## Constraints

- 1 <= people.length <= 5 * 10^4
- 1 <= people[i] <= limit <= 3 * 10^4

## Examples

Example 1:
```
Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
```

Example 2:
```
Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
```

Example 3:
```
Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
```

## Approaches

### 1. Two Pointers After Sorting

**Time Complexity:** O(n log n)
**Space Complexity:** O(1)

```python
def numRescueBoats(self, people: List[int], limit: int) -> int:
    people.sort()

    boats = 0
    left = 0
    right = len(people) - 1

    while left <= right:
        # Always take the heaviest person
        boats += 1

        # Try to pair with the lightest person
        if people[left] + people[right] <= limit:
            left += 1

        right -= 1

    return boats
```

**Why this works:**
By sorting and using two pointers, we always try to pair the heaviest person with the lightest. If they can share a boat, great! If not, the heavy person goes alone. This greedy approach minimizes boats because pairing light with heavy maximizes weight utilization.

## Key Insights

1. Sort array first
2. Use two pointers from both ends
3. Pair lightest with heaviest if possible
4. Greedy pairing minimizes boats

## Common Mistakes

1. Trying to fit more than 2 people per boat (constraint says max 2)
2. Not sorting first
3. Forgetting the single person case (left == right)

## Related Problems

- 611. Valid Triangle Number
- 826. Most Profit Assigning Work

## Tags

Array, Two Pointers, Greedy, Sorting
