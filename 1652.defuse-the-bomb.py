#
# @lc app=leetcode id=1652 lang=python3
#
# [1652] Defuse the Bomb
#

# @lc code=start
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # 由于 k 小于code的长度 ，所以两个code组成的新数组可以模拟循环数组 
        new_code = code + code
        ans = []
        length_code = len(code)
        if k > 0:
            for i in range(length_code):
                ans.append(sum(new_code[i + 1 : i + k + 1]))
        elif  k < 0:
            for i in range(length_code):
                ans.append(sum(new_code[length_code + i + k :length_code  + i]))
        else:
            ans = [0 for _ in code]
        return ans

                


# @lc code=end

