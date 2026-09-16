# s = "Was it a car or a cat I saw?"
# turn s into: wasitacaroracatisaw
# we need to remove the junk words
# turn capital letters into lower letters
# l                 r
# wasitacaroracatisaw
# l < r

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "" # clean s here 
        for char in s:
            if char.isalnum():  # removes junk characters such as space, commas
                clean_s += char.lower()

        l, r = 0, len(clean_s)-1

        while l < r:
            if clean_s[l] != clean_s[r]:
                return False
            l += 1
            r -= 1
        
        return True
        