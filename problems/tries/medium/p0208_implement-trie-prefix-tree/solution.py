"""
LeetCode Problem #208: Implement Trie (Prefix Tree)
Difficulty: Medium
Pattern: Tries
Link: https://leetcode.com/problems/implement-trie-prefix-tree/

Problem:
--------
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

- `Trie()` Initializes the trie object.
	
- `void insert(String word)` Inserts the string `word` into the trie.
	
- `boolean search(String word)` Returns `true` if the string `word` is in the trie (i.e., was inserted before), and `false` otherwise.
	
- `boolean startsWith(String prefix)` Returns `true` if there is a previously inserted string `word` that has the prefix `prefix`, and `false` otherwise.

Constraints:
-----------
- `1
- word` and `prefix` consist only of lowercase English letters.
- At most `3 * 10^4` calls in total will be made to `insert`, `search`, and `startsWith`.

Examples:
---------
Example 1:
```

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True

```
"""

from typing import List, Optional
from collections import Counter, defaultdict


class Solution:
    """
    Solution to LeetCode Problem #208: Implement Trie (Prefix Tree)

    Approach: [TODO: Describe approach]
    Time Complexity: O(?)
    Space Complexity: O(?)

    Key Insights:
    [TODO: Add key insights]
    """

    def __init__(self):
        """
        [TODO: Implement]
        """
        pass

    def insert(self, word: str) -> None:
        """
        [TODO: Implement]
        """
        pass

    def search(self, word: str) -> bool:
        """
        [TODO: Implement]
        """
        pass

    def startsWith(self, prefix: str) -> bool:
        """
        [TODO: Implement]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 208,
    "name": "Implement Trie (Prefix Tree)",
    "difficulty": "Medium",
    "pattern": "Tries",
    "topics": ['Hash Table', 'String', 'Design', 'Trie'],
    "url": "https://leetcode.com/problems/implement-trie-prefix-tree/",
    "companies": [],
    "time_complexity": "O(?)",
    "space_complexity": "O(?)",
}
