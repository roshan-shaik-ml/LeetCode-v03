class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        total = sum(nums)
        n = len(nums)
        n_numbers = (n * (n+1)) // 2 
        return n_numbers - total