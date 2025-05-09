#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 快速
        # nums = [nums[i]**2 for i in range(len(nums))]
        # return sorted(nums)

        # 双指针   关键是逆序
        new_nums = [0] * len(nums)
        pos = len(nums) - 1
        left,right = 0, len(nums) - 1


        for _ in range(len(nums) ):

            left_square = nums[left] ** 2
            right_square = nums[right] ** 2

            if left_square >= right_square:
                new_nums[pos] = left_square
                left += 1
            else:
                new_nums[pos] = right_square
                right -= 1

            pos -= 1
        return new_nums
        
# @lc code=end

