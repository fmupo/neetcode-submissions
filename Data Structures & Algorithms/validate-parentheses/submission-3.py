class Solution:
    def isValid(self, s: str) -> bool:
        matches = { "(":")", "[":"]","{":"}"}
        stack = []
        for i in s:
            if i in matches:
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    if matches[stack[-1]] == i:
                        stack.pop(-1)
                    else:
                        return False
        return len(stack) ==0
                   
