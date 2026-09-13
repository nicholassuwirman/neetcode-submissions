# hash
# len s != len t return False, bcs if it doesnt have the same length then it wont be anagram
# put s and t into two dicts
# compare dicts

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_s, hash_t = {}, {}

        for i in range(len(s)):
            hash_s[s[i]] = 1 + hash_s.get(s[i], 0)
            hash_t[t[i]] = 1 + hash_t.get(t[i], 0)
        
        for ch in hash_s:
            if hash_s[ch] != hash_t.get(ch, 0):
                return False
        
        return True
        