class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = dict()
        for i in range(0, len(nums)):

            if hashmap.get(target - nums[i]) != None:

                return i, hashmap[target-nums[i]]
            else:
                hashmap[nums[i]] = i 