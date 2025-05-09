#
# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#

# @lc code=start
from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #题目的意思是   求包含两种元素的连续最长子序列的长度
        ans, left = 0, 0
        baskets = defaultdict(int)

        for right,num in enumerate(fruits):
            baskets[num] += 1
            while len(baskets) > 2:
                baskets[fruits[left]] -= 1
                if baskets[fruits[left]] == 0:
                    del baskets[fruits[left]]
                left += 1
            ans = max(ans,right - left + 1)
        
        return ans


# @lc code=end

