class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        allwords = {}
        
        for i, word in enumerate(strs):
            sortedword = ''.join(sorted(word))
            if sortedword in allwords:
                allwords[sortedword].append(strs[i])
            else:
                allwords[sortedword] = [strs[i]]

        return allwords.values()



        