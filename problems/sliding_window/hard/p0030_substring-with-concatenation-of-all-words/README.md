# Problem 30: Substring with Concatenation of All Words

**Difficulty:** Hard
**Pattern:** Sliding Window
**Link:** [LeetCode](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)

## Problem Description

You are given a string `s` and an array of strings `words`. All the strings of `words` are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of `words` concatenated.

- For example, if `words = ["ab","cd","ef"]`, then `"abcdef"`, `"abefcd"`, `"cdabef"`, `"cdefab"`, `"efabcd"`, and `"efcdab"` are all concatenated strings. `"acdbef"` is not a concatenated string because it is not the concatenation of any permutation of `words`.

Return an array of the starting indices of all the concatenated substrings in `s`. You can return the answer in any order.

## Constraints

- 1 <= s.length <= 10^4
- 1 <= words.length <= 5000
- 1 <= words[i].length <= 30
- s and words[i] consist of lowercase English letters.

## Examples

**Example 1:**
```
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation:
The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.
```

**Example 2:**
```
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Explanation: There is no concatenated substring.
```

**Example 3:**
```
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
Explanation:
The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].
```

## Approaches

### 1. Sliding Window with Word-Level Granularity

**Time Complexity:** O(n * word_len) where n is the length of string s
**Space Complexity:** O(m * word_len) where m is the number of words

```python
def findSubstring(self, s: str, words: List[str]) -> List[int]:
    if not s or not words:
        return []

    word_len = len(words[0])
    num_words = len(words)
    total_len = word_len * num_words
    n = len(s)

    if n < total_len:
        return []

    # Count frequency of each word in words list
    word_count = Counter(words)
    result = []

    # Try each starting offset from 0 to word_len - 1
    for offset in range(word_len):
        left = offset
        right = offset
        window_count = defaultdict(int)
        formed = 0  # Number of unique words with correct frequency

        while right + word_len <= n:
            # Add word at right pointer
            word = s[right:right + word_len]
            right += word_len

            if word in word_count:
                window_count[word] += 1

                if window_count[word] == word_count[word]:
                    formed += 1
                elif window_count[word] == word_count[word] + 1:
                    formed -= 1

                # Shrink window if we have excess of current word
                while window_count[word] > word_count[word]:
                    left_word = s[left:left + word_len]
                    window_count[left_word] -= 1
                    if window_count[left_word] == word_count[left_word]:
                        formed += 1
                    elif window_count[left_word] == word_count[left_word] - 1:
                        formed -= 1
                    left += word_len

                # Check if we have a valid window with all words
                if formed == len(word_count) and (right - left) == total_len:
                    result.append(left)
            else:
                # Word not in words list, reset window
                window_count.clear()
                formed = 0
                left = right

    return result
```

**Why this works:**

Since all words have the same length, we can treat the string as a sequence of word-sized chunks. We use multiple starting offsets (0 to word_len-1) to cover all possible alignments. For each offset, we use a sliding window of exactly (num_words * word_len) characters. We track word frequencies using a hash map and use a "formed" counter to efficiently know when the window is valid.

## Key Insights

1. All words have the same length, which is crucial for the sliding window approach
2. We need to try word_len different starting offsets to cover all alignments
3. Use a sliding window that moves by one word at a time (not one character)
4. Track "formed" count to know when window contains all required words
5. When we have excess of a word, shrink window from the left

## Common Mistakes

- Only checking one starting offset instead of all word_len offsets
- Moving the window by one character instead of one word
- Not handling duplicate words in the words array
- Rechecking the entire window instead of using incremental updates

## Related Problems

- Minimum Window Substring
- Find All Anagrams in a String
