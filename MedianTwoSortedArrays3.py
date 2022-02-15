from cgitb import small
from cmath import exp
from typing import List
import random

from numpy import pi

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
        divisor = 1
        larger_idx = m//2
        smaller_idx = n//2
        found = False

        while found == False and (divisor <= n):
            divisor *= 2
            larger_left, larger_right = larger[larger_idx - 1], larger[larger_idx]
            smaller_left, smaller_right = smaller[smaller_idx - 1], smaller[smaller_idx]
            if larger_left > smaller_right:
                print('no bueno shift smaller to the right and larger to the left')
                shift = n//divisor
                smaller_idx = smaller_idx + shift 
                larger_idx = larger_idx - shift
            elif smaller_left > larger_right:
                print('pas tres bien shift smaller to the left and larger to the right')
                shift = n//divisor
                smaller_shift = smaller_idx - shift
                if smaller_shift < 0:
                    smaller_idx = smaller_shift
                    larger_idx = larger_idx + smaller_shift
                    found = True 
                else:                
                    smaller_idx = smaller_shift
                    larger_idx = larger_idx + shift
            else:
                found = True 

        return (larger_idx,smaller_idx)




    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int], debug=False) -> float:
        pivots = (0,0)
        answer = 0
        if debug:
            answer = self.findMedianSortedArraysTest(nums1, nums1)
            print('debug mode')
        
        if (len(nums2) > len(nums1)):
            pivots = self._determine_pivot_indexes(nums2, nums1)
            if (pivots[1] >= 0):
                answer = (nums2[pivots[0]] + nums1[pivots[1]])/2
            else:
                answer = (nums2[pivots[0]] + nums2[pivots[0] + 1])/2
        else:
            pivots = self._determine_pivot_indexes(nums1, nums2)
            if pivots[1] >= 0:
                answer = (nums1[pivots[0]] + nums2[pivots[1]])/2
            else:
                answer = (nums1[pivots[0]] + nums1[pivots[0] + 1])/2

        return answer


            
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