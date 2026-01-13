# Stacks and Queues Pattern - Study Guide

## Overview
Stacks and Queues are fundamental data structures that manage collections of elements with specific access patterns. Stacks follow LIFO (Last In, First Out), while Queues follow FIFO (First In, First Out). They're essential for many algorithmic problems.

## Stack Fundamentals

### Stack Implementation
```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# All operations: O(1) time
```

### Using List as Stack
```python
stack = []
stack.append(item)  # Push
top = stack.pop()   # Pop
top = stack[-1]     # Peek
```

## Queue Fundamentals

### Queue Implementation
```python
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()

    def front(self):
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# All operations: O(1) time
```

### Using Deque as Queue
```python
from collections import deque

queue = deque()
queue.append(item)      # Enqueue
front = queue.popleft() # Dequeue
front = queue[0]        # Peek
```

## Stack Patterns

### 1. Valid Parentheses

```python
def is_valid(s):
    """Check if parentheses are valid"""
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            # Closing bracket
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            # Opening bracket
            stack.append(char)

    return len(stack) == 0

# Time: O(n), Space: O(n)
```

### 2. Monotonic Stack

**Next Greater Element:**
```python
def next_greater_element(nums):
    """Find next greater element for each element"""
    n = len(nums)
    result = [-1] * n
    stack = []  # Stores indices

    for i in range(n):
        # Pop smaller elements and update their next greater
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]

        stack.append(i)

    return result

# Time: O(n), Space: O(n)
# Example: [2,1,2,4,3] -> [4,2,4,-1,-1]
```

**Next Greater Element (Circular):**
```python
def next_greater_elements_circular(nums):
    """Next greater in circular array"""
    n = len(nums)
    result = [-1] * n
    stack = []

    # Process array twice for circular
    for i in range(2 * n):
        while stack and nums[stack[-1]] < nums[i % n]:
            result[stack.pop()] = nums[i % n]

        if i < n:
            stack.append(i)

    return result

# Time: O(n), Space: O(n)
```

**Daily Temperatures:**
```python
def daily_temperatures(temperatures):
    """Days until warmer temperature"""
    n = len(temperatures)
    result = [0] * n
    stack = []

    for i in range(n):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            idx = stack.pop()
            result[idx] = i - idx

        stack.append(i)

    return result

# Time: O(n), Space: O(n)
```

**Largest Rectangle in Histogram:**
```python
def largest_rectangle_area(heights):
    """Find largest rectangle in histogram"""
    stack = []
    max_area = 0
    heights.append(0)  # Sentinel

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)

        stack.append(i)

    heights.pop()  # Remove sentinel
    return max_area

# Time: O(n), Space: O(n)
```

### 3. Expression Evaluation

**Basic Calculator:**
```python
def calculate(s):
    """Evaluate expression with +, -, (, )"""
    stack = []
    num = 0
    sign = 1
    result = 0

    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == '+':
            result += sign * num
            num = 0
            sign = 1
        elif char == '-':
            result += sign * num
            num = 0
            sign = -1
        elif char == '(':
            # Push current result and sign
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif char == ')':
            result += sign * num
            num = 0
            result *= stack.pop()  # Pop sign
            result += stack.pop()  # Pop previous result

    return result + sign * num

# Time: O(n), Space: O(n)
```

**Reverse Polish Notation:**
```python
def eval_rpn(tokens):
    """Evaluate Reverse Polish Notation"""
    stack = []

    for token in tokens:
        if token in ['+', '-', '*', '/']:
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:
                stack.append(int(a / b))  # Truncate toward zero
        else:
            stack.append(int(token))

    return stack[0]

# Time: O(n), Space: O(n)
```

### 4. String Manipulation

**Remove Duplicates:**
```python
def remove_duplicates(s):
    """Remove adjacent duplicates"""
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return ''.join(stack)

# Time: O(n), Space: O(n)
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

    # Remove remaining k digits
    stack = stack[:len(stack) - k]

    return ''.join(stack).lstrip('0') or '0'

# Time: O(n), Space: O(n)
```

**Decode String:**
```python
def decode_string(s):
    """Decode string with pattern k[encoded_string]"""
    stack = []
    current_num = 0
    current_str = ''

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append(current_str)
            stack.append(current_num)
            current_str = ''
            current_num = 0
        elif char == ']':
            num = stack.pop()
            prev_str = stack.pop()
            current_str = prev_str + current_str * num
        else:
            current_str += char

    return current_str

# Time: O(n), Space: O(n)
```

### 5. Min/Max Stack

```python
class MinStack:
    """Stack with O(1) min operation"""
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()
            return val

    def top(self):
        return self.stack[-1] if self.stack else None

    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None

# All operations: O(1) time, O(n) space
```

## Queue Patterns

### 1. Queue Using Stacks

```python
class MyQueue:
    """Queue implemented using two stacks"""
    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x):
        self.input_stack.append(x)

    def pop(self):
        self._move()
        return self.output_stack.pop()

    def peek(self):
        self._move()
        return self.output_stack[-1]

    def empty(self):
        return not self.input_stack and not self.output_stack

    def _move(self):
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())

# Push: O(1), Pop/Peek: O(1) amortized
```

