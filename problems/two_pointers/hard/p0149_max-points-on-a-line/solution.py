"""
LeetCode Problem #149: Max Points on a Line
Difficulty: Hard
Pattern: Two Pointers
Link: https://leetcode.com/problems/max-points-on-a-line/

Problem:
--------
Given an array of `points` where `points[i] = [xi, yi]` represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

Constraints:
-----------
- `1
- points[i].length == 2
- 10^4 i, yi
- All the `points` are unique.

Examples:
---------
Example 1:
```

Input: points = [[1,1],[2,2],[3,3]]
Output: 3

```

Example 2:
```

Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4

```
"""

from typing import List, Optional
from collections import Counter, defaultdict


class Solution:
    """
    Solution to LeetCode Problem #149: Max Points on a Line

    Approach: For each point, calculate the slope to all other points
    and group by slope using a hash map. The max points on a line through
    the current point is the max count in any slope group + 1.

    Time Complexity: O(n^2) - For each point, check all other points
    Space Complexity: O(n) - Hash map for slope counts per point

    Key Insights:
    1. Two points define a unique line
    2. Use slope as key to group collinear points
    3. Handle vertical lines (infinite slope) separately
    4. Use GCD to normalize slope as fraction to avoid floating point errors
    5. For each anchor point, track slopes to all other points
    """

    def maxPoints(self, points: List[List[int]]) -> int:
        from math import gcd

        n = len(points)
        if n <= 2:
            return n

        def get_slope(p1: List[int], p2: List[int]) -> tuple:
            """Return normalized slope as (dy, dx) tuple."""
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]

            if dx == 0:
                # Vertical line
                return (1, 0)
            if dy == 0:
                # Horizontal line
                return (0, 1)

            # Normalize using GCD
            g = gcd(abs(dx), abs(dy))
            dx //= g
            dy //= g

            # Ensure consistent sign (dx always positive, or if dx=0, dy positive)
            if dx < 0:
                dx, dy = -dx, -dy

            return (dy, dx)

        max_points = 1

        for i in range(n):
            slope_count = defaultdict(int)
            for j in range(i + 1, n):
                slope = get_slope(points[i], points[j])
                slope_count[slope] += 1
                max_points = max(max_points, slope_count[slope] + 1)

        return max_points


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 149,
    "name": "Max Points on a Line",
    "difficulty": "Hard",
    "pattern": "Two Pointers",
    "topics": ['Array', 'Hash Table', 'Math', 'Geometry'],
    "url": "https://leetcode.com/problems/max-points-on-a-line/",
    "companies": ["Google", "Amazon", "LinkedIn", "Apple", "Microsoft", "Facebook"],
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
}
