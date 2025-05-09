#
# @lc app=leetcode id=3439 lang=python3
#
# [3439] Reschedule Meetings for Maximum Free Time I
#

# @lc code=start
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:

    # 等价于 ：给你 n+1 个空余时间段，合并其中 k+1 个连续的空余时间段，得到的最大长度是多少？
    
        def get_space(i):
            # 处理首尾两个空闲时间
            if i == 0:
                return startTime[i]
            if i == len(startTime):
                return eventTime - endTime[-1]
            # 处理中间的空闲时间段
            return startTime[i] - endTime[i - 1]

        length = len(startTime)
        ans, tmp = 0, 0

        for i in range(length + 1):
            tmp += get_space(i)

            if i < k :
                continue
            ans = max(ans, tmp)

            tmp -= get_space(i - k)
        return ans

        

# @lc code=end

