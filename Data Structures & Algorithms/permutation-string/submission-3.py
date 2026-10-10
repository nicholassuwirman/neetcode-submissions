# s1 = "abc"
#       l r
# s2 = "lecabee"
# listS1 = [a,b,c] //sort this
# listS2 = [a,c,e] //sort this too
# compare listS1 == listS2

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        listS1 = sorted(list(s1))
        listS2 = list(s2[:len(s1)])
        l = 0
        r = len(s1) - 1

        while True:
            if listS1 == sorted(listS2):
                print(listS1)
                print(listS2)
                return True
            if r == len(s2) - 1:
                break
            listS2.remove(s2[l])
            l += 1
            r += 1
            listS2.append(s2[r])
            
        return False