"""
LeetCode Problem #677: Map Sum Pairs
Difficulty: Medium
Pattern: Tries
Link: https://leetcode.com/problems/map-sum-pairs/

Problem:
--------
Design a map that allows you to do the following:

Maps a string key to a given value.
Returns the sum of the values that have a key with a prefix equal to a given string.

Implement the MapSum class:

MapSum() Initializes the MapSum object.
void insert(String key, int val) Inserts the key-val pair into the map. If the key already existed, the original key-value pair will be overridden to the new one.
int sum(String prefix) Returns the sum of all the pairs' value whose key starts with the prefix.

Constraints:
-----------
- 1 <= key.length, prefix.length <= 50
- key and prefix consist of only lowercase English letters
- 1 <= val <= 1000
- At most 50 calls will be made to insert and sum

Examples:
---------
Input
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
Output
[null, null, 3, null, 5]

Explanation
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);  
mapSum.sum("ap");           // return 3 (apple = 3)
mapSum.insert("app", 2);    
mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #677: Map Sum Pairs

    Approach: Trie with value storage
    Time Complexity: O(m) for both operations where m is key/prefix length
    Space Complexity: O(n * m)

    Key Insights:
    - Store values in Trie nodes
    - Track previous values for updates
    - DFS to sum all values with prefix
    - HashMap to handle key updates
    """

    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 677,
    "name": "Map Sum Pairs",
    "difficulty": "Medium",
    "pattern": "Tries",
    "topics": ['Hash Table', 'String', 'Design', 'Trie'],
    "url": "https://leetcode.com/problems/map-sum-pairs/",
    "companies": ['Amazon', 'Google'],
    "time_complexity": "O(m) for both operations where m is key/prefix length",
    "space_complexity": "O(n * m)",
}
