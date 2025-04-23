class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        if not nums:
            return 0
        ans = nums * 2
        return ans