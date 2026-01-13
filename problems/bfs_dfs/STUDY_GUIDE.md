# BFS/DFS Pattern - Study Guide

## Overview
BFS (Breadth-First Search) and DFS (Depth-First Search) are fundamental graph/tree traversal algorithms. BFS explores level by level, while DFS explores as deep as possible before backtracking. These patterns are essential for solving maze, grid, and graph problems.

## When to Use BFS vs DFS

### Use BFS When:
- Finding shortest path (unweighted graph)
- Level-order traversal needed
- Finding nodes at a certain distance
- Exploring neighbors before going deeper
- Finding minimum steps/moves

### Use DFS When:
- Exploring all paths
- Detecting cycles
- Topological sorting
- Finding connected components
- Memory constrained (DFS uses less memory than BFS for wide graphs)
- Backtracking problems

## DFS (Depth-First Search)

### DFS Template (Recursive)
```python
def dfs_recursive(graph, start, visited=None):
    """Standard DFS template using recursion"""
    if visited is None:
        visited = set()

    visited.add(start)
    # Process current node
    print(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

    return visited

# Time: O(V + E), Space: O(V) for recursion stack
```

### DFS Template (Iterative with Stack)
```python
def dfs_iterative(graph, start):
    """DFS using explicit stack"""
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            # Process node
            print(node)

            # Add neighbors to stack (reverse order for same order as recursive)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return visited

# Time: O(V + E), Space: O(V)
```

### DFS on Grid/Matrix
```python
def dfs_grid(grid, row, col, visited):
    """DFS on 2D grid with 4 directions"""
    rows, cols = len(grid), len(grid[0])

    # Bounds check
    if (row < 0 or row >= rows or
        col < 0 or col >= cols or
        (row, col) in visited or
        grid[row][col] == 0):  # Example: 0 is obstacle
        return

    visited.add((row, col))
    # Process cell
    print(f"Visiting ({row}, {col})")

    # Explore 4 directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        dfs_grid(grid, row + dr, col + dc, visited)

# Time: O(rows * cols), Space: O(rows * cols)
```

### DFS Applications

**Count Islands:**
```python
def num_islands(grid):
    """Count number of islands (connected 1s)"""
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    count = 0

    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or
            (r, c) in visited or grid[r][c] == '0'):
            return

        visited.add((r, c))
        # Visit all 4 directions
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                dfs(r, c)
                count += 1

    return count

# Time: O(m*n), Space: O(m*n)
```

**Detect Cycle in Directed Graph:**
```python
def has_cycle_directed(graph, n):
    """Detect cycle in directed graph using DFS"""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n

    def dfs(node):
        color[node] = GRAY  # Currently processing

        for neighbor in graph[node]:
            if color[neighbor] == GRAY:
                return True  # Back edge found (cycle)
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

**All Paths from Source to Target:**
```python
def all_paths_source_target(graph):
    """Find all paths from node 0 to node n-1"""
    n = len(graph)
    target = n - 1
    paths = []

    def dfs(node, path):
        if node == target:
            paths.append(path[:])
            return

        for neighbor in graph[node]:
            path.append(neighbor)
            dfs(neighbor, path)
            path.pop()  # Backtrack

    dfs(0, [0])
    return paths

