from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        for i in range(len(s2)):
            sub_string = s2[i:i+window_size]
            if Counter(sub_string) == Counter(s1):
                return True 
        return False

        


