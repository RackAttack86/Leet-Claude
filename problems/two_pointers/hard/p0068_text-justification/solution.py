"""
LeetCode Problem #68: Text Justification
Difficulty: Hard
Pattern: Two Pointers
Link: https://leetcode.com/problems/text-justification/

Problem:
--------
Given an array of strings `words` and a width `maxWidth`, format the text such that each line has exactly `maxWidth` characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces `' '` when necessary so that each line has exactly `maxWidth` characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

- A word is defined as a character sequence consisting of non-space characters only.
	
- Each word's length is guaranteed to be greater than `0` and not exceed `maxWidth`.
	
- The input array `words` contains at least one word.

Constraints:
-----------
- `1
- words[i]` consists of only English letters and symbols.
- words[i].length

Examples:
---------
Example 1:
```

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
```

Example 2:
```

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
```

Example 3:
```

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
```
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #68: Text Justification

    Approach: Greedy line packing with two-pointer technique. Pack words
    greedily into each line, then distribute spaces evenly. Handle three
    cases: middle lines (full justify), last line (left justify), and
    single-word lines (left justify).

    Time Complexity: O(n) where n is total characters in all words
    Space Complexity: O(n) for the result

    Key Insights:
    1. Greedily pack words until next word would exceed maxWidth
    2. For middle lines: distribute extra spaces left-to-right
    3. For last line: left-justify with single spaces
    4. Single-word lines: left-justify (pad right with spaces)
    5. Extra spaces = maxWidth - (sum of word lengths) - (min spaces needed)
    """

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0
        n = len(words)

        while i < n:
            # Find words that fit on current line
            line_words = []
            line_length = 0

            while i < n:
                # Check if we can add the next word
                # Need: current length + new word + spaces between words
                spaces_needed = len(line_words)  # One space between each word
                if line_length + len(words[i]) + spaces_needed <= maxWidth:
                    line_words.append(words[i])
                    line_length += len(words[i])
                    i += 1
                else:
                    break

            # Build the line
            if i == n:
                # Last line: left-justify
                line = ' '.join(line_words)
                line += ' ' * (maxWidth - len(line))
            elif len(line_words) == 1:
                # Single word: left-justify
                line = line_words[0] + ' ' * (maxWidth - len(line_words[0]))
            else:
                # Middle line: full justify
                total_spaces = maxWidth - line_length
                gaps = len(line_words) - 1
                space_per_gap = total_spaces // gaps
                extra_spaces = total_spaces % gaps

                line = ''
                for j, word in enumerate(line_words):
                    line += word
                    if j < gaps:
                        # Add spaces (extra spaces go to left gaps first)
                        spaces = space_per_gap + (1 if j < extra_spaces else 0)
                        line += ' ' * spaces

            result.append(line)

        return result


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 68,
    "name": "Text Justification",
    "difficulty": "Hard",
    "pattern": "Two Pointers",
    "topics": ['Array', 'String', 'Simulation'],
    "url": "https://leetcode.com/problems/text-justification/",
    "companies": ["Google", "LinkedIn", "Amazon", "Microsoft", "Apple", "Airbnb", "Facebook"],
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
}
