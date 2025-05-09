#
# @lc app=leetcode id=2134 lang=python3
#
# [2134] Minimum Swaps to Group All 1's Together II
#

# @lc code=start
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # 滑动窗口的话  长度为 1的数量的窗口内   如果0的个数最少  那么交换的次数就最少
        new_nums = nums + nums
        k = sum(nums)
        ans, tmp = float('inf'), 0
        for i, num in enumerate(new_nums):
            if num == 0:
                tmp += 1
            
            if i < k -1:
                continue
            if i >= k - 1:
                ans = min(ans,tmp)

                if new_nums[i - k + 1] == 0:
                     tmp -= 1
            
        return ans


        
# @lc code=end

