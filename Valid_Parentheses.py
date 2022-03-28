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

    def isValid(self, s: str) -> bool:
        length = len(s)
        if length == 0: return True
        if length % 2 == 1: return False 
        idx_pair = 1
        char = s[0]
        next = s[1]
        result = (True, 1)
        match char:
            case ('(' | '[' | '{'):
                if next != self._pairs[char]:
                    result = self._is_valid_close(s, char)
            case(_):
                return False 

        if not result[0]:
            return False
        idx_pair = result[1]
        s = s[:idx_pair] + s[idx_pair + 1:]
        s = s[1:]
 
        return self.isValid(s)


    def _is_valid_close(self, str, char):
        length = len(str)
        reverse_iterator = enumerate(reversed(str))
        allowed = [char]
        for idx, c in reverse_iterator:
            original_idx = length - idx - 1
            match c:
                case(')'|']'| '}'):
                    pair = self._pairs[c]
                    if char == pair: 
                        if idx == 0:
                            return(True, original_idx)
                        if len(allowed) == 0:
                            return (False,original_idx)
                        top = allowed.pop()
                        if top != char:
                            return (False, original_idx)
                        return (True,original_idx)
                    allowed.append(pair)
                case('(' | '[' | '{'):
                    if len(allowed) > 0:
                        top= allowed.pop()
                        if top != c:
                            return (False, original_idx)
                    else:
                        return (False, original_idx)
        return (True,original_idx)  


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