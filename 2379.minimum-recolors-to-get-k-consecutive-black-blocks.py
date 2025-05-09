#
# @lc app=leetcode id=2379 lang=python3
#
# [2379] Minimum Recolors to Get K Consecutive Black Blocks
#

# @lc code=start
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # 统计滑动窗口内  最小的白色块的个数 
        res, temp = float('inf'), 0
        for i, c in enumerate(blocks):
            if c == 'W':
                temp += 1
            
            if i < k - 1:
                continue
            res = min(res, temp)

            if blocks[i - k + 1] == 'W':
                temp -= 1
            
        return res 
         
# @lc code=end

