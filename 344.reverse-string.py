#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if s is None:
            return s
            
        left = 0
        right = len(s) - 1
        while left < right:
            # 1.临时变量
            # temp = s[left]
            # s[left] = s[right]
            # s[right] = temp 
            # left += 1
            # right -= 1

            # 2.位运算
            s[left] = chr(ord(s[left]) ^ ord(s[right]))
            s[right] = chr(ord(s[right]) ^ ord(s[left]))
            s[left] = chr(ord(s[left]) ^ ord(s[right]))
            left += 1
            right -= 1
        return s 



        
# @lc code=end

