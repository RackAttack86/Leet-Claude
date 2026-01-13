# Quick Start Guide

Welcome to Leet-Claude! This guide will get you solving problems in 5 minutes.

## Setup (One Time)

```bash
# Install dependencies
pip install -r requirements.txt

# Install package
pip install -e .
```

## Your First Problem

Let's solve **Binary Search (#704)** - a classic algorithm:

### Step 1: Open the Problem

```bash
# Open in your editor
code problems/binary_search/p0704_binary-search/solution.py
```

### Step 2: Read the Hints

Check [PROBLEM_HINTS.md](PROBLEM_HINTS.md) for approach hints:

**#704 Binary Search**
- **Hint:** Compare mid with target, adjust search range
- **Pattern:** Standard binary search
- **Time:** O(log n)

### Step 3: Implement

Replace the `solve()` method with your solution:

```python
def search(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

### Step 4: Write Tests

Open the test file and add test cases:

```bash
code problems/binary_search/p0704_binary-search/test_solution.py
```

```python
def test_example_1(self, solution):
    assert solution.search([-1,0,3,5,9,12], 9) == 4

def test_not_found(self, solution):
    assert solution.search([-1,0,3,5,9,12], 2) == -1
```

### Step 5: Run Tests

```bash
python -m pytest problems/binary_search/p0704_binary-search/ -v
```

### Step 6: Track Progress

```bash
python scripts/generate_progress.py
```

## Next Steps

### Recommended Learning Path

**Week 1: Easy Two Pointers**
1. #1 Two Sum (Already solved! ✓)
2. #125 Valid Palindrome (Already solved! ✓)
3. #283 Move Zeroes

**Week 2: More Easy Problems**
4. #704 Binary Search
5. #20 Valid Parentheses
6. #206 Reverse Linked List

**Week 3: Trees**
7. #226 Invert Binary Tree
8. #104 Maximum Depth
9. #100 Same Tree

**Week 4: Medium Problems**
10. #15 3Sum
11. #200 Number of Islands
12. #198 House Robber

## Common Commands

```bash
# Create new problem
python scripts/create_problem.py -n 206 --name "Reverse Linked List" -p linked_lists -d Easy

# Run all tests
python -m pytest

# Run tests by difficulty
python -m pytest -m easy
python -m pytest -m medium

# Run tests by pattern
python -m pytest problems/two_pointers/ -v

# Check progress
python scripts/generate_progress.py
```

## Getting Hints

Three places to find help:

1. **Pattern README** - Check `problems/{pattern}/README.md` for pattern overview
2. **Problem Hints** - Check [PROBLEM_HINTS.md](PROBLEM_HINTS.md) for specific problem hints
3. **Example Solutions** - Look at completed solutions (#1, #70, #125)

## Problem-Solving Framework

For any problem, follow these steps:

### 1. Understand
- Read the problem carefully
- Understand inputs, outputs, constraints
- Work through examples manually

### 2. Pattern Recognition
- What pattern does this fit?
- Array/String + pairs = Two Pointers?
- Need all combinations = Backtracking?
- Optimization problem = DP/Greedy?

### 3. Plan
- Start with brute force
- Identify bottlenecks
- Apply pattern to optimize

### 4. Code
- Implement solution
- Add clear comments
- Use good variable names

### 5. Test
- Test with examples
- Test edge cases
- Verify complexity

### 6. Optimize
- Can you do better?
- Different approach?
- Trade time for space or vice versa?

## Tips for Success

✅ **Do:** Focus on understanding patterns
❌ **Don't:** Memorize solutions

✅ **Do:** Solve 1-2 problems daily consistently
❌ **Don't:** Try to solve 10 problems in one day

✅ **Do:** Write your own tests
❌ **Don't:** Just copy test cases

✅ **Do:** Implement multiple approaches
❌ **Don't:** Stop at first working solution

✅ **Do:** Track your progress weekly
❌ **Don't:** Rush through problems

## When You're Stuck

1. **Read the hint** in PROBLEM_HINTS.md
2. **Check the pattern README** for template code
3. **Look at a similar solved problem** (#1, #70, #125)
4. **Break it down** - solve a simpler version first
5. **Come back later** - sometimes a break helps!

## Resources

- [PROBLEM_HINTS.md](PROBLEM_HINTS.md) - Hints for all 50 problems
- [Pattern READMEs](../problems/) - Templates and tips for each pattern
- [Main README](../README.md) - Full documentation

Happy coding! 🚀
