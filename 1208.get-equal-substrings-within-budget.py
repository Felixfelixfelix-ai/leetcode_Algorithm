#
# @lc app=leetcode id=1208 lang=python3
#
# [1208] Get Equal Substrings Within Budget
#

# @lc code=start
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        #思路 先计算两个字符串元素之差的列表  然后 求 和不超过maxCost的最长子序列的个数
        nums = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        ans=total=left = 0
        for right,num in enumerate(nums):
            total += num
            while total > maxCost :
                total -= nums[left] 
                left += 1
            ans = max(ans,right - left + 1)
        return ans 

            



        
# @lc code=end

