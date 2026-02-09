# Problem 134: Gas Station

**Difficulty:** Medium
**Pattern:** Greedy
**Link:** [LeetCode](https://leetcode.com/problems/gas-station/)

## Problem Description

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i]. You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations. Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

## Constraints

- n == gas.length == cost.length
- 1 <= n <= 10^5
- 0 <= gas[i], cost[i] <= 10^4

## Examples

Example 1:
```
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation: Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
```

Example 2:
```
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation: You can't start at any station and make it around the circuit.
```

## Approaches

### 1. Greedy with Total and Current Tank

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    total_tank = 0  # Total gas - total cost for entire circuit
    current_tank = 0  # Current gas in tank
    start = 0  # Starting station candidate

    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total_tank += diff
        current_tank += diff

        # If tank becomes negative, can't start from any station before i+1
        if current_tank < 0:
            start = i + 1
            current_tank = 0

    # If total gas < total cost, circuit is impossible
    return start if total_tank >= 0 else -1
```

**Why this works:**
If total gas >= total cost, a solution exists. If we fail at station i (tank goes negative), we know we can't start from any station 0 to i. We reset our start to i+1 and continue. The greedy choice is to keep moving the start point forward whenever we fail.

## Key Insights

1. If total gas < total cost, impossible
2. If tank becomes negative, start can't be before current position
3. Reset start position when tank negative
4. One pass solution

## Common Mistakes

1. Using O(n^2) brute force trying each starting point
2. Not realizing that if we fail at i, we can't start from 0 to i
3. Forgetting to check total_tank at the end

## Related Problems

- 871. Minimum Number of Refueling Stops

## Tags

Array, Greedy
