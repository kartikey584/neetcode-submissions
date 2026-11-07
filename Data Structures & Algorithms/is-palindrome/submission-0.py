class Solution:
    def isPalindrome(self, s: str) -> bool:

        strs = ""

        for i in s:
            if i.isalnum():
                strs += i.lower()
        
        if strs == strs[::-1]:
            return True

        return False