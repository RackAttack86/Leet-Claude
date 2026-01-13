# Greedy Pattern - Study Guide

## Overview
The Greedy algorithm makes locally optimal choices at each step with the hope of finding a global optimum. Unlike Dynamic Programming, greedy algorithms don't look ahead or reconsider previous choices. They work when local optimum leads to global optimum.

## When to Use Greedy

- Problem exhibits greedy choice property (local optimum → global optimum)
- Problem has optimal substructure
- Making the best choice at each step works
- Usually simpler and faster than DP
- Common in optimization problems

## Signs a Greedy Approach Works

1. **Can prove greedy choice is safe**
2. **Optimal substructure exists**
3. **No need to reconsider past decisions**
4. **Problem asks for maximum/minimum with constraints**
5. **Sorting helps reveal the pattern**

## Common Greedy Patterns

### 1. Activity Selection / Interval Scheduling

**Maximum Non-Overlapping Intervals:**
```python
def erase_overlap_intervals(intervals):
    """Minimum removals to make non-overlapping"""
    if not intervals:
        return 0

    # Sort by end time (greedy choice)
    intervals.sort(key=lambda x: x[1])

    count = 0
    prev_end = intervals[0][1]

    for i in range(1, len(intervals)):
        if intervals[i][0] < prev_end:
            count += 1  # Overlap, remove one
        else:
            prev_end = intervals[i][1]  # Update end time

    return count

# Time: O(n log n), Space: O(1)
# Greedy choice: Always pick interval that ends earliest
```

**Meeting Rooms:**
```python
def can_attend_meetings(intervals):
    """Check if person can attend all meetings"""
    if not intervals:
        return True

    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False  # Overlap

    return True

# Time: O(n log n), Space: O(1)
```

**Minimum Meeting Rooms:**
```python
def min_meeting_rooms(intervals):
    """Minimum meeting rooms needed"""
    if not intervals:
        return 0

    # Separate start and end times
    starts = sorted([i[0] for i in intervals])
    ends = sorted([i[1] for i in intervals])

    rooms = 0
    max_rooms = 0
    s, e = 0, 0

    while s < len(starts):
        if starts[s] < ends[e]:
            rooms += 1
            max_rooms = max(max_rooms, rooms)
            s += 1
        else:
            rooms -= 1
            e += 1

    return max_rooms

# Time: O(n log n), Space: O(n)
```

### 2. Array/String Greedy

**Jump Game:**
```python
def can_jump(nums):
    """Can reach last index"""
    max_reach = 0

    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])

    return True

# Time: O(n), Space: O(1)


def jump_min_steps(nums):
    """Minimum jumps to reach end"""
    if len(nums) <= 1:
        return 0

    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])

        if i == current_end:
            jumps += 1
            current_end = farthest

    return jumps

# Time: O(n), Space: O(1)
```

**Container With Most Water:**
```python
def max_area(height):
    """Maximum water between two lines"""
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        max_water = max(max_water, min(height[left], height[right]) * width)

        # Greedy: Move pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water

# Time: O(n), Space: O(1)
```

**Gas Station:**
```python
def can_complete_circuit(gas, cost):
    """Find starting gas station to complete circuit"""
    if sum(gas) < sum(cost):
        return -1

    start = 0
    tank = 0

    for i in range(len(gas)):
        tank += gas[i] - cost[i]

        if tank < 0:
            # Can't start from any station before i
            start = i + 1
            tank = 0

    return start

# Time: O(n), Space: O(1)
```

### 3. Greedy with Sorting

**Assign Cookies:**
```python
def find_content_children(g, s):
    """Maximize number of content children"""
    g.sort()  # Children greed factors
    s.sort()  # Cookie sizes

    child = cookie = 0

    while child < len(g) and cookie < len(s):
        if s[cookie] >= g[child]:
            child += 1  # Child satisfied
        cookie += 1

    return child

# Time: O(n log n + m log m), Space: O(1)
```

