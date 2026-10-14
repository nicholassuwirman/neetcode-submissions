# Input: strs = ["act","pots","tops","cat","stop","hat"]
# []

# seen = {'act':[0,3],'pots':[1,2,4],'aht':[5]}


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = dict()

        for i in range(len(strs)):
            sorted_str = ''.join(sorted(strs[i]))
            if sorted_str not in seen:
                seen[sorted_str] = [i]
            else:
                seen[sorted_str].append(i)
        
        output = []
        for key, values in seen.items():
            tmp_arr = []
            for index in values:
                tmp_arr.append(strs[index])
            output.append(tmp_arr)
        return output
