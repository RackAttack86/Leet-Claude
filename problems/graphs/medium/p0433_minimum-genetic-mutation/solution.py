"""
LeetCode Problem #433: Minimum Genetic Mutation
Difficulty: Medium
Pattern: Graphs
Link: https://leetcode.com/problems/minimum-genetic-mutation/

Problem:
--------
A gene string can be represented by an 8-character long string, with choices from `'A'`, `'C'`, `'G'`, and `'T'`.

Suppose we need to investigate a mutation from a gene string `startGene` to a gene string `endGene` where one mutation is defined as one single character changed in the gene string.

- For example, `"AACCGGTT" --> "AACCGGTA"` is one mutation.

There is also a gene bank `bank` that records all the valid gene mutations. A gene must be in `bank` to make it a valid gene string.

Given the two gene strings `startGene` and `endGene` and the gene bank `bank`, return the minimum number of mutations needed to mutate from `startGene` to `endGene`. If there is no such a mutation, return `-1`.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

Constraints:
-----------
- `0
- startGene.length == endGene.length == bank[i].length == 8
- startGene`, `endGene`, and `bank[i]` consist of only the characters `['A', 'C', 'G', 'T']`.

Examples:
---------
Example 1:
```

Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1

```

Example 2:
```

Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2

```
"""

from typing import List, Optional
from collections import Counter, defaultdict


class Solution:
    """
    Solution to LeetCode Problem #433: Minimum Genetic Mutation

    Approach: [TODO: Describe approach]
    Time Complexity: O(?)
    Space Complexity: O(?)

    Key Insights:
    [TODO: Add key insights]
    """

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        """
        [TODO: Implement]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 433,
    "name": "Minimum Genetic Mutation",
    "difficulty": "Medium",
    "pattern": "Graphs",
    "topics": ['Hash Table', 'String', 'Breadth-First Search'],
    "url": "https://leetcode.com/problems/minimum-genetic-mutation/",
    "companies": [],
    "time_complexity": "O(?)",
    "space_complexity": "O(?)",
}
