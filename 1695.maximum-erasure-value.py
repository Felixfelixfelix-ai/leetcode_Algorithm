#
# @lc app=leetcode id=1695 lang=python3
#
# [1695] Maximum Erasure Value
#

# @lc code=start
from collections import defaultdict
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # 删除子数组得最大得分也就是求：一个包含不同元素的子序列的最大和
        # 未优化
        # seq = defaultdict(int)
        # ans, left = 0, 0
        # for right, num in enumerate(nums):
        #     seq[num] += 1
        #     while seq[num] > 1:
        #         seq[nums[left]] -= 1
        #         if seq[nums[left]] == 0:
        #             del seq[nums[left]]
        #         left += 1
        #     ans = max(ans,sum(nums[left : right + 1 ]))
        # return ans


        # 优化之后的代码
        seq = set()
        ans,total,left = 0, 0, 0
        for num in nums:
            total += num
            while num in seq:
                seq.remove(nums[left])
                total -= nums[left]
                left += 1
            seq.add(num)
            ans = max(ans, total)
        return ans

        
# @lc code=end

