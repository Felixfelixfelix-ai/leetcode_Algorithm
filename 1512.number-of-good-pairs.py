#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#

# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        nums_len = len(nums)
        ans = 0
        for i in range(nums_len):
            j = i + 1
            for j in range(j,nums_len):
                if nums[i] == nums[j]:
                    ans += 1
        return ans
        
# @lc code=end

