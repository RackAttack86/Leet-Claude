"""
LeetCode Problem #495: Teemo Attacking
Difficulty: Easy
Pattern: Intervals
Link: https://leetcode.com/problems/teemo-attacking/

Problem:
--------
Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, Ashe gets poisoned for a exactly duration seconds. More formally, an attack at second t will mean Ashe is poisoned during the inclusive time interval [t, t + duration - 1]. If Teemo attacks again before the poison effect ends, the timer for it is reset, and the poison effect will end duration seconds after the new attack.

You are given a non-decreasing integer array timeSeries, where timeSeries[i] denotes that Teemo attacks Ashe at second timeSeries[i], and an integer duration.

Return the total number of seconds that Ashe is poisoned.

Constraints:
-----------
- 1 <= timeSeries.length <= 10^4
- 0 <= timeSeries[i], duration <= 10^7
- timeSeries is sorted in non-decreasing order

Examples:
---------
Input: timeSeries = [1,4], duration = 2
Output: 4
Explanation: Teemo's attacks on Ashe go as follows:
- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
- At second 4, Teemo attacks, and Ashe is poisoned for seconds 4 and 5.
Ashe is poisoned for seconds 1, 2, 4, and 5, which is 4 seconds in total.

Input: timeSeries = [1,2], duration = 2
Output: 3
Explanation: At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
At second 2 however, Teemo attacks again and resets the poison timer. Ashe is poisoned for seconds 2 and 3.
Ashe is poisoned for seconds 1, 2, and 3, which is 3 seconds in total.
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #495: Teemo Attacking

    Approach: Interval simulation
    Time Complexity: O(n)
    Space Complexity: O(1)

    Key Insights:
    - If gap >= duration, add full duration
    - Otherwise add gap between attacks
    - Track overlapping poison effects
    - Simple one-pass solution
    """

    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0

        total = 0
        for i in range(len(timeSeries) - 1):
            gap = timeSeries[i + 1] - timeSeries[i]
            total += min(gap, duration)

        # Add the last attack's full duration
        total += duration
        return total


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 495,
    "name": "Teemo Attacking",
    "difficulty": "Easy",
    "pattern": "Intervals",
    "topics": ['Array', 'Simulation'],
    "url": "https://leetcode.com/problems/teemo-attacking/",
    "companies": ['Amazon', 'Google'],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}
