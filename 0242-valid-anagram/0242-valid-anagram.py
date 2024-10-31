class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        annie = list(s)
        o_tay = list(t)
        annie_s = sorted(annie)
        o_tay_s = sorted(o_tay)
        if annie_s != o_tay_s:
            return False
        else:
            return True