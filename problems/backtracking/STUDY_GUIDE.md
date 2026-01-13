# Backtracking Pattern - Study Guide

## Overview
Backtracking is an algorithmic technique that builds candidates for solutions incrementally and abandons a candidate ("backtracks") as soon as it determines the candidate cannot lead to a valid solution. It's essentially a refined brute force approach with pruning.

## When to Use Backtracking

- Finding all possible solutions (not just one)
- Problems involving combinations, permutations, subsets
- Constraint satisfaction problems (N-Queens, Sudoku)
- Path finding with constraints
- Decision problems where you need to try all possibilities
- Problems where you make a choice, explore, then undo that choice

## Backtracking Template

```python
def backtrack(path, choices):
    """General backtracking template"""
    if is_solution(path):
        output(path)
        return

    for choice in choices:
        if is_valid(choice, path):
            # Make choice
            path.append(choice)

            # Explore
            backtrack(path, remaining_choices)

            # Undo choice (backtrack)
            path.pop()

# Key steps:
# 1. Choose - make a decision
# 2. Explore - recursively explore consequences
# 3. Unchoose - undo the decision (backtrack)
```

## Common Backtracking Patterns

### 1. Permutations

**All Permutations:**
```python
def permute(nums):
    """Generate all permutations"""
    result = []

    def backtrack(path, remaining):
        if not remaining:
            result.append(path[:])  # Copy path
            return

        for i in range(len(remaining)):
            # Choose
            path.append(remaining[i])

            # Explore
            backtrack(path, remaining[:i] + remaining[i+1:])

            # Unchoose
            path.pop()

    backtrack([], nums)
    return result

# Time: O(n! * n), Space: O(n!)


def permute_optimized(nums):
    """Permutations using swap method (more efficient)"""
    result = []

    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return

        for i in range(start, len(nums)):
            # Swap
            nums[start], nums[i] = nums[i], nums[start]

            # Explore
            backtrack(start + 1)

            # Backtrack (swap back)
            nums[start], nums[i] = nums[i], nums[start]

    backtrack(0)
    return result

# Time: O(n! * n), Space: O(n)
```

**Permutations with Duplicates:**
```python
def permute_unique(nums):
    """Generate unique permutations (with duplicates in input)"""
    result = []
    nums.sort()  # Sort to handle duplicates

    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            # Skip if used
            if used[i]:
                continue

            # Skip duplicates: if same as previous and previous not used
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue

            # Choose
            path.append(nums[i])
            used[i] = True

            # Explore
            backtrack(path, used)

            # Unchoose
            path.pop()
            used[i] = False

    backtrack([], [False] * len(nums))
    return result

# Time: O(n! * n), Space: O(n!)
```

### 2. Combinations

**Generate Combinations:**
```python
def combine(n, k):
    """Generate all combinations of k numbers from 1 to n"""
    result = []

    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return

        for i in range(start, n + 1):
            # Choose
            path.append(i)

            # Explore
            backtrack(i + 1, path)  # Next must be > i

            # Unchoose
            path.pop()

    backtrack(1, [])
    return result

# Time: O(C(n,k) * k), Space: O(C(n,k))


def combination_sum(candidates, target):
    """Find all combinations that sum to target (can reuse)"""
    result = []
    candidates.sort()

    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return

        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            # Can reuse same element, so pass i (not i+1)
            backtrack(i, path, remaining - candidates[i])
            path.pop()

    backtrack(0, [], target)
    return result

# Time: O(n^(target/min)), Space: O(target/min)
```

**Combination Sum II (No Reuse, With Duplicates):**
```python
def combination_sum2(candidates, target):
    """Combinations summing to target, each number used once"""
    result = []
    candidates.sort()

    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return

        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            # Skip duplicates
            if i > start and candidates[i] == candidates[i-1]:
                continue

            path.append(candidates[i])
            backtrack(i + 1, path, remaining - candidates[i])
            path.pop()

    backtrack(0, [], target)
    return result

# Time: O(2^n), Space: O(n)
```

### 3. Subsets

**All Subsets:**
```python
def subsets(nums):
    """Generate all subsets (power set)"""
    result = []

    def backtrack(start, path):
        result.append(path[:])  # Add current subset

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result

# Time: O(2^n * n), Space: O(2^n)


def subsets_iterative(nums):
    """Iterative approach"""
    result = [[]]

    for num in nums:
        result += [curr + [num] for curr in result]

    return result

# Time: O(2^n * n), Space: O(2^n)
```

