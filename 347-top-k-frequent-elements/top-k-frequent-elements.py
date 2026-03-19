class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqMap = Counter(nums)
        result = []

        sortedByFreq = dict(sorted(freqMap.items(), key = lambda item : item[1], reverse = True))

        for key in sortedByFreq.keys():
            
            if len(result) < k:
                result.append(key)
            else:
                break
        return result