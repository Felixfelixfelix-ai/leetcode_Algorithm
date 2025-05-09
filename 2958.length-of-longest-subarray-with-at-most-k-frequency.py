#
# @lc app=leetcode id=2958 lang=python3
#
# [2958] Length of Longest Subarray With at Most K Frequency
#

# @lc code=start
from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        seq = defaultdict(int)
        ans, left = 0, 0
        for right,num in enumerate(nums):
            seq[num] += 1
            while seq[num] > k:
                seq[nums[left]] -= 1
                if seq[nums[left]] == 0:
                    del seq[nums[left]]
                left += 1
            ans = max(ans, right - left + 1)
        return ans
        
# @lc code=end

