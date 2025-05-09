#
# @lc app=leetcode id=2461 lang=python3
#
# [2461] Maximum Sum of Distinct Subarrays With Length K
#

# @lc code=start
from collections  import defaultdict
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans, s = 0, 0
        cnt = defaultdict(int)

        for i, num in enumerate(nums):
            s += num
            cnt[num] += 1

            if i < k - 1:
                continue

            if len(cnt) == k:
                ans = max(ans, s)
            
            # 出
            out = nums[i - k + 1]

            s -= out

            cnt[out] -= 1

            if cnt[out] == 0:
                del(cnt[out])
        
        return  ans
# @lc code=end

