# @Sk70249 Reverse Integer solution in Python
'''Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (str(x) == str(x)[::-1]) and x>=0:
            return 1
        else:
            return 0