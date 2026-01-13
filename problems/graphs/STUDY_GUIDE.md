# Graphs Pattern - Study Guide

## Overview
A graph is a data structure consisting of vertices (nodes) and edges connecting them. Graphs can represent networks, relationships, dependencies, and many real-world scenarios. Understanding graph algorithms is crucial for solving complex connectivity and path problems.

## Graph Representations

### 1. Adjacency List (Most Common)
```python
# Using dictionary
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}

# Using list of lists (when nodes are 0 to n-1)
n = 5
graph = [[] for _ in range(n)]
graph[0] = [1, 2]
graph[1] = [0, 3, 4]
# ...

# For weighted graphs
graph = {
    0: [(1, 5), (2, 3)],  # (neighbor, weight)
    1: [(0, 5), (3, 2)],
    # ...
}
```

### 2. Adjacency Matrix
```python
# For n nodes
n = 5
graph = [[0] * n for _ in range(n)]

# Add edge from u to v
graph[u][v] = 1  # Unweighted
graph[u][v] = weight  # Weighted

# Example:
# graph[0][1] = 1 means edge from node 0 to node 1
```

### 3. Edge List
```python
# List of edges
edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4)]

# For weighted graphs
edges = [(0, 1, 5), (0, 2, 3), ...]  # (from, to, weight)
```

## Graph Types

- **Undirected**: Edges have no direction (bidirectional)
- **Directed**: Edges have direction (one-way)
- **Weighted**: Edges have weights/costs
- **Unweighted**: All edges have equal weight
- **Cyclic**: Contains at least one cycle
- **Acyclic**: No cycles (DAG - Directed Acyclic Graph)
- **Connected**: Path exists between any two vertices
- **Disconnected**: Some vertices are unreachable

## Building Graph from Input

```python
def build_graph(n, edges, directed=False):
    """Build adjacency list from edge list"""
    graph = {i: [] for i in range(n)}

    for edge in edges:
        if len(edge) == 2:  # Unweighted
            u, v = edge
            graph[u].append(v)
            if not directed:
                graph[v].append(u)
        else:  # Weighted
            u, v, w = edge
            graph[u].append((v, w))
            if not directed:
                graph[v].append((u, w))

    return graph
```

## Connected Components

### Find All Connected Components
```python
def find_connected_components(n, edges):
    """Find all connected components in undirected graph"""
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    components = []

    def dfs(node, component):
        visited.add(node)
        component.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, component)

    for node in range(n):
        if node not in visited:
            component = []
            dfs(node, component)
            components.append(component)

    return components

# Time: O(V + E), Space: O(V)
```

### Count Connected Components
```python
def count_components(n, edges):
    """Count number of connected components"""
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    count = 0

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    for node in range(n):
        if node not in visited:
            dfs(node)
            count += 1

    return count

# Time: O(V + E), Space: O(V)
```

## Union-Find (Disjoint Set Union)

```python
class UnionFind:
    """Union-Find data structure for connected components"""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x):
        """Find root with path compression"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Union by rank"""
        root_x, root_y = self.find(x), self.find(y)

        if root_x == root_y:
            return False  # Already connected

        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        self.components -= 1
        return True  # Successfully connected

    def connected(self, x, y):
        """Check if x and y are in same component"""
        return self.find(x) == self.find(y)

# Time: O(α(n)) per operation (nearly constant)
# Space: O(n)


# Usage example:
def count_components_uf(n, edges):
    uf = UnionFind(n)
    for u, v in edges:
        uf.union(u, v)
    return uf.components
```

## Cycle Detection

### Detect Cycle in Undirected Graph (DFS)
```python
def has_cycle_undirected(n, edges):
    """Detect cycle in undirected graph"""
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node, parent):
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True  # Back edge found (cycle)

        return False

    for node in range(n):
        if node not in visited:
            if dfs(node, -1):
                return True

    return False

# Time: O(V + E), Space: O(V)
```

### Detect Cycle in Directed Graph
```python
def has_cycle_directed(n, edges):
    """Detect cycle in directed graph using colors"""
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)

    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n

    def dfs(node):
        color[node] = GRAY  # Currently processing

        for neighbor in graph[node]:
            if color[neighbor] == GRAY:
                return True  # Back edge (cycle)
            if color[neighbor] == WHITE and dfs(neighbor):
                return True

        color[node] = BLACK  # Done processing
        return False

    for node in range(n):
        if color[node] == WHITE:
            if dfs(node):
                return True

    return False

# Time: O(V + E), Space: O(V)
```

