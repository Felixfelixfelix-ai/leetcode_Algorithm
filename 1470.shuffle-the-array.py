#
# @lc app=leetcode id=1470 lang=python3
#
# [1470] Shuffle the Array
#

# @lc code=start
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left = nums[:n ]
        right = nums[n:]
        ans = []
        for i in range(n):
            ans.append(left[i])
            ans.append(right[i])
        return ans

        
# @lc code=end

