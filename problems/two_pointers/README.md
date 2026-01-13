# Two Pointers Pattern

## Overview

The two pointers pattern is a technique where we use two pointers to traverse a data structure, typically an array or linked list. The pointers can move toward each other, away from each other, or at different speeds.

## When to Use

- Array/string problems involving pairs or subarrays
- Finding pairs that meet certain conditions
- Removing duplicates
- Reversing arrays/strings
- Detecting cycles in linked lists
- Problems involving sorted arrays

## Common Variations

### 1. Opposite Direction (Converging)
- Start at both ends, move toward center
- Examples: Two Sum II, Container With Most Water, Valid Palindrome

### 2. Same Direction (Fast & Slow)
- Both pointers move forward at different speeds
- Examples: Remove Duplicates, Linked List Cycle, Move Zeroes

### 3. Sliding Window
- Pointers define a window that slides through data
- Examples: Longest Substring Without Repeating Characters

## Time/Space Complexity

- **Time:** Usually O(n) - single pass
- **Space:** Usually O(1) - only pointer variables

## Template Code

```python
def two_pointers_converging(arr):
    """Opposite direction pointers"""
    left, right = 0, len(arr) - 1

    while left < right:
        # Process current pair
        if condition_met:
            return result
        elif should_move_left:
            left += 1
        else:
            right -= 1

    return result

def two_pointers_same_direction(arr):
    """Same direction pointers"""
    slow = fast = 0

    while fast < len(arr):
        if condition:
            slow += 1
        fast += 1

    return slow
```

## Problems in This Category

### Easy
- [x] #1 - Two Sum (Completed - Hash Map approach)
- [x] #125 - Valid Palindrome (Completed - Converging pointers)
- [ ] #283 - Move Zeroes (Ready to solve - Same direction)
- [ ] #26 - Remove Duplicates from Sorted Array
- [ ] #27 - Remove Element
- [ ] #344 - Reverse String

### Medium
- [ ] #11 - Container With Most Water (Ready to solve - Greedy two pointers)
- [ ] #15 - 3Sum (Ready to solve - Classic interview question)
- [ ] #75 - Sort Colors (Ready to solve - Dutch National Flag)
- [ ] #167 - Two Sum II - Input Array Is Sorted (Ready to solve - Classic converging)
- [ ] #16 - 3Sum Closest
- [ ] #80 - Remove Duplicates from Sorted Array II
- [ ] #88 - Merge Sorted Array
- [ ] #142 - Linked List Cycle II

### Hard
- [ ] #42 - Trapping Rain Water (Ready to solve - Advanced two pointers)
- [ ] #76 - Minimum Window Substring

## Tips & Tricks

1. **Sort first**: Many two-pointer problems benefit from sorted input
2. **Skip duplicates**: Use while loops to skip over duplicate values
3. **Maintain invariants**: Clearly define what each pointer represents
4. **Edge cases**: Empty arrays, single elements, all duplicates
5. **Boundary checks**: Always check if pointers are in valid range

## Common Mistakes

- Forgetting to move pointers (infinite loop)
- Not handling edge cases properly
- Confusing when to move left vs right pointer
- Off-by-one errors with indices
