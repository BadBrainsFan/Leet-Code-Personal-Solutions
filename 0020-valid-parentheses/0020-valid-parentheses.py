class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(','}':'{',']':'['}
        ch_list = []
        for ch in s:
            if ch in hashmap:
                if ch_list and ch_list[-1] == hashmap.get(ch):
                    ch_list.pop()
                else:
                    return False
            else:
                ch_list.append(ch)
        return True if not ch_list else False