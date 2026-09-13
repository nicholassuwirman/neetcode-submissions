#                  0  ,  1  ,  2
# Input: strs = ["act","cba","cat"]
# 0. sort act -> act
# check in hashmap, if not in hashmap add "act":position, else just append to position 
# map to hash: {"act":[0, 2], "abc":[1]}
# output: [[strs[0], strs[2]], [strs[1]]]
# output: [[act, cat], [cba]]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_strs = {}

        #sorting the strings from original input array
        for i in range(len(strs)):
            sorted_str = ''.join(sorted(strs[i]))
            if sorted_str not in hash_strs:
                hash_strs[sorted_str] = [i]
            else: 
                hash_strs[sorted_str].append(i)
        
        output = []

        for values in hash_strs.values():   # [0, 2]
            arr = []
            for index in values:
                arr.append(strs[index])
            output.append(arr)

        return output

