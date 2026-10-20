# clean (lower case) and merge the words into 1
# make 2 pointers from first and back
# wasitacaroracatisaw
# l                 r
#  l               r 
#   l             r
# until l == r   
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean

        clean_s = "" # clean s here 
        for char in s:
            if char.isalnum():  # removes junk characters such as space, commas
                clean_s += char.lower()

        l = 0
        r = len(clean_s) - 1
        while l <= r:
            if clean_s[l] != clean_s[r]:
                return False
            l += 1
            r -= 1
        return True


