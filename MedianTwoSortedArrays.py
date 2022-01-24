# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

from typing import List
import numpy as np

class Solution:

    def _find_median(self, nums: List[int]) -> float:
        n = len(nums)
        median = 0
        if n == 0:
            return median
        
        if (n % 2 == 0):
            idx1 = n//2
            idx2 = idx1 - 1
            median = (nums[idx1] + nums[idx2])/2
        else:
            idx = int(n/2)
            median = nums[idx]
        return median

    def _merge_sorted_lists(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i = 0
        j = 0
        nums1_condition = True
        nums2_condition = True
        m = len(nums1)
        n = len(nums2)
        merged = [None] * (m + n)

        while nums1_condition or nums2_condition:
            
            if nums1[i] <= nums2[j] :
                merged[i + j] = nums1[i]
                i += 1
            else:
                merged[i + j] = nums2[j]
                j += 1

            nums1_condition = i + 1 <= m
            nums2_condition = j + 1 <= n

            if nums1_condition == False:
                merged[i + j:] = nums2[j:]
                break 
            
            if nums2_condition == False:
                merged[i + j:] = nums1[i:]
                break
        return merged
            

        
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = self._merge_sorted_lists(nums1, nums2)        
        median = self._find_median(merged)
        return median

    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:

        m = len(nums1)
        n = len(nums2)
        max_ops = np.log2(m+n)
        return max_ops


def test(answer, expected):
    result = "Bad"
    if answer == expected:
        result = "Good"
    print(f"answer is: {result}")



if __name__ == "__main__":
    sol = Solution()
    nums1 = range(1,11)
    nums2 = range(1,10)
    answer = sol.findMedianSortedArrays(nums1, nums2)
    test(answer, 5)
    answer2 = sol.findMedianSortedArrays2(nums1,nums2)
    print(f"answer2 is {answer2}")
    nums1 = [1,3]
    nums2 = [2]
    answer = sol.findMedianSortedArrays(nums1, nums2)
    test(answer, 2)
    answer2 = sol.findMedianSortedArrays2(nums1,nums2)
    print(f"answer2 is {answer2}")
    nums1 = [1,2]
    nums2 = [3,4]
    answer = sol.findMedianSortedArrays(nums1, nums2)
    test(answer, 2.5)
    answer2 = sol.findMedianSortedArrays2(nums1,nums2)
    print(f"answer2 is {answer2}")
    nums1 = range(1,33, 1)
    nums2 = range(33,65,1)
    answer = sol.findMedianSortedArrays(nums1, nums2)
    test(answer, 2.5)
    answer2 = sol.findMedianSortedArrays2(nums1,nums2)
    print(f"answer2 is {answer2}")
    


    
