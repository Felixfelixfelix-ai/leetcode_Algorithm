#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # ransomNote = Counter(ransomNote)
        # magazine = Counter(magazine)
        # for c in ransomNote:
        #     if not magazine[c] or ransomNote[c] > magazine[c]:
        #         return False
        # return True
        return not (Counter(ransomNote) - Counter(magazine))
# @lc code=end

