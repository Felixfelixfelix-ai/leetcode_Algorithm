#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans, total = float('-inf'), 0
        for i, num in enumerate(nums):
            total += num

            if i < k - 1:
                continue

            ans = max(ans, total / k)

            total -= nums[i -k + 1]

        return ans 
# @lc code=end

