"""
LeetCode Problem #135: Candy
Difficulty: Hard
Pattern: Greedy
Link: https://leetcode.com/problems/candy/

Problem:
--------
There are `n` children standing in a line. Each child is assigned a rating value given in the integer array `ratings`.

You are giving candies to these children subjected to the following requirements:

- Each child must have at least one candy.
	
- Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children.

Constraints:
-----------
- `n == ratings.length

Examples:
---------
Example 1:
```

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

```

Example 2:
```

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

```
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #135: Candy

    Approach: Two-pass greedy approach. First pass (left to right) ensures
    children with higher ratings than their left neighbor get more candies.
    Second pass (right to left) ensures children with higher ratings than
    their right neighbor get more candies while maintaining the left constraint.

    Time Complexity: O(n) - two passes through the array
    Space Complexity: O(n) - array to store candy counts

    Key Insights:
    1. Each child must have at least 1 candy
    2. Left-to-right pass: if rating[i] > rating[i-1], then candies[i] = candies[i-1] + 1
    3. Right-to-left pass: if rating[i] > rating[i+1], then candies[i] = max(candies[i], candies[i+1] + 1)
    4. The max in the second pass preserves the constraint from the first pass
    5. Equal ratings don't require more candies (only strictly greater does)
    """

    def candy(self, ratings: List[int]) -> int:
        """
        Find the minimum number of candies needed to distribute to children.

        Args:
            ratings: List of rating values for each child

        Returns:
            Minimum total candies needed
        """
        n = len(ratings)
        if n == 0:
            return 0
        if n == 1:
            return 1

        # Initialize all children with 1 candy
        candies = [1] * n

        # Left to right pass: ensure right neighbor constraint
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Right to left pass: ensure left neighbor constraint
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 135,
    "name": "Candy",
    "difficulty": "Hard",
    "pattern": "Greedy",
    "topics": ['Array', 'Greedy'],
    "url": "https://leetcode.com/problems/candy/",
    "companies": ["Amazon", "Google", "Microsoft", "Apple", "Bloomberg", "Facebook", "Uber"],
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
}
