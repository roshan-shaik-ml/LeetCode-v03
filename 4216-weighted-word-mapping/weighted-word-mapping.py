class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        
        ans = []
        for word in words:
            weight = 0
            for char in word:
                char_ascii = ord(char) - ord('a')
                weight += weights[char_ascii]
            
            modulo = weight % 26
            ans.append(chr(ord('z')-modulo))
        
        return "".join(ans)