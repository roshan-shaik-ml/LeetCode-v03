class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        n = len(numbers)
        low = 0
        high = n - 1

        while(numbers[low] + numbers[high] != target and low < high):

            if numbers[low] + numbers[high] < target:
                low+=1
            
            if numbers[low] + numbers[high] > target:
                high-=1

        return [low+1, high+1]
        
