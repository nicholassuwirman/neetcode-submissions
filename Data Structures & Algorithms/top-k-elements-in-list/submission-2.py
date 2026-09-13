# clear hash map
# nums = [2,2,1,3,3,3], k = 2   // k used for last looping
# 0. if 2 not in hash_nums add to hash_nums orginalNum:count, else add to count
# 1. if 1 not in hash_nums add to hash_nums orginalNum:count, else add to count
#               0    1    2
# hash_nums = {2:2, 1:1, 3:3}
# sorted_hash = {1:1, 2:2, 3:3}
# k = 2, start for loop from len(hash_nums)-1 until k
# so start last loop from behind to front until k

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_nums = {}

        for i in range(len(nums)):
            if nums[i] not in hash_nums:
                hash_nums[nums[i]] = 1
            else:
                hash_nums[nums[i]] += 1

      # def sorted(iterable, key=None, reverse=False):
        # look at very bottom for explanation about lambda pair: pair[1]
        # basically, sort hash_nums, based on its count, descending
        sorted_items = sorted(hash_nums.items(), key=lambda pair: pair[1], reverse=True)
        # now sorted_items looks like {3:3, 2:2, 1:1}
        
        output = []

        for i in range(k):
            # sorted_items[i][0] accesses key (here orginalNum)
            # sorted_items[i][1] accesses value (here count)
            output.append(sorted_items[i][0])

        return output


# f = lambda pair: pair[1]
# print(f((3, 3)))    # 3
# print(f(("x", 99)))  # 99