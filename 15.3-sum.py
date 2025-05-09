#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if nums[i] > 0 :
                return res
            
            if i > 0 and nums[i] == nums[i - 1]:  # 对第一个数字去重
                continue
            
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum_th = nums[i] + nums[left] + nums[right]
                if sum_th > 0:
                    right -= 1
                elif sum_th < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]: 
                        left += 1           # 对第二个数字去重
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1          # 对第三个数字去重  
                    left += 1 # 在这里一定要注意 else里面更新left 和 right
                    right -= 1
            
        return res 


        
# @lc code=end

