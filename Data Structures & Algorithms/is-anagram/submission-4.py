class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        check = Counter(s)
        for i in t:
            if check[i] > 0:
                check[i] -= 1
            else:
                return False
        return True