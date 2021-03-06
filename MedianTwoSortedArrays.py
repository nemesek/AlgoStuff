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
# test
from typing import List
import numpy as np

class Solution:

    def _find_median(self, nums: List[int]):
        n = len(nums)
        median = 0
        idx1, idx2 = None, None
        if n == 0:
            return None
        
        if (n % 2 == 0):
            idx1 = n//2
            idx2 = idx1 - 1
            median = (nums[idx1] + nums[idx2])/2
        else:
            idx1 = int(n/2)
            median = nums[idx1]
        return (idx1, idx2,median)

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
            
    def _filter(self, nums, predicate):
        try:
            filtered= filter(predicate, nums)
            filtered_list = list(filtered)
            print(len(filtered_list))
            return filtered_list
        except:
            # print(e.message)
            return []
        
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = self._merge_sorted_lists(nums1, nums2)        
        median = self._find_median(merged)
        return median[2]

    def _binary_search(self, arr, elem, start=0, end=None):
        if end is None:
            end = len(arr) - 1
        if start > end:
            return False

        mid = (start + end) // 2
        if elem == arr[mid]:
            return mid
        if elem < arr[mid]:
            return self._binary_search(arr, elem, start, mid-1)
        # elem > arr[mid]
        return self._binary_search(arr, elem, mid+1, end)

    def _binary_filter(self, arr, elem, start=0, end=None, isLessThan = True):
        if end is None:
            end = len(arr) -1
        if start > end:
            if isLessThan:
                return arr[start:]
            else:
                return arr[:start]

        mid = (start + end) // 2
        if elem == arr[mid]:
            return arr[:mid]
        if elem < arr[mid]:
            return self._binary_filter(arr, elem, start, mid - 1, isLessThan)
        return self._binary_filter(arr, elem, mid + 1, end, isLessThan)


    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:

        # def pred(sorted_nums, n):
        #     filtered_nums = []

        #     if len(sorted_nums == 0):
        #         return filtered_nums
        #     else:
        m = len(nums1)
        n = len(nums2)
        total_elements = m + n 
        max_ops = np.log2(total_elements)
        nums1_median_data = self._find_median(nums1) #(O(1))
        nums2_median_data = self._find_median(nums2) #(O(1))
        nums1_median = nums1_median_data[2]
        nums2_median = nums2_median_data[2]
        nums1_median_idx = nums1_median_data[0]
        nums2_median_idx = nums2_median_data[0]
        median = (nums1_median + nums2_median)/2

        while total_elements > 2:
            if ( nums2_median > nums1_median):
                nums1 = nums1[nums1_median_idx:]
                nums2 = nums2[:nums2_median_idx]
                # # nums1 = self._filter(temp, lambda x: x > nums2_median_data[2])
                # # nums1 = self._filter(temp, pred())
                # nums1 = list(filter(lambda x: x > nums2_median_data[2], temp))
                # temp = nums2[:nums2_median_data[0]]
                # nums2 = list(filter(lambda x: x < nums1_median_data[2], temp))
                nums1 = self._binary_filter(nums1, nums2_median,0, None, False)
                nums2 = self._binary_filter(nums2, nums1_median, 0, None, True)
                #median = self.findMedianSortedArrays(nums1, nums2)
                m = len(nums1)
                n = len(nums2)
                total_elements = m + n
                print('foo')

                nums1_median_data = self._find_median(nums1) #(O(1))
                nums2_median_data = self._find_median(nums2) #(O(1))
                
                if nums2_median_data == None or nums2_median_data == None:
                    return median
                nums1_median = nums1_median_data[2]
                nums2_median = nums2_median_data[2]
                nums1_median_idx = nums1_median_data[0]
                nums2_median_idx = nums2_median_data[0]
                median = (nums1_median + nums2_median)/2

            elif nums2_median < nums1_median:
                print('bar')
                
                nums1 = nums1[nums1_median_data[0]:]
                nums2 = nums2[:nums2_median_data[0]]
                nums1 = self._binary_filter(nums1, nums2_median_data[2],0, None, False)
                nums2 = self._binary_filter(nums2, nums1_median_data[2], 0, None, True)
                median = self.findMedianSortedArrays(nums1, nums2)
                m = len(nums1)
                n = len(nums2)
            else:
                print('baz')


        return median


def test(answer, expected):
    result = "Bad"
    if answer == expected:
        result = "Good"
    print(f"answer is: {result}")



if __name__ == "__main__":
    sol = Solution()
    # nums1 = range(1,11)
    # nums2 = range(1,10)
    # answer = sol.findMedianSortedArrays(nums1, nums2)
    # test(answer, 5)
    # answer2 = sol.findMedianSortedArrays2(nums1,nums2)
    # print(f"answer2 is {answer2}")
    # nums1 = [1,3]
    # nums2 = [2]
    # answer = sol.findMedianSortedArrays(nums1, nums2)
    # test(answer, 2)
    # answer2 = sol.findMedianSortedArrays2(nums1,nums2)
    # print(f"answer2 is {answer2}")
    # nums1 = [1,2]
    # nums2 = [3,4]
    # answer = sol.findMedianSortedArrays(nums1, nums2)
    # test(answer, 2.5)
    # answer2 = sol.findMedianSortedArrays2(nums1,nums2)
    # print(f"answer2 is {answer2}")
    # nums1 = range(1,33, 1)
    # nums2 = range(33,65,1)
    nums1 = [1,3,5,6,7,8]
    nums2 = [2,4,10,15,20,21] # [1,2,3,4,5,6,7,8,10,15,20,21] median is 5.5
    answer = sol.findMedianSortedArrays(nums1, nums2)
    test(answer, 6.5)
    answer2 = sol.findMedianSortedArrays2(nums1,nums2)
    print(f"answer2 is {answer2}")
    


    
