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

class Solution:
    def isValid(self, s: str) -> bool:
        length = len(s)
        if length % 2 == 1:
            return False 
        for idx, char in enumerate(s):
            match char:
                case('('):
                    next = s[idx + 1]
                    if next != ')':
                        return False
                case('['):
                    next = s[idx + 1]
                    if next != ']':
                        return False 
                case('{'):
                    next = s[idx + 1]
                    if next != '}':
                        return False
                
        return True 


def test(s):
    sol = Solution()
    answer = sol.isValid(s)
    print(answer)

if __name__ == "__main__":
    test("()")
    test("(")
    test("())")
    test("[]")
    test("{}")
    test("()[]{}")
    test("()[]{)")