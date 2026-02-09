# Problem 151: Reverse Words in a String

**Difficulty:** Medium
**Pattern:** Two Pointers
**Link:** [LeetCode](https://leetcode.com/problems/reverse-words-in-a-string/)

## Problem Description

Given an input string `s`, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in `s` will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

## Constraints

- `1 <= s.length <= 10^4`
- `s` contains English letters (upper-case and lower-case), digits, and spaces `' '`.
- There is at least one word in `s`.

## Examples

Example 1:
```

Input: s = "the sky is blue"
Output: "blue is sky the"

```

Example 2:
```

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

```

Example 3:
```

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

```

## Approaches

### 1. Split, Reverse, Join

**Time Complexity:** O(n) where n is the length of the string
**Space Complexity:** O(n) for storing the words

```python
def reverseWords(self, s: str) -> str:
    # Split by whitespace, reverse, and join with single space
    words = s.split()
    return ' '.join(reversed(words))
```

**Why this works:**
Split the string by whitespace to get words, filter out empty strings (from multiple spaces), reverse the list of words, and join with single spaces.

## Key Insights

1. split() without arguments splits on any whitespace and removes empty strings
2. Reversing a list of words is O(number of words)
3. Two-pointer approach can be used for in-place reversal in languages with mutable strings
4. Python strings are immutable, so O(n) space is unavoidable

## Common Mistakes

- Not handling multiple spaces between words
- Not trimming leading/trailing spaces
- Using split(' ') instead of split() (split(' ') keeps empty strings)

## Related Problems

- Reverse String (LeetCode #344)
- Reverse Words in a String II (LeetCode #186)