**Minimum Arrows to Burst Balloons:**
```python
def find_min_arrows(points):
    """Minimum arrows to burst all balloons"""
    if not points:
        return 0

    # Sort by end position
    points.sort(key=lambda x: x[1])

    arrows = 1
    current_end = points[0][1]

    for i in range(1, len(points)):
        if points[i][0] > current_end:
            arrows += 1
            current_end = points[i][1]

    return arrows

# Time: O(n log n), Space: O(1)
```

**Two City Scheduling:**
```python
def two_city_sched_cost(costs):
    """Minimum cost to send n people to city A and n to city B"""
    # Greedy: Sort by difference in cost
    costs.sort(key=lambda x: x[0] - x[1])

    n = len(costs) // 2
    total = 0

    # Send first n to city A, rest to city B
    for i in range(n):
        total += costs[i][0]
    for i in range(n, 2 * n):
        total += costs[i][1]

    return total

# Time: O(n log n), Space: O(1)
```

### 4. Greedy with Heap/Priority Queue

**Task Scheduler:**
```python
def least_interval(tasks, n):
    """Minimum intervals to complete all tasks with cooldown"""
    from collections import Counter
    import heapq

    count = Counter(tasks)
    max_heap = [-c for c in count.values()]
    heapq.heapify(max_heap)

    time = 0
    cooldown = []

    while max_heap or cooldown:
        time += 1

        if max_heap:
            count = heapq.heappop(max_heap) + 1
            if count != 0:
                cooldown.append((count, time + n))

        if cooldown and cooldown[0][1] == time:
            heapq.heappush(max_heap, cooldown.pop(0)[0])

    return time

# Time: O(n), Space: O(1) - limited by 26 letters
```

**Reorganize String:**
```python
def reorganize_string(s):
    """Reorganize so no two adjacent chars are same"""
    from collections import Counter
    import heapq

    count = Counter(s)
    max_heap = [(-freq, char) for char, freq in count.items()]
    heapq.heapify(max_heap)

    prev_freq, prev_char = 0, ''
    result = []

    while max_heap:
        freq, char = heapq.heappop(max_heap)
        result.append(char)

        if prev_freq < 0:
            heapq.heappush(max_heap, (prev_freq, prev_char))

        prev_freq, prev_char = freq + 1, char

    result_str = ''.join(result)
    return result_str if len(result_str) == len(s) else ""

# Time: O(n log k), Space: O(k) where k is unique chars
```

### 5. Partition Problems

**Partition Labels:**
```python
def partition_labels(s):
    """Partition string into maximum parts"""
    # Record last occurrence of each character
    last = {char: i for i, char in enumerate(s)}

    partitions = []
    start = 0
    end = 0

    for i, char in enumerate(s):
        end = max(end, last[char])

        if i == end:
            partitions.append(end - start + 1)
            start = i + 1

    return partitions

# Time: O(n), Space: O(1) - limited by 26 letters
```

### 6. Stock Trading

**Best Time to Buy and Sell Stock II:**
```python
def max_profit(prices):
    """Max profit with unlimited transactions"""
    profit = 0

    for i in range(1, len(prices)):
        # Greedy: Capture every increase
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]

    return profit

# Time: O(n), Space: O(1)
```

**Best Time with Transaction Fee:**
```python
def max_profit_with_fee(prices, fee):
    """Max profit with transaction fee"""
    cash = 0  # Max profit if not holding stock
    hold = -prices[0]  # Max profit if holding stock

    for i in range(1, len(prices)):
        cash = max(cash, hold + prices[i] - fee)
        hold = max(hold, cash - prices[i])

    return cash

# Time: O(n), Space: O(1)
```

### 7. Minimum/Maximum Problems

**Minimum Add to Make Parentheses Valid:**
```python
def min_add_to_make_valid(s):
    """Minimum additions to make valid parentheses"""
    open_needed = 0
    close_needed = 0

    for char in s:
        if char == '(':
            open_needed += 1
        elif char == ')':
            if open_needed > 0:
                open_needed -= 1
            else:
                close_needed += 1

    return open_needed + close_needed

# Time: O(n), Space: O(1)
```

