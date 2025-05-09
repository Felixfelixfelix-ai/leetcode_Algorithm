#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 使用滑动窗口 统计最长子序列
        ans, left =0, 0
        cnt = defaultdict(int) #键值对维护子序列中每个字符出现的次数
        for right, c in enumerate(s):
            cnt[c] += 1
            
            while cnt[c] > 1:
                cnt[s[left]] -= 1 #当出现重复字符时候，缩小滑动窗口，直到没有重复字符串
                left += 1
            ans = max(ans,right - left + 1)
        return ans 
             
        
# @lc code=end

