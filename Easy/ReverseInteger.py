# @Sk70249 Reverse Integer solution in Python
'''
Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
'''
class Solution:
    def reverse(self, x):
        out = int(str(x)[::-1]) if x >= 0 else -int(str(-x)[::-1])
        if -2 ** 31 <= out <= 2 ** 31 - 1:
            return out
        else:
            return 0

