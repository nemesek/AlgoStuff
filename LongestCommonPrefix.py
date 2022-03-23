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
        return self._find_match(smallest, strs)

    def _find_match(self, s, strs: List[str]):
        length = len(s)
        if length == 0 : return ""
        for idx,str in enumerate(strs):
            prefix = str[0:length]
            strs[idx] = prefix
            if prefix != s:
                s = s[0: length -1]
                return self._find_match(s, strs)
        return s


    def _find_min_string(self,strs):
        min_str = strs[0]
        for s in strs:
            if len(s) < len(min_str):
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
    test(["dog", "racecar", "car" ], "")
    test(["cherry", "chew", "chest"], "che")
    
