"""
LeetCode Problem #167: Two Sum II - Input Array Is Sorted
Difficulty: Medium
Pattern: Two Pointers
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

Problem:
--------
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number. Return the indices of
the two numbers (index1 and index2) where index1 < index2.

Constraints:
-----------
- 2 <= numbers.length <= 3 * 10^4
- -1000 <= numbers[i] <= 1000
- numbers is sorted in non-decreasing order
- -1000 <= target <= 1000
- The tests are generated such that there is exactly one solution

Examples:
---------
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]

Input: numbers = [2,3,4], target = 6
Output: [1,3]
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #167: Two Sum II - Input Array Is Sorted

    Approach: Two Pointers
    Time Complexity: O(n)
    Space Complexity: O(1)

    Key Insights:
    - Array is sorted - use two pointers
    - If sum < target, move left pointer right
    - If sum > target, move right pointer left
    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l<r:
            if numbers[l] + numbers[r] == target:
                return [l+1,r+1]
            else:
                if numbers[l] + numbers[r] < target:
                    l+=1
                else:
                    r-=1



# Metadata for tracking
PROBLEM_METADATA = {
    "number": 167,
    "name": "Two Sum II - Input Array Is Sorted",
    "difficulty": "Medium",
    "pattern": "Two Pointers",
    "topics": ["Array", "Two Pointers", "Binary Search"],
    "url": "https://leetcode.com/problems/two-sum-ii---input-array-is-sorted/",
    "companies": ["Amazon", "Adobe", "Apple"],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}
