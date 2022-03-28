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

    def __init__(self) -> None:
        self._pairs = {'(':')', ')': '(', '[':']', ']':'[', '{':'}','}':'{' }

    def isValid(self, s: str) -> None:
        stack = []
        for c in s:
            match c:
                case(')'|']'| '}'):
                    pair = self._pairs[c]
                    if len(stack) == 0:
                        return False
                    if pair not in stack:
                        return False
                    top = stack.pop()
                    if top != pair:
                        stack.append(top)
                        stack.append(pair)

                case('(' | '[' | '{'):
                    stack.append(c)
        
        result = True if len(stack) == 0 else False
        return result 
                    

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
    test("((", False)
    test("[[[]", False)
    test("(([]){})", True)
    test("(()(", False)
    test("[({(())}[()])]", True)
    test("(())[()]", True)
    test("[()]", True)