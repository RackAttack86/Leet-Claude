# Problem 128: Longest Consecutive Sequence

**Difficulty:** Medium
**Pattern:** Two Pointers
**Link:** [LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/)

## Problem Description

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in `O(n)` time.

## Constraints

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Examples

Example 1:
```

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is `[1, 2, 3, 4]`. Therefore its length is 4.

```

Example 2:
```

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

```

Example 3:
```

Input: nums = [1,0,1,2]
Output: 3

```

## Approaches

### 1. Hash Set with Sequence Start Detection

**Time Complexity:** O(n) - Each element is visited at most twice
**Space Complexity:** O(n) - For storing elements in the set

```python
def longestConsecutive(self, nums: List[int]) -> int:
    if not nums:
        return 0

    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Only start counting if this is the beginning of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Count consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest = max(longest, current_streak)

    return longest
```

**Why this works:**
Use a hash set for O(1) lookups. For each number, only start counting a sequence if the number is the beginning of a sequence (i.e., num-1 is not in the set). This ensures each element is visited at most twice.

## Key Insights

1. Only start counting from sequence beginnings (num-1 not in set)
2. This optimization makes the algorithm O(n) despite nested loops
3. Converting to set removes duplicates and enables O(1) lookup
4. Each number is part of exactly one sequence count operation

## Common Mistakes

- Starting a sequence count from every element (makes it O(n^2))
- Not handling empty input
- Using sorting (would be O(n log n))

## Related Problems

- Binary Tree Longest Consecutive Sequence (LeetCode #298)
- Consecutive Numbers Sum (LeetCode #829)
