# @Sk70249 solution in Python
'''
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
'''

####################################### - SIMPLE SOLUTION - #################################################
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = tail = ListNode(0)

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 or l2
        return head.next

#################################### - OPTIMIZED SOLUTION - #################################################
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = tail = ListNode(0)

        while l1 and l2:
            if l1 is None:
                node = ListNode(l2.val)
                tail.next = node
                tail = tail.next
                l2 = l2.next
            elif l2 is None:
                node = ListNode(l1.val)
                tail.next = node
                tail = tail.next
                l1 = l1.next
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            elif l1.val >= l2.val:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 or l2
        return head.next