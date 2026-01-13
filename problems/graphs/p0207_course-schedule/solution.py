"""
LeetCode Problem #207: Course Schedule
Difficulty: Medium
Pattern: Graphs (Topological Sort)
Link: https://leetcode.com/problems/course-schedule/

Problem:
--------
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you
must take course bi first if you want to take course ai.

Return true if you can finish all courses. Otherwise, return false.

Constraints:
-----------
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- All pairs [ai, bi] are unique

Examples:
---------
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are 2 courses. To take course 1 you should have finished course 0.

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are 2 courses. To take course 1 you should have finished course 0,
and to take course 0 you should have finished course 1. This is impossible (cycle).
"""

from typing import List
from collections import defaultdict, deque


class Solution:
    """
    Solution to LeetCode Problem #207: Course Schedule

    Approach: Topological Sort (DFS Cycle Detection)
    Time Complexity: O(V + E) where V = numCourses, E = prerequisites
    Space Complexity: O(V + E)

    Key Insights:
    - This is a cycle detection problem in a directed graph
    - If there's a cycle, impossible to finish all courses
    - Use DFS with three states: unvisited, visiting, visited
    - Or use Kahn's algorithm (BFS with in-degrees)
    """

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Determine if all courses can be completed.

        Args:
            numCourses: Total number of courses
            prerequisites: List of [course, prerequisite] pairs

        Returns:
            True if can finish all courses, False otherwise

        Approach:
        1. Build adjacency list graph
        2. Use DFS to detect cycles
        3. Track three states: 0=unvisited, 1=visiting, 2=visited
        4. If we encounter a node in 'visiting' state, there's a cycle
        """
        # Build adjacency list
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        # DFS with cycle detection
        states = [0] * numCourses  # 0=unvisited, 1=visiting, 2=visited

        def has_cycle(course):
            if states[course] == 1:  # Currently visiting - cycle!
                return True
            if states[course] == 2:  # Already visited
                return False

            states[course] = 1  # Mark as visiting
            for next_course in graph[course]:
                if has_cycle(next_course):
                    return True
            states[course] = 2  # Mark as visited
            return False

        for course in range(numCourses):
            if has_cycle(course):
                return False
        return True

    def canFinish_kahns(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Alternative: Kahn's Algorithm (BFS with in-degrees)
        Time: O(V + E), Space: O(V + E)

        Approach:
        1. Calculate in-degree for each course
        2. Start with courses having 0 in-degree
        3. Process courses and reduce in-degrees of neighbors
        4. If processed all courses, no cycle exists
        """
        # Calculate in-degree for each course
        in_degree = [0] * numCourses
        graph = defaultdict(list)

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        # Start with courses having 0 in-degree
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        processed = 0

        # Process courses and reduce in-degrees
        while queue:
            course = queue.popleft()
            processed += 1

            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        # If processed all courses, no cycle exists
        return processed == numCourses


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 207,
    "name": "Course Schedule",
    "difficulty": "Medium",
    "pattern": "Graphs",
    "topics": ["Graph", "DFS", "BFS", "Topological Sort"],
    "url": "https://leetcode.com/problems/course-schedule/",
    "companies": ["Amazon", "Google", "Facebook", "Microsoft"],
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V + E)",
}
