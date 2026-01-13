# Binary Search Pattern - Study Guide

## Overview
Binary Search is a divide-and-conquer algorithm that efficiently searches for a target value in a sorted data structure by repeatedly dividing the search space in half. The pattern can be extended beyond simple searching to solve optimization and "feasibility check" problems.

## When to Use Binary Search
- Searching in a sorted array
- Finding insertion position
- Finding first/last occurrence of a value
- Searching in rotated sorted arrays
- Optimization problems with monotonic property
- Finding square root, peak element
- Matrix search (if sorted)
- "Minimize maximum" or "maximize minimum" problems

## Core Binary Search Template

### Standard Binary Search (Iterative)
```python
def binary_search(arr, target):
    """Find target in sorted array, return index or -1"""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half

    return -1  # Not found

# Time: O(log n), Space: O(1)
```

### Standard Binary Search (Recursive)
```python
def binary_search_recursive(arr, target, left=0, right=None):
    """Recursive implementation of binary search"""
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1  # Base case: not found

    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Time: O(log n), Space: O(log n) due to recursion stack
```

## Binary Search Variants

### 1. Find First/Last Occurrence
```python
def find_first_occurrence(arr, target):
    """Find leftmost (first) occurrence of target"""
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result

# Time: O(log n), Space: O(1)
# Example: [1,2,2,2,3], target=2 -> 1


def find_last_occurrence(arr, target):
    """Find rightmost (last) occurrence of target"""
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continue searching right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result

# Time: O(log n), Space: O(1)
# Example: [1,2,2,2,3], target=2 -> 3
```

### 2. Find Insertion Position (Lower Bound)
```python
def find_insert_position(arr, target):
    """Find the index where target should be inserted to keep array sorted"""
    left, right = 0, len(arr)  # Note: right = len(arr), not len(arr) - 1

    while left < right:  # Note: left < right, not <=
        mid = left + (right - left) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid  # Don't exclude mid, it might be answer

    return left  # left == right at end

# Time: O(log n), Space: O(1)
# Example: [1,3,5,6], target=2 -> 1
# Example: [1,3,5,6], target=5 -> 2


def lower_bound(arr, target):
    """Find first position where arr[i] >= target"""
    left, right = 0, len(arr)

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left  # Index of first element >= target


def upper_bound(arr, target):
    """Find first position where arr[i] > target"""
    left, right = 0, len(arr)

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] <= target:  # Note: <= instead of <
            left = mid + 1
        else:
            right = mid

    return left  # Index of first element > target
```

### 3. Search in Rotated Sorted Array
```python
def search_rotated(arr, target):
    """Search in rotated sorted array (no duplicates)"""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        # Determine which half is sorted
        if arr[left] <= arr[mid]:  # Left half is sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1  # Target in left half
            else:
                left = mid + 1   # Target in right half
        else:  # Right half is sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1   # Target in right half
            else:
                right = mid - 1  # Target in left half

    return -1

# Time: O(log n), Space: O(1)
# Example: [4,5,6,7,0,1,2], target=0 -> 4
```

### 4. Find Minimum in Rotated Sorted Array
```python
def find_min_rotated(arr):
    """Find minimum element in rotated sorted array"""
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        # Compare mid with right to determine which half has minimum
        if arr[mid] > arr[right]:
            # Minimum is in right half
            left = mid + 1
        else:
            # Minimum is in left half (including mid)
            right = mid

    return arr[left]  # left == right at end

# Time: O(log n), Space: O(1)
# Example: [4,5,6,7,0,1,2] -> 0


def find_min_with_duplicates(arr):
    """Find minimum in rotated sorted array with duplicates"""
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] > arr[right]:
            left = mid + 1
        elif arr[mid] < arr[right]:
            right = mid
        else:
            # arr[mid] == arr[right], can't determine which half
            right -= 1  # Worst case O(n)

    return arr[left]

# Time: O(log n) average, O(n) worst case, Space: O(1)
```

### 5. Find Peak Element
```python
def find_peak(arr):
    """Find a peak element (greater than neighbors)"""
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] < arr[mid + 1]:
            # Peak is in right half
            left = mid + 1
        else:
            # Peak is in left half (including mid)
            right = mid

    return left  # Peak index

# Time: O(log n), Space: O(1)
# Example: [1,2,3,1] -> 2 (element 3)
# Example: [1,2,1,3,5,6,4] -> 5 (element 6) or 1 (element 2)
```

## Binary Search on Answer Space

This powerful technique uses binary search to find an optimal value by searching through possible answers rather than array indices.

### Template for Binary Search on Answer
```python
def binary_search_on_answer(arr, target):
    """Template for binary search on answer space"""

    def is_feasible(mid):
        """Check if 'mid' is a valid/feasible answer"""
        # Implement problem-specific feasibility check
        # Return True if mid satisfies the condition
        pass

    left = min_possible_answer
    right = max_possible_answer
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if is_feasible(mid):
            result = mid
            # Depending on problem: minimize or maximize
            right = mid - 1  # For minimization
            # left = mid + 1  # For maximization
        else:
            left = mid + 1   # For minimization
            # right = mid - 1  # For maximization

    return result
```

