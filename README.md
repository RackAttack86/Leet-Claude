# Leet-Claude: LeetCode Mastery by Pattern

A comprehensive LeetCode learning environment organized by coding patterns, with detailed explanations, multiple approaches, and comprehensive test coverage using Python and pytest.

## Quick Start

### Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Install package in development mode (recommended)
pip install -e .
```

### Running Tests

```bash
# Run all tests
pytest

# Run tests for a specific problem
pytest problems/two_pointers/p0001_two-sum/

# Run tests for a specific pattern
pytest problems/two_pointers/

# Run by difficulty
pytest -m easy
pytest -m medium
pytest -m hard

# Skip slow tests
pytest -m "not slow"

# Run with coverage
pytest --cov=problems --cov-report=html
```

### Adding a New Problem

```bash
# Use the scaffolding script
python scripts/create_problem.py \
  --number 1 \
  --name "Two Sum" \
  --pattern two_pointers \
  --difficulty Easy

# Then edit the generated files:
# - solution.py: Implement your solution
# - test_solution.py: Add comprehensive test cases
# - README.md: Document your approach
```

### Generate Progress Report

```bash
python scripts/generate_progress.py
```

## Project Structure

```
Leet-Claude/
├── problems/              # Solutions organized by pattern
│   ├── two_pointers/
│   ├── sliding_window/
│   ├── binary_search/
│   ├── bfs_dfs/
│   ├── dynamic_programming/
│   ├── backtracking/
│   ├── greedy/
│   ├── graphs/
│   ├── trees/
│   ├── heaps/
│   ├── tries/
│   ├── intervals/
│   ├── linked_lists/
│   ├── stacks_queues/
│   └── bit_manipulation/
│
├── utils/                 # Common data structures and helpers
│   ├── data_structures.py # ListNode, TreeNode, Node
│   ├── test_helpers.py    # Testing utilities
│   └── decorators.py      # Timing, memoization
│
├── scripts/               # Automation tools
│   ├── create_problem.py  # Scaffold new problems
│   ├── run_pattern.py     # Run tests by pattern
│   └── generate_progress.py # Progress reports
│
└── docs/                  # Learning materials (TBD)
    └── patterns/          # Pattern-specific guides
