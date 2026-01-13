# Tries Pattern - Study Guide

## Overview
A Trie (pronounced "try"), also called a prefix tree or digital tree, is a tree-like data structure used for storing and searching strings. Each node represents a character, and paths from root to nodes represent prefixes. Tries excel at prefix-based operations and are commonly used in autocomplete, spell checkers, and IP routing.

## Trie Structure

### Basic Trie Node
```python
class TrieNode:
    def __init__(self):
        self.children = {}  # or [None] * 26 for lowercase letters
        self.is_end_of_word = False
        # Optional: store additional data
        # self.word = None
        # self.count = 0
```

### Complete Trie Implementation
```python
class Trie:
    """Standard Trie implementation"""
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Insert word into trie"""
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end_of_word = True

    def search(self, word):
        """Search for exact word"""
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.is_end_of_word

    def starts_with(self, prefix):
        """Check if any word starts with prefix"""
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True

# Time: O(m) for all operations where m is word length
# Space: O(n*m) where n is number of words
```

## Common Trie Patterns

### 1. Word Search and Prefix

**Implement Trie (Prefix Tree):**
```python
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node['#'] = True  # End marker

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return '#' in node

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True

# Time: O(m), Space: O(n*m)
```

**Longest Common Prefix:**
```python
def longest_common_prefix(strs):
    """Find longest common prefix using trie"""
    if not strs:
        return ""

    # Build trie
    trie = {}
    for word in strs:
        node = trie
        for char in word:
            node = node.setdefault(char, {})
        node['#'] = True

    # Find longest prefix
    result = []
    node = trie

    while len(node) == 1 and '#' not in node:
        char = next(iter(node))
        result.append(char)
        node = node[char]

    return ''.join(result)

# Time: O(S) where S is sum of all characters
# Space: O(S)
```

### 2. Word Dictionary with Wildcards

**Add and Search Word:**
```python
class WordDictionary:
    """Support . as wildcard"""
    def __init__(self):
        self.root = {}

    def add_word(self, word):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node['#'] = True

    def search(self, word):
        def dfs(node, i):
            if i == len(word):
                return '#' in node

            char = word[i]

            if char == '.':
                # Try all possible characters
                for child in node:
                    if child != '#' and dfs(node[child], i + 1):
                        return True
                return False
            else:
                if char not in node:
                    return False
                return dfs(node[char], i + 1)

        return dfs(self.root, 0)

# Add: O(m), Search: O(26^m) worst case with wildcards
```

### 3. Autocomplete / Search Suggestions

**Search Suggestions System:**
```python
def suggested_products(products, search_word):
    """Return top 3 suggestions for each prefix"""
    products.sort()  # Lexicographically

    result = []
    trie = {}

    # Build trie with product lists
    for product in products:
        node = trie
        for char in product:
            node = node.setdefault(char, {})
            if 'products' not in node:
                node['products'] = []
            if len(node['products']) < 3:
                node['products'].append(product)

    # Search for each prefix
    node = trie
    for char in search_word:
        if char in node:
            node = node[char]
            result.append(node.get('products', []))
        else:
            result.append([])
            node = {}  # Empty node for remaining searches

    return result

# Time: O(n*m + k*m) where k is search word length
# Space: O(n*m)
```

### 4. Word Search in Grid

**Word Search II:**
```python
def find_words(board, words):
    """Find all words in board using backtracking + trie"""
    # Build trie
    trie = {}
    for word in words:
        node = trie
        for char in word:
            node = node.setdefault(char, {})
        node['#'] = word  # Store complete word

    rows, cols = len(board), len(board[0])
    result = set()

    def backtrack(row, col, node):
        char = board[row][col]

        if char not in node:
            return

        node = node[char]

        # Found complete word
        if '#' in node:
            result.add(node['#'])

        # Mark as visited
        board[row][col] = '*'

        # Explore neighbors
        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '*':
                backtrack(nr, nc, node)

        # Restore
        board[row][col] = char

    # Start from each cell
    for r in range(rows):
        for c in range(cols):
            backtrack(r, c, trie)

    return list(result)

# Time: O(m*n*4^L) where L is max word length
# Space: O(n*m) for trie
```

### 5. Replace Words (Dictionary Compression)

**Replace Words:**
```python
def replace_words(dictionary, sentence):
    """Replace words with shortest root"""
    # Build trie
    trie = {}
    for root in dictionary:
        node = trie
        for char in root:
            node = node.setdefault(char, {})
        node['#'] = True

    def find_root(word):
        node = trie
        for i, char in enumerate(word):
            if char not in node:
                return word
            node = node[char]
            if '#' in node:
                return word[:i+1]
        return word

    words = sentence.split()
    return ' '.join(find_root(word) for word in words)

# Time: O(n*m) where n is words, m is avg length
# Space: O(d*k) where d is dict size
```

### 6. Map Sum Pairs