### Example - Capacity to Ship Packages
```python
def ship_within_days(weights, days):
    """Find minimum ship capacity to ship all packages within days"""

    def can_ship(capacity):
        """Check if all packages can be shipped in 'days' with 'capacity'"""
        current_load = 0
        days_needed = 1

        for weight in weights:
            if current_load + weight > capacity:
                days_needed += 1
                current_load = weight
            else:
                current_load += weight

        return days_needed <= days

    # Answer must be between max(weights) and sum(weights)
    left = max(weights)  # Must carry heaviest package
    right = sum(weights)  # Can carry all at once

    while left < right:
        mid = left + (right - left) // 2

        if can_ship(mid):
            right = mid  # Try smaller capacity
        else:
            left = mid + 1  # Need larger capacity

    return left

# Time: O(n * log(sum - max)), Space: O(1)
```

### Example - Minimum Time to Complete Tasks
```python
def min_time_to_complete(tasks, workers):
    """Find minimum time needed to complete all tasks with workers"""

    def can_complete(time):
        """Check if all tasks can be completed in 'time' with workers"""
        tasks_completed = 0

        for worker_speed in workers:
            tasks_completed += time // worker_speed
            if tasks_completed >= tasks:
                return True

        return tasks_completed >= tasks

    left, right = 1, max(tasks) * tasks  # Reasonable bounds

    while left < right:
        mid = left + (right - left) // 2

        if can_complete(mid):
            right = mid  # Try less time
        else:
            left = mid + 1  # Need more time

    return left

# Time: O(m * log(max_time)), Space: O(1)
```

### Example - Koko Eating Bananas
```python
def min_eating_speed(piles, h):
    """Find minimum eating speed to finish all bananas in h hours"""
    import math

    def can_finish(speed):
        """Check if can finish all piles at this speed in h hours"""
        hours_needed = 0
        for pile in piles:
            hours_needed += math.ceil(pile / speed)
        return hours_needed <= h

    left = 1  # Minimum speed
    right = max(piles)  # Maximum speed needed

    while left < right:
        mid = left + (right - left) // 2

        if can_finish(mid):
            right = mid  # Try slower speed
        else:
            left = mid + 1  # Need faster speed

    return left

# Time: O(n * log(max_pile)), Space: O(1)
```

### Example - Split Array Largest Sum
```python
def split_array(nums, m):
    """Split array into m subarrays to minimize largest subarray sum"""

    def can_split(max_sum):
        """Check if can split into m subarrays with each sum <= max_sum"""
        splits = 1
        current_sum = 0

        for num in nums:
            if current_sum + num > max_sum:
                splits += 1
                current_sum = num
            else:
                current_sum += num

        return splits <= m

    left = max(nums)  # At least the largest element
    right = sum(nums)  # All in one subarray

    while left < right:
        mid = left + (right - left) // 2

        if can_split(mid):
            right = mid  # Try smaller maximum sum
        else:
            left = mid + 1  # Need larger maximum sum

    return left

# Time: O(n * log(sum)), Space: O(1)
```

## Binary Search in 2D

### Search in 2D Matrix (Sorted Rows and Columns)
```python
def search_matrix_sorted_rows_cols(matrix, target):
    """Search in matrix where rows and columns are sorted"""
    if not matrix or not matrix[0]:
        return False

    # Start from top-right corner
    row, col = 0, len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1  # Go down
        else:
            col -= 1  # Go left

    return False

# Time: O(m + n), Space: O(1)
# Note: Not pure binary search, but efficient for this structure
```

### Search in Row-Wise and Column-Wise Sorted Matrix
```python
def search_matrix_fully_sorted(matrix, target):
    """Search in matrix where rows are sorted and first element of each row
    is greater than last element of previous row (treats as 1D sorted array)"""
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = left + (right - left) // 2
        # Convert 1D index to 2D coordinates
        mid_value = matrix[mid // n][mid % n]

        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

# Time: O(log(m*n)), Space: O(1)
```

## Advanced Binary Search Patterns

### 1. Find Kth Smallest Element in Sorted Matrix
```python
def kth_smallest(matrix, k):
    """Find kth smallest element in row and column sorted matrix"""
    n = len(matrix)
    left, right = matrix[0][0], matrix[n-1][n-1]

    def count_less_equal(mid):
        """Count elements <= mid"""
        count = 0
        col = n - 1  # Start from top-right

        for row in range(n):
            # Move left while elements are greater than mid
            while col >= 0 and matrix[row][col] > mid:
                col -= 1
            count += col + 1

        return count

    while left < right:
        mid = left + (right - left) // 2

        if count_less_equal(mid) < k:
            left = mid + 1
        else:
            right = mid

    return left

# Time: O(n * log(max - min)), Space: O(1)
```

### 2. Find Smallest Letter Greater Than Target
```python
def next_greatest_letter(letters, target):
    """Find smallest letter greater than target (wraps around)"""
    left, right = 0, len(letters)

    while left < right:
        mid = left + (right - left) // 2

        if letters[mid] <= target:
            left = mid + 1
        else:
            right = mid

    # Wrap around if no letter greater than target
    return letters[left % len(letters)]

# Time: O(log n), Space: O(1)
```

