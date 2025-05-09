#
# @lc app=leetcode id=2841 lang=python3
#
# [2841] Maximum Sum of Almost Unique Subarray
#

# @lc code=start
from collections import defaultdict
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        # 这道题实质上是维护一个 动态的哈希表(频率映射) ，结合滑动窗口 
        ans, s = 0, 0
        cnt = defaultdict(int)

        for i ,num in enumerate(nums):
            # s 是滑动窗口所有元素之和
            s += num
            cnt[num] += 1  # 统计滑动窗口中 每个元素的频率

            if i < k - 1:  # 滑动窗口元素个数不够 k ，继续统计
                continue

            if len(cnt) >= m:
                ans = max(ans, s) # 更新答案
            
            out = nums[i - k + 1]
            s -= out
            cnt[out] -= 1

            if cnt[out] <= 0:
                del(cnt[out])

        return ans




            

            


        
# @lc code=end

