"""
LeetCode Problem #621: Task Scheduler
Difficulty: Medium
Pattern: Greedy
Link: https://leetcode.com/problems/task-scheduler/

Problem:
--------
You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.

Return the minimum number of intervals required to complete all tasks.

Constraints:
-----------
- 1 <= tasks.length <= 10^4
- tasks[i] is an uppercase English letter
- 0 <= n <= 100

Examples:
---------
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

Input: tasks = ["A","C","A","B","D","B"], n = 1
Output: 6
Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #621: Task Scheduler

    Approach: Greedy with frequency calculation
    Time Complexity: O(n)
    Space Complexity: O(1) - only 26 letters

    Key Insights:
    - Find max frequency and count of max freq tasks
    - Formula: max((max_freq - 1) * (n + 1) + count, len(tasks))
    - Schedule most frequent task first with gaps
    - Fill gaps with other tasks
    """

    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Find minimum intervals to complete all tasks with cooling time.

        Args:
            tasks: Array of task characters
            n: Cooling time between identical tasks

        Returns:
            Minimum number of intervals needed
        """
        from collections import Counter

        # Count frequency of each task
        freq = Counter(tasks)

        # Find maximum frequency
        max_freq = max(freq.values())

        # Count how many tasks have the maximum frequency
        max_count = sum(1 for f in freq.values() if f == max_freq)

        # Formula: (max_freq - 1) * (n + 1) + max_count
        # Creates (max_freq - 1) full cycles of (n + 1) slots
        # Plus the final row with max_count tasks
        result = (max_freq - 1) * (n + 1) + max_count

        # Result can't be less than total number of tasks
        # (when n is small and many different tasks fill all gaps)
        return max(result, len(tasks))


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 621,
    "name": "Task Scheduler",
    "difficulty": "Medium",
    "pattern": "Greedy",
    "topics": ['Array', 'Hash Table', 'Greedy', 'Sorting', 'Heap (Priority Queue)', 'Counting'],
    "url": "https://leetcode.com/problems/task-scheduler/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google'],
    "time_complexity": "O(n)",
    "space_complexity": "O(1) - only 26 letters",
}