### 3. Find Square Root
```python
def sqrt(x):
    """Find square root (integer part) using binary search"""
    if x < 2:
        return x

    left, right = 1, x // 2

    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid

        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1

    return right  # Return floor of sqrt

# Time: O(log n), Space: O(1)


def sqrt_with_precision(x, precision=0.0001):
    """Find square root with decimal precision"""
    if x < 0:
        return None

    left, right = 0, max(1, x)

    while right - left > precision:
        mid = (left + right) / 2
        square = mid * mid

        if square < x:
            left = mid
        else:
            right = mid

    return (left + right) / 2

# Time: O(log(x / precision)), Space: O(1)
```

## Key Techniques and Patterns

### 1. Choosing Initial Boundaries
```python
# For array search
left, right = 0, len(arr) - 1  # Inclusive both ends

# For insertion position
left, right = 0, len(arr)  # Exclusive right end

# For answer space
left = minimum_possible_answer
right = maximum_possible_answer
```

### 2. Avoiding Integer Overflow
```python
# Bad: Can overflow for large values
mid = (left + right) // 2

# Good: Safe from overflow
mid = left + (right - left) // 2

# Alternative (in Python, less concern)
mid = (left + right) >> 1  # Bit shift (division by 2)
```

### 3. Loop Termination Conditions
```python
# Use when you need to check mid and return exact match
while left <= right:
    mid = left + (right - left) // 2
    # Can return from inside loop
    if arr[mid] == target:
        return mid
    # Update: left = mid + 1 or right = mid - 1

# Use when mid might be the answer (finding boundaries)
while left < right:
    mid = left + (right - left) // 2
    # Don't exclude mid from search space
    # Update: left = mid + 1 or right = mid
    # Return left after loop (left == right)
```

### 4. Handling Duplicates
```python
def search_with_duplicates(arr, target):
    """Handle duplicates by checking both sides"""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        # Can't determine which side is sorted
        if arr[left] == arr[mid] == arr[right]:
            left += 1
            right -= 1
        elif arr[left] <= arr[mid]:
            # Left side is sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right side is sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

# Time: O(log n) average, O(n) worst case
```

## Problem-Solving Strategy

1. **Identify Binary Search Applicability:**
   - Is the data sorted (or rotated sorted)?
   - Is there a monotonic property (if X works, X+1 also works)?
   - Are we searching for a specific value or optimal value?

2. **Choose the Right Variant:**
   - Exact match: Standard binary search
   - First/last occurrence: Adjust search after finding match
   - Insert position: Use exclusive right boundary
   - Answer space: Define feasibility function

3. **Define Search Space:**
   - For arrays: indices 0 to n-1
   - For answer space: minimum to maximum possible answer
   - Consider if boundaries are inclusive or exclusive

4. **Implement Feasibility Check (for answer space):**
   - Must be clear and efficient
   - Usually O(n) to check if a value works
   - Overall complexity: O(n log k) where k is search space size

5. **Handle Edge Cases:**
   - Empty array
   - Single element
   - Target not in array
   - All elements same
   - Boundaries of search space

## Time and Space Complexity

### Standard Binary Search:
- **Time:** O(log n) - halves search space each iteration
- **Space:** O(1) iterative, O(log n) recursive (call stack)

### Binary Search on Answer:
- **Time:** O(n * log k) where k is answer space size, n is feasibility check cost
- **Space:** O(1) typically

### Why O(log n)?
```
Iteration 1: n elements
Iteration 2: n/2 elements
Iteration 3: n/4 elements
...
Iteration k: 1 element

n / 2^k = 1
n = 2^k
k = log₂(n)
```

## Common Mistakes to Avoid

1. **Infinite loops with wrong mid calculation:**
   - Use `left + (right - left) // 2`, not `(left + right) // 2` for large values
   - Be careful with `mid + 1` vs `mid` and `mid - 1` vs `mid`

2. **Wrong loop condition:**
   - `<=` vs `<` affects when to return and how to update boundaries

3. **Not checking for empty array or out of bounds**

4. **Confusion between finding exact value vs boundary:**
   - Exact value: can return early
   - Boundary: must complete loop to converge

5. **Incorrect boundary updates:**
   - If `right = mid`, must ensure progress (`left < right`, not `left <= right`)
   - If `right = mid - 1`, can use `left <= right`

6. **Forgetting to handle not found case:**
   - Always return appropriate value when target doesn't exist

## Practice Tips

1. **Start with standard binary search:** Master the basics first
2. **Understand loop invariants:** Know what your boundaries represent
3. **Trace through examples:** Walk through array step-by-step
4. **Practice boundary conditions:** First element, last element, not present
5. **Master answer space pattern:** Opens up many optimization problems
6. **Recognize monotonic properties:** Key to identifying binary search opportunities

## Related Patterns

- **Two Pointers:** Can combine with binary search for some problems
- **Divide and Conquer:** Binary search is a special case
- **Ternary Search:** For finding maximum/minimum in unimodal functions
- **Dynamic Programming:** Some DP problems use binary search for optimization
