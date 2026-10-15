class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen_count = dict()
        for i, val in enumerate(nums):
            if val not in seen_count:
                seen_count[nums[i]] = 1
            else:
                seen_count[nums[i]] += 1
        
        # sort the seen_count
        sorted_items = sorted(seen_count.items(), key=lambda pair: pair[1], reverse=True)

        # output for i in range(k)
        output = []
        for i in range(k):
            output.append(sorted_items[i][0])
        return output