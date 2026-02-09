"""
LeetCode Problem #133: Clone Graph
Difficulty: Medium
Pattern: Graphs
Link: https://leetcode.com/problems/clone-graph/

Problem:
--------
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (`int`) and a list (`List[Node]`) of its neighbors.

```

class Node {
    public int val;
    public List neighbors;
}

```

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with `val == 1`, the second node with `val == 2`, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with `val = 1`. You must return the copy of the given node as a reference to the cloned graph.

Constraints:
-----------
- The number of nodes in the graph is in the range `[0, 100]`.
- Node.val` is unique for each node.
- There are no repeated edges and no self-loops in the graph.
- The Graph is connected and all nodes can be visited starting from the given node.

Examples:
---------
Example 1:
```

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

```

Example 2:
```

Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

```

Example 3:
```

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.

```
"""

from typing import List, Optional
from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        pass

class Solution:
    """
    Solution to LeetCode Problem #133: Clone Graph

    Approach: DFS with Hash Map for Node Mapping

    Use a hash map to store the mapping from original nodes to their clones.
    For each node:
    1. If already cloned, return the clone from the map
    2. Otherwise, create a new clone and add to map
    3. Recursively clone all neighbors and add them to the clone's neighbor list

    Time Complexity: O(V + E) - visit each node and edge once
    Space Complexity: O(V) - hash map stores V nodes, recursion stack up to V

    Key Insights:
    - Hash map prevents infinite loops in cyclic graphs
    - Must create clone before processing neighbors (handles self-references)
    - DFS naturally handles the recursive nature of graph cloning
    - BFS can also be used with similar time/space complexity
    """
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Create a deep copy of the graph starting from the given node.
        """
        pass



PROBLEM_METADATA = {
    "number": 133,
    "name": "Clone Graph",
    "difficulty": "Medium",
    "pattern": "Graphs",
    "topics": ['Hash Table', 'Depth-First Search', 'Breadth-First Search', 'Graph Theory'],
    "url": "https://leetcode.com/problems/clone-graph/",
    "companies": ["Facebook", "Amazon", "Google", "Microsoft", "Bloomberg", "Uber"],
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V)",
}