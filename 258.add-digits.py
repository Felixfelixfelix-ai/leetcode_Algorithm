#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
from functools import reduce
class Solution:
    def addDigits(self, num: int) -> int:
        num_str = str(num)
        while len(num_str) > 1:
            temp = reduce(lambda x ,y :int(x) + int(y),num_str)
            num_str = str(temp)
        return int(num_str)

        
        
# @lc code=end

