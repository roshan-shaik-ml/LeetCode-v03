class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}

        for string in strs:

            key = ''.join(sorted(string))
            
            if hashmap.get(key) == None:
                hashmap[key] = [string]
            else:
                hashmap.get(key).append(string)
        

        results = []
        for value in hashmap.values():

            results.append(value)
        
        return results