## Topological Sort

### Topological Sort using DFS
```python
def topological_sort_dfs(n, edges):
    """Topological sort using DFS (works for DAG only)"""
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)

    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

        stack.append(node)  # Add after visiting all descendants

    for node in range(n):
        if node not in visited:
            dfs(node)

    return stack[::-1]  # Reverse to get topological order

# Time: O(V + E), Space: O(V)
```

### Topological Sort using BFS (Kahn's Algorithm)
```python
def topological_sort_bfs(n, edges):
    """Topological sort using BFS (Kahn's algorithm)"""
    from collections import deque

    graph = {i: [] for i in range(n)}
    in_degree = [0] * n

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    # Start with nodes having no incoming edges
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If result doesn't contain all nodes, there's a cycle
    return result if len(result) == n else []

# Time: O(V + E), Space: O(V)
```

## Shortest Path Algorithms

### Dijkstra's Algorithm (Single Source, Non-Negative Weights)
```python
def dijkstra(graph, start, n):
    """Find shortest paths from start to all nodes"""
    import heapq

    distances = [float('inf')] * n
    distances[start] = 0
    heap = [(0, start)]  # (distance, node)
    visited = set()

    while heap:
        dist, node = heapq.heappop(heap)

        if node in visited:
            continue

        visited.add(node)

        for neighbor, weight in graph[node]:
            new_dist = dist + weight

            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return distances

# Time: O((V + E) log V), Space: O(V)
```

### Bellman-Ford Algorithm (Single Source, Can Handle Negative Weights)
```python
def bellman_ford(n, edges, start):
    """Find shortest paths, detect negative cycles"""
    distances = [float('inf')] * n
    distances[start] = 0

    # Relax edges n-1 times
    for _ in range(n - 1):
        for u, v, weight in edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    # Check for negative cycles
    for u, v, weight in edges:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            return None  # Negative cycle exists

    return distances

# Time: O(V * E), Space: O(V)
```

### Floyd-Warshall Algorithm (All Pairs Shortest Path)
```python
def floyd_warshall(n, edges):
    """Find shortest paths between all pairs of nodes"""
    # Initialize distance matrix
    dist = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for u, v, weight in edges:
        dist[u][v] = weight

    # Try each intermediate node
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# Time: O(V³), Space: O(V²)
```

## Minimum Spanning Tree

### Kruskal's Algorithm (Using Union-Find)
```python
def kruskal_mst(n, edges):
    """Find minimum spanning tree using Kruskal's algorithm"""
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    uf = UnionFind(n)
    mst_edges = []
    total_cost = 0

    for u, v, weight in edges:
        if uf.union(u, v):
            mst_edges.append((u, v, weight))
            total_cost += weight

            if len(mst_edges) == n - 1:
                break

    return mst_edges, total_cost

# Time: O(E log E), Space: O(V)
```

### Prim's Algorithm (Using Heap)
```python
def prim_mst(graph, n):
    """Find minimum spanning tree using Prim's algorithm"""
    import heapq

    visited = set([0])
    heap = [(weight, 0, neighbor) for neighbor, weight in graph[0]]
    heapq.heapify(heap)

    mst_edges = []
    total_cost = 0

    while heap and len(visited) < n:
        weight, frm, to = heapq.heappop(heap)

        if to in visited:
            continue

        visited.add(to)
        mst_edges.append((frm, to, weight))
        total_cost += weight

        for neighbor, edge_weight in graph[to]:
            if neighbor not in visited:
                heapq.heappush(heap, (edge_weight, to, neighbor))

    return mst_edges, total_cost

# Time: O(E log V), Space: O(V + E)
```

## Bipartite Graph

### Check if Bipartite (Coloring Method)
```python
def is_bipartite(graph, n):
    """Check if graph is bipartite using 2-coloring"""
    color = [-1] * n  # -1 means uncolored

    def bfs(start):
        from collections import deque
        queue = deque([start])
        color[start] = 0

        while queue:
            node = queue.popleft()

            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False  # Same color as neighbor

        return True

    # Check all components
    for node in range(n):
        if color[node] == -1:
            if not bfs(node):
                return False

    return True

# Time: O(V + E), Space: O(V)
```

