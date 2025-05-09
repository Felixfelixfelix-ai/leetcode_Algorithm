#
# @lc app=leetcode id=1052 lang=python3
#
# [1052] Grumpy Bookstore Owner
#

# @lc code=start
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # 老板不生气时候的客户数和  生气时，窗口长度为minutes 内的最大和
        s0 = sum([num for i, num in enumerate(customers) if grumpy[i] == 0])
        s1, total = 0, 0
        for i, num  in  enumerate(customers):
            if grumpy[i] == 1:
                total += num

            if i < minutes - 1:
                continue

            s1 = max(s1, total)

            if grumpy[i - minutes + 1] == 1:
                total -= customers[i - minutes + 1]
            
        return s0 + s1




# @lc code=end

