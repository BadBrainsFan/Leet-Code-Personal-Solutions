class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(', '}':'{',']':'['}
        stack = []
        for ch in s:
            if ch in hashmap:
                if stack and stack[-1] == hashmap.get(ch):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return True if not stack else False