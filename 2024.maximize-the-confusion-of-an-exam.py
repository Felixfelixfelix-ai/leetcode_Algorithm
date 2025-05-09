#
# @lc app=leetcode id=2024 lang=python3
#
# [2024] Maximize the Confusion of an Exam
#

# @lc code=start
from collections import defaultdict
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        #1. 分类讨论，F 最多或者 T 最多，这样就变成了 比较包含k个T 的最长F子序列 与 包含K个F的最长T子序列
        # def find_seq(false_answer):
        #     seq = defaultdict(int)
        #     ans,left = 0, 0
        #     for right, answer in enumerate(answerKey):
        #         seq[answer] += 1
        #         while seq[false_answer] > k:
        #             seq[answerKey[left]] -= 1
        #             if seq[answerKey[left]] == 0:
        #                 del seq[answerKey[left]]
        #             left += 1
        #         ans = max(ans, right - left + 1)
        #     return ans 
        # f_max = find_seq('F')
        # t_max = find_seq('T')
        # return max(f_max, t_max)  
        # 
         
        #2.子串中最多包含K个 F  或者K个 T  对第一种情况的优化
        cnt = defaultdict(int)
        ans, left = 0, 0
        for right, ch in enumerate(answerKey):
            cnt[ch] += 1
            while min(cnt['F'] , cnt['T']) > k:
                cnt[answerKey[left]] -= 1
                if cnt[answerKey[left]] == 0:
                    del cnt[answerKey[left]]
                left += 1
            ans = max(ans, right - left + 1)
        return ans




        
# @lc code=end

