from typing import List, Optional

class WordFilter:
    def __init__(self, words):
        self.trie = {}
        for idx, word in enumerate(words):
    for i in range(len(word) + 1):
        suffix = word[i:]
        key = suffix + '#' + word
        node = self.trie
        for char in key:
            if char not in node:
                node[char] = {}
            node = node[char]
            node['idx'] = idx
    def f(self, pref, suff):
        pass

class Solution: