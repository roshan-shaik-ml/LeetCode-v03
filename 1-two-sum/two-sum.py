class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}
        ans = []
        t = len(nums)
        for i in range(t):
            
            if hashmap.get(nums[i]) == None:
                hashmap[nums[i]] = [i]
            else:
                hashmap[nums[i]].append(i)

        
        for i in range(t):

            to_find = target - nums[i]
            if hashmap.get(to_find) != None:
                
                indices = hashmap.get(to_find)
                for j in indices:

                    if j != i:
                        return [i, j]
        