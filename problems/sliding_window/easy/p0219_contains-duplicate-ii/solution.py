"""
LeetCode Problem #219: Contains Duplicate II
Difficulty: Easy
Pattern: Sliding Window
Link: https://leetcode.com/problems/contains-duplicate-ii/

Problem:
--------
Given an integer array `nums` and an integer `k`, return `true` if there are two distinct indices `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j)

Constraints:
-----------
- `1
- 10^9

Examples:
---------
Example 1:
```

Input: nums = [1,2,3,1], k = 3
Output: true

```

Example 2:
```

Input: nums = [1,0,1,1], k = 1
Output: true

```

Example 3:
```

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

```
"""

from typing import List, Optional
from collections import Counter, defaultdict


class Solution:
    """
    Solution to LeetCode Problem #219: Contains Duplicate II

    Approach: Sliding Window with Hash Set
    - Use a hash set to maintain all elements within the current window of size k
    - As we iterate through the array, check if the current element exists in the set
    - If it does, we found a duplicate within distance k, return True
    - If the window size exceeds k, remove the element that falls out of the window
    - Add the current element to the set and continue

    Time Complexity: O(n)
    - We iterate through the array once
    - Hash set operations (add, remove, lookup) are O(1) on average

    Space Complexity: O(min(n, k))
    - We store at most k elements in the hash set
    - If n < k, we store at most n elements

    Key Insights:
    1. The sliding window approach naturally handles the "distance <= k" constraint
    2. Using a hash set allows O(1) duplicate detection within the window
    3. We only need to track elements within the current window, not their indices
    4. When the window slides, we remove the oldest element (nums[i-k]) to maintain size
    5. If k >= n, the window covers the entire array (just check for any duplicate)
    """

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Check if there are two equal elements within distance k.

        Args:
            nums: List of integers to check for duplicates
            k: Maximum allowed distance between duplicate elements

        Returns:
            True if there exist two distinct indices i and j such that
            nums[i] == nums[j] and abs(i - j) <= k, False otherwise
        """
        # Edge case: if k is 0, we can never have two distinct indices with distance <= 0
        if k == 0:
            return False

        # Hash set to store elements in the current sliding window
        window = set()

        for i, num in enumerate(nums):
            # If current element already exists in window, found duplicate within distance k
            if num in window:
                return True

            # Add current element to the window
            window.add(num)

            # If window size exceeds k, remove the oldest element (leftmost in window)
            # This ensures we only keep elements within distance k from current position
            if len(window) > k:
                window.remove(nums[i - k])

        # No duplicates found within distance k
        return False


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 219,
    "name": "Contains Duplicate II",
    "difficulty": "Easy",
    "pattern": "Sliding Window",
    "topics": ['Array', 'Hash Table', 'Sliding Window'],
    "url": "https://leetcode.com/problems/contains-duplicate-ii/",
    "companies": ["Google", "Amazon", "Facebook", "Microsoft", "Apple", "Bloomberg", "Adobe"],
    "time_complexity": "O(n)",
    "space_complexity": "O(min(n, k))",
}
