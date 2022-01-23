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

        
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m_median = self._find_median(nums1)
        print(m_median)
        n_median = self._find_median(nums2)
        print(n_median)
        return 5



if __name__ == "__main__":
    nums1 = range(1,11)
    nums2 = range(1,10)
    nums1 = [1,3]
    nums2 = [2]
    nums1 = [1,2]
    nums2 = [3,4]
    sol = Solution()
    answer = sol.findMedianSortedArrays(nums1, nums2)
    print(answer)
