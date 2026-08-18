class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").replace(",", "").replace("'", "").replace(".", "").replace(":", "").replace("!", "")

        if s and s[-1] in ["?", "!", "."]:
            s = s[:-1]
        
        end = -1
        half = len(s)//2
        for i in range(half):
            print(s[i].lower(), s[end].lower())
            if s[i].lower() != s[end].lower():
                return False
            end -= 1
        return True