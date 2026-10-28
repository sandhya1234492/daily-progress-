# LeetCode 2: Add Two Numbers

## Problem

You are given two non-empty linked lists representing two non-negative integers.

Each node contains a single digit, and digits are stored in reverse order.

For example, the list `[2, 4, 3]` represents the number `342`.

Your task is to add the two numbers and return the sum as a linked list.

## Approach

We add the numbers digit by digit, just like in manual addition:

- Add the current digits from both lists
- Add any carry from the previous step
- Store the last digit of the sum in a new node
- Keep the carry for the next position

We use a dummy node to make the result list easier to build.

## Example

Input:

- `l1 = [2, 4, 3]`
- `l2 = [5, 6, 4]`

This represents:

- `342 + 465 = 807`

Output:

- `[7, 0, 8]`

## Complexity

Let `m` and `n` be the lengths of the two linked lists.

- Time complexity: `O(max(m, n))`
- Space complexity: `O(max(m, n))`

## Python Solution

```python
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            total = carry

            if l1 is not None:
                total += l1.val
                l1 = l1.next

            if l2 is not None:
                total += l2.val
                l2 = l2.next

            current.next = ListNode(total % 10)
            current = current.next
            carry = total // 10

        return dummy.next
```
