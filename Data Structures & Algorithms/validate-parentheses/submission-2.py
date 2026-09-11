class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pairs = {
        ')': '(',
        '}': '{', 
        ']': '['
    }

        stack = []
        for i in s:
            if i in bracket_pairs.values():
                stack.append(i)
            if i in bracket_pairs.keys():
                if not stack:
                    return False
                if stack.pop() != bracket_pairs[i]:
                    return False
        
        return len(stack) == 0

        