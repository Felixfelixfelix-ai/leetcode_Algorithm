#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
                pre = dummy = ListNode(next = head)
                for _ in range(left - 1 ):
                        pre = pre.next
                cur = pre.next
                while right - left >= 0:
                        temp = cur.next
                        pre.next = cur.next
                        
                        pre = cur 
                        cur = temp 
                return  dummy.next 
                
# @lc code=end

