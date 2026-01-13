# Bit Manipulation Pattern - Study Guide

## Overview
Bit manipulation involves using bitwise operators to manipulate individual bits. It's one of the fastest operations in computing and is used for optimization, cryptography, compression, and low-level programming. Mastering bit manipulation can lead to elegant, efficient solutions.

## Bitwise Operators

### Basic Operations
```python
# AND: Both bits must be 1
5 & 3  # 0101 & 0011 = 0001 = 1

# OR: At least one bit must be 1
5 | 3  # 0101 | 0011 = 0111 = 7

# XOR: Bits must be different
5 ^ 3  # 0101 ^ 0011 = 0110 = 6

# NOT: Flip all bits
~5     # ~0101 = 1010 (in 2's complement: -6)

# Left Shift: Multiply by 2^n
5 << 1 # 0101 << 1 = 1010 = 10
5 << 2 # 0101 << 2 = 10100 = 20

# Right Shift: Divide by 2^n
5 >> 1 # 0101 >> 1 = 0010 = 2
5 >> 2 # 0101 >> 2 = 0001 = 1
```

## Fundamental Bit Tricks

### Check if ith Bit is Set
```python
def is_bit_set(num, i):
    """Check if ith bit is 1"""
    return (num & (1 << i)) != 0

# Example: is_bit_set(5, 0) = True (101 -> rightmost bit is 1)
# Example: is_bit_set(5, 1) = False (101 -> middle bit is 0)
```

### Set ith Bit
```python
def set_bit(num, i):
    """Set ith bit to 1"""
    return num | (1 << i)

# Example: set_bit(5, 1) = 7 (101 -> 111)
```

### Clear ith Bit
```python
def clear_bit(num, i):
    """Set ith bit to 0"""
    return num & ~(1 << i)

# Example: clear_bit(5, 2) = 1 (101 -> 001)
```

### Toggle ith Bit
```python
def toggle_bit(num, i):
    """Flip ith bit"""
    return num ^ (1 << i)

# Example: toggle_bit(5, 1) = 7 (101 -> 111)
# Example: toggle_bit(5, 0) = 4 (101 -> 100)
```

### Clear Rightmost Set Bit
```python
def clear_rightmost_set_bit(num):
    """Clear the rightmost 1 bit"""
    return num & (num - 1)

# Example: 6 & 5 = 4 (110 & 101 = 100)
# Use: Count set bits, check power of 2
```

### Isolate Rightmost Set Bit
```python
def isolate_rightmost_set_bit(num):
    """Get only the rightmost 1 bit"""
    return num & (-num)

# Example: 12 & -12 = 4 (1100 -> 0100)
# Use: Finding LSB in tree structures
```

### Check if Power of Two
```python
def is_power_of_two(n):
    """Power of 2 has only one bit set"""
    return n > 0 and (n & (n - 1)) == 0

# Example: 8 = 1000 -> 8 & 7 = 0 -> True
# Example: 6 = 0110 -> 6 & 5 = 4 -> False
```

## Common Bit Manipulation Patterns

### 1. Single Number Problems

**Single Number:**
```python
def single_number(nums):
    """Find number that appears once (others appear twice)"""
    result = 0
    for num in nums:
        result ^= num  # XOR cancels out pairs
    return result

# Time: O(n), Space: O(1)
# Property: a ^ a = 0, a ^ 0 = a
```

**Single Number II (Three Times):**
```python
def single_number_three_times(nums):
    """Find number appearing once (others thrice)"""
    ones = twos = 0

    for num in nums:
        twos |= ones & num
        ones ^= num
        threes = ones & twos
        ones &= ~threes
        twos &= ~threes

    return ones

# Time: O(n), Space: O(1)


def single_number_three_times_v2(nums):
    """Alternative: Count bits"""
    result = 0

    for i in range(32):
        bit_sum = sum((num >> i) & 1 for num in nums)
        if bit_sum % 3:
            result |= (1 << i)

    # Handle negative numbers in Python
    if result >= 2**31:
        result -= 2**32

    return result

# Time: O(32n), Space: O(1)
```

**Single Number III (Two Numbers Once):**
```python
def single_number_two_unique(nums):
    """Find two numbers appearing once"""
    # Get XOR of two unique numbers
    xor = 0
    for num in nums:
        xor ^= num

    # Find rightmost set bit (where numbers differ)
    rightmost_bit = xor & (-xor)

    # Partition numbers into two groups
    num1 = num2 = 0
    for num in nums:
        if num & rightmost_bit:
            num1 ^= num
        else:
            num2 ^= num

    return [num1, num2]

# Time: O(n), Space: O(1)
```

### 2. Count Set Bits

