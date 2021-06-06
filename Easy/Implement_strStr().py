# @Sk70249 solution in Python
'''
Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0 or haystack == needle: return 0
        else:
            if haystack.count(needle)>0:
                return haystack.index(needle)
            else:
                return -1