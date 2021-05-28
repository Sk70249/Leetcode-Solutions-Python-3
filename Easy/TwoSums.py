# @Sk70249 TwoSum solution in Python
'''
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i, j in enumerate(nums):
            if target - j in a:
                return a[target - j], i
            a[j] = i
