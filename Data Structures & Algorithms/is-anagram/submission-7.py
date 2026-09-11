class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        if len(s) != len(t):
            return False

        checkA = {}

        for i in s:
            if i not in checkA:
                checkA[i] = 1
            else:
                checkA[i] +=1 

        for i in t:
            if i not in checkA:
                checkA[i] = 1
            else:
                checkA[i] -=1
          

        for i in checkA:
            if checkA[i] > 0:
                return False
        return True