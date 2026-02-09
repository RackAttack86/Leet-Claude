# Problem 763: Partition Labels

**Difficulty:** Medium
**Pattern:** Greedy
**Link:** [LeetCode](https://leetcode.com/problems/partition-labels/)

## Problem Description

You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

## Constraints

- 1 <= s.length <= 500
- s consists of lowercase English letters

## Examples

Example 1:
```
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
```

Example 2:
```
Input: s = "eccbbbbdec"
Output: [10]
```

## Approaches

### 1. Greedy with Last Occurrence

**Time Complexity:** O(n)
**Space Complexity:** O(1) - only 26 letters

```python
def partitionLabels(self, s: str) -> List[int]:
    # Record last occurrence of each character
    last = {char: i for i, char in enumerate(s)}

    result = []
    start = 0
    end = 0

    for i, char in enumerate(s):
        # Extend partition to include all occurrences of current char
        end = max(end, last[char])

        # When we reach the end of current partition
        if i == end:
            result.append(end - start + 1)
            start = i + 1

    return result
```

**Why this works:**
For each character in the current partition, we must include all its occurrences. So we track the last occurrence of each character and expand our partition end as needed. When the current index reaches the partition end, we know we've included all necessary characters.

## Key Insights

1. Record last occurrence of each character
2. Expand partition end to include all occurrences
3. Create new partition when reaching partition end
4. One pass solution after preprocessing

## Common Mistakes

1. Not considering that a character might appear later in the string
2. Starting new partition too early
3. Off-by-one errors in partition sizes

## Related Problems

- 56. Merge Intervals
- 768. Max Chunks To Make Sorted II

## Tags

Hash Table, Two Pointers, String, Greedy
