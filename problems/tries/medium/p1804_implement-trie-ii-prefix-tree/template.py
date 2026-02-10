from typing import List, Optional

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_count = 0
        self.prefix_count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        pass
    def countWordsEqualTo(self, word):
        pass
    def countWordsStartingWith(self, prefix):
        pass
    def erase(self, word):
        pass

class Solution: