# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

 

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

# Constraints:

# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].

class Solution:
    def __init__(self) -> None:
        self._dict = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
            }

    def romanToInt(self, s: str) -> int:
        length = len(s)
        total = 0
        for idx in range(len(s)):
            while idx < length:
                val, idx = self._process_char(s, idx, total)
                total += val 
            return total 
    

    def _process_char(self, s, idx, total):
        total = 0
        length = len(s)
        c = s[idx]
        if c == 'I' or c == 'X' or c == 'C':
            if (length - 1) <= idx:
                return self._handle_base(c,idx,total)
            if c == 'I':
                next = s[idx + 1]
                if next == 'V':
                    total += 4
                    idx += 2
                elif next == 'X':
                    total += 9
                    idx += 2
                else:
                    total, idx = self._handle_base(c, idx, total)
            elif c == 'X':
                next = s[idx + 1]
                if next == 'L':
                    total += 40
                    idx += 2
                elif next == 'C':
                    total += 90
                    idx += 2
                else:
                    total, idx = self._handle_base(c, idx, total)
            elif c == 'C':
                next = s[idx + 1]
                if next == 'D':
                    total += 400
                    idx += 2
                    return (total, idx)
                elif next == 'M':
                    total += 900
                    idx += 2
                    return (total, idx)
                else:
                    total, idx = self._handle_base(c, idx, total)
            else:
                total, idx = self._handle_base(c, idx, total)
        else:
                total, idx = self._handle_base(c, idx, total)
        
        return (total, idx)
    
    def _handle_base(self, c, idx,total):
        total += self._dict[c]
        idx += 1
        return (total, idx)

        
def test(roman_num, expected):
    sol = Solution()
    answer = sol.romanToInt(roman_num)
    if answer == expected:
        print(f'Success: {roman_num} is equal to {answer}')
    else:
        print(f'!!!!Fail!!!!: {answer} is not equal to {expected}')

if __name__ == "__main__":
    test('V', 5)
    test('III', 3)
    test('XII', 12)
    test('X', 10)
    test('L', 50)
    test('C', 100)
    test('D', 500)
    test('M', 1000)
    test('LVIII', 58)
    test('MCMXCIV', 1994)
    test('IV', 4)
    test('IX', 9)
    test('XL', 40)