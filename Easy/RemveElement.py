# @Sk70249 solution in Python
'''
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2]
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = len(nums) - 1
        while i >= 0:
            if nums[i] == val:
                nums.pop(i)
            i -= 1
