# So if s1 = "ab", its permutations are "ab" and "ba". 
# If s1 = "abc", permutations include "abc", "acb", "bac", "bca", "cab", "cba" — all 6 orderings.

# longest = 0  //longsest tracked permutation in the string
# s1 = "ab"
#          lr
# s2 = "lecabee"
#           lr
# s3 = "laxxabcxxx"

# s1="adc"
# seen_s1 = {a:1,d:1,c:1}
# seen_s2 = {d:2,c:1,
# start from 0. iteration
#     r
#     l
# s2="dcda"     seen_s2 = {d:1
# 1.
#     lr            
# s2="dcda"     seen_s2 = {d:1,c:1
# 2.
#     l r
# s2="dcda"     seen_s2 = {d:2,c:1
# 3.
#     l  r
# s2="dcda"   hits case of current_window_size > s1_window_size
#      l r
# s2="dcda"  seen_s2 = {d:1,c:1,a:1)
# checks seen_s1 == seen_s2, so return True!!!

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen_s1 = {}
        seen_s2 = {}

        for i in range(len(s1)):
            seen_s1[s1[i]] = seen_s1.get(s1[i], 0) + 1

        l = 0

        for r in range(len(s2)):
            if r - l + 1 > len(s1):
                seen_s2[s2[l]] -= 1
                if seen_s2[s2[l]] == 0:
                    del seen_s2[s2[l]]
                l += 1

            seen_s2[s2[r]] = seen_s2.get(s2[r], 0) + 1

            if seen_s1 == seen_s2:
                return True
        return False
