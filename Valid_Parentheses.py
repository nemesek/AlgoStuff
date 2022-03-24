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

class Solution:
    def isValid(self, s: str) -> bool:
        length = len(s)
        if length % 2 == 1 and length < 2:
            return False 
        for idx, char in enumerate(s):
            match char:
                case('('):
                    remaining = s[idx +1:]
                    if not any(n == ')' for n in remaining):
                        return False
                    next = s[idx +1]
                    if next != ')':
                        return self.isValid(remaining)
                case('['):
                    remaining = s[idx +1:]
                    if not any(n == ']' for n in remaining):
                        return False 
                case('{'):
                    remaining = s[idx +1:]
                    if not any(n == '}' for n in remaining):
                        return False 
                
        return True 


def test(s, expected):

    sol = Solution()
    answer = sol.isValid(s)
    success = answer == expected
    print(success)

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