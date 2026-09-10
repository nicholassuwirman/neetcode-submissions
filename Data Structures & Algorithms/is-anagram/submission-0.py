class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # turn s into a dict
        sDict = {}
        for char in s:
            sDict[char] = sDict.get(char, 0) + 1

        # turn t into a dict
        tDict = {}
        for char in t:
            tDict[char] = tDict.get(char, 0) + 1

        # compare the values of each key (alphabet)
        return sDict == tDict
