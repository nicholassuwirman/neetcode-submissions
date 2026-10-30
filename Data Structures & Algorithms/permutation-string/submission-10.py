# s2 = "lecabee"
#       l r

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        l = 0
        r = len(s1) - 1

        sorted_list_s1 = sorted(list(s1))
        list_s2 = []

        for i in range(len(s1)):
            list_s2.append(s2[i])
        
        while r < len(s2):
            sorted_list_s2 = sorted(list_s2)
            if sorted_list_s1 == sorted_list_s2:
                return True
            if r + 1 == len(s2):
                break
            list_s2.remove(s2[l])
            l += 1
            r += 1
            list_s2.append(s2[r])
            
        
        return False
