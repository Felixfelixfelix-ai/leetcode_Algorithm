#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:

        st = set()
        
        while n != 1:
            n_sum = 0
            n_str = str(n)
            # 1.显式循环，Python 不需要创建生成器对象 更快
            for c in n_str: 
                n_sum += int(c) ** 2
            # 2.n_sum = sum(int(c) ** 2 for c in n_str) # 生成器表达式
            # 3.生成器表达式
            # n_sum = sum([int(c) ** 2 for c in n_str])
            n = n_sum
            if n_sum not in st:
                st.add(n_sum)
            else:
                return False
        
        return True
        
# @lc code=end

