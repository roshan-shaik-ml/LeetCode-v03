class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap= {}

        for i, num in enumerate(nums):

            to_find = target - num
            if hashmap.get(to_find) != None:
                return [hashmap.get(to_find), i]
            
            hashmap[num] = i