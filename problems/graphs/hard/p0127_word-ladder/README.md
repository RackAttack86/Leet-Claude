# Problem 127: Word Ladder

**Difficulty:** Hard
**Pattern:** Graphs
**Link:** [LeetCode](https://leetcode.com/problems/word-ladder/)

## Problem Description

A transformation sequence from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s1 -> s2 -> ... -> sk` such that:

- Every adjacent pair of words differs by a single letter.

- Every `si` for `1

- `sk == endWord`

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return the number of words in the shortest transformation sequence from `beginWord` to `endWord`, or `0` if no such sequence exists.

## Constraints

- `1
- endWord.length == beginWord.length
- wordList[i].length == beginWord.length
- beginWord`, `endWord`, and `wordList[i]` consist of lowercase English letters.
- beginWord != endWord
- All the words in `wordList` are unique.

## Examples

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

## Approaches

### 1. BFS with Pattern-Based Preprocessing

**Time Complexity:** O(M^2 * N)
**Space Complexity:** O(M^2 * N)

```python
def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    """
    Find length of shortest transformation sequence.
    """
    from collections import deque, defaultdict

    # endWord must be in wordList
    word_set = set(wordList)
    if endWord not in word_set:
        return 0

    # Build pattern map: pattern -> list of words
    # e.g., "*ot" -> ["hot", "dot", "lot"]
    word_len = len(beginWord)
    pattern_map = defaultdict(list)

    # Add beginWord to consideration (might not be in wordList)
    all_words = word_set | {beginWord}

    for word in all_words:
        for i in range(word_len):
            pattern = word[:i] + '*' + word[i+1:]
            pattern_map[pattern].append(word)

    # BFS
    queue = deque([(beginWord, 1)])  # (word, length)
    visited = {beginWord}

    while queue:
        current, length = queue.popleft()

        # Try all patterns for current word
        for i in range(word_len):
            pattern = current[:i] + '*' + current[i+1:]

            for neighbor in pattern_map[pattern]:
                if neighbor == endWord:
                    return length + 1

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, length + 1))

    return 0
```

**Why this works:**

Create an intermediate graph where words connect through "wildcard patterns".
For word "hot", patterns are "*ot", "h*t", "ho*".
Words sharing a pattern differ by exactly one character.

This optimization reduces neighbor lookup from O(26*L*N) to O(L) per word.

## Key Insights

- BFS guarantees shortest path (minimum transformations)
- Wildcard patterns efficiently group words differing by one char
- endWord must be in wordList (beginWord doesn't need to be)
- Return count of words in sequence, not number of transformations
- Bidirectional BFS can optimize further but adds complexity

## Common Mistakes

- Forgetting to check if endWord is in wordList
- Returning number of transformations instead of words in sequence
- Not adding beginWord to the pattern map
- Using DFS which doesn't guarantee shortest path

## Related Problems

- Word Ladder II (126)
- Minimum Genetic Mutation (433)
