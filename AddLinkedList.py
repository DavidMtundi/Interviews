"""
You are given two non-empty linked list representing two non negative intergers.
the digits are stored in erverse order and each of their nodes contains
a single digit.
add the two numbers and return it as a linked list
you may assume the two numbers do not contain any leading zero, except the number
0 itself
you may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        if l1 or l2 is None:
            return 0
        finalresult = ListNode(0)
        listnode = finalresult

        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            remainder = carry % 10
            carry = carry // 10
            listnode = ListNode(remainder)
            listnode = listnode.next

        return finalresult.next

        return finalresult.next


sol = Solution()
print(sol.addTwoNumbers())
