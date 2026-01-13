# Sliding Window Pattern - Study Guide

## Overview
The Sliding Window pattern is a computational technique that converts nested loops into a single loop, reducing time complexity from O(n²) or O(n³) to O(n). It maintains a "window" of elements and slides it across the data structure to examine different subsets efficiently.

## When to Use Sliding Window
- Finding subarrays or substrings that satisfy certain conditions
- Problems involving contiguous sequences
- Maximum/minimum subarray problems
- String permutation/anagram problems
- Problems with "window size" constraints
- Optimization problems on sequences

## Types of Sliding Windows

### 1. Fixed-Size Window
The window size remains constant as it slides across the array.

**Use cases:**
- Maximum/minimum of all subarrays of size K
- Average of subarrays
- Finding anagrams with fixed pattern length

**Template:**
```python
def fixed_window_template(arr, k):
    """Template for fixed-size sliding window"""
    if len(arr) < k:
        return None

    # Initialize window for first k elements
    window_sum = sum(arr[:k])
    result = window_sum  # or track max/min

    # Slide window across remaining elements
    for i in range(k, len(arr)):
        # Add new element, remove leftmost element
        window_sum = window_sum + arr[i] - arr[i - k]
        result = max(result, window_sum)  # Update result

    return result

# Time: O(n), Space: O(1)
```

**Example - Maximum Sum of Subarray of Size K:**
```python
def max_sum_subarray(arr, k):
    """Find maximum sum of any subarray of size k"""
    if not arr or len(arr) < k:
        return 0

    # Calculate sum of first window
    window_sum = 0
    for i in range(k):
        window_sum += arr[i]

    max_sum = window_sum

    # Slide window and track maximum
    for i in range(k, len(arr)):
        window_sum = window_sum + arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum

# Time: O(n), Space: O(1)
# Example: [2, 1, 5, 1, 3, 2], k=3 -> 9 (subarray [5,1,3])
```

**Example - Find All Anagrams (Fixed Pattern):**
```python
def find_anagrams_fixed(s, pattern):
    """Find all starting indices of pattern anagrams in s"""
    if len(pattern) > len(s):
        return []

    from collections import Counter

    pattern_count = Counter(pattern)
    window_count = Counter()
    result = []
    k = len(pattern)

    # Build initial window
    for i in range(k):
        window_count[s[i]] += 1

    # Check first window
    if window_count == pattern_count:
        result.append(0)

    # Slide window
    for i in range(k, len(s)):
        # Add new character
        window_count[s[i]] += 1

        # Remove old character
        window_count[s[i - k]] -= 1
        if window_count[s[i - k]] == 0:
            del window_count[s[i - k]]

        # Check if current window is anagram
        if window_count == pattern_count:
            result.append(i - k + 1)

    return result

# Time: O(n), Space: O(k) where k is pattern length
```

### 2. Dynamic-Size Window (Expandable/Shrinkable)
The window size changes based on conditions - expands when criteria not met, shrinks when violated.

**Use cases:**
- Longest/shortest substring with certain properties
- Subarray with sum equal to target
- String with at most K distinct characters

**Template:**
```python
def dynamic_window_template(arr, condition):
    """Template for dynamic-size sliding window"""
    left = 0
    result = 0  # or float('inf') for minimum
    current_state = initialize_state()

    for right in range(len(arr)):
        # Expand window by including arr[right]
        update_state(current_state, arr[right])

        # Shrink window while condition is violated
        while not is_valid(current_state, condition) and left <= right:
            remove_from_state(current_state, arr[left])
            left += 1

        # Update result with current valid window
        result = max(result, right - left + 1)

    return result

# Time: O(n), Space: O(1) or O(k) for state
```