**Subsets with Duplicates:**
```python
def subsets_with_dup(nums):
    """Generate unique subsets with duplicates in input"""
    result = []
    nums.sort()

    def backtrack(start, path):
        result.append(path[:])

        for i in range(start, len(nums)):
            # Skip duplicates
            if i > start and nums[i] == nums[i-1]:
                continue

            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result

# Time: O(2^n * n), Space: O(2^n)
```

### 4. Grid/Board Problems

**N-Queens:**
```python
def solve_n_queens(n):
    """Place n queens on n×n board"""
    result = []
    board = [['.'] * n for _ in range(n)]
    cols = set()
    diag1 = set()  # row - col
    diag2 = set()  # row + col

    def backtrack(row):
        if row == n:
            result.append([''.join(row) for row in board])
            return

        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue

            # Place queen
            board[row][col] = 'Q'
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            # Explore
            backtrack(row + 1)

            # Remove queen
            board[row][col] = '.'
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)
    return result

# Time: O(n!), Space: O(n²)
```

**Sudoku Solver:**
```python
def solve_sudoku(board):
    """Solve Sudoku puzzle"""
    def is_valid(row, col, num):
        # Check row
        if num in board[row]:
            return False

        # Check column
        if num in [board[i][col] for i in range(9)]:
            return False

        # Check 3x3 box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if board[i][j] == num:
                    return False

        return True

    def backtrack():
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in '123456789':
                        if is_valid(i, j, num):
                            board[i][j] = num

                            if backtrack():
                                return True

                            board[i][j] = '.'  # Backtrack

                    return False  # No valid number found

        return True  # All cells filled

    backtrack()

# Time: O(9^m) where m is empty cells, Space: O(m)
```

**Word Search:**
```python
def exist(board, word):
    """Find if word exists in board"""
    rows, cols = len(board), len(board[0])

    def backtrack(row, col, index):
        if index == len(word):
            return True

        if (row < 0 or row >= rows or
            col < 0 or col >= cols or
            board[row][col] != word[index]):
            return False

        # Mark as visited
        temp = board[row][col]
        board[row][col] = '#'

        # Explore all 4 directions
        found = (backtrack(row + 1, col, index + 1) or
                 backtrack(row - 1, col, index + 1) or
                 backtrack(row, col + 1, index + 1) or
                 backtrack(row, col - 1, index + 1))

        # Unmark (backtrack)
        board[row][col] = temp

        return found

    for i in range(rows):
        for j in range(cols):
            if backtrack(i, j, 0):
                return True

    return False

# Time: O(m*n*4^L) where L is word length, Space: O(L)
```

### 5. Partition Problems

**Palindrome Partitioning:**
```python
def partition(s):
    """Partition s into all possible palindrome substrings"""
    result = []

    def is_palindrome(sub):
        return sub == sub[::-1]

    def backtrack(start, path):
        if start == len(s):
            result.append(path[:])
            return

        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                path.append(substring)
                backtrack(end, path)
                path.pop()

    backtrack(0, [])
    return result

# Time: O(n * 2^n), Space: O(n)
```

### 6. Expression Generation

**Generate Parentheses:**
```python
def generate_parenthesis(n):
    """Generate all valid parentheses combinations"""
    result = []

    def backtrack(path, open_count, close_count):
        if len(path) == 2 * n:
            result.append(''.join(path))
            return

        if open_count < n:
            path.append('(')
            backtrack(path, open_count + 1, close_count)
            path.pop()

        if close_count < open_count:
            path.append(')')
            backtrack(path, open_count, close_count + 1)
            path.pop()

    backtrack([], 0, 0)
    return result

# Time: O(4^n / sqrt(n)), Space: O(n)
```