**Hamming Weight:**
```python
def hamming_weight(n):
    """Count number of 1 bits"""
    count = 0
    while n:
        n &= n - 1  # Clear rightmost set bit
        count += 1
    return count

# Time: O(number of set bits), Space: O(1)


def hamming_weight_v2(n):
    """Using Brian Kernighan's algorithm"""
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

# Time: O(log n), Space: O(1)


def hamming_weight_builtin(n):
    """Using Python builtin"""
    return bin(n).count('1')
```

**Hamming Distance:**
```python
def hamming_distance(x, y):
    """Number of positions where bits differ"""
    return bin(x ^ y).count('1')

# Time: O(1), Space: O(1)
```

**Total Hamming Distance:**
```python
def total_hamming_distance(nums):
    """Sum of Hamming distances between all pairs"""
    total = 0
    n = len(nums)

    for i in range(32):
        count_ones = sum((num >> i) & 1 for num in nums)
        count_zeros = n - count_ones
        total += count_ones * count_zeros

    return total

# Time: O(32n), Space: O(1)
```

### 3. Bit Manipulation Arithmetic

**Add Without Plus:**
```python
def add(a, b):
    """Add two numbers without + operator"""
    mask = 0xFFFFFFFF  # For 32-bit numbers

    while b != 0:
        # Sum without carry
        sum_without_carry = (a ^ b) & mask

        # Carry
        carry = ((a & b) << 1) & mask

        a = sum_without_carry
        b = carry

    # Handle negative numbers
    return a if a <= 0x7FFFFFFF else ~(a ^ mask)

# Time: O(1) - at most 32 iterations, Space: O(1)
```

**Subtract Without Minus:**
```python
def subtract(a, b):
    """Subtract using add"""
    return add(a, add(~b, 1))  # a + (-b), where -b = ~b + 1
```

**Multiply Without Operator:**
```python
def multiply(a, b):
    """Multiply using bit shifts"""
    result = 0
    while b > 0:
        if b & 1:
            result = add(result, a)
        a <<= 1
        b >>= 1
    return result

# Time: O(log b), Space: O(1)
```

**Divide Without Division:**
```python
def divide(dividend, divisor):
    """Divide without / operator"""
    if dividend == -2**31 and divisor == -1:
        return 2**31 - 1

    sign = (dividend > 0) == (divisor > 0)
    dividend, divisor = abs(dividend), abs(divisor)

    result = 0
    while dividend >= divisor:
        temp, multiple = divisor, 1

        while dividend >= (temp << 1):
            temp <<= 1
            multiple <<= 1

        dividend -= temp
        result += multiple

    return result if sign else -result

# Time: O(log²n), Space: O(1)
```

### 4. Reverse Bits

**Reverse Bits:**
```python
def reverse_bits(n):
    """Reverse bits of 32-bit unsigned integer"""
    result = 0
    for i in range(32):
        result <<= 1
        result |= n & 1
        n >>= 1
    return result

# Time: O(1), Space: O(1)


def reverse_bits_swap(n):
    """Using divide and conquer swapping"""
    # Swap adjacent bits
    n = ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)
    # Swap adjacent pairs
    n = ((n & 0xCCCCCCCC) >> 2) | ((n & 0x33333333) << 2)
    # Swap adjacent nibbles
    n = ((n & 0xF0F0F0F0) >> 4) | ((n & 0x0F0F0F0F) << 4)
    # Swap adjacent bytes
    n = ((n & 0xFF00FF00) >> 8) | ((n & 0x00FF00FF) << 8)
    # Swap halves
    n = (n >> 16) | (n << 16)
    return n & 0xFFFFFFFF

# Time: O(1), Space: O(1)
```

**Reverse Integer:**
```python
def reverse_integer(x):
    """Reverse digits of integer"""
    sign = -1 if x < 0 else 1
    x = abs(x)

    result = 0
    while x:
        result = result * 10 + x % 10
        x //= 10

    result *= sign

    # Check 32-bit overflow
    if result < -2**31 or result > 2**31 - 1:
        return 0

    return result

# Time: O(log x), Space: O(1)
```

### 5. Subsets Using Bits

**Generate All Subsets:**
```python
def subsets_bitwise(nums):
    """Generate all subsets using bit manipulation"""
    n = len(nums)
    result = []

    # Iterate through all possible subsets
    for mask in range(1 << n):  # 2^n subsets
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])
        result.append(subset)

    return result

# Time: O(2^n * n), Space: O(2^n)
```

### 6. Swap Operations

**Swap Without Temp Variable:**
```python
def swap_xor(a, b):
    """Swap using XOR"""
    a ^= b
    b ^= a
    a ^= b
    return a, b

# Only works when a and b are different variables
# Don't use for same variable or array elements at same index
```

