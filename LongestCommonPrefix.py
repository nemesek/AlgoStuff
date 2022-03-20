# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        smallest = self._find_min_string(strs)

    def _find_min_string(self,strs):
        min_str = strs[0]
        for s in strs:
            if len(s) < min_str:
                min_str = s 
        return min_str


def test(strs, expected):
    sol = Solution()
    answer = sol.longestCommonPrefix(strs)
    if answer == expected:
        print(f'Success: You did it right')
    else:
        print(f'!!!!Fail!!!!: You did it wrong')

if __name__ == "__main__":
    test([], "")
    test(["flower", "flow", "flight"], "fl")
    
