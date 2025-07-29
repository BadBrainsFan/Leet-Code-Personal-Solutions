class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = {}
        for index,num in enumerate(nums):
            if target - num not in answer:
                answer[num] = index
            else:
                return [answer[target - num], index]