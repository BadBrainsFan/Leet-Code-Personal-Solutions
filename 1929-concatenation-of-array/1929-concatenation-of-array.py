class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        count = 0
        while count < 2:
            for index in range(len(nums)):
                ans.append(nums[index])
            count += 1
        return ans