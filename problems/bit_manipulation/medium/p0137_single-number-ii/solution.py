"""
LeetCode Problem #137: Single Number II
Difficulty: Medium
Pattern: Bit Manipulation
Link: https://leetcode.com/problems/single-number-ii/

Problem:
--------
Given an integer array `nums` where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Constraints:
-----------
- `1
- 2^31
- Each element in `nums` appears exactly three times except for one element which appears once.

Examples:
---------
Example 1:
```
Input: nums = [2,2,3,2]
Output: 3

```

Example 2:
```
Input: nums = [0,1,0,1,0,1,99]
Output: 99

```
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #137: Single Number II

    Approach: Bit Manipulation with Two State Variables (ones, twos)

    We use two variables to track the count of each bit position modulo 3:
    - 'ones' stores bits that have appeared 1 time (mod 3)
    - 'twos' stores bits that have appeared 2 times (mod 3)

    For each number, we update these state variables:
    1. A bit goes into 'twos' if it was already in 'ones' and appears again
    2. A bit goes into 'ones' if it appears (XOR)
    3. If a bit is in both 'ones' and 'twos', it appeared 3 times, so reset both

    Time Complexity: O(n) - single pass through the array
    Space Complexity: O(1) - only two integer variables used

    Key Insights:
    1. We need to count bits modulo 3, not modulo 2 (unlike Single Number I)
    2. Use two bit masks to represent three states: 00 (0 times), 01 (1 time), 10 (2 times)
    3. When count reaches 3, we reset to 0 (00 state)
    4. At the end, 'ones' contains the bits of the single element
    5. The state transitions: 00 -> 01 -> 10 -> 00 (cycles every 3)
    """

    def singleNumber(self, nums: List[int]) -> int:
        """
        Find the single number that appears once while all others appear three times.
        Uses bit manipulation with O(1) space.
        """
        ones = 0  # Bits that have appeared 1 time (mod 3)
        twos = 0  # Bits that have appeared 2 times (mod 3)

        for num in nums:
            # 'ones' gets the bit if it's currently in 'ones' XOR num,
            # but only if it's not already in 'twos' after this update
            #
            # 'twos' gets the bit if it was in 'ones' before and appears in num
            # OR if it was already in 'twos' and doesn't appear in num

            # Update twos: add bits that are in ones AND in num (appearing 2nd time)
            twos |= (ones & num)

            # Update ones: XOR with num (toggle bits)
            ones ^= num

            # Find bits that are in both ones and twos (appeared 3 times)
            # These need to be cleared from both
            common_mask = ones & twos

            # Clear the bits that appeared 3 times
            ones &= ~common_mask
            twos &= ~common_mask

        # After processing, 'ones' contains bits of the number appearing once
        return ones


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 137,
    "name": "Single Number II",
    "difficulty": "Medium",
    "pattern": "Bit Manipulation",
    "topics": ['Array', 'Bit Manipulation'],
    "url": "https://leetcode.com/problems/single-number-ii/",
    "companies": ["Google", "Amazon", "Microsoft", "Apple", "Facebook", "Bloomberg"],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}
