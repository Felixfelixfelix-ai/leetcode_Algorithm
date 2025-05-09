#
# @lc app=leetcode id=1343 lang=python3
#
# [1343] Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
#

# @lc code=start
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans, total = 0, 0

        for i, num in enumerate(arr):

            total += num

            if i < k - 1:
                continue

            if total / k >= threshold:
                ans += 1

            total -= arr[i - k + 1] 
        
        return ans
    

        
# @lc code=end

