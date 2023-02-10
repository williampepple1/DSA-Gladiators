class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap = {}
	
        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord in hashMap.keys():
                hashMap[sortedWord].append(word)
            else:
                hashMap[sortedWord] = [word]
        return list(hashMap.values())