### 2. Circular Queue

```python
class MyCircularQueue:
    """Circular queue with fixed size"""
    def __init__(self, k):
        self.queue = [0] * k
        self.head = 0
        self.tail = -1
        self.size = 0
        self.capacity = k

    def enqueue(self, value):
        if self.is_full():
            return False
        self.tail = (self.tail + 1) % self.capacity
        self.queue[self.tail] = value
        self.size += 1
        return True

    def dequeue(self):
        if self.is_empty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def front(self):
        return -1 if self.is_empty() else self.queue[self.head]

    def rear(self):
        return -1 if self.is_empty() else self.queue[self.tail]

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

# All operations: O(1) time, O(k) space
```

### 3. Sliding Window Maximum

```python
def max_sliding_window(nums, k):
    """Maximum of each sliding window"""
    from collections import deque

    result = []
    deq = deque()  # Stores indices

    for i in range(len(nums)):
        # Remove elements outside window
        while deq and deq[0] < i - k + 1:
            deq.popleft()

        # Remove smaller elements (not useful)
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()

        deq.append(i)

        # Add to result once window is full
        if i >= k - 1:
            result.append(nums[deq[0]])

    return result

# Time: O(n), Space: O(k)
```

### 4. Moving Average

```python
class MovingAverage:
    """Calculate moving average from stream"""
    def __init__(self, size):
        from collections import deque
        self.queue = deque()
        self.size = size
        self.sum = 0

    def next(self, val):
        self.queue.append(val)
        self.sum += val

        if len(self.queue) > self.size:
            self.sum -= self.queue.popleft()

        return self.sum / len(self.queue)

# Time: O(1) per operation, Space: O(size)
```

## Deque Patterns

### Deque (Double-Ended Queue)
```python
from collections import deque

# Can operate on both ends efficiently
dq = deque()

# Operations: all O(1)
dq.append(x)      # Add to right
dq.appendleft(x)  # Add to left
dq.pop()          # Remove from right
dq.popleft()      # Remove from left
```

### Monotonic Deque

```python
def shortest_subarray_with_sum_k(nums, k):
    """Shortest subarray with sum >= k"""
    from collections import deque

    n = len(nums)
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)

    deq = deque()
    min_len = float('inf')

    for i in range(n + 1):
        # Check if we can form valid subarray
        while deq and prefix[i] - prefix[deq[0]] >= k:
            min_len = min(min_len, i - deq.popleft())

        # Maintain increasing deque
        while deq and prefix[i] <= prefix[deq[-1]]:
            deq.pop()

        deq.append(i)

    return min_len if min_len != float('inf') else -1

# Time: O(n), Space: O(n)
```

## Priority Queue (Heap)

### Basic Heap Operations
```python
import heapq

# Min heap (default in Python)
heap = []
heapq.heappush(heap, item)
min_item = heapq.heappop(heap)
min_item = heap[0]  # Peek

# Max heap (negate values)
max_heap = []
heapq.heappush(max_heap, -item)
max_item = -heapq.heappop(max_heap)

# Heapify list
heapq.heapify(arr)
```

### Top K Elements

```python
def find_kth_largest(nums, k):
    """Find kth largest element"""
    import heapq

    # Use min heap of size k
    heap = []

    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]

# Time: O(n log k), Space: O(k)
```

## Problem-Solving Strategy

### When to Use Stack:
- Last In, First Out access needed
- Matching/balancing problems (parentheses)
- Expression evaluation
- Backtracking
- Next greater/smaller element
- Histogram problems

### When to Use Queue:
- First In, First Out access needed
- BFS traversal
- Level-order processing
- Sliding window problems
- Rate limiting / scheduling

### When to Use Deque:
- Need access to both ends
- Sliding window maximum/minimum
- Palindrome checking
- Implementing stack or queue

## Time and Space Complexity

### Stack Operations:
- Push: O(1)
- Pop: O(1)
- Peek: O(1)
- Space: O(n)

### Queue Operations:
- Enqueue: O(1)
- Dequeue: O(1) with deque
- Peek: O(1)
- Space: O(n)

### Common Patterns:
- Monotonic stack: O(n) time, O(n) space
- Queue with stacks: O(1) amortized
- Sliding window: O(n) time, O(k) space

## Common Mistakes

1. **Using list for queue (O(n) dequeue)**
2. **Not checking if stack/queue is empty**
3. **Wrong monotonic stack direction**
4. **Forgetting to handle edge cases**
5. **Not maintaining invariants**

## Practice Tips

1. **Master basic stack/queue operations**
2. **Understand monotonic stack thoroughly**
3. **Practice with parentheses problems**
4. **Learn sliding window with deque**
5. **Implement data structures from scratch**

## Related Patterns

- **DFS:** Uses stack (recursion or explicit)
- **BFS:** Uses queue
- **Sliding Window:** Often uses deque
- **Expression Parsing:** Uses stack
- **Backtracking:** Implicitly uses stack