**Example - Longest Substring with K Distinct Characters:**
```python
def longest_substring_k_distinct(s, k):
    """Find length of longest substring with at most k distinct chars"""
    if k == 0 or not s:
        return 0

    from collections import defaultdict

    char_count = defaultdict(int)
    left = 0
    max_length = 0

    for right in range(len(s)):
        # Expand window
        char_count[s[right]] += 1

        # Shrink window while more than k distinct chars
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        # Update maximum length
        max_length = max(max_length, right - left + 1)

    return max_length

# Time: O(n), Space: O(k)
# Example: "eceba", k=2 -> 3 (substring "ece")
```

**Example - Minimum Window Substring:**
```python
def min_window_contains_all(s, t):
    """Find minimum window in s that contains all characters of t"""
    if not s or not t or len(s) < len(t):
        return ""

    from collections import Counter

    required = Counter(t)
    window_counts = {}
    formed = 0  # How many unique chars in t are in window with desired frequency
    required_chars = len(required)

    left = 0
    min_len = float('inf')
    min_window = (0, 0)

    for right in range(len(s)):
        # Expand window
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1

        # Check if frequency matches requirement
        if char in required and window_counts[char] == required[char]:
            formed += 1

        # Shrink window while it's still valid
        while formed == required_chars and left <= right:
            # Update result if smaller window found
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window = (left, right)

            # Remove leftmost character
            char = s[left]
            window_counts[char] -= 1
            if char in required and window_counts[char] < required[char]:
                formed -= 1

            left += 1

    return "" if min_len == float('inf') else s[min_window[0]:min_window[1] + 1]

# Time: O(n + m), Space: O(n + m)
```

**Example - Longest Substring Without Repeating Characters:**
```python
def longest_unique_substring(s):
    """Find length of longest substring without repeating characters"""
    char_index = {}  # Last seen index of each character
    left = 0
    max_length = 0

    for right in range(len(s)):
        # If character seen and in current window, shrink window
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1

        # Update last seen index
        char_index[s[right]] = right

        # Update maximum length
        max_length = max(max_length, right - left + 1)

    return max_length

# Time: O(n), Space: O(min(n, charset_size))
# Example: "abcabcbb" -> 3 (substring "abc")
```

### 3. Window with Target Sum/Value
Find subarrays that sum to a specific target.

**Example - Subarray Sum Equals K:**
```python
def subarray_sum_equals_k(arr, k):
    """Count subarrays with sum equal to k (handles negatives)"""
    # For arrays with negative numbers, use prefix sum + hashmap
    from collections import defaultdict

    prefix_sum = 0
    sum_count = defaultdict(int)
    sum_count[0] = 1  # Empty prefix
    count = 0

    for num in arr:
        prefix_sum += num

        # If (prefix_sum - k) exists, we found subarray(s)
        if prefix_sum - k in sum_count:
            count += sum_count[prefix_sum - k]

        sum_count[prefix_sum] += 1

    return count

# Time: O(n), Space: O(n)
```

**Example - Maximum Size Subarray Sum Equals K (Positive Numbers):**
```python
def max_subarray_sum_k_positive(arr, k):
    """Find max length subarray with sum = k (positive numbers only)"""
    left = 0
    current_sum = 0
    max_length = 0

    for right in range(len(arr)):
        # Expand window
        current_sum += arr[right]

        # Shrink window while sum exceeds k
        while current_sum > k and left <= right:
            current_sum -= arr[left]
            left += 1

        # Check if we found target sum
        if current_sum == k:
            max_length = max(max_length, right - left + 1)

    return max_length

# Time: O(n), Space: O(1)
```

## Advanced Sliding Window Patterns

### 1. Two Pointers with Condition Tracking
```python
def longest_subarray_with_ones_after_k_flips(arr, k):
    """Find longest subarray of 1s after flipping at most k 0s"""
    left = 0
    zeros_count = 0
    max_length = 0

    for right in range(len(arr)):
        # Expand window
        if arr[right] == 0:
            zeros_count += 1

        # Shrink window if more than k zeros
        while zeros_count > k:
            if arr[left] == 0:
                zeros_count -= 1
            left += 1

        # Update maximum length
        max_length = max(max_length, right - left + 1)

    return max_length

# Time: O(n), Space: O(1)
# Example: [1,1,0,0,1,1,1,0,1], k=2 -> 7
```

