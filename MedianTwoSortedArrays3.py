from cmath import exp
from typing import List
import random

class Solution:
    

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
    
    def findMedianSortedArraysTest(self, nums1: List[int], nums2: List[int]) -> float:
        merged = self._merge_sorted_lists(nums1, nums2)        
        median = self._find_median(merged)
        return median[2]

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
        return (idx1, idx2, median)
    
    def _determine_pivot_indexes(self, larger, smaller):
        m = len(larger)
        n = len(smaller)
        divisor = 2
        idx1 = m//divisor
        idx2 = n//divisor
        found = False
        while found == False:
            divisor *= 2
            larger_left, larger_right = larger[idx1 - 1], larger[idx1]
            smaller_left, smaller_right = smaller[idx2 - 1], smaller[idx2]
            if larger_left > smaller_right:
                print('no bueno shift smaller to the right and larger to the left')
                shift = n//divisor
                idx2 = idx2 + shift 
                idx1 = idx1 - shift
            elif smaller_left > larger_right:
                print('pas tres bien shift smaller to the left and larger to the right')
                shift = n//divisor
                idx2 = idx2 - shift
                idx1 = idx1 + shift
            else:
                found = True 

        return (idx1,idx2)




    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int], debug=False) -> float:
        answer = (0,0)
        if debug:
            answer = self.findMedianSortedArraysTest(nums1, nums1)
            print('debug mode')
        
        if (len(nums2) > len(nums1)):
            answer = self._determine_pivot_indexes(nums2, nums1)
        else:
            answer = self._determine_pivot_indexes(nums1, nums2)
        return 1.0


            
def runTest(nums1, nums2, debug=False):
    test_answer = sol.findMedianSortedArraysTest(nums1,nums2)
    answer = sol.findMedianSortedArrays(nums1, nums2, debug)
    result = "pass" if answer == test_answer else "!!!!!!!!!!!!!!!!!fail!!!!!!!!!!!!!!!!!" 
    print(result)     
    print(f"Actual: {answer} Expected: {test_answer}")
    print("+++++++++++++++")
    return result

def build_list():
    n = random.randint(2,10)
    randomlist = random.sample(range(1, 100000), n)
    sorted_list = sorted(randomlist)
    return sorted_list

if __name__ == "__main__":
    sol = Solution()
    # [1,3,4,5,6,7,8]
    # nums1 = range(1,11)
    # nums2 = range(1,10)
    # runTest(nums1,nums2)
    # nums1 = [1,3]
    # nums2 = [2]
    # runTest(nums1,nums2)
    # nums1 = [1,2]
    # nums2 = [3,4]
    # runTest(nums1,nums2)
    # nums1 = range(1,33, 1)
    # nums2 = range(33,65,1)
    # runTest(nums1, nums2)
    # nums1 = [1,3,5,6,7,8]
    # nums2 = [2,4,10,15,20,21] # [1,2,3,4,5,6,7,8,10,15,20,21] median is 6.5
    # runTest(nums1, nums2)
    # nums1 = range(1,100, 1)
    # nums2 = [100,101,102]
    # runTest(nums1, nums2)
    # nums2 = range(1,100, 1)
    # nums1 = [100,101,102]
    # nums1 = [17037, 47647, 54131, 57685, 59273, 63808, 65619, 72075, 99335]
    # nums2 = [26594, 32089, 51015, 64259]
    nums1 = list(range(1,7,1))
    nums2 = list(range(7,11,1))
    result = runTest(nums1, nums2)
    # count = 0
    # for i in range(100):
        
    #     nums1 = build_list()
    #     nums2 = build_list()
    #     result = runTest(nums1, nums2)
    #     if result == "!!!!!!!!!!!!!!!!!fail!!!!!!!!!!!!!!!!!":
    #         count += 1
    #         print('got some debugging to do')
    #         runTest(nums1, nums2, debug=True)

    # print(f"total failures {count} out of 100")