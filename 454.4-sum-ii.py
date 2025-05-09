#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#

# @lc code=start
# from collections import Counter
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        cnt = Counter(x + y for x in nums1 for y in nums2)
        return sum(cnt[-x - y] for x in nums3 for y in nums4)


        
# @lc code=end

