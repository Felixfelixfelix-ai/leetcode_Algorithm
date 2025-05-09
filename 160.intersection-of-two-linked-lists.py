#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        # 关键在于交叉遍历两个链表: a + c + b = b + c + a  https://leetcode.cn/problems/intersection-of-two-linked-lists/solutions/2958778/tu-jie-yi-zhang-tu-miao-dong-xiang-jiao-m6tg1/
        
        cur_a = headA
        cur_b = headB

        while cur_a != cur_b:
                cur_a = cur_a.next if cur_a else headB
                cur_b = cur_b.next if cur_b else headA
        return cur_a
        


        
# @lc code=end

