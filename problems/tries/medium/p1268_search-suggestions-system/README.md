# Problem 1268: Search Suggestions System

**Difficulty:** Medium
**Pattern:** Tries
**Link:** [LeetCode](https://leetcode.com/problems/search-suggestions-system/)

## Problem Description

You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.

**Constraints:**
- 1 <= products.length <= 1000
- 1 <= products[i].length <= 3000
- 1 <= sum(products[i].length) <= 2 * 10^4
- All the strings of products are unique
- products[i] consists of lowercase English letters
- 1 <= searchWord.length <= 1000
- searchWord consists of lowercase English letters

**Examples:**
```
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
```

## Approaches

### 1. Sorting with Binary Search

**Time Complexity:** O(n log n + m * n) where n is products count, m is searchWord length
**Space Complexity:** O(n) for sorted products

```python
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        import bisect

        # Sort products lexicographically
        products.sort()
        result = []
        prefix = ''

        for char in searchWord:
            prefix += char
            # Find the leftmost position where products >= prefix
            left = bisect.bisect_left(products, prefix)

            suggestions = []
            # Check up to 3 products starting from this position
            for i in range(left, min(left + 3, len(products))):
                if products[i].startswith(prefix):
                    suggestions.append(products[i])
                else:
                    break  # No more matches since products are sorted

            result.append(suggestions)

        return result
```

**Why this works:**
By sorting products lexicographically, all products with the same prefix are adjacent. For each prefix (after typing each character), we use binary search to find the first product that could match (>= prefix). Then we check up to 3 products from that position, verifying they start with the prefix. Since products are sorted, once we find a non-matching product, all subsequent ones won't match either.

## Key Insights

- Sort products lexicographically to group matching prefixes together
- For each prefix, use binary search to find the starting point
- Take up to 3 products that match the prefix
- Sorting approach is simpler and efficient for this problem
- Binary search gives O(log n) per character instead of O(n)

## Common Mistakes

- Not sorting products first
- Not limiting results to 3 suggestions
- Continuing to check after finding a non-matching product
- Using inefficient linear search for each prefix

## Related Problems

- 208 - Implement Trie
- 211 - Design Add and Search Words Data Structure
- 720 - Longest Word in Dictionary

## Tags

Array, String, Binary Search, Trie, Sorting, Heap (Priority Queue)
