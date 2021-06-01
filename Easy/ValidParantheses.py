# @Sk70249 solution in Python
'''
Example 1:
Input: s = "()[]{}"
Output: true

Example 2:
Input: s = "(]"
Output: false

Example 3:
Input: s = "([)]"
Output: false
'''
class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        bracket = {")": "(",
                 "}": "{",
                 "]": "["}

        for i in s:
            if(i in ["(", "{", "["]):
                l.append(i)
            elif(len(l) == 0 or bracket[i] != l.pop()):
                return 0

        return l == []

