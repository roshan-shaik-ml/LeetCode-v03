class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqMap = Counter(nums)
        result = []

        sortedByFreq = sorted(freqMap.items(), key = lambda item : item[1], reverse = True)
        return [num for num, _ in sortedByFreq[:k]]