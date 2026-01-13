# Two Pointers Pattern - Study Guide

## Overview
The Two Pointers pattern is a technique where two pointers iterate through a data structure (usually an array or linked list) in tandem until one or both pointers meet a condition. This pattern is highly efficient for problems involving sorted arrays, palindromes, or finding pairs/triplets.

## When to Use Two Pointers
- Working with sorted arrays or linked lists
- Finding pairs, triplets, or subarrays that satisfy certain conditions
- Palindrome problems
- Removing duplicates in-place
- Merging sorted arrays
- Problems that can be optimized from O(n²) to O(n)

## Common Two Pointer Patterns

### 1. Opposite Direction (Converging Pointers)
Two pointers start at opposite ends and move toward each other.

**Use cases:**
- Palindrome checking
- Finding pairs in sorted arrays
- Reversing arrays/strings
- Container with most water type problems

**Template:**
```python
def opposite_direction_example(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # Process current pair
        if condition_met(arr[left], arr[right]):
            # Found solution or record result
            return True

        # Move pointers based on logic
        if arr[left] + arr[right] < target:
            left += 1  # Need larger sum
        else:
            right -= 1  # Need smaller sum

    return False
```

**Example - Check if Palindrome:**
```python
def is_palindrome(s):
    """Check if string is palindrome using two pointers"""
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

# Time: O(n), Space: O(1)
```

**Example - Two Sum in Sorted Array:**
```python
def two_sum_sorted(arr, target):
    """Find two numbers that sum to target in sorted array"""
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1  # Need larger sum
        else:
            right -= 1  # Need smaller sum

    return [-1, -1]

# Time: O(n), Space: O(1)
```

### 2. Same Direction (Fast and Slow Pointers)
Both pointers start at the beginning and move in the same direction at different speeds.

**Use cases:**
- Removing duplicates in-place
- Moving elements (like moving zeros to end)
- Partitioning arrays
- Finding cycles in linked lists

**Template:**
```python
def same_direction_example(arr):
    slow = 0  # Usually for writing/placement

    for fast in range(len(arr)):
        # Fast pointer explores
        if should_keep(arr[fast]):
            # Slow pointer places valid elements
            arr[slow] = arr[fast]
            slow += 1

    return slow  # Often returns new length
```

**Example - Remove Duplicates:**
```python
def remove_duplicates(arr):
    """Remove duplicates in-place from sorted array"""
    if not arr:
        return 0

    slow = 0  # Position for next unique element

    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]

    return slow + 1  # New length

# Time: O(n), Space: O(1)
# Example: [1,1,2,2,3] -> [1,2,3,_,_], returns 3
```

**Example - Move Zeros to End:**
```python
def move_zeros(arr):
    """Move all zeros to end while maintaining order of non-zeros"""
    slow = 0  # Position for next non-zero

    # Place all non-zeros at the front
    for fast in range(len(arr)):
        if arr[fast] != 0:
            arr[slow] = arr[fast]
            slow += 1

    # Fill remaining positions with zeros
    while slow < len(arr):
        arr[slow] = 0
        slow += 1

# Time: O(n), Space: O(1)
# Example: [0,1,0,3,12] -> [1,3,12,0,0]
```

### 3. Sliding Window with Two Pointers
A special case where both pointers define a window that slides through the array.

**Example - Find Longest Subarray with Sum ≤ K:**
```python
def longest_subarray_sum(arr, k):
    """Find longest subarray with sum <= k"""
    left = 0
    current_sum = 0
    max_length = 0

    for right in range(len(arr)):
        current_sum += arr[right]

        # Shrink window while sum exceeds k
        while current_sum > k and left <= right:
            current_sum -= arr[left]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

# Time: O(n), Space: O(1)
```

### 4. Multiple Pointers for Complex Problems
Some problems require more than two pointers.

**Example - Three Sum Framework:**
```python
def three_pointers_example(arr, target):
    """Framework for three sum type problems"""
    arr.sort()  # Often need sorted array
    result = []

    # Fix first pointer
    for i in range(len(arr) - 2):
        # Skip duplicates for first pointer
        if i > 0 and arr[i] == arr[i-1]:
            continue

        # Use two pointers for remaining elements
        left, right = i + 1, len(arr) - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == target:
                result.append([arr[i], arr[left], arr[right]])

                # Skip duplicates for second pointer
                while left < right and arr[left] == arr[left+1]:
                    left += 1
                # Skip duplicates for third pointer
                while left < right and arr[right] == arr[right-1]:
                    right -= 1

                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return result

# Time: O(n²), Space: O(1) excluding output
```

## Key Techniques and Patterns

### Handling Duplicates
```python
def skip_duplicates_example(arr):
    """Technique to skip duplicates while using two pointers"""
    arr.sort()
    i = 0

    while i < len(arr):
        # Process arr[i]

        # Skip all duplicates
        while i + 1 < len(arr) and arr[i] == arr[i+1]:
            i += 1

        i += 1
```

### Partition Pattern
```python
def partition_array(arr, pivot):
    """Partition array around a pivot value"""
    left = 0  # Next position for elements < pivot
    right = len(arr) - 1  # Next position for elements > pivot
    i = 0  # Current element being examined

    while i <= right:
        if arr[i] < pivot:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1
            i += 1
        elif arr[i] > pivot:
            arr[right], arr[i] = arr[i], arr[right]
            right -= 1
            # Don't increment i, need to examine swapped element
        else:
            i += 1  # arr[i] == pivot

    return left, right  # Boundaries of pivot section

# Time: O(n), Space: O(1)
# Dutch National Flag problem variation
```

### Reverse Portions of Array
```python
def reverse_portion(arr, start, end):
    """Reverse array elements between start and end indices"""
    left, right = start, end

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

# Usage: Rotate array, reverse words in string, etc.
```

## Common Variations and Edge Cases

### 1. Dealing with Special Characters
```python
def is_palindrome_alphanumeric(s):
    """Check palindrome ignoring non-alphanumeric characters"""
    left, right = 0, len(s) - 1

    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1

        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare case-insensitive
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
```

### 2. Finding Multiple Pairs
```python
def find_all_pairs(arr, target):
    """Find all unique pairs that sum to target"""
    arr.sort()
    pairs = []
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            pairs.append([arr[left], arr[right]])

            # Move both pointers and skip duplicates
            left += 1
            right -= 1

            while left < right and arr[left] == arr[left-1]:
                left += 1
            while left < right and arr[right] == arr[right+1]:
                right -= 1

        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return pairs
```

### 3. Closest Pair Problems
```python
def closest_sum_to_target(arr, target):
    """Find pair with sum closest to target"""
    arr.sort()
    left, right = 0, len(arr) - 1
    closest_sum = float('inf')
    result = []

    while left < right:
        current_sum = arr[left] + arr[right]

        # Update closest if current is closer
        if abs(target - current_sum) < abs(target - closest_sum):
            closest_sum = current_sum
            result = [arr[left], arr[right]]

        # Move pointers
        if current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1
        else:
            return result  # Exact match

    return result
```

## Time and Space Complexity Analysis

### Typical Complexities:
- **Time:** O(n) for single pass with two pointers
- **Time:** O(n²) when fixing one element and using two pointers on remaining
- **Time:** O(n log n) when sorting is required first
- **Space:** O(1) for in-place operations
- **Space:** O(n) when creating new result array

### Example Analysis:
```python
def example_with_analysis(arr, target):
    # Sorting: O(n log n) time
    arr.sort()

    # Two pointers: O(n) time
    left, right = 0, len(arr) - 1
    while left < right:
        # O(1) operations
        if arr[left] + arr[right] == target:
            return [left, right]
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1

    # Total Time: O(n log n) + O(n) = O(n log n)
    # Space: O(1) if sort is in-place, O(n) otherwise
```

## Problem-Solving Strategy

1. **Identify if Two Pointers is Appropriate:**
   - Is the input sorted (or can it be sorted)?
   - Are we looking for pairs/subarrays?
   - Can we reduce from O(n²) brute force?

2. **Choose the Right Pattern:**
   - Opposite direction: Target sum, palindrome
   - Same direction: Remove/move elements
   - Sliding window: Subarray problems

3. **Consider Edge Cases:**
   - Empty array
   - Single element
   - All elements same
   - Negative numbers
   - Duplicate handling

4. **Optimize:**
   - Skip duplicates when necessary
   - Early termination conditions
   - In-place modifications when possible

## Practice Tips

1. **Master the basics first:** Start with simple palindrome and two-sum problems
2. **Understand pointer movement logic:** Know when to move left, right, or both
3. **Handle duplicates correctly:** This is often the tricky part
4. **Draw it out:** Visualize pointer positions on paper
5. **Consider all edge cases:** Empty arrays, single elements, all duplicates
6. **Time yourself:** Two pointer problems should be solvable in 15-20 minutes once you master the pattern

## Common Mistakes to Avoid

1. **Off-by-one errors:** Check loop conditions carefully (< vs <=)
2. **Forgetting to handle duplicates:** Can lead to duplicate results
3. **Wrong pointer movement:** Moving the wrong pointer based on condition
4. **Not validating indices:** Check bounds before accessing array elements
5. **Sorting when not needed:** Some problems work on unsorted arrays
6. **Creating unnecessary space:** Try to work in-place when possible

## Related Patterns

- **Sliding Window:** Often uses two pointers to define window boundaries
- **Binary Search:** Uses two pointers (start/end) in different way
- **Fast & Slow Pointers:** Special case for linked list cycle detection
- **Merge Intervals:** Uses pointer-like indices to merge sorted intervals
