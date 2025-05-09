#
# @lc app=leetcode id=1493 lang=python3
#
# [1493] Longest Subarray of 1's After Deleting One Element
#

# @lc code=start
from collections import defaultdict
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # 思路  找到只包含一个0的最长子序列
        ans ,left= 0, 0
        zero_count = 0
        for right ,num in enumerate(nums):
            if num == 0:
                zero_count += 1
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            ans = max(ans,right - left + 1)
        return ans -1 
        
# @lc code=end