**Remove K Digits:**
```python
def remove_kdigits(num, k):
    """Remove k digits to get smallest number"""
    stack = []

    for digit in num:
        while stack and k > 0 and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)

    # Remove remaining k digits from end
    stack = stack[:len(stack) - k]

    # Remove leading zeros
    result = ''.join(stack).lstrip('0')

    return result if result else '0'

# Time: O(n), Space: O(n)
```

### 8. Fractional Knapsack

```python
def fractional_knapsack(capacity, items):
    """Maximum value with fractional items allowed"""
    # items = [(value, weight), ...]

    # Sort by value per unit weight (greedy choice)
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0
    remaining = capacity

    for value, weight in items:
        if remaining >= weight:
            # Take whole item
            total_value += value
            remaining -= weight
        else:
            # Take fraction of item
            total_value += value * (remaining / weight)
            break

    return total_value

# Time: O(n log n), Space: O(1)
```

## Greedy vs Dynamic Programming

### When Greedy Works:
```python
# Example: Coin change with coins [1, 5, 10, 25]
def coin_change_greedy(amount):
    coins = [25, 10, 5, 1]  # Sorted descending
    count = 0

    for coin in coins:
        count += amount // coin
        amount %= coin

    return count

# Works for standard US coins
# Time: O(1), Space: O(1)
```

### When Greedy Fails (Need DP):
```python
# Example: Coin change with coins [1, 3, 4]
# Amount = 6
# Greedy: 4 + 1 + 1 = 3 coins
# Optimal: 3 + 3 = 2 coins

# Need DP for this case
```

## Proving Greedy Correctness

### 1. Greedy Choice Property
Show that making greedy choice at each step doesn't prevent finding optimal solution.

### 2. Optimal Substructure
Show that optimal solution contains optimal solutions to subproblems.

### 3. Exchange Argument
Show that any optimal solution can be transformed into greedy solution without making it worse.

## Problem-Solving Strategy

1. **Identify if Greedy:**
   - Can you sort input meaningfully?
   - Is local optimum enough?
   - No need to reconsider choices?

2. **Find Greedy Choice:**
   - What locally optimal choice makes sense?
   - Sort by what criterion?
   - What to prioritize at each step?

3. **Prove Correctness:**
   - Does greedy choice lead to optimal?
   - Can you prove with exchange argument?
   - Test with counter examples

4. **Implement:**
   - Often involves sorting
   - May need heap for dynamic priorities
   - Usually simple implementation

5. **Optimize:**
   - Can avoid sorting?
   - Can use O(1) space?
   - Early termination possible?

## Common Greedy Strategies

### 1. Sort then Scan
```python
# Sort by some criterion
items.sort(key=lambda x: some_function(x))

# Make greedy choices
for item in items:
    if is_good_choice(item):
        take(item)
```

### 2. Two Pointers After Sort
```python
items.sort()
left, right = 0, len(items) - 1

while left < right:
    if condition:
        # Greedy choice
        left += 1
    else:
        right -= 1
```

### 3. Heap for Dynamic Priority
```python
import heapq

heap = []
for item in items:
    heapq.heappush(heap, priority(item))

while heap:
    process(heapq.heappop(heap))
```

## Time and Space Complexity

### Typical Complexities:
- **With sorting:** O(n log n) time, O(1) space
- **Without sorting:** O(n) time, O(1) space
- **With heap:** O(n log k) time, O(k) space

## Common Mistakes

1. **Using greedy when DP needed**
2. **Wrong sorting criterion**
3. **Not proving greedy is correct**
4. **Missing edge cases**
5. **Forgetting to sort when needed**

## Practice Tips

1. **Learn classic problems (interval scheduling, etc.)**
2. **Practice identifying when greedy works**
3. **Understand sorting criteria**
4. **Try to prove correctness**
5. **Compare with DP solutions**

## Related Patterns

- **Sorting:** Often prerequisite for greedy
- **Two Pointers:** Used with sorted input
- **Heap:** For dynamic priorities
- **Dynamic Programming:** Alternative when greedy fails
