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
    values = [3,4,2,4,6,5,0,0,9,9,9,9,9,9,9,9,9,9,9]
    nodes = []
    for idx, val in enumerate(values):
        if idx in (0, 3,6,7,8, 15):
            nodes.append(ListNode(val, None))
        else:
            nodes.append(ListNode(val, nodes[idx - 1]))
   
    sol = Solution()
    answer1 = sol.addTwoNumbers(nodes[2], nodes[5])
    answer2 = sol.addTwoNumbers(nodes[6], nodes[7])
    # answer3 = sol.addTwoNumbers(nodes[], nodes[15])
    print('done')
