#
# @lc app=leetcode id=2090 lang=python3
#
# [2090] K Radius Subarray Averages
#

# @lc code=start
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # 滑动窗口 其实就是一个长度不为一的指针  
        # 本题的长度
        ans = [-1] * len(nums)
        k_sum = 0
        for i , num in enumerate(nums):
            k_sum += num

            if i < 2 * k:
                continue
            ans[i - k] = k_sum // ( 2 * k + 1 )

            k_sum -= nums[i - k * 2]

        return ans        
# @lc code=end
 