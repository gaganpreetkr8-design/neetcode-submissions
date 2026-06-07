class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        stack=[]
        for i in s:
            if i in mapping.values():
                stack.append(i)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top != mapping[i]:
                    return False
        return len(stack) == 0