# Time: O(2^V * V), Space: O(V)
```

## BFS (Breadth-First Search)

### BFS Template
```python
def bfs(graph, start):
    """Standard BFS template"""
    from collections import deque

    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()
        # Process node
        print(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited

# Time: O(V + E), Space: O(V)
```

### BFS with Level Tracking
```python
def bfs_with_levels(graph, start):
    """BFS that tracks levels/distances"""
    from collections import deque

    visited = {start}
    queue = deque([(start, 0)])  # (node, level)
    levels = {start: 0}

    while queue:
        node, level = queue.popleft()
        print(f"Node {node} at level {level}")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                levels[neighbor] = level + 1
                queue.append((neighbor, level + 1))

    return levels

# Time: O(V + E), Space: O(V)
```

### BFS on Grid/Matrix
```python
def bfs_grid(grid, start_row, start_col):
    """BFS on 2D grid"""
    from collections import deque

    rows, cols = len(grid), len(grid[0])
    visited = set([(start_row, start_col)])
    queue = deque([(start_row, start_col, 0)])  # (row, col, distance)

    while queue:
        row, col, dist = queue.popleft()
        # Process cell
        print(f"Cell ({row}, {col}) at distance {dist}")

        # Explore 4 directions
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + dr, col + dc

            if (0 <= new_row < rows and
                0 <= new_col < cols and
                (new_row, new_col) not in visited and
                grid[new_row][new_col] != 0):  # Example: 0 is obstacle

                visited.add((new_row, new_col))
                queue.append((new_row, new_col, dist + 1))

# Time: O(rows * cols), Space: O(rows * cols)
```

### BFS Applications

**Shortest Path in Unweighted Graph:**
```python
def shortest_path(graph, start, end):
    """Find shortest path using BFS"""
    from collections import deque

    if start == end:
        return [start]

    visited = {start}
    queue = deque([(start, [start])])

    while queue:
        node, path = queue.popleft()

        for neighbor in graph[node]:
            if neighbor == end:
                return path + [neighbor]

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None  # No path found

# Time: O(V + E), Space: O(V)
```

**Minimum Steps in Grid:**
```python
def shortest_path_binary_matrix(grid):
    """Find shortest path from top-left to bottom-right"""
    from collections import deque

    n = len(grid)

    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1

    # 8 directions (including diagonals)
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

    visited = {(0, 0)}
    queue = deque([(0, 0, 1)])  # (row, col, distance)

    while queue:
        row, col, dist = queue.popleft()

        if row == n - 1 and col == n - 1:
            return dist

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if (0 <= new_row < n and
                0 <= new_col < n and
                (new_row, new_col) not in visited and
                grid[new_row][new_col] == 0):

                visited.add((new_row, new_col))
                queue.append((new_row, new_col, dist + 1))

    return -1

# Time: O(n²), Space: O(n²)
```

**Level Order Traversal:**
```python
def level_order_traversal(root):
    """Level order traversal of binary tree"""
    from collections import deque

    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result

# Time: O(n), Space: O(w) where w is max width
```

**Word Ladder:**
```python
def ladder_length(begin_word, end_word, word_list):
    """Find shortest transformation sequence"""
    from collections import deque

    word_set = set(word_list)
    if end_word not in word_set:
        return 0

    queue = deque([(begin_word, 1)])

    while queue:
        word, length = queue.popleft()

        if word == end_word:
            return length

        # Try changing each character
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]

                if next_word in word_set:
                    word_set.remove(next_word)  # Mark as visited
                    queue.append((next_word, length + 1))

    return 0

# Time: O(M² * N) where M is word length, N is word list size
# Space: O(M * N)
```

## Multi-Source BFS

```python
def multi_source_bfs(grid):
    """BFS starting from multiple sources simultaneously"""
    from collections import deque

    rows, cols = len(grid), len(grid[0])
    queue = deque()
    visited = set()

    # Add all sources to queue initially
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # Example: 1 is source
                queue.append((r, c, 0))
                visited.add((r, c))

    while queue:
        row, col, dist = queue.popleft()
        # Process cell

        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            new_row, new_col = row + dr, col + dc

            if (0 <= new_row < rows and
                0 <= new_col < cols and
                (new_row, new_col) not in visited):

                visited.add((new_row, new_col))
                queue.append((new_row, new_col, dist + 1))
                grid[new_row][new_col] = dist + 1  # Update distance

# Time: O(rows * cols), Space: O(rows * cols)
# Example use: Find distance to nearest source from every cell
```

## Bidirectional BFS

```python
def bidirectional_bfs(graph, start, end):
    """BFS from both start and end to meet in middle"""
    from collections import deque

    if start == end:
        return 0

    # Two queues and visited sets
    front_queue = deque([start])
    back_queue = deque([end])
    front_visited = {start: 0}
    back_visited = {end: 0}

    while front_queue and back_queue:
        # Expand smaller frontier first
        if len(front_queue) <= len(back_queue):
            node = front_queue.popleft()
            depth = front_visited[node]

            for neighbor in graph[node]:
                if neighbor in back_visited:
                    return depth + 1 + back_visited[neighbor]

                if neighbor not in front_visited:
                    front_visited[neighbor] = depth + 1
                    front_queue.append(neighbor)
        else:
            node = back_queue.popleft()
            depth = back_visited[node]

            for neighbor in graph[node]:
                if neighbor in front_visited:
                    return depth + 1 + front_visited[neighbor]

                if neighbor not in back_visited:
                    back_visited[neighbor] = depth + 1
                    back_queue.append(neighbor)

    return -1  # No path

