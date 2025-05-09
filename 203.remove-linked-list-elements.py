#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next :
            if cur.next.val == val:
                cur.next = cur.next.next
            else: # 易错 不要忘了移动cur  
                cur = cur.next
             
        return dummy.next
        
# @lc code=end

