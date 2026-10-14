

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1Hash = dict()
        s2Hash = dict()

        for i in range(len(s)):
            if s[i] not in s1Hash:
                s1Hash[s[i]] = 0
            else:
                s1Hash[s[i]] += 1
        
        for i in range(len(t)):
            if t[i] not in s2Hash:
                s2Hash[t[i]] = 0
            else:
                s2Hash[t[i]] += 1
        
        return s1Hash == s2Hash