# Time: O(b^(d/2)) instead of O(b^d), Space: O(b^(d/2))
# where b is branching factor, d is depth
```

## 0-1 BFS (for weighted graphs with weights 0 and 1)

```python
def zero_one_bfs(graph, start, end):
    """BFS for graphs with edge weights 0 or 1"""
    from collections import deque

    distance = {start: 0}
    deq = deque([start])

    while deq:
        node = deq.popleft()

        for neighbor, weight in graph[node]:
            new_dist = distance[node] + weight

            if neighbor not in distance or new_dist < distance[neighbor]:
                distance[neighbor] = new_dist

                if weight == 0:
                    deq.appendleft(neighbor)  # Add to front for 0-weight
                else:
                    deq.append(neighbor)  # Add to back for 1-weight

    return distance.get(end, -1)

# Time: O(V + E), Space: O(V)
# More efficient than Dijkstra for 0-1 weights
```

## DFS vs BFS Comparison

### Matrix Flood Fill (Both Approaches)

**Using DFS:**
```python
def flood_fill_dfs(image, sr, sc, new_color):
    """Flood fill using DFS"""
    rows, cols = len(image), len(image[0])
    original_color = image[sr][sc]

    if original_color == new_color:
        return image

    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or
            image[r][c] != original_color):
            return

        image[r][c] = new_color

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    dfs(sr, sc)
    return image

# Time: O(m*n), Space: O(m*n) for recursion
```

**Using BFS:**
```python
def flood_fill_bfs(image, sr, sc, new_color):
    """Flood fill using BFS"""
    from collections import deque

    rows, cols = len(image), len(image[0])
    original_color = image[sr][sc]

    if original_color == new_color:
        return image

    queue = deque([(sr, sc)])
    image[sr][sc] = new_color

    while queue:
        r, c = queue.popleft()

        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc

            if (0 <= nr < rows and 0 <= nc < cols and
                image[nr][nc] == original_color):

                image[nr][nc] = new_color
                queue.append((nr, nc))

    return image

# Time: O(m*n), Space: O(m*n) for queue
```

## Common Patterns and Tricks

### 1. Visited Set vs Modifying Grid
```python
# Using visited set
visited = set()

# Modifying grid in-place (saves space)
grid[row][col] = '#'  # Mark as visited
```

### 2. Directions Array
```python
# 4 directions
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 8 directions (with diagonals)
directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

# Using in loop
for dr, dc in directions:
    new_r, new_c = row + dr, col + dc
```

### 3. State Representation
```python
# For problems with additional state
state = (row, col, keys_collected)
state = (position, direction, steps)
queue.append(state)
```

## Problem-Solving Strategy

1. **Choose BFS or DFS:**
   - Shortest path → BFS
   - All paths → DFS
   - Connected components → Either

2. **Consider Grid Representation:**
   - Graph adjacency list
   - 2D matrix/grid
   - Implicit graph (state space)

3. **Handle Visited Nodes:**
   - Set for visited tracking
   - Modify grid in-place
   - Distance dictionary

4. **Optimize for Large Inputs:**
   - Bidirectional BFS for meeting in middle
   - Multi-source BFS for multiple starting points
   - 0-1 BFS for binary weights

## Time and Space Complexity

### DFS:
- **Time:** O(V + E) for graphs, O(rows * cols) for grids
- **Space:** O(V) for recursion stack, O(h) for tree height

### BFS:
- **Time:** O(V + E) for graphs, O(rows * cols) for grids
- **Space:** O(V) for queue, O(w) for tree width

## Common Mistakes to Avoid

1. **Not checking bounds in grid problems**
2. **Forgetting to mark as visited before adding to queue (BFS)**
3. **Infinite loops from not tracking visited nodes**
4. **Wrong queue operations (append vs appendleft)**
5. **Not handling disconnected components**

## Practice Tips

1. **Master both DFS and BFS implementations**
2. **Practice grid problems with 4 and 8 directions**
3. **Understand when to use each algorithm**
4. **Learn state space representation**
5. **Practice with different graph representations**

## Related Patterns

- **Backtracking:** Uses DFS with state restoration
- **Dynamic Programming:** Can optimize DFS with memoization
- **Topological Sort:** Uses DFS or BFS
- **Shortest Path:** Dijkstra extends BFS for weighted graphs
