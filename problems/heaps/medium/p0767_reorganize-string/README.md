# Problem 767: Reorganize String

**Difficulty:** Medium
**Pattern:** Heaps
**Link:** [LeetCode](https://leetcode.com/problems/reorganize-string/)

## Problem Description

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

## Constraints

- 1 <= s.length <= 500
- s consists of lowercase English letters

## Examples

Example 1:
```
Input: s = "aab"
Output: "aba"
```

Example 2:
```
Input: s = "aaab"
Output: ""
Explanation: No valid rearrangement exists.
```

## Approaches

### 1. Max Heap with Frequency

**Time Complexity:** O(n log k) where k is unique characters
**Space Complexity:** O(k)

```python
def reorganizeString(self, s: str) -> str:
    freq = Counter(s)

    heap = [(-count, char) for char, count in freq.items()]
    heapq.heapify(heap)

    result = []
    prev_count, prev_char = 0, ''

    while heap:
        count, char = heapq.heappop(heap)

        if prev_count < 0:
            heapq.heappush(heap, (prev_count, prev_char))

        result.append(char)
        prev_count = count+1
        prev_char = char

    result_str = ''.join(result)

    if len(result_str) < len(s):
        return ""

    return result_str
```

**Why this works:**
We always place the character with the highest remaining frequency, but we can't place the same character consecutively. So we hold the previous character and only push it back to the heap after placing a different character.

## Key Insights

1. Count character frequencies
2. Use max heap to prioritize most frequent
3. Place highest frequency char, then second highest
4. If any char frequency > (n+1)/2, impossible

## Common Mistakes

1. Not checking if rearrangement is possible before trying
2. Placing same character consecutively
3. Forgetting to push previous character back to heap

## Related Problems

- 621. Task Scheduler
- 358. Rearrange String k Distance Apart

## Tags

Hash Table, String, Greedy, Sorting, Heap (Priority Queue), Counting
