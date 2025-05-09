#
# @lc app=leetcode id=1486 lang=python3
#
# [1486] XOR Operation in an Array
#

# @lc code=start
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        arr = [start + i *2  for i in range(n)]
        result = arr[0]

        for i in arr[1:]:
            result = result ^ i

        return result
        
# @lc code=end

