"""
LeetCode Problem #16: 3Sum Closest
Difficulty: Medium
Pattern: Two Pointers
Link: https://leetcode.com/problems/3sum-closest/

Problem:
--------
Given an integer array nums of length n and an integer target, find three integers in
nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Constraints:
-----------
- 3 <= nums.length <= 500
- -1000 <= nums[i] <= 1000
- -10^4 <= target <= 10^4

Examples:
---------
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2 (-1 + 2 + 1 = 2).

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0 (0 + 0 + 0 = 0).
"""

from typing import List


class Solution:
    """
    Solution to LeetCode Problem #16: 3Sum Closest

    Approach: Sorting + Two Pointers
    Time Complexity: O(n^2)
    Space Complexity: O(1) or O(n) depending on sorting implementation

    Key Insights:
    - Sort the array first
    - Fix one element and use two pointers for the remaining two
    - Track the closest sum seen so far
    - Move pointers based on comparison with target
    - Early termination when exact match found
    """

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Find three integers in nums such that the sum is closest to target.

        Args:
            nums: List of integers
            target: Target sum

        Returns:
            Sum of the three integers closest to target
        """
        nums.sort()
        total = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            l,r = i+1, len(nums)-1
            while l<r:
                curr = nums[i] + nums[l] + nums[r]
                if abs(target - curr) < abs(target - total):
                    total = curr
                if curr == target:
                    return target
                elif curr < target:
                    l+=1
                else:
                    r-=1
        return total
        


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 16,
    "name": "3Sum Closest",
    "difficulty": "Medium",
    "pattern": "Two Pointers",
    "topics": ["Array", "Two Pointers", "Sorting"],
    "url": "https://leetcode.com/problems/3sum-closest/",
    "companies": ["Amazon", "Facebook", "Bloomberg", "Adobe", "Microsoft"],
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
}
