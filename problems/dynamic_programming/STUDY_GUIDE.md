# Dynamic Programming Pattern - Study Guide

## Overview
Dynamic Programming (DP) is an optimization technique that solves complex problems by breaking them down into simpler subproblems. It stores solutions to subproblems to avoid redundant calculations. DP is applicable when a problem has optimal substructure and overlapping subproblems.

## When to Use Dynamic Programming

Signs that DP might be useful:
- Problem asks for maximum/minimum/optimal solution
- Problem asks to count total number of ways
- Problem involves making choices at each step
- Current decisions depend on previous decisions
- You can solve the problem recursively with overlapping subproblems

## Key Concepts

### 1. Optimal Substructure
The optimal solution can be constructed from optimal solutions of subproblems.

### 2. Overlapping Subproblems
The same subproblems are solved multiple times.

### 3. Memoization (Top-Down)
Store results of expensive function calls and return cached result when same inputs occur.

### 4. Tabulation (Bottom-Up)
Build solution iteratively from smallest subproblems to the target problem.

## DP Approaches

### Top-Down (Memoization)
```python
def fib_memoization(n, memo=None):
    """Fibonacci with memoization"""
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib_memoization(n-1, memo) + fib_memoization(n-2, memo)
    return memo[n]

# Time: O(n), Space: O(n)
```

### Bottom-Up (Tabulation)
```python
def fib_tabulation(n):
    """Fibonacci with tabulation"""
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

# Time: O(n), Space: O(n)


def fib_optimized(n):
    """Fibonacci with space optimization"""
    if n <= 1:
        return n

    prev2, prev1 = 0, 1

    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current

    return prev1

# Time: O(n), Space: O(1)
```

## Common DP Patterns

### 1. Linear DP (1D)

**Climbing Stairs:**
```python
def climb_stairs(n):
    """Ways to climb n stairs (1 or 2 steps at a time)"""
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2

    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

# Time: O(n), Space: O(n), can optimize to O(1)
```

**House Robber:**
```python
def rob(nums):
    """Max money robbing houses (can't rob adjacent)"""
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])

    return dp[n-1]

# Time: O(n), Space: O(n)


def rob_optimized(nums):
    """Space-optimized version"""
    if not nums:
        return 0

    prev2, prev1 = 0, 0

    for num in nums:
        current = max(prev1, prev2 + num)
        prev2, prev1 = prev1, current

    return prev1

# Time: O(n), Space: O(1)
```

