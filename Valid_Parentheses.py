# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

# Input: s = "{[]}"
# Output: true

# Input s = "([)]"
# Output = false

from xmlrpc.client import Boolean


class Solution:
    def isValid(self, s: str) -> bool:
        length = len(s)
        if length == 0: return True
        if length % 2 == 1: return False 

        char = s[0]
        result = self._is_valid_close(s, char)

        if not result[0]:
            return False
        idx_pair = result[1]
        s = s[:idx_pair] + s[idx_pair + 1:]
        s = s[1:]
 
        return self.isValid(s)

        # for idx, char in enumerate(s):
        #     result = self._is_valid_close(s, char)
        #     if result[0] == False:
        #         return False 
        
        #return True

            # match char:
            #     case('('):
            #         if not self._is_valid_close(s, char):
            #             return False
            #     case('['):
            #         if not self._is_valid_close(s, char):
            #     case('{'):
            #         if not i

    def _is_valid_close(self, str, char):
        length = len(str)
        reverse_iterator = enumerate(reversed(str))
        allowed = []
        for idx, c in reverse_iterator:
            original_idx = length - idx - 1
            match c:
                case(')'):
                    if char == '(': return (True,original_idx)
                    allowed.append('(')
                case(']'):
                    if char == '[': return (True, original_idx) 
                    allowed.append('[')
                case('}'):
                    if char == '{': return (True,original_idx)
                    allowed.append('{')
                case('('):
                    if c in allowed:
                        allowed.remove(c)
                    else:
                        return (False,original_idx) 
                case('['):
                    if c in allowed:
                        allowed.remove(c)
                    else:
                        return (False, original_idx)
                case('{'):
                    if c in allowed:
                        allowed.remove(c)
                    else:
                        return (False,original_idx) 
        return (True,original_idx)  


# class Solution:
#     def isValid(self, s: str):
#         length = len(s)
#         if length == 0:
#             return True 
#         if length % 2 == 1:
#             return False 
#         mid = length // 2
#         left = s[mid-1]
#         right = s[mid]

#         match left:
#             case('('):
#                 if right != ')':
#                     return False
#                 if length == 2: return True
#                 remaining = self.remove_middle_character(s)
#                 return self.isValid(remaining)
#             case('['):
#                 if right != ']':
#                     return False 
#                 if length == 2: return True
#                 remaining = self.remove_middle_character(s)
#                 return self.isValid(remaining)
#             case('{'):
#                 if right != '}':
#                     return False 
#                 if length == 2: return True

#                 remaining = self.remove_middle_character(s)
#                 return self.isValid(remaining)
#             case(_):
#                 return False 

        
    # def _remove_middle_character(self, s):
    #     # why doesn't this work?
    #     # remaining = s[:left - 1] + s[right + 1:]
    #     h = len(s)//2
    #     mod = (len(s) + 1) % 2
    #     return s[:h - mod] + s[h + 1:]
                


def test(s, expected):

    sol = Solution()
    answer = sol.isValid(s)
    print ("Success" if answer == expected else f"Failed Sucka: {s}")
    # success = answer == expected
    # print(success)

if __name__ == "__main__":
    test("()", True)
    test("(", False)
    test("())", False)
    test("[]", True)
    test("{}", True)
    test("()[]{}", True)
    test("()[]{)", False)
    test("({[]})", True)
    test("{[]}", True)
    test("([)]", False)
    test("){", False)
    test("(())", True)