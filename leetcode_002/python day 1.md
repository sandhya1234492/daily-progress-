# Python Coding Practice — Day 1: Two Sum

## Problem

Given a list of integers `nums` and an integer `target`, return the indices of
the two numbers that add up to `target`. You cannot use the same element twice.

## Solution

```python
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Map each number we've seen to its index.
        seen = {}

        for index, number in enumerate(nums):
            complement = target - number
            if complement in seen:
                return [seen[complement], index]
            seen[number] = index

        raise ValueError("No two numbers add up to the target")
```

## Logic

As we go through the list, we calculate the number needed to reach the target:
`complement = target - number`. A dictionary stores each earlier number and its
index. If the complement is already in the dictionary, we have found both
indices. Otherwise, we save the current number and continue.

The current number is checked before it is added to the dictionary, so it
cannot be used twice. This also handles duplicate values such as `[3, 3]`.

- **Time complexity:** `O(n)` — each list element is visited once.
- **Space complexity:** `O(n)` — the dictionary may store the numbers visited.

## Tests

```python
solution = Solution()

assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
assert solution.twoSum([3, 2, 4], 6) == [1, 2]
assert solution.twoSum([3, 3], 6) == [0, 1]

print("All three examples passed.")
```