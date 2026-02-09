# Problem 207: Course Schedule

**Difficulty:** Medium
**Pattern:** Graphs
**Link:** [LeetCode](https://leetcode.com/problems/course-schedule/)

## Problem Description

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you
must take course bi first if you want to take course ai.

Return true if you can finish all courses. Otherwise, return false.

## Constraints

- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- All pairs [ai, bi] are unique

## Examples

Example 1:
```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are 2 courses. To take course 1 you should have finished course 0.
```

Example 2:
```
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are 2 courses. To take course 1 you should have finished course 0,
and to take course 0 you should have finished course 1. This is impossible (cycle).
```

## Approaches

### 1. Topological Sort (DFS Cycle Detection)

**Time Complexity:** O(V + E)
**Space Complexity:** O(V + E)

```python
def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    Determine if all courses can be completed.
    """
    from collections import defaultdict

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
```

**Why this works:**

1. Build adjacency list graph
2. Use DFS to detect cycles
3. Track three states: 0=unvisited, 1=visiting, 2=visited
4. If we encounter a node in 'visiting' state, there's a cycle

## Key Insights

- This is a cycle detection problem in a directed graph
- If there's a cycle, impossible to finish all courses
- Use DFS with three states: unvisited, visiting, visited
- Or use Kahn's algorithm (BFS with in-degrees)

## Common Mistakes

- Using only two states (visited/not visited) which doesn't detect all cycles
- Not handling disconnected components
- Confusing the direction of edges

## Related Problems

- Course Schedule II (210)
- Alien Dictionary (269)

## Tags

Graph, DFS, BFS, Topological Sort
