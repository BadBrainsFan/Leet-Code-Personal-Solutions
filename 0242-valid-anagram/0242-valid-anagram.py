class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        for item in s:
            if item not in count_s:
                count_s[item] = 1
            else:
                count_s[item] += 1

        count_t = {}
        for item in t:
            if item not in count_t:
                count_t[item] = 1
            else:
                count_t[item] += 1
        
        return count_s == count_t