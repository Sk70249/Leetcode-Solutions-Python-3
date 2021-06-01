# @Sk70249 Reverse Integer solution in Python
'''
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]
'''
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        result_tail = result
        carry = 0

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1 + val2 + carry, 10)

            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return result.next