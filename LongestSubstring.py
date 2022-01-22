# Problem : Given a string s, find the length of the longest substring without repeating characters.

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.


# Input: s = "bbbbb"
# Output: 1


# Explanation: The answer is "b", with the length of 1.

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        max = 0
        current_sub = []   
        for idx in range(len(s)):
            current = len(current_sub)
            if s[idx] not in current_sub:
                current_sub.append(s[idx])
                current += 1
            else:
                # I also need to backtrack
                current_sub = []
                current_sub.append(s[idx])
                for i in reversed(s[0:idx]):
                    if i not in current_sub:
                        current_sub.append(i)
                    else:
                        break
                current = len(current_sub)
            if current > max:
                max = current
        return max



if  __name__ == "__main__":
    sol = Solution()
    answer1 = sol.lengthOfLongestSubstring("abcabcbb")         
    print(f"answer1 is {answer1}")
    answer2 = sol.lengthOfLongestSubstring("bbbbb")         
    print(f"answer1 is {answer2}")
    answer3 = sol.lengthOfLongestSubstring("pwwkew")         
    print(f"answer1 is {answer3}")
    answer4 = sol.lengthOfLongestSubstring(" ")         
    print(f"answer1 is {answer4}")
    answer5 = sol.lengthOfLongestSubstring("dvdf")
    print(f"answer5 is {answer5}")
