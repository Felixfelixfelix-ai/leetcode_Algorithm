#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        res = set([3 ** i for i in  range(0,20) ]) 
        return  n in res 
# @lc code=end