**Swap Odd and Even Bits:**
```python
def swap_odd_even_bits(x):
    """Swap all odd and even bits"""
    # Get odd bits and shift right
    odd_bits = (x & 0xAAAAAAAA) >> 1

    # Get even bits and shift left
    even_bits = (x & 0x55555555) << 1

    return odd_bits | even_bits

# Time: O(1), Space: O(1)
```

### 7. Gray Code

**Gray Code:**
```python
def gray_code(n):
    """Generate n-bit Gray code sequence"""
    result = []
    for i in range(1 << n):
        result.append(i ^ (i >> 1))
    return result

# Time: O(2^n), Space: O(1) excluding output
# Gray code: Adjacent codes differ by exactly one bit
```

### 8. Bit Manipulation in Ranges

**Bitwise AND of Numbers Range:**
```python
def range_bitwise_and(left, right):
    """AND of all numbers in range [left, right]"""
    shift = 0
    while left < right:
        left >>= 1
        right >>= 1
        shift += 1

    return left << shift

# Time: O(log n), Space: O(1)
# Key insight: Result has common prefix of left and right
```

**Count Bits in Range:**
```python
def count_bits_range(n):
    """Count bits for numbers 0 to n"""
    result = [0] * (n + 1)

    for i in range(1, n + 1):
        result[i] = result[i >> 1] + (i & 1)

    return result

# Time: O(n), Space: O(n)
# DP: bits[i] = bits[i//2] + (i%2)
```

## Advanced Techniques

### Bit Masking for Subset DP
```python
def traveling_salesman_dp(dist):
    """TSP using bitmask DP"""
    n = len(dist)
    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1][0] = 0  # Start at city 0

    for mask in range(1 << n):
        for u in range(n):
            if mask & (1 << u):
                for v in range(n):
                    if not (mask & (1 << v)):
                        new_mask = mask | (1 << v)
                        dp[new_mask][v] = min(dp[new_mask][v],
                                             dp[mask][u] + dist[u][v])

    # Return to start
    mask = (1 << n) - 1
    return min(dp[mask][i] + dist[i][0] for i in range(1, n))

# Time: O(2^n * n²), Space: O(2^n * n)
```

### Bit Field Structures
```python
class Permissions:
    """Use bits for boolean flags"""
    READ = 1 << 0    # 0001
    WRITE = 1 << 1   # 0010
    EXECUTE = 1 << 2 # 0100
    DELETE = 1 << 3  # 1000

    def __init__(self, perms=0):
        self.perms = perms

    def grant(self, perm):
        self.perms |= perm

    def revoke(self, perm):
        self.perms &= ~perm

    def has(self, perm):
        return (self.perms & perm) == perm

    def toggle(self, perm):
        self.perms ^= perm

# Usage:
p = Permissions()
p.grant(Permissions.READ | Permissions.WRITE)
p.has(Permissions.READ)  # True
```

## Problem-Solving Strategy

1. **Identify Bit Manipulation Opportunity:**
   - Set operations (union, intersection)
   - Counting problems
   - Finding unique elements
   - Space optimization
   - Fast arithmetic

2. **Choose Right Technique:**
   - XOR for pairing/cancellation
   - AND for checking bits
   - OR for setting bits
   - Shifts for multiplication/division by 2

3. **Common Patterns to Recognize:**
   - `n & (n-1)`: Clear rightmost bit
   - `n & -n`: Isolate rightmost bit
   - `n ^ n`: Always 0
   - `n | 0`: Always n

4. **Handle Edge Cases:**
   - Negative numbers
   - Overflow
   - Different bit widths

## Time and Space Complexity

### Bit Operations:
- **All basic operations:** O(1) time
- **Counting bits:** O(log n) or O(number of bits)
- **Generating subsets:** O(2^n)

### Space Optimization:
- Can use bits instead of boolean arrays
- 32 booleans fit in one integer
- Reduce space by 32x for large datasets

## Common Mistakes

1. **Confusing & (bitwise AND) with && (logical AND)**
2. **Not handling negative numbers correctly**
3. **Integer overflow in shifts**
4. **Wrong operator precedence**
5. **Using signed vs unsigned integers**

## Practice Tips

1. **Memorize fundamental tricks**
2. **Practice converting to binary**
3. **Draw bit representations**
4. **Understand two's complement**
5. **Learn common bit masks**

## Use Cases

- **Optimization:** Fast arithmetic, space reduction
- **Cryptography:** XOR encryption
- **Compression:** Bit packing
- **Graphics:** Color manipulation
- **Networking:** IP address operations
- **System Programming:** Hardware interaction
- **Algorithms:** Subset enumeration, dynamic programming

## Related Patterns

- **Math:** Often combined with number theory
- **Dynamic Programming:** Bitmask DP for subsets
- **Hashing:** Bit manipulation in hash functions
- **Data Structures:** Binary indexed trees use bits
