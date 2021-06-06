# @Sk70249 solution in Python
'''
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6

Example 2:
Input: nums = [1]
Output: 1
'''
class Solution:
    def maxSubArray(self, a: List[int]) -> int:
        m = a[0]
        c = 0

        for i in a:
            if c < 0:
                c = 0
            c += i
            m = max(m, c)

        return m