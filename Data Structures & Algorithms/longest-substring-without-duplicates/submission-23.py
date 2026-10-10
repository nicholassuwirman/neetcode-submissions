#         r
#       l
# s = "zxyzxyz"
# seen = [x,y]
# highest = 3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        highest = 0
        l = 0
        r = 0
        seenSet = set()

        while r < len(s):
            if s[r] not in seenSet:
                seenSet.add(s[r])
                highest = max(highest, len(seenSet))
                r += 1
            elif s[r] in seenSet:
                seenSet.remove(s[l])
                l += 1
        return highest
