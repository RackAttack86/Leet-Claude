# Problem 17: Letter Combinations of a Phone Number

**Difficulty:** Medium
**Pattern:** Backtracking
**Link:** [LeetCode](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

## Problem Description

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on telephone buttons) is given below. Note that 1 does not map to any letters.

**Constraints:**
- 0 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9']

**Examples:**

```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = ""
Output: []

Input: digits = "2"
Output: ["a","b","c"]
```

## Approaches

### 1. Backtracking

**Time Complexity:** O(4^n) where n is length of digits
**Space Complexity:** O(n) for recursion depth

```python
def letterCombinations(self, digits: str) -> List[str]:
    if not digits:
        return []

    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    result = []

    def backtrack(index: int, current: str):
        if index == len(digits):
            result.append(current)
            return

        for char in phone_map[digits[index]]:
            backtrack(index + 1, current + char)

    backtrack(0, "")
    return result
```

**Why this works:**

We use backtracking to generate all possible letter combinations. For each digit in the input string, we map it to its corresponding letters and recursively build combinations by appending each possible letter. When we've processed all digits, we add the complete combination to our result.

## Key Insights

- Map each digit to its letters using a dictionary
- Use backtracking to generate all combinations
- Each digit adds 3-4 possibilities (7 and 9 have 4 letters, others have 3)
- Handle empty input as edge case

## Common Mistakes

- Forgetting to handle the empty string input case
- Not using the correct digit-to-letter mapping
- Creating unnecessary string copies (can use list and join for optimization)

## Related Problems

- Generate Parentheses (#22)
- Combination Sum (#39)
- Permutations (#46)

## Tags

Hash Table, String, Backtracking
