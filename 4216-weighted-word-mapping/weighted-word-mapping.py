class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = []
        append = ans.append
        weights = weights

        for word in words:
            weight = 0
            for char in word:
                weight += weights[ord(char) - 97]

            append(chr(122 - weight % 26))

        return "".join(ans)