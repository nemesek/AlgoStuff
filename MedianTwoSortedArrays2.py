from typing import List

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
        return (idx1, idx2, median)
    
    def _handle_list_size_one(self, single: int, nums: List[int]) -> float:
        # one or both lists have an element of one...assumption is that the first list has a size of one
        n = len(nums)
        if n == 1:
            return (single + nums[0])/2
        if n % 2 == 0:
            idx = int(n/2)
            elem1 = nums[idx-1]
            elem2 = nums[idx]
            if single >= elem2:
                return elem2
            elif single <= elem1:
                return elem1
            else:
                return single
        else:
            idx = int(n/2)
            elem1 = nums[idx-1]
            elem2 = nums[idx]
            elem3 = nums[idx + 1]
            numbers = [single, elem1, elem2, elem3]
            sorted_numbers = sorted(numbers)
            return self._find_median(sorted_numbers)[2]


    def _handle_list_size_two(self, two_element_list: List[int], nums: List[int]) -> float:
        n = len(nums)
        num_mid_idx = int(n/2)
        
        if n == 2:
            nums.extend(two_element_list)
            sorted_numbers = sorted(nums)
            return self._find_median(sorted_numbers)[2]

        if n % 2 == 0:
            # check for min of second element in smaller array and element just after the second middle in the bigger array N/2 + 1 element
            # todo : start from here dan
            median_data = self._find_median(nums)
            minBigger = nums[median_data[1]]
            maxBigger = nums[median_data[0]]
            minSmaller = two_element_list[0]
            maxSmaller = two_element_list[1]

            if minBigger >= minSmaller and maxBigger <= maxSmaller: # case where minSmaller, minBigger, maxBigger, maxSmaller
                return median_data[2]
            if minBigger >= maxSmaller: # case where minSmaller maxSmaller minBigger maxBigger, we need to consider elements two positions before middle
                two_from_middle = nums[num_mid_idx - 2]
                if two_from_middle > minSmaller: # todo: should I just return the max of two_from_middle and minSmaller?
                    return (two_from_middle + minBigger)/2
                else:
                    return (two_from_middle + minSmaller)/2
            if minSmaller >= maxBigger: # case where minBigger maxBigger minSmaller maxSmaller, we need to consider elements two position beyond middle
                two_from_middle = nums[num_mid_idx + 1]
                return min(two_from_middle, maxBigger)
            
            
        return 0

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


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        if (m > 2 and n > 2):
            nums1_median_data = self._find_median(nums1)
            nums2_median_data = self._find_median(nums2)
            nums1_median = nums1_median_data[2]
            nums2_median = nums2_median_data[2]
            if nums1_median == nums2_median:
                return nums1_median
            elif nums2_median > nums1_median:
                nums1 = nums1[nums1_median_data[0]:]
                nums2 = nums2[:nums2_median_data[0]]
              #  nums1 = self._binary_filter(nums1, nums2_median,0,None,False)
               # nums2 = self._binary_filter(nums2, nums1_median, 0, None, True)
                return self.findMedianSortedArrays(nums1, nums2)
            else:
                nums1 = nums1[:nums1_median_data[0]]
                nums2 = nums2[nums2_median_data[0]:]
                #nums1 = self._binary_filter(nums1, nums2_median, 0, None, True)
                #nums2 = self._binary_filter(nums2, nums1_median, 0, None, False)
                return self.findMedianSortedArrays(nums1,nums2)

        if m > n:
            if n == 0:
                return self._find_median(nums1)[2]
            elif n == 1:
                return self._handle_list_size_one(nums2[0], nums1)
            elif n == 2:
                return self._handle_list_size_two(nums2, nums1)
        elif n > m:
            if m == 0:
                return self._find_median(nums2)[2]
            elif m == 1:
                return self._handle_list_size_one(nums1[0], nums2)
            elif m == 2:
                return self._handle_list_size_two(nums1, nums2)
        else:
            if m == 1:
                return self._handle_list_size_one(nums1[0], nums2)
            elif m == 2:
                return self._handle_list_size_two(nums1, nums2)
            else:
                return 0
        return 0

            
                


if __name__ == "__main__":
    sol = Solution()
    nums1 = [3,7,8]
    nums2 = [1,4,5,6]
    answer = sol.findMedianSortedArrays(nums1, nums2) # [1,3,4,5,6,7,8] answer should be 5 but it's 5.5 (if I do binary filter) right now
    print(answer)
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
    # nums1 = [1,3,5,6,7,8]
    # nums2 = [2,4,10,15,20,21] # [1,2,3,4,5,6,7,8,10,15,20,21] median is 5.5
    # answer = sol.findMedianSortedArrays(nums1, nums2)
    #test(answer, 6.5)
    #answer2 = sol.findMedianSortedArrays2(nums1,nums2)