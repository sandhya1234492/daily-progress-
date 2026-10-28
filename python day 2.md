# Python Day 2: LeetCode 2 - Add Two Numbers

This is a beginner-friendly explanation of the problem and the solution.

## 1) Problem statement in simple words

You are given two linked lists.

- Each node in the list contains one digit.
- The digits are stored in reverse order.
- Example: 342 is stored as 2 -> 4 -> 3
- We need to add the two numbers represented by the lists.
- Then return the result also as a linked list.

Example:

- l1 = [2, 4, 3] means number 342
- l2 = [5, 6, 4] means number 465
- 342 + 465 = 807
- result = [7, 0, 8]

Important idea:

- This is not a normal integer addition problem.
- We add digit by digit, just like school math.
- If the sum is 10 or more, we carry the extra value to the next digit.

## 2) Logic of the solution step by step

We use a linked list to store the answer.

The main ideas are:

1. Start from the beginning of both lists.
2. Add the values in each node.
3. Add the carry from the previous step.
4. Store the last digit of the sum in a new node.
5. Keep the carry for the next digit.
6. Keep going until both lists are finished and carry is 0.

### Example

Input:

- l1 = 2 -> 4 -> 3
- l2 = 5 -> 6 -> 4

Step-by-step:

- 2 + 5 = 7 -> write 7, carry 0
- 4 + 6 = 10 -> write 0, carry 1
- 3 + 4 + 1 = 8 -> write 8, carry 0

Result:

- 7 -> 0 -> 8

So output is:

- [7, 0, 8]

## 3) Explain every line of the Python code

Here is the standard correct solution:

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

### Line by line

#### `from typing import Optional`

This imports `Optional` from Python's `typing` module.

It tells Python that a value may be a `ListNode` or `None`.

This is helpful for type hints.

---

#### `class ListNode:`

This creates a custom class for a linked list node.

Each node has:

- `val`: the digit stored in the node
- `next`: a reference to the next node in the list

---

#### `def __init__(self, val=0, next=None):`

This is the constructor method.

It runs automatically when we create a new node.

Example:

```python
node = ListNode(5)
```

This creates a node with:

- `val = 5`
- `next = None`

---

#### `self.val = val`

This stores the value in the node.

---

#### `self.next = next`

This links this node to the next node.

If there is no next node, it is `None`.

---

#### `class Solution:`

This is the class where the problem solution is written.

LeetCode usually expects the method inside this class.

---

#### `def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:`

This defines the method to solve the problem.

- `self` is the class instance
- `l1` is the first linked list
- `l2` is the second linked list
- Return type is `Optional[ListNode]`, meaning the result is either a linked list or `None`

---

#### `dummy = ListNode(0)`

This creates a fake node at the beginning.

Why do we need it?

Because the real first node of the answer may not exist yet when we begin.

`dummy` makes our code simpler.

This is a common linked-list trick.

---

#### `current = dummy`

This makes `current` point to the dummy node.

We will build the answer from here.

At the beginning:

- `dummy` is the starting node
- `current` is used to move along the result list

---

#### `carry = 0`

This tracks the extra value from a sum greater than 9.

Example:

- 4 + 6 = 10
- write 0
- carry = 1

---

#### `while l1 is not None or l2 is not None or carry != 0:`

This is the loop condition.

We keep looping while any of these are true:

- there are more nodes in `l1`
- there are more nodes in `l2`
- there is still a carry value

This makes sure we do not miss the final carry.

---

#### `total = carry`

We start the current digit sum with the carry from the previous step.

---

#### `if l1 is not None:`

If there is still a node in `l1`, we add its value.

---

#### `total += l1.val`

Add the current digit from the first list.

---

#### `l1 = l1.next`

Move to the next node in `l1`.

This is important because we process the linked list from left to right (from head to tail).

---

#### `if l2 is not None:`

If there is still a node in `l2`, add its value.

---

#### `total += l2.val`

Add the digit from the second list.

---

#### `l2 = l2.next`

Move to the next node in `l2`.

---

#### `current.next = ListNode(total % 10)`

This creates a new node for the digit in the answer.

- `total % 10` keeps only the last digit
- Example: if `total = 13`, then `13 % 10 = 3`

We attach it to `current.next`.

---

#### `current = current.next`

Move `current` to the newly created node.

Now we are ready to add the next digit.

---

#### `carry = total // 10`

This finds the carry value.

- Example: `total = 13`, `13 // 10 = 1`
- Example: `total = 8`, `8 // 10 = 0`

---

#### `return dummy.next`

We return the node after the dummy node.

This is the real head of the result list.

The dummy node is only used as a helper.

## 4) Explain linked lists, ListNode, carry, dummy, and current with simple examples

### Linked list

A linked list is a chain of nodes.

Each node contains:

- data/value
- pointer/reference to the next node

Example:

```python
node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)

node1.next = node2
node2.next = node3
```

This means:

- node1 stores 2
- node2 stores 4
- node3 stores 3
- node1 points to node2
- node2 points to node3

So we represent:

- 2 -> 4 -> 3

### `ListNode`

`ListNode` is just a custom class for one node.

It looks like this:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

Example:

```python
n = ListNode(7)
print(n.val)   # 7
print(n.next)  # None
```

