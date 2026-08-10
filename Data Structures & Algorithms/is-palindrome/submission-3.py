class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        news = s.lower().replace(" ", "")
        res = "".join([j for i, j in enumerate(news) if j in a])

        end = -1
        for i in range(len(res)):
            if res[i] != res[end]:
                return False
            end -= 1
        return True