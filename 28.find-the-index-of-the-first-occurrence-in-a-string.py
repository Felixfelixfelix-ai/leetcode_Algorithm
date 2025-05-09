#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle is None:
            return 0
        if len(haystack) < len(needle):
            return -1
        
        for i in range(i,len(haystack)):
            if haystack

        
# @lc code=end

