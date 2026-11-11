class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen = dict(sorted(Counter(s1).items()))
        left = 0
        for right in range(len(s1)-1,len(s2)):
            
            check = dict(sorted(Counter(s2[left:right+1]).items()))
            if check == seen:
                return True
            else:
                left +=1
        return False