**Map Sum Pairs:**
```python
class MapSum:
    """Sum of values for keys with given prefix"""
    def __init__(self):
        self.trie = {}
        self.values = {}

    def insert(self, key, val):
        delta = val - self.values.get(key, 0)
        self.values[key] = val

        node = self.trie
        for char in key:
            node = node.setdefault(char, {})
            node['sum'] = node.get('sum', 0) + delta

    def sum(self, prefix):
        node = self.trie
        for char in prefix:
            if char not in node:
                return 0
            node = node[char]
        return node.get('sum', 0)

# Insert: O(m), Sum: O(m)
```

### 7. Lexicographical Numbers

**Lexicographical Numbers:**
```python
def lexical_order(n):
    """Return 1 to n in lexicographical order"""
    result = []

    def dfs(current):
        if current > n:
            return

        result.append(current)

        for digit in range(10):
            next_num = current * 10 + digit
            if next_num > n:
                break
            dfs(next_num)

    for i in range(1, 10):
        dfs(i)

    return result

# Time: O(n), Space: O(log n) for recursion
# Trie-like traversal without building trie
```

## Advanced Trie Patterns

### Suffix Trie
```python
class SuffixTrie:
    """Trie of all suffixes"""
    def __init__(self, text):
        self.root = {}
        self.build(text)

    def build(self, text):
        for i in range(len(text)):
            node = self.root
            for char in text[i:]:
                node = node.setdefault(char, {})
            node['#'] = i  # Store starting index

    def search(self, pattern):
        """Find all occurrences of pattern"""
        node = self.root
        for char in pattern:
            if char not in node:
                return []
            node = node[char]

        # Collect all indices
        indices = []
        def collect(n):
            if '#' in n:
                indices.append(n['#'])
            for child in n:
                if child != '#':
                    collect(n[child])

        collect(node)
        return indices

# Space: O(n²) - can use suffix arrays for O(n)
```

### Compressed Trie (Radix Tree)
```python
class RadixNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.edge = ""  # Edge label

# More space-efficient but complex implementation
# Compresses paths with single child
```

### Ternary Search Tree
```python
class TSTNode:
    def __init__(self, char):
        self.char = char
        self.left = None    # Less than
        self.middle = None  # Equal
        self.right = None   # Greater than
        self.is_end = False

# More space-efficient than trie
# But slightly slower search
```

## Optimization Techniques

### 1. Array vs Dictionary
```python
# Dictionary (flexible, any characters)
children = {}

# Array (fixed alphabet, faster)
children = [None] * 26  # For lowercase a-z

def char_to_index(char):
    return ord(char) - ord('a')
```

### 2. Memory Optimization
```python
class CompactTrieNode:
    """Use slots to reduce memory"""
    __slots__ = ['children', 'is_end', 'count']

    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0  # Optional: word frequency
```

### 3. Pruning
```python
def remove_word(trie, word):
    """Remove word and prune unnecessary nodes"""
    def dfs(node, depth):
        if depth == len(word):
            node.is_end = False
            return len(node.children) == 0

        char = word[depth]
        if char not in node.children:
            return False

        should_delete = dfs(node.children[char], depth + 1)

        if should_delete:
            del node.children[char]
            return not node.is_end and len(node.children) == 0

        return False

    dfs(trie.root, 0)
```

## Problem-Solving Strategy

1. **Identify Trie Applicability:**
   - Prefix-based queries?
   - Multiple string searches?
   - Autocomplete feature?
   - Word dictionary?

2. **Choose Representation:**
   - Dictionary for flexibility
   - Array for speed (fixed alphabet)
   - Compressed trie for space

3. **Decide on Metadata:**
   - Just presence: is_end flag
   - Count frequency: counter
   - Store word: word field
   - Sum values: sum field

4. **Consider Alternatives:**
   - Hash set for exact match
   - Suffix array for suffix queries
   - Aho-Corasick for multiple pattern matching

## Time and Space Complexity

### Trie Operations:
- **Insert:** O(m) where m is word length
- **Search:** O(m)
- **Prefix search:** O(m)
- **Delete:** O(m)
- **Space:** O(ALPHABET_SIZE * m * n) where n is number of words

### Comparison with Other Structures:
- **vs Hash Set:** Trie supports prefix queries, hash doesn't
- **vs BST:** Trie O(m) independent of n, BST O(m log n)
- **vs Suffix Array:** Trie easier to build, suffix array more space-efficient

## Common Mistakes

1. **Not handling empty strings**
2. **Forgetting end-of-word marker**
3. **Not pruning deleted words**
4. **Memory explosion with large alphabets**
5. **Not considering character encoding**

## Practice Tips

1. **Implement basic trie from scratch**
2. **Master dictionary vs array representation**
3. **Practice with wildcards**
4. **Learn suffix trie for advanced problems**
5. **Understand space-time tradeoffs**

## Use Cases

- **Autocomplete:** Search suggestions
- **Spell checker:** Find similar words
- **IP routing:** Longest prefix matching
- **String matching:** Multiple pattern search
- **Dictionary:** Prefix-based word lookup
- **Genome sequencing:** DNA sequence analysis

## Related Patterns

- **Backtracking:** Word search in grid with trie
- **DFS:** Traverse trie to collect words
- **Hash Map:** Alternative for exact match
- **Suffix Array/Tree:** For suffix-based queries
