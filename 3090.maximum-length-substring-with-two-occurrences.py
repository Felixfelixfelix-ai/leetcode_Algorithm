#
# @lc app=leetcode id=3090 lang=python3
#
# [3090] Maximum Length Substring With Two Occurrences
#

# @lc code=start
from collections import defaultdict
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans,left = 0, 0
        cnt = defaultdict(int)
        for right,c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 2:
                cnt[s[left]] -= 1
                left += 1

            ans = max(ans,right - left + 1)
        return ans
        
# @lc code=end

