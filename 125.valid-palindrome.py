#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. 内置函数提前处理字符串
        # s = s.lower().strip()
        # for c in s:
        #     if not c.isalnum():
        #         s = s.replace(c,'')
        # left, right =0, len(s) - 1
        # while left < right:
        #     if s[left] != s[right]:
        #         return False
            
        #     left +=1
        #     right -= 1

        # return True
        
        # 2. 不提前处理字符串
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        
        return True

# @lc code=end

