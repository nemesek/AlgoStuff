
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

 #Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional 

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        i = 0
        j = 0
        
        # m = len(list1)
        # n = len(list2)
        # merged = [None] * (m + n)
        # list1_condition = True if m > 0 else False
        # list2_condition = True if n > 0 else False

        # if list1_condition == False or list2_condition == False:
        #     return []
        merge_list = ListNode()
        list1_current = list1
        list2_current = list2
        if list1_current is None and list2_current is None:
            return []

        
        while list1_current is not None  or list2_current is not None:
            if list1_current <= list2_current:
                merge_list.val = list1_current.val 
                list1_current = list1_current.next
            else:
                # merged[i + j] = list2[j]
                # j += 1
                merge_list.val = list2_current.val
                list2_current = list2_current.next

            # list1_condition = i + 1 <= m
            # list2_condition = j + 1 <= n

            if list1_current is None:
                #merged[i + j:] = list2[j:]
                break 
            
            if list2_current is None:
                #merged[i + j:] = list1[i:]
                break
        return merge_list

def test(list1, list2):
    sol = Solution()
    l = sol.mergeTwoLists(list1,list2)
    success = all(l[i] <= l[i+1] for i in range(len(l) - 1))
    if success: 
        print("Success")
    else:
        print("fail")

if __name__ == "__main__":
    list1 = [1,2,4]
    list2 = [1,3,4]
    test(list1,list2)
    test([], [])
    test([], [0])
    test([-1, 13], [0])