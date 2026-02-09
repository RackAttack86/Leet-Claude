# Problem 12: Integer to Roman

**Difficulty:** Medium
**Pattern:** Two Pointers
**Link:** [LeetCode](https://leetcode.com/problems/integer-to-roman/)

## Problem Description

Seven different symbols represent Roman numerals with the following values:

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

- If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.

- If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (`I`) less than 5 (`V`): `IV` and 9 is 1 (`I`) less than 10 (`X`): `IX`. Only the following subtractive forms are used: 4 (`IV`), 9 (`IX`), 40 (`XL`), 90 (`XC`), 400 (`CD`) and 900 (`CM`).

- Only powers of 10 (`I`, `X`, `C`, `M`) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (`V`), 50 (`L`), or 500 (`D`) multiple times. If you need to append a symbol 4 times use the subtractive form.

Given an integer, convert it to a Roman numeral.

## Constraints

- `1 <= num <= 3999`

## Examples

Example 1:
Input: num = 3749

Output: "MMMDCCXLIX"

Explanation:

```

3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places

```

Example 2:
Input: num = 58

Output: "LVIII"

Explanation:

```

50 = L
 8 = VIII

```

Example 3:
Input: num = 1994

Output: "MCMXCIV"

Explanation:

```

1000 = M
 900 = CM
  90 = XC
   4 = IV

```

## Approaches

### 1. Greedy with Value-Symbol Mapping

**Time Complexity:** O(1) - The number of iterations is bounded by the fixed set of Roman numeral values (at most 13 values, each used at most 3 times)
**Space Complexity:** O(1) - Output string length is bounded (max ~15 chars for 3999)

```python
def intToRoman(self, num: int) -> str:
    # Value-symbol pairs in descending order (including subtractive forms)
    value_symbols = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]

    result = []
    for value, symbol in value_symbols:
        # Add as many of this symbol as possible
        while num >= value:
            result.append(symbol)
            num -= value

    return ''.join(result)
```

**Why this works:**
Greedy approach using a value-symbol mapping that includes subtractive forms. Process from largest to smallest value, repeatedly subtracting and appending symbols.

## Key Insights

1. Include subtractive forms (4, 9, 40, 90, 400, 900) in the mapping
2. Process values in descending order for greedy approach
3. The mapping table handles all edge cases naturally
4. Maximum number in constraints is 3999, limiting output size

## Common Mistakes

- Forgetting to include the subtractive forms in the mapping
- Processing values in wrong order (must be descending)
- Not handling edge cases for 4s and 9s

## Related Problems

- Roman to Integer (LeetCode #13)
- Integer to English Words
