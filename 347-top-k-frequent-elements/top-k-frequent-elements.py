class Solution:
    # Using sorted with key and reverse along with a frequency map
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqMap = Counter(nums)
        result = []

        sortedByFreq = sorted(freqMap.items(), key = lambda item : item[1], reverse = True)
        return [num for num, _ in sortedByFreq[:k]]

    # Using counter's internal method 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        
        freqMap = Counter(nums)
        return [num for num, freq in Counter(nums).most_common(k)]
