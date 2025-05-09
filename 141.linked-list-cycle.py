#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        fast,slow  = head, head
        
        while fast and fast.next : # 判断条件很重要  这里只能用fast判断
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return  True
        
        return False 
        
# @lc code=end