**Expression Add Operators:**
```python
def add_operators(num, target):
    """Add operators (+, -, *) to get target"""
    result = []

    def backtrack(index, path, value, prev):
        if index == len(num):
            if value == target:
                result.append(path)
            return

        for i in range(index, len(num)):
            # Skip leading zeros
            if i != index and num[index] == '0':
                break

            curr_str = num[index:i+1]
            curr = int(curr_str)

            if index == 0:
                backtrack(i + 1, curr_str, curr, curr)
            else:
                # Addition
                backtrack(i + 1, path + '+' + curr_str, value + curr, curr)

                # Subtraction
                backtrack(i + 1, path + '-' + curr_str, value - curr, -curr)

                # Multiplication (need to undo previous operation)
                backtrack(i + 1, path + '*' + curr_str,
                         value - prev + prev * curr, prev * curr)

    backtrack(0, "", 0, 0)
    return result

# Time: O(4^n), Space: O(n)
```

### 7. Path Finding

**All Paths from Source to Target:**
```python
def all_paths_source_target(graph):
    """Find all paths from 0 to n-1"""
    n = len(graph)
    result = []

    def backtrack(node, path):
        if node == n - 1:
            result.append(path[:])
            return

        for neighbor in graph[node]:
            path.append(neighbor)
            backtrack(neighbor, path)
            path.pop()

    backtrack(0, [0])
    return result

# Time: O(2^n * n), Space: O(n)
```

## Optimization Techniques

### 1. Pruning
```python
def backtrack_with_pruning(path, choices):
    # Early termination conditions
    if is_invalid(path):
        return  # Prune this branch

    if is_solution(path):
        output(path)
        return

    for choice in choices:
        if can_lead_to_solution(choice, path):  # Pruning
            path.append(choice)
            backtrack_with_pruning(path, remaining)
            path.pop()
```

### 2. Memoization (DP with Backtracking)
```python
def backtrack_with_memo(state, memo):
    if state in memo:
        return memo[state]

    if is_base_case(state):
        return base_value

    result = []
    for choice in get_choices(state):
        result.extend(backtrack_with_memo(new_state, memo))

    memo[state] = result
    return result
```

### 3. State Representation
```python
# Use tuples for hashable state
state = (tuple(path), remaining_target)

# Use bit masks for visited sets
visited = (1 << n) - 1  # All visited

# Use frozenset for unordered collections
state = frozenset(used_elements)
```

## Backtracking vs Other Techniques

### Backtracking vs Brute Force
- Backtracking prunes invalid branches early
- Brute force generates all possibilities then filters

### Backtracking vs Dynamic Programming
- Backtracking finds all solutions
- DP finds optimal solution
- DP has optimal substructure, backtracking may not

### Backtracking vs Greedy
- Backtracking explores all possibilities
- Greedy makes locally optimal choices
- Greedy faster but may miss global optimum

## Problem-Solving Strategy

1. **Identify Backtracking:**
   - Need all solutions?
   - Multiple choices at each step?
   - Can recognize invalid paths early?

2. **Define State:**
   - What represents current progress?
   - What choices are available?
   - When is solution complete?

3. **Implement Template:**
   - Base case (solution found)
   - Make choice
   - Recurse with new state
   - Undo choice (backtrack)

4. **Optimize:**
   - Add pruning conditions
   - Sort input for better pruning
   - Use memoization if subproblems overlap

5. **Handle Edge Cases:**
   - Empty input
   - Single element
   - Duplicates
   - No valid solution

## Time and Space Complexity

### Typical Complexities:
- **Permutations:** O(n! * n) time, O(n!) space
- **Combinations:** O(2^n * n) time, O(2^n) space
- **Subsets:** O(2^n * n) time, O(2^n) space
- **N-Queens:** O(n!) time, O(n²) space
- **Sudoku:** O(9^m) where m is empty cells

### Space Complexity Factors:
- Recursion stack depth: O(h) where h is max depth
- Storing results: O(number of solutions)
- Temporary state: O(state size)

## Common Mistakes

1. **Forgetting to backtrack (undo choice)**
2. **Modifying shared state without undoing**
3. **Not handling duplicates correctly**
4. **Missing base case**
5. **Not pruning when possible**
6. **Shallow copy vs deep copy of path**

## Practice Tips

1. **Master the template**
2. **Draw the decision tree**
3. **Start with permutations/combinations**
4. **Practice with and without duplicates**
5. **Learn pruning techniques**
6. **Understand when to backtrack**

## Related Patterns

- **DFS:** Backtracking is DFS with pruning
- **Dynamic Programming:** Can optimize some backtracking
- **Branch and Bound:** Extension of backtracking
- **Constraint Satisfaction:** Uses backtracking
