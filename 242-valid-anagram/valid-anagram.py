class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_hashmap = Counter(s)
        t_hashmap = Counter(t)

        if s_hashmap == t_hashmap:
            return True

        return False