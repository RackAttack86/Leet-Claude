# Problem 49: Group Anagrams

**Difficulty:** Medium
**Pattern:** Two Pointers
**Link:** [LeetCode](https://leetcode.com/problems/group-anagrams/)

## Problem Description

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

## Constraints

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

## Examples

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

- There is no string in strs that can be rearranged to form `"bat"`.

- The strings `"nat"` and `"tan"` are anagrams as they can be rearranged to form each other.

- The strings `"ate"`, `"eat"`, and `"tea"` are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]

Output: [[""]]

Example 3:
Input: strs = ["a"]

Output: [["a"]]

## Approaches

### 1. Sorted String as Key

**Time Complexity:** O(n * k * log(k)) where n is number of strings, k is max string length. Using character count as key: O(n * k)
**Space Complexity:** O(n * k) for storing all strings in the hash map

```python
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # Group anagrams by their sorted character tuple
    anagram_groups = defaultdict(list)

    for s in strs:
        # Use sorted tuple as key (anagrams will have same sorted form)
        key = tuple(sorted(s))
        anagram_groups[key].append(s)

    return list(anagram_groups.values())
```

**Why this works:**
Use a hash map where the key is a canonical representation of each anagram group. Two strings are anagrams if they have the same sorted characters or the same character frequency count.

## Key Insights

1. Anagrams have the same sorted character sequence
2. Alternative: Use character count tuple as key (faster for long strings)
3. defaultdict simplifies grouping logic
4. Tuple of sorted string works as hashable key

## Common Mistakes

- Using a list as dictionary key (lists are not hashable)
- Not handling empty strings correctly
- Inefficient key generation for long strings

## Related Problems

- Valid Anagram (LeetCode #242)
- Find All Anagrams in a String (LeetCode #438)
