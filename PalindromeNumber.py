# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False

        reversed = self._reverse_int(x)
        return x == reversed 

    def _reverse_int(self, x: int) -> int:

        reversed_num = 0

        while x != 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        return reversed_num



if __name__ == "__main__":
    sol = Solution()
    x = 10
    is_Palindrome = sol.isPalindrome(x)
    if is_Palindrome:
        print(f'{x} is a palindrome')
    else:
        print(f'{x} is not a palindrome')