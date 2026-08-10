class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        all_words = {}

        for i, word in enumerate(strs):
            sorted_word = ''.join(sorted(word))
            if sorted_word in all_words:
                all_words[sorted_word].append(strs[i])
            else:
                all_words[sorted_word] = [strs[i]]

        return all_words.values()