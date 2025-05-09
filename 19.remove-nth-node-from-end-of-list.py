#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        凡是涉及到链表节点的删除  都应该设立哨兵节点
        
        技巧：如果要遍历到最后一个节点，需要写 while node;如果要遍历到倒数第二个节点，需要写 while node.next
        """
        dummy = ListNode(next=head)
        fast = slow = dummy
        for _ in range( n + 1):# fast先走 n+1 步 
            fast = fast.next
        while fast:
            slow = slow.next # slow先走一步 此时 slow和fast 之间相差 n + 1 -1 = n步
            fast = fast.next #跟新fast 直到末尾
        slow.next = slow.next.next

        return dummy.next


        
# @lc code=end

