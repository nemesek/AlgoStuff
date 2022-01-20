# Definition for singly-linked list.

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Constraints:
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

from typing import List, Optional
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

    def __convert_int_to_ListNode(self, n: int, node: Optional[ListNode]) -> Optional[ListNode]:

        val = n % 10
        n = n//10
        node.val = val
        if n > 0:
            node.next = self.__convert_int_to_ListNode(n, ListNode())
        return node
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number1 = self.__calculate_number(l1)
        number2 = self.__calculate_number(l2)
        sum = number1 + number2
        answer = self.__convert_int_to_ListNode(sum, ListNode())
        return answer

if __name__ == "__main__":
    sol = Solution()
    node1 = ListNode(3, None)
    node2 = ListNode(4, node1)
    node3 = ListNode(2, node2)
    node4 = ListNode(4, None)
    node5 = ListNode(6, node4)
    node6 = ListNode(5, node5)
    answer1 = sol.addTwoNumbers(node3, node6)
    node1 = ListNode(0, None)
    node4 = ListNode(0, None)
    answer2 = sol.addTwoNumbers(node1, node4)
    node1 = ListNode(9, None)
    node2 = ListNode(9, node1)
    node3 = ListNode(9, node2)
    node4 = ListNode(9, node3)
    node5 = ListNode(9, node4)
    node6 = ListNode(9, node5)
    node7 = ListNode(9, node6)
    node8 = ListNode(9, None)
    node9 = ListNode(9, node8)
    node10 = ListNode(9, node9)
    node11 = ListNode(9, node10)
    answer3 = sol.addTwoNumbers(node7, node11)
    print('done')
