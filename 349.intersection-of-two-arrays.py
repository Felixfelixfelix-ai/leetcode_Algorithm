#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return list(set(nums1) & set(nums2))

        # 一次遍历 返回答案
        st = set(nums1)
        arr = []

        for num in nums2:
            if num in st:
                st.remove(num)
                arr.append(num)

        return arr 
          


# @lc code=end

