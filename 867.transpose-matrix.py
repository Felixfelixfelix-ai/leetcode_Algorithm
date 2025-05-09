#
# @lc app=leetcode id=867 lang=python3
#
# [867] Transpose Matrix
#

# @lc code=start
# import numpy  as np
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # 1. use numpy
        # return np.array(matrix).T.tolist()

        # 2. 暴力循环
        # row = len(matrix)
        # col = len(matrix[0])
        # ans = [[0] * row  for _ in range(col)]

        # ans = [[matrix[j][i] for j in range(row)]   for i in range(col)]

        # return ans

        # 3.zip  函数
        # return list(zip(*matrix))

# @lc code=end

