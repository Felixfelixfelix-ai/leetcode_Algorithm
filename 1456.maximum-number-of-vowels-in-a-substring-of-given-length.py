#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans, vowels = 0, 0

        for i, c in  enumerate(s,start=0):

            if c in 'aeiou':
                vowels += 1

            if i < k - 1:
                continue

            ans = max(ans,vowels)

            if s[i - k + 1] in 'aeiou':
                vowels -= 1
            
        return ans

# @lc code=end

