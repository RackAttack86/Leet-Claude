"""
LeetCode Problem #904: Fruit Into Baskets
Difficulty: Medium
Pattern: Sliding Window
Link: https://leetcode.com/problems/fruit-into-baskets/

Problem:
--------
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Given the integer array fruits, return the maximum number of fruits you can pick.

Constraints:
-----------
- 1 <= fruits.length <= 10^5
- 0 <= fruits[i] < fruits.length

Examples:
---------
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #904: Fruit Into Baskets

    Approach: Sliding Window with hash map
    Time Complexity: O(n)
    Space Complexity: O(1) - at most 3 fruit types tracked

    Key Insights:
    - Find longest subarray with at most 2 distinct elements
    - Use hash map to track fruit types in window
    - Expand window and contract when types > 2
    - Classic sliding window pattern
    """

    def totalFruit(self, fruits: List[int]) -> int:
        """
        Find maximum number of fruits collectible with 2 baskets (at most 2 types).

        Equivalent to finding longest subarray with at most 2 distinct elements.
        Uses sliding window with hash map to track fruit types.
        """
        fruit_count = {}
        max_fruits = 0
        left = 0

        for right in range(len(fruits)):
            # Add fruit to window
            fruit = fruits[right]
            fruit_count[fruit] = fruit_count.get(fruit, 0) + 1

            # Shrink window while we have more than 2 fruit types
            while len(fruit_count) > 2:
                left_fruit = fruits[left]
                fruit_count[left_fruit] -= 1
                if fruit_count[left_fruit] == 0:
                    del fruit_count[left_fruit]
                left += 1

            # Update maximum
            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 904,
    "name": "Fruit Into Baskets",
    "difficulty": "Medium",
    "pattern": "Sliding Window",
    "topics": ['Array', 'Hash Table', 'Sliding Window'],
    "url": "https://leetcode.com/problems/fruit-into-baskets/",
    "companies": ['Amazon', 'Facebook', 'Google'],
    "time_complexity": "O(n)",
    "space_complexity": "O(1) - at most 3 fruit types tracked",
}
