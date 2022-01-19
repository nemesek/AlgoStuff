#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.
from typing import List 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        low = 0
        high = len(nums) -1
        while  high > low:
            x = sorted_nums[low]
            y = sorted_nums[high]
            sum = x + y
            if sum == target:
                first = 0
                second = 0
                if x == y:
                    matches = [index for index, i in enumerate(nums) if i == x]
                    first = matches[0]
                    second = matches[1]
                else:   
                    first = nums.index(x)
                    second = nums.index(y)
                return [first, second]
            elif sum > target:
                high -= 1
            else:
                low += 1
        return [0,0]