**Maximum Subarray (Kadane's Algorithm):**
```python
def max_subarray(nums):
    """Find contiguous subarray with maximum sum"""
    max_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

# Time: O(n), Space: O(1)
```

### 2. 2D DP (Grid/Matrix)

**Unique Paths:**
```python
def unique_paths(m, n):
    """Number of paths from top-left to bottom-right"""
    dp = [[0] * n for _ in range(m)]

    # Initialize first row and column
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]

# Time: O(m*n), Space: O(m*n)


def unique_paths_optimized(m, n):
    """Space-optimized using 1D array"""
    dp = [1] * n

    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j-1]

    return dp[n-1]

# Time: O(m*n), Space: O(n)
```

**Minimum Path Sum:**
```python
def min_path_sum(grid):
    """Find path with minimum sum from top-left to bottom-right"""
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    dp[0][0] = grid[0][0]

    # Initialize first row
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    # Initialize first column
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    # Fill rest of table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    return dp[m-1][n-1]

# Time: O(m*n), Space: O(m*n)
```

**Longest Common Subsequence:**
```python
def longest_common_subsequence(text1, text2):
    """Find length of longest common subsequence"""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]

# Time: O(m*n), Space: O(m*n)
```

**Edit Distance:**
```python
def min_distance(word1, word2):
    """Minimum operations to convert word1 to word2"""
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # Delete
                    dp[i][j-1],    # Insert
                    dp[i-1][j-1]   # Replace
                )

    return dp[m][n]

# Time: O(m*n), Space: O(m*n)
```

### 3. Knapsack Pattern

**0/1 Knapsack:**
```python
def knapsack(weights, values, capacity):
    """Maximum value with capacity constraint"""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(
                    dp[i-1][w],  # Don't take item
                    dp[i-1][w - weights[i-1]] + values[i-1]  # Take item
                )
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]

# Time: O(n*W), Space: O(n*W)


def knapsack_optimized(weights, values, capacity):
    """Space-optimized version"""
    dp = [0] * (capacity + 1)

    for i in range(len(weights)):
        # Traverse backwards to avoid using updated values
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]

# Time: O(n*W), Space: O(W)
```

**Subset Sum:**
```python
def can_partition(nums):
    """Check if array can be partitioned into two equal subsets"""
    total = sum(nums)

    if total % 2 != 0:
        return False

    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]

    return dp[target]

# Time: O(n*sum), Space: O(sum)
```

**Coin Change:**
```python
def coin_change(coins, amount):
    """Minimum coins needed to make amount"""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

# Time: O(amount * n), Space: O(amount)


def coin_change_ways(coins, amount):
    """Number of ways to make amount"""
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]

# Time: O(amount * n), Space: O(amount)
```

### 4. Subsequence/Substring Patterns

**Longest Increasing Subsequence:**
```python
def length_of_lis(nums):
    """Length of longest increasing subsequence"""
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Time: O(n²), Space: O(n)


def length_of_lis_optimized(nums):
    """O(n log n) solution using binary search"""
    import bisect

    sub = []

    for num in nums:
        pos = bisect.bisect_left(sub, num)

        if pos == len(sub):
            sub.append(num)
        else:
            sub[pos] = num

    return len(sub)

# Time: O(n log n), Space: O(n)
```

**Longest Palindromic Substring:**
```python
def longest_palindrome(s):
    """Find longest palindromic substring"""
    n = len(s)
    if n < 2:
        return s

    dp = [[False] * n for _ in range(n)]
    start, max_len = 0, 1

    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2

    # Check substrings of length 3 and more
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_len = length

    return s[start:start + max_len]

# Time: O(n²), Space: O(n²)
```

**Palindromic Substrings Count:**
```python
def count_substrings(s):
    """Count all palindromic substrings"""
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    count = 0

    # Length 1
    for i in range(n):
        dp[i][i] = True
        count += 1

    # Length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            count += 1

    # Length 3+
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                count += 1

    return count

# Time: O(n²), Space: O(n²)
```

### 5. String/Pattern Matching

**Word Break:**
```python
def word_break(s, word_dict):
    """Check if s can be segmented into words from dictionary"""
    word_set = set(word_dict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # Empty string

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[n]

# Time: O(n² * m) where m is max word length, Space: O(n)
```

**Regular Expression Matching:**
```python
def is_match(s, p):
    """Match string with pattern (* and .)"""
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    dp[0][0] = True

    # Handle patterns like a*, a*b*, a*b*c*
    for j in range(2, n + 1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-2]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j-1] == '*':
                # Two cases: use * or don't use *
                dp[i][j] = dp[i][j-2]  # Don't use *

                if p[j-2] == '.' or p[j-2] == s[i-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j]  # Use *
            elif p[j-1] == '.' or p[j-1] == s[i-1]:
                dp[i][j] = dp[i-1][j-1]

    return dp[m][n]

# Time: O(m*n), Space: O(m*n)
```

### 6. Decision Making Patterns

**Best Time to Buy/Sell Stock:**
```python
def max_profit_one_transaction(prices):
    """Max profit with one transaction"""
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

# Time: O(n), Space: O(1)


def max_profit_unlimited(prices):
    """Max profit with unlimited transactions"""
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]

    return profit

# Time: O(n), Space: O(1)


def max_profit_k_transactions(prices, k):
    """Max profit with at most k transactions"""
    if not prices or k == 0:
        return 0

    n = len(prices)

    # If k >= n/2, unlimited transactions
    if k >= n // 2:
        return max_profit_unlimited(prices)

    # dp[i][j] = max profit with at most i transactions by day j
    dp = [[0] * n for _ in range(k + 1)]

    for i in range(1, k + 1):
        max_diff = -prices[0]
        for j in range(1, n):
            dp[i][j] = max(dp[i][j-1], prices[j] + max_diff)
            max_diff = max(max_diff, dp[i-1][j] - prices[j])

    return dp[k][n-1]

# Time: O(n*k), Space: O(n*k)
```

### 7. Game Theory / Min-Max

**Predict the Winner:**
```python
def predict_winner(nums):
    """Predict if player 1 can win"""
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    # Base case: choosing from single element
    for i in range(n):
        dp[i][i] = nums[i]

    # Fill diagonals
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = max(
                nums[i] - dp[i+1][j],  # Take left
                nums[j] - dp[i][j-1]   # Take right
            )

    return dp[0][n-1] >= 0

# Time: O(n²), Space: O(n²)
```

## DP Problem-Solving Framework

### Step 1: Identify if DP is Applicable
- Optimization problem (min/max)
- Counting problem
- Current choice depends on previous choices
- Can be solved recursively with overlapping subproblems

### Step 2: Define State
- What information do we need to track?
- `dp[i]` = answer for subproblem ending at index i
- `dp[i][j]` = answer for subproblem from i to j
- `dp[i][j][k]` = answer with additional constraint k

### Step 3: Define Recurrence Relation
- How does current state depend on previous states?
- Consider all possible choices at current step
- Example: `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`

### Step 4: Identify Base Cases
- What are the smallest subproblems?
- `dp[0] = ...`
- `dp[0][0] = ...`

### Step 5: Determine Computation Order
- Bottom-up: Compute smaller subproblems first
- Top-down: Use recursion with memoization

### Step 6: Optimize Space
- Can we use rolling array?
- Do we only need previous row/column?
- Can we reduce dimensions?

## Common DP Optimizations

### 1. Space Optimization
```python
# 2D -> 1D
# Instead of: dp[i][j] = dp[i-1][j] + dp[i][j-1]
# Use: dp[j] = dp[j] + dp[j-1]

# Keep only last row/column needed
```

### 2. State Compression
```python
# Use bit manipulation for state representation
# Example: visited cities in TSP
state = (1 << n) - 1  # All cities visited
```

### 3. Dimension Reduction
```python
# If only need previous value, use variables instead of array
prev, curr = 0, 1
```

## Time and Space Complexity

### Common Patterns:
- **1D DP:** O(n) time, O(n) or O(1) space
- **2D DP:** O(n²) or O(m*n) time, O(n²) or O(m*n) space
- **Knapsack:** O(n*W) time, O(W) space
- **LCS/Edit Distance:** O(m*n) time and space

## Common Mistakes

1. **Not identifying overlapping subproblems**
2. **Wrong base cases**
3. **Incorrect recurrence relation**
4. **Array index out of bounds**
5. **Not considering all possible transitions**
6. **Forgetting to initialize DP table**

## Practice Tips

1. **Start with recursive solution**
2. **Identify repeated computations**
3. **Add memoization**
4. **Convert to bottom-up if needed**
5. **Optimize space**
6. **Draw the DP table for small examples**

## Related Patterns

- **Greedy:** Sometimes DP can be optimized to greedy
- **Backtracking:** DP can optimize backtracking with memoization
- **Divide and Conquer:** DP is divide and conquer with memoization
