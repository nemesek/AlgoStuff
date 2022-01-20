# Definition for singly-linked list.

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Constraints:
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __calculate_number(self, node: Optional[ListNode]) -> Optional[ListNode]:
        if node is None:
            return None
        power = 0
        number = 0
        
        while node != None:
            number += node.val * (10**power)
            node = node.next
            power += 1

        return number
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number1 = self.__calculate_number(l1)
        number2 = self.__calculate_number(l2)
        print(number1 + number2)
        return None