```

## 15 Patterns Covered

### 1. Two Pointers
Opposite direction, same direction, fast & slow pointer techniques.
**Use for:** Sorted arrays, finding pairs, removing duplicates, cycle detection.

### 2. Sliding Window
Fixed and variable size windows for substring/subarray problems.
**Use for:** Longest/shortest substring, subarrays with conditions.

### 3. Binary Search
Classic binary search and its variations.
**Use for:** Searching sorted arrays, finding boundaries, answer search.

### 4. BFS/DFS
Tree and graph traversal, backtracking.
**Use for:** Tree/graph problems, level-order traversal, paths.

### 5. Dynamic Programming
1D, 2D, knapsack, and subsequence problems.
**Use for:** Optimization, counting paths, subsequences.

### 6. Backtracking
Combinations, permutations, subsets.
**Use for:** Finding all solutions, constraint satisfaction.

### 7. Greedy
Interval scheduling and optimization.
**Use for:** Local optimal choices leading to global optimum.

### 8. Graphs
Shortest path, MST, topological sort.
**Use for:** Graph connectivity, shortest paths, dependencies.

### 9. Trees
Binary trees, BST, tree traversals.
**Use for:** Hierarchical data, tree properties.

### 10. Heaps
Priority queues, k-way merge.
**Use for:** Top K elements, median finding, scheduling.

### 11. Tries
Prefix trees and autocomplete.
**Use for:** Prefix matching, word search.

### 12. Intervals
Merge, insert, scheduling intervals.
**Use for:** Time intervals, range problems.

### 13. Linked Lists
Reversal, cycles, merge operations.
**Use for:** Sequential data, in-place operations.

### 14. Stacks/Queues
Monotonic stacks, deques.
**Use for:** Next greater element, sliding window maximum.

### 15. Bit Manipulation
XOR tricks, counting bits.
**Use for:** Low-level operations, optimization.

## LeetCode Problem-Solving Framework

### Step 1: Understand the Problem
1. Read the problem statement carefully
2. Identify inputs, outputs, and constraints
3. Work through the examples manually
4. Ask clarifying questions (edge cases, assumptions)

### Step 2: Recognize the Pattern
- Does it involve pairs or subarrays? → Two Pointers / Sliding Window
- Is the input sorted? → Binary Search / Two Pointers
- Need all combinations/permutations? → Backtracking
- Optimization problem? → Dynamic Programming / Greedy
- Graph/tree structure? → BFS/DFS
- Top K elements? → Heap
- Prefix matching? → Trie

### Step 3: Start Simple
1. **Brute force first**: Solve it any way you can
2. **Test your logic**: Walk through examples
3. **Analyze complexity**: What's the time/space cost?

### Step 4: Optimize
1. **Identify bottlenecks**: Where is time wasted?
2. **Apply patterns**: Which pattern reduces complexity?
3. **Trade-offs**: Space for time? Time for simplicity?

### Step 5: Implement & Test
1. Write clean, readable code
2. Add comments for complex logic
3. Test with examples and edge cases
4. Verify time/space complexity

## Tips for LeetCode Success

### General Strategy
- **Pattern recognition is key**: Focus on learning patterns, not memorizing solutions
- **Practice consistently**: Do 1-2 problems daily rather than 10 in one day
- **Start with Easy**: Build confidence and pattern recognition
- **Understand, don't memorize**: Understand why a solution works
- **Time yourself**: Practice under interview conditions (45 minutes)

### Common Patterns to Recognize

**"Find pair/triplet with sum"** → Two Pointers (if sorted) or Hash Map
**"Longest/shortest substring with condition"** → Sliding Window
**"Find in sorted array"** → Binary Search
**"All combinations/permutations"** → Backtracking
**"Min/max path/cost"** → Dynamic Programming
**"Tree level-by-level"** → BFS
**"Tree recursive property"** → DFS
**"Top K elements"** → Heap
**"Prefix matching"** → Trie
**"Merge intervals"** → Sorting + Intervals
**"Detect cycle"** → Fast & Slow Pointers

### Complexity Analysis Quick Reference

**O(1)** - Constant: Hash map lookup, array access
**O(log n)** - Logarithmic: Binary search, balanced tree operations
**O(n)** - Linear: Single loop, hash map creation
**O(n log n)** - Linearithmic: Sorting, heap operations
**O(n²)** - Quadratic: Nested loops, bubble sort
**O(2ⁿ)** - Exponential: Recursive backtracking

### Common Tricks & Techniques

1. **Hash Map for O(1) lookups**: Trade space for time
2. **Two Pointers**: Reduce O(n²) to O(n) for many problems
3. **Sliding Window**: Track window state incrementally
4. **Binary Search variations**: Search for answers, not just elements
5. **DFS + Memoization = DP**: Top-down dynamic programming
6. **Fast & Slow Pointers**: Cycle detection in O(1) space
7. **Monotonic Stack**: Next greater/smaller element in O(n)
8. **XOR properties**: Find unique elements, swap without temp
9. **Prefix Sum**: Range queries in O(1)
10. **Union-Find**: Connected components efficiently

## Example Problem Structure

Each problem follows this structure:

```
problems/two_pointers/p0001_two-sum/
├── solution.py        # Implementation with multiple approaches
├── test_solution.py   # Comprehensive test cases
└── README.md          # Problem explanation and insights
```

### solution.py includes:
- Problem description and constraints
- Multiple solution approaches
- Time and space complexity analysis
- Detailed comments and docstrings
- Metadata for tracking

### test_solution.py includes:
- Example test cases from LeetCode
- Edge cases and boundary conditions
- Parametrized tests
- Metadata validation

## Recommended Learning Path

### Weeks 1-2: Foundations
- **Two Pointers**: #1, #167, #15, #11
- **Arrays/Hash Tables**: #217, #242, #49

### Weeks 3-4: Search & Sort
- **Binary Search**: #704, #33, #34
- **Sliding Window**: #121, #3, #424

### Weeks 5-6: Trees
- **Tree Basics**: #226, #104, #100
- **BFS/DFS**: #102, #200, #133

### Weeks 7-8: Dynamic Programming Intro
- **1D DP**: #70, #198, #322
- **String DP**: #5, #72

### Weeks 9-10: Advanced Patterns
- **Backtracking**: #46, #78, #39
- **Greedy**: #55, #122, #45

### Weeks 11-12: Graphs & Advanced Trees
- **Graphs**: #207, #743, #261
- **Advanced Trees**: #98, #235, #297

### Weeks 13-14: Data Structures
- **Heaps**: #215, #347, #23
- **Tries**: #208, #212

### Weeks 15-16: Advanced DP
- **2D DP**: #62, #64, #72
- **Interval problems**: #56, #57, #435

## Progress Tracking

Run the progress report to see your achievements:

```bash
python scripts/generate_progress.py
```

Shows:
- Total problems solved
- Breakdown by difficulty
- Breakdown by pattern
- Recent solutions

## Contributing

Add your solutions:
1. Use `create_problem.py` to scaffold
2. Implement solution in `solution.py`
3. Add comprehensive tests in `test_solution.py`
4. Document your approach in the problem's `README.md`
5. Update the pattern's `README.md` checklist

## Example Usage

```bash
# Create a new problem
python scripts/create_problem.py -n 15 --name "3Sum" -p two_pointers -d Medium

# Implement the solution
# Edit problems/two_pointers/p0015_3sum/solution.py

# Run the tests
pytest problems/two_pointers/p0015_3sum/ -v

# Check your progress
python scripts/generate_progress.py
```

## Resources

- [LeetCode](https://leetcode.com)
- Pattern guides in each pattern's README.md
- Problem-specific READMEs with multiple approaches

## License

MIT License - Use freely for learning purposes

---

**Happy Coding!** Master patterns, not just problems.