### 2. Multiple Windows
```python
def max_sum_two_non_overlapping_subarrays(arr, len1, len2):
    """Find max sum of two non-overlapping subarrays"""
    n = len(arr)

    # Calculate prefix sums for easy range sum calculation
    prefix = [0]
    for num in arr:
        prefix.append(prefix[-1] + num)

    def get_sum(i, j):
        """Get sum of arr[i:j+1]"""
        return prefix[j + 1] - prefix[i]

    max_sum = 0

    # Try len1 first, then len2
    max_len1_sum = 0
    for i in range(len1 + len2 - 1, n):
        # Max sum of len1 subarray ending before current len2 window
        if i >= len1 + len2 - 1:
            max_len1_sum = max(max_len1_sum, get_sum(i - len1 - len2 + 1, i - len2))

        # Current len2 window sum
        len2_sum = get_sum(i - len2 + 1, i)

        max_sum = max(max_sum, max_len1_sum + len2_sum)

    # Try len2 first, then len1 (if different sizes)
    if len1 != len2:
        max_len2_sum = 0
        for i in range(len1 + len2 - 1, n):
            if i >= len1 + len2 - 1:
                max_len2_sum = max(max_len2_sum, get_sum(i - len1 - len2 + 1, i - len1))

            len1_sum = get_sum(i - len1 + 1, i)
            max_sum = max(max_sum, max_len2_sum + len1_sum)

    return max_sum

# Time: O(n), Space: O(n) for prefix sums
```

### 3. String Permutation Pattern
```python
def check_inclusion(pattern, s):
    """Check if any permutation of pattern is substring of s"""
    if len(pattern) > len(s):
        return False

    from collections import Counter

    pattern_count = Counter(pattern)
    window_count = Counter(s[:len(pattern)])

    if window_count == pattern_count:
        return True

    for i in range(len(pattern), len(s)):
        # Add new character
        window_count[s[i]] += 1

        # Remove old character
        old_char = s[i - len(pattern)]
        window_count[old_char] -= 1
        if window_count[old_char] == 0:
            del window_count[old_char]

        # Check match
        if window_count == pattern_count:
            return True

    return False

# Time: O(n), Space: O(k) where k is pattern length
```

## Key Techniques

### 1. Using HashMap/Counter for Frequency Tracking
```python
from collections import defaultdict

def frequency_based_window(arr):
    """Track element frequencies in window"""
    freq = defaultdict(int)
    left = 0

    for right in range(len(arr)):
        # Add element to window
        freq[arr[right]] += 1

        # Check condition and shrink if needed
        while condition_violated(freq):
            freq[arr[left]] -= 1
            if freq[arr[left]] == 0:
                del freq[arr[left]]  # Clean up zero counts
            left += 1

        # Process valid window
```

### 2. Tracking Window State
```python
def window_with_state_tracking(arr):
    """Maintain multiple state variables"""
    left = 0
    window_sum = 0
    window_max = float('-inf')
    distinct_count = 0
    element_set = set()

    for right in range(len(arr)):
        # Update all state variables when expanding
        window_sum += arr[right]
        window_max = max(window_max, arr[right])

        if arr[right] not in element_set:
            distinct_count += 1
            element_set.add(arr[right])

        # Shrink window and update state
        while needs_shrinking():
            window_sum -= arr[left]
            # Update other state variables as needed
            left += 1
```

### 3. Optimization with Early Termination
```python
def optimized_window(arr, target):
    """Use early termination when result found"""
    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(len(arr)):
        current_sum += arr[right]

        # Shrink window
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)

            # Early termination: can't get shorter than 1
            if min_length == 1:
                return 1

            current_sum -= arr[left]
            left += 1

    return min_length if min_length != float('inf') else 0
```

## Common Patterns and Variations

