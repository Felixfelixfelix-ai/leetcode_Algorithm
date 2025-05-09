#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)  # Counter()函数  返回key 为字母  value为次数的 键值对字典
        
        # 根据ASII中字母对应数字的特性解题
        arr = [0 for _ in range(26)]

        for c in s :
            arr[ord(c) -  ord('a')] += 1  # 易错   ord(c)  写为  ord('c')
        for c in t :
            arr[ord(c) -  ord('a')] -= 1

        return all(c == 0 for c in arr)
# @lc code=end

