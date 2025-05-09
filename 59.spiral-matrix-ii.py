#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        DIRS = [(0, 1),(1, 0),(0, -1),(-1, 0)] # 注意方向数组 向右移动  列数加一
        ans = [[0] * n for _ in range(n)] 
        i, j, di = 0, 0, 0
        for val in range(1, n ** 2 + 1):
            ans[i][j] = val
            x, y = i + DIRS[di][0], j + DIRS[di][1] # x, y 是 i, j的下一步
            if x < 0 or x >= n or y < 0 or y >= n or ans[x][y]: # 判断是否需要右转
                di = (di + 1) % 4
            #更新 i j 
            i += DIRS[di][0] 
            j += DIRS[di][1]
        return ans


        
# @lc code=end

