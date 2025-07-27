class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            if target - num not in hashmap:
                hashmap[num] = index
            else:
                return [hashmap[target-num], index]