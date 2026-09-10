# hashing, O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seenDict = {}
        for i in range(len(nums)):
            seenDict[nums[i]] = seenDict.get(nums[i], 0) + 1

        # wht even is this?
        # essentially just sort the dict, and slice the top k of the sorted dict, but idk how to do it
        sortedItems = sorted(seenDict.items(), key=lambda x: x[1], reverse=True)
        topK = sortedItems[:k]
        result = [x[0] for x in topK]
        return result