## Advanced Graph Patterns

### Tarjan's Algorithm (Strongly Connected Components)
```python
def tarjan_scc(n, graph):
    """Find strongly connected components"""
    index_counter = [0]
    stack = []
    lowlinks = [0] * n
    index = [0] * n
    on_stack = [False] * n
    index_initialized = [False] * n
    sccs = []

    def strongconnect(v):
        index[v] = index_counter[0]
        lowlinks[v] = index_counter[0]
        index_counter[0] += 1
        index_initialized[v] = True
        stack.append(v)
        on_stack[v] = True

        for w in graph[v]:
            if not index_initialized[w]:
                strongconnect(w)
                lowlinks[v] = min(lowlinks[v], lowlinks[w])
            elif on_stack[w]:
                lowlinks[v] = min(lowlinks[v], index[w])

        if lowlinks[v] == index[v]:
            component = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                component.append(w)
                if w == v:
                    break
            sccs.append(component)

    for v in range(n):
        if not index_initialized[v]:
            strongconnect(v)

    return sccs

# Time: O(V + E), Space: O(V)
```

### Eulerian Path/Circuit
```python
def has_eulerian_path(n, edges, directed=False):
    """Check if Eulerian path exists"""
    graph = {i: [] for i in range(n)}
    in_degree = [0] * n
    out_degree = [0] * n

    for u, v in edges:
        graph[u].append(v)
        out_degree[u] += 1
        in_degree[v] += 1

        if not directed:
            graph[v].append(u)
            out_degree[v] += 1
            in_degree[u] += 1

    if directed:
        start_nodes = sum(1 for i in range(n) if out_degree[i] - in_degree[i] == 1)
        end_nodes = sum(1 for i in range(n) if in_degree[i] - out_degree[i] == 1)
        return (start_nodes == 1 and end_nodes == 1) or (start_nodes == 0 and end_nodes == 0)
    else:
        odd_degree = sum(1 for i in range(n) if (in_degree[i] + out_degree[i]) % 2 == 1)
        return odd_degree == 0 or odd_degree == 2

# Time: O(V + E), Space: O(V + E)
```

## Problem-Solving Strategy

1. **Identify Graph Type:**
   - Directed or undirected?
   - Weighted or unweighted?
   - Dense or sparse? (affects representation choice)

2. **Choose Representation:**
   - Adjacency list (most problems)
   - Adjacency matrix (dense graphs, matrix operations)
   - Edge list (Union-Find, MST problems)

3. **Select Algorithm:**
   - Connectivity: DFS, BFS, Union-Find
   - Shortest path: BFS (unweighted), Dijkstra, Bellman-Ford
   - Cycles: DFS with colors
   - Topological sort: DFS or Kahn's algorithm
   - MST: Kruskal or Prim

4. **Handle Edge Cases:**
   - Empty graph
   - Disconnected components
   - Self-loops
   - Multiple edges between same nodes

## Time and Space Complexity

### Graph Operations:
- **Add vertex:** O(1)
- **Add edge:** O(1) for adjacency list
- **Check if edge exists:** O(V) for list, O(1) for matrix
- **Get all neighbors:** O(degree) for list, O(V) for matrix

### Common Algorithms:
- **DFS/BFS:** O(V + E) time, O(V) space
- **Dijkstra:** O((V + E) log V) with heap
- **Bellman-Ford:** O(V * E)
- **Floyd-Warshall:** O(V³)
- **Kruskal MST:** O(E log E)
- **Prim MST:** O(E log V)

## Common Mistakes to Avoid

1. **Not handling disconnected graphs**
2. **Forgetting to mark nodes as visited**
3. **Wrong graph representation for problem type**
4. **Not checking for cycles in DAG assumptions**
5. **Using wrong algorithm (Dijkstra with negative weights)**

## Practice Tips

1. **Master graph representations**
2. **Understand DFS and BFS deeply**
3. **Practice Union-Find thoroughly**
4. **Learn when to use each shortest path algorithm**
5. **Visualize graphs on paper**
6. **Practice both directed and undirected variants**

## Related Patterns

- **BFS/DFS:** Foundation of graph algorithms
- **Dynamic Programming:** Can optimize graph problems
- **Greedy:** Used in MST and some shortest path algorithms
- **Backtracking:** For finding all paths
