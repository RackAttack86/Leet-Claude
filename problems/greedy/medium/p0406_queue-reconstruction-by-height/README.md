# Problem 406: Queue Reconstruction by Height

**Difficulty:** Medium
**Pattern:** Greedy
**Link:** [LeetCode](https://leetcode.com/problems/queue-reconstruction-by-height/)

## Problem Description

You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order). Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people in front who have a height greater than or equal to hi.

Reconstruct and return the queue that is represented by the input array people. The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] is the attributes of the jth person in the queue (queue[0] is the person at the front of the queue).

## Constraints

- 1 <= people.length <= 2000
- 0 <= hi <= 10^6
- 0 <= ki < people.length
- It is guaranteed that the queue can be reconstructed

## Examples

Example 1:
```
Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
Explanation:
Person 0 has height 5 with no other people taller or the same height in front.
Person 1 has height 7 with no other people taller or the same height in front.
Person 2 has height 5 with two persons taller or the same height in front.
Person 3 has height 6 with one person taller or the same height in front.
Person 4 has height 4 with four people taller or the same height in front.
Person 5 has height 7 with one person taller or the same height in front.
```

Example 2:
```
Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
```

## Approaches

### 1. Sort by Height Descending, Insert by K

**Time Complexity:** O(n^2) - due to list insertions
**Space Complexity:** O(n)

```python
def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
    # Sort by height descending, then by k ascending
    # This ensures taller people are placed first
    people.sort(key=lambda x: (-x[0], x[1]))

    result = []

    # Insert each person at position k
    # Since taller people are already placed, inserting at k works
    for person in people:
        result.insert(person[1], person)

    return result
```

**Why this works:**
By processing taller people first, when we insert a shorter person at position k, we know that exactly k people in front of them are taller (or equal). Shorter people inserted later don't affect the k value of taller people already placed.

## Key Insights

1. Sort by height descending, k ascending
2. Insert each person at position k
3. Taller people processed first don't affect shorter
4. Greedy insertion works due to sorting

## Common Mistakes

1. Sorting in the wrong order
2. Not understanding why inserting at k works
3. Using wrong tie-breaking (should sort by k ascending for same height)

## Related Problems

- 315. Count of Smaller Numbers After Self

## Tags

Array, Binary Indexed Tree, Segment Tree, Sorting
