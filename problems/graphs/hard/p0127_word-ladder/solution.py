"""
LeetCode Problem #127: Word Ladder
Difficulty: Hard
Pattern: Graphs
Link: https://leetcode.com/problems/word-ladder/

Problem:
--------
A transformation sequence from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s1 -> s2 -> ... -> sk` such that:

- Every adjacent pair of words differs by a single letter.
	
- Every `si` for `1 
	
- `sk == endWord`

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return the number of words in the shortest transformation sequence from `beginWord` to `endWord`, or `0` if no such sequence exists.

Constraints:
-----------
- `1
- endWord.length == beginWord.length
- wordList[i].length == beginWord.length
- beginWord`, `endWord`, and `wordList[i]` consist of lowercase English letters.
- beginWord != endWord
- All the words in `wordList` are unique.

Examples:
---------
Example 1:
```

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

```

Example 2:
```

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

```
"""

from typing import List, Optional
from collections import Counter, defaultdict


class Solution:
    """
    Solution to LeetCode Problem #127: Word Ladder

    Approach: [TODO: Describe approach]
    Time Complexity: O(?)
    Space Complexity: O(?)

    Key Insights:
    [TODO: Add key insights]
    """

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        [TODO: Implement]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 127,
    "name": "Word Ladder",
    "difficulty": "Hard",
    "pattern": "Graphs",
    "topics": ['Hash Table', 'String', 'Breadth-First Search'],
    "url": "https://leetcode.com/problems/word-ladder/",
    "companies": [],
    "time_complexity": "O(?)",
    "space_complexity": "O(?)",
}
