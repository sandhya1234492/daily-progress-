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


def build_list(values):
    dummy = ListNode(0)
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def print_list(node):
    values = []
    while node is not None:
        values.append(node.val)
        node = node.next
    print(values)


if __name__ == "__main__":
    l1 = build_list([2, 4, 3])
    l2 = build_list([5, 6, 4])
    result = Solution().addTwoNumbers(l1, l2)
    print_list(result)
