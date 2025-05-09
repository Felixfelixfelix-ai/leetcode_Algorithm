#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. 暴力枚举
        # ans = []
        # for i in range(len(nums)):
        #     for j in range(i + 1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             ans.extend([i,j])
        #             return ans
        # return ans 

        # 2. 哈希表
        res = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in res:
                return [i,res[diff]]
            res[num] = i
        return []

    
        
# @lc code=end

