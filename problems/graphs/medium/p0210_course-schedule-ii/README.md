# Problem 210: Course Schedule II

**Difficulty:** Medium
**Pattern:** Graphs
**Link:** [LeetCode](https://leetcode.com/problems/course-schedule-ii/)

## Problem Description

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

## Constraints

- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= numCourses * (numCourses - 1)
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- ai != bi
- All the pairs [ai, bi] are distinct

## Examples

Example 1:
```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
```

Example 2:
```
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
```

## Approaches

### 1. Topological Sort

**Time Complexity:** O(V + E)
**Space Complexity:** O(V + E)

```python
def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    """
    Return a valid ordering of courses to finish all courses.
    """
    from collections import defaultdict

    # Build adjacency list
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    # DFS with cycle detection and topological ordering
    states = [0] * numCourses  # 0=unvisited, 1=visiting, 2=visited
    result = []

    def dfs(course: int) -> bool:
        """Returns False if cycle detected."""
        if states[course] == 1:  # Currently visiting - cycle!
            return False
        if states[course] == 2:  # Already visited
            return True

        states[course] = 1  # Mark as visiting
        for next_course in graph[course]:
            if not dfs(next_course):
                return False
        states[course] = 2  # Mark as visited
        result.append(course)
        return True

    for course in range(numCourses):
        if not dfs(course):
            return []

    # Reverse to get topological order (prerequisites first)
    return result[::-1]
```

**Why this works:**

1. Build adjacency list graph
2. Use DFS with post-order traversal
3. Track three states: 0=unvisited, 1=visiting, 2=visited
4. If cycle detected, return empty list
5. Reverse the post-order to get topological order

## Key Insights

- Return topological order if valid
- Use Kahn's algorithm (BFS) or DFS post-order
- Track visited nodes to detect cycles
- Return empty array if cycle detected

## Common Mistakes

- Forgetting to reverse the post-order result
- Not handling cycles properly
- Missing courses with no prerequisites

## Related Problems

- Course Schedule (207)
- Alien Dictionary (269)
- Minimum Height Trees (310)

## Tags

Depth-First Search, Breadth-First Search, Graph, Topological Sort
