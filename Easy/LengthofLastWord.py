# @Sk70249 solution in Python
'''
Example 1:
Input: s = "Hello World"
Output: 5

Example 2:
Input: s = " "
Output: 0
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.strip()
        b = s.split()
        if len(a)==0:return 0
        else: return len(b[len(b) - 1])