### `carry`

Carry is like in normal addition.

When the sum is 10 or more, we write the last digit and carry the extra part.

Example:

- 8 + 9 = 17
- write 7
- carry 1

In the code:

```python
carry = total // 10
```

### `dummy`

`dummy` is a fake node used as a starting placeholder.

It helps because we often build the answer list while moving `current` forward.

Example:

```python
dummy = ListNode(0)
current = dummy
```

Now `current` starts at a safe starting point.

When we create answer nodes, we connect them like:

```python
current.next = ListNode(7)
current = current.next
```

This is much easier than trying to handle the first node separately.

### `current`

`current` is the node we are currently working on in the result list.

At first, it points to `dummy`.

Then we keep moving it forward.

Example:

```python
current = dummy
current.next = ListNode(5)
current = current.next
current.next = ListNode(3)
```

Now the result list is:

- 0 -> 5 -> 3

And if we return `dummy.next`, we get:

- 5 -> 3

## 5) How the code works with l1 = [2,4,3] and l2 = [5,6,4]

We are adding two numbers:

- l1 = 2 -> 4 -> 3
- l2 = 5 -> 6 -> 4

This means:

- 342 + 465 = 807

### Step 1: Start

```python
dummy = ListNode(0)
current = dummy
carry = 0
```

The result list starts empty.

### Step 2: First digit

l1 value = 2
l2 value = 5

Sum = 2 + 5 + carry = 2 + 5 + 0 = 7

- `total = 7`
- `current.next = ListNode(7)`
- `current = current.next`
- `carry = 7 // 10 = 0`

Result list now:

- 7

### Step 3: Second digit

l1 value = 4
l2 value = 6

Sum = 4 + 6 + 0 = 10

- `total = 10`
- `current.next = ListNode(10 % 10)` => `ListNode(0)`
- `current = current.next`
- `carry = 10 // 10 = 1`

Result list now:

- 7 -> 0

### Step 4: Third digit

l1 value = 3
l2 value = 4

Also add carry = 1

Sum = 3 + 4 + 1 = 8

- `total = 8`
- `current.next = ListNode(8)`
- `current = current.next`
- `carry = 8 // 10 = 0`

Result list now:

- 7 -> 0 -> 8

### Step 5: End

Both lists are done and carry = 0, so we stop.

Return `dummy.next`, which is:

- 7 -> 0 -> 8

Final answer:

```python
[7, 0, 8]
```

## 6) Time complexity and space complexity

### Time complexity

We visit each node once.

- `l1` may have length `m`
- `l2` may have length `n`

The loop runs up to `max(m, n) + 1` times because of carry.

So the time complexity is:

```python
O(max(m, n))
```

### Space complexity

We create a new linked list for the result.

The extra space used is for the output nodes.

So the space complexity is:

```python
O(max(m, n))
```

This is standard for this problem.

## 7) Check if the solution is correct and follows LeetCode requirements

This solution is correct because:

- It processes both lists from left to right.
- It adds digits and carry properly.
- It creates a new result list.
- It handles the final carry.
- It works even when one list is longer than the other.

It follows LeetCode requirements because:

- The function signature matches the problem
- It returns the sum as a linked list
- It uses `ListNode` correctly
- It does not print unnecessary output
- It works in the expected online judge environment

## 8) Python file: 002_add_two_numbers.py

I created a working Python file for this solution in the repository.

File created:

- [leetcode_002/002_add_two_numbers.py](C:/Users/sandh/daily-progress-/leetcode_002/002_add_two_numbers.py)

## 9) README file

I also created a beginner-friendly README for the problem here:

- [leetcode_002/README.md](C:/Users/sandh/daily-progress-/leetcode_002/README.md)

## 10) How to upload it to GitHub (repository name: LeetCode-Practice)

Follow these steps.

### Step 1: Open Git Bash or Terminal

Go to the folder where your project is saved.

Example:

```bash
cd C:/Users/yourname/LeetCode-Practice
```

### Step 2: Check the files

```bash
git status
```

### Step 3: Add files

```bash
git add .
```

### Step 4: Commit files

```bash
git commit -m "Add solution for Add Two Numbers"
```

### Step 5: Create a GitHub repository

On GitHub:

- click New repository
- name it `LeetCode-Practice`
- choose public or private
- click Create repository

### Step 6: Connect local repo to GitHub

```bash
git remote add origin https://github.com/YOUR_USERNAME/LeetCode-Practice.git
```

Replace `YOUR_USERNAME` with your actual GitHub username.

### Step 7: Push code

```bash
git push -u origin main
```

If your branch is `master`, use:

```bash
git push -u origin master
```

### Step 8: Check on GitHub

Open your GitHub repository and confirm that your file is uploaded.

## Final beginner summary

This problem teaches us how to:

- work with linked lists
- add numbers digit by digit
- use carry values
- build a new list without changing the original input

The key idea is:

- add digits
- store the remainder
- carry the extra value

This is exactly how regular addition works, but with linked lists instead of arrays.

## Standard accepted solution

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

If you want, I can also help you:

1. convert this into a LeetCode-submission style answer
2. explain the same logic using a diagram
3. create more beginner practice problems from Day 3 onward