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
from collections import deque


class Solution:
    """
    Solution to LeetCode Problem #433: Minimum Genetic Mutation

    Approach: BFS for Shortest Path

    This is a shortest path problem in an implicit graph where:
    - Each valid gene string is a node
    - Two nodes are connected if they differ by exactly one character

    Use BFS to find minimum mutations (edges) from start to end.

    Time Complexity: O(B * G * 4) = O(B * G) where B = bank size, G = gene length (8)
                     For each gene, try 4 chars at 8 positions, check if in bank
    Space Complexity: O(B) - visited set and queue store at most B genes

    Key Insights:
    - BFS guarantees shortest path (minimum mutations)
    - Only genes in the bank are valid intermediate states
    - Each mutation changes exactly one character
    - Gene length is fixed at 8, so mutation generation is O(32) = O(1)
    """

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        """
        Find minimum mutations to transform startGene to endGene.
        """
        # Convert bank to set for O(1) lookup
        bank_set = set(bank)

        # endGene must be in bank to be reachable
        if endGene not in bank_set:
            return -1

        # BFS setup
        queue = deque([(startGene, 0)])  # (current_gene, mutation_count)
        visited = {startGene}
        genes = ['A', 'C', 'G', 'T']

        while queue:
            current, mutations = queue.popleft()

            # Found the target
            if current == endGene:
                return mutations

            # Try all possible single-character mutations
            for i in range(len(current)):
                for gene in genes:
                    if gene != current[i]:
                        # Create mutated gene
                        mutated = current[:i] + gene + current[i+1:]

                        # Only process if valid (in bank) and not visited
                        if mutated in bank_set and mutated not in visited:
                            visited.add(mutated)
                            queue.append((mutated, mutations + 1))

        # No path found
        return -1


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 433,
    "name": "Minimum Genetic Mutation",
    "difficulty": "Medium",
    "pattern": "Graphs",
    "topics": ['Hash Table', 'String', 'Breadth-First Search'],
    "url": "https://leetcode.com/problems/minimum-genetic-mutation/",
    "companies": ["Google", "Amazon", "Twitter", "Facebook"],
    "time_complexity": "O(B * G)",
    "space_complexity": "O(B)",
}
