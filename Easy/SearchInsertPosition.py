# @Sk70249 solution in Python
'''
Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1
'''
class Solution:
    def searchInsert(self, n: List[int], t: int) -> int:
        if t in n:
            return n.index(t)
        elif t not in n:
            n.append(t)
            a = sorted(n)
            return a.index(t)