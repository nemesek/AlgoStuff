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


# class Solution:
#     def isValid(self, s: str, recurse: Boolean, response: Boolean) -> bool:
#         length = len(s)
#         if length == 0:
#             return False 
#         if length % 2 ==  1 and not recurse:
#             return False 

#         if recurse and not response:
#             return False 
        
#         response = True 
#         for idx, char in enumerate(s):
#                 match char:
#                     case('('):
#                         remaining = s[idx +1:]
#                         if not any(n == ')' for n in remaining):
#                             response = False
#                             return response 
#                         next = s[idx +1]
#                         if next != ')':
#                             response = self.isValid(remaining, True, response)
#                             return response 
#                     case('['):
#                         remaining = s[idx +1:]
#                         if not any(n == ']' for n in remaining):
#                             response = False
#                             return response  
#                     case('{'):
#                         remaining = s[idx +1:]
#                         if not any(n == '}' for n in remaining):
#                             response = False
#                             return response  
                
#         return response 

class Solution:
    def isValid(self, s: str):
        length = len(s)
        if length == 0:
            return True 
        if length % 2 == 1:
            return False 
        mid = length // 2
        left = s[mid-1]
        right = s[mid]

        match left:
            case('('):
                if right != ')':
                    return False
                if length == 2: return True
                # remaining = s[:left - 1] + s[right + 1:]
                remaining = self.remove_middle_character(s)
                return self.isValid(remaining)
            case('['):
                if right != ']':
                    return False 
                if length == 2: return True
                # remaining = s[:left - 1] + s[right + 1:]
                remaining = self.remove_middle_character(s)
                return self.isValid(remaining)
            case('{'):
                if right != '}':
                    return False 
                if length == 2: return True
                # remaining = s[:left - 1] + s[right + 1:]
                remaining = self.remove_middle_character(s)
                return self.isValid(remaining)
            case(_):
                return False 

        return True

    def remove_middle_character(self, s):
        h = len(s)//2
        mod = (len(s) + 1) % 2
        return s[:h - mod] + s[h + 1:]
                


def test(s, expected):

    sol = Solution()
    answer = sol.isValid(s)
    print ("Success" if answer == expected else "Failed Sucka")
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