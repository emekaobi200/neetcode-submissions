class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_hash = {}
        for i in s:
            if i not in first_hash:
                first_hash[i] = 1
            else:
                first_hash[i] +=1
        for i in t:
            if i not in first_hash:
                first_hash[i] = 1
            else:
                first_hash[i] -=1 
        
        for i in first_hash:
            if first_hash[i]> 0:
                return False
        return True