### 1. At Most K Pattern
```python
def at_most_k_pattern(arr, k):
    """Template for 'at most k' problems"""
    left = 0
    count = 0  # Track constraint (e.g., distinct chars, zeros)
    result = 0

    for right in range(len(arr)):
        # Update count when adding arr[right]
        if should_increase_count(arr[right]):
            count += 1

        # Shrink while count exceeds k
        while count > k:
            if should_decrease_count(arr[left]):
                count -= 1
            left += 1

        result = max(result, right - left + 1)

    return result

# Trick: "Exactly K" = "At most K" - "At most K-1"
```

### 2. Maximum/Minimum Window Size
```python
def find_min_window_size(arr, condition):
    """Find minimum window size satisfying condition"""
    left = 0
    min_size = float('inf')
    current_state = {}

    for right in range(len(arr)):
        # Expand window
        update_state(current_state, arr[right])

        # Shrink window while condition is met
        while condition_met(current_state):
            min_size = min(min_size, right - left + 1)
            remove_from_state(current_state, arr[left])
            left += 1

    return min_size if min_size != float('inf') else 0

# Note: Shrink while condition MET (not violated) for minimum size
```

### 3. Count All Valid Windows
```python
def count_subarrays_with_property(arr):
    """Count all subarrays with certain property"""
    left = 0
    count = 0

    for right in range(len(arr)):
        # Expand window
        update_window(arr[right])

        # Shrink window to maintain property
        while property_violated():
            remove_from_window(arr[left])
            left += 1

        # All subarrays ending at right and starting
        # from left to right are valid
        count += right - left + 1

    return count

# Key insight: Each position of left pointer contributes
# one valid subarray for current right pointer
```

## Problem-Solving Strategy

1. **Identify Sliding Window Applicability:**
   - Does the problem involve contiguous elements?
   - Can we use information from previous window?
   - Is brute force O(n²) or worse?

2. **Choose Window Type:**
   - Fixed size: Window size given or implied
   - Dynamic: Finding optimal window size
   - Multiple windows: Non-overlapping subarrays

3. **Determine Expand/Shrink Logic:**
   - When to expand? (Usually every iteration)
   - When to shrink? (Condition violated or optimization opportunity)
   - What to track? (Sum, frequency, distinct count, etc.)

4. **Handle Edge Cases:**
   - Empty array
   - Window size larger than array
   - All elements same
   - Single element

## Time and Space Complexity

### Typical Complexities:
- **Time:** O(n) - each element visited at most twice (once by right, once by left)
- **Space:** O(1) for simple counters, O(k) for frequency maps where k is window size or character set

### Why O(n) despite nested loop?
```python
# Although there's a while loop inside for loop,
# each element is added once (right pointer) and
# removed once (left pointer), so total operations = 2n = O(n)

for right in range(n):           # n iterations
    # add arr[right]
    while condition:              # Total across ALL iterations: at most n
        # remove arr[left]
        left += 1
```

## Practice Tips

1. **Start with fixed-size windows:** Easier to understand and implement
2. **Master the expand-shrink logic:** Key to dynamic windows
3. **Use descriptive variable names:** `left`, `right`, `window_sum` better than `i`, `j`, `s`
4. **Draw the window:** Visualize on paper as it slides
5. **Test with edge cases:** Empty array, size 1, window size > array length
6. **Optimize incrementally:** Get correct solution first, then optimize

## Common Mistakes to Avoid

1. **Resetting window state:** Don't recalculate from scratch, update incrementally
2. **Wrong window size calculation:** `right - left + 1`, not `right - left`
3. **Not handling empty collections:** Check before deleting from dictionary/set
4. **Incorrect shrink condition:** Shrink WHILE violated (max) or WHILE valid (min)
5. **Forgetting to update result:** Update before or after shrinking based on problem
6. **Off-by-one in fixed window:** Window of size k ends at index k-1

## Related Patterns

- **Two Pointers:** Sliding window is a special case with contiguous elements
- **Prefix Sum:** Can combine for range sum queries in windows
- **Monotonic Queue/Stack:** For min/max in sliding window
- **Dynamic Programming:** Some DP problems can be optimized with sliding window
