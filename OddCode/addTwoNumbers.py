"""
Add two numbers from a linked list
Ex. (2 -> 4 -> 3) + (5 -> 6 -> 4) = 7 -> 0 -> 8
    342 + 465 = 807
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp1 = l1
        temp2 = l2
        list1 = []
        list2 = []
        while temp1 is not None:
            list1.append(temp1.val)
            temp1 = temp1.next

        while temp2 is not None:
            list2.append(temp2.val)
            temp2 = temp2.next

        list1.reverse()
        list2.reverse()
        lst = int(''.join([str(x) for x in list1])) + int(''.join([str(x) for x in list2]))
        n = list(str(lst))
        n.reverse()

        root = ListNode(0)
        temp = root
        for num in n:
            temp.next = ListNode(num)
            temp = temp.next

        temp = root.next
